'''
This file allows reports to be run directly from this python script (without need for the bokeh server and bokehpivot UI).

Easiest process:
1. Update bokehpivot/reeds_scenarios.csv with desired scenario names and paths.
2. If a different report is desired (other than standard_report_reduced), update 'report_path' (below).
3. Run this file. If you haven't updated 'output_dir', you'll find the results in bokehpivot/out.

If you run this file from another location, update 'bokehpivot_dir' below.
'''
import os
import sys
import pandas as pd
import shutil
import importlib
from pdb import set_trace as b
#EDIT: Manually set bokehpivot_dir to another path if this file is in a different location.
bokehpivot_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, bokehpivot_dir)
import reeds_bokeh as rb

#EDIT THE FOLLOWING FIELDS
report_path = f'{bokehpivot_dir}/reports/templates/reeds2/value_factor_report.py' #Path to report that is to be run
diff = 'No' #Use 'Yes' if adding differences to a base case, specified below (default base case is first scenario in reeds_scenarios.csv)

data_source = f'{bokehpivot_dir}/reeds_scenarios.csv' #either a scenarios.csv file or ReEDS run directory (or directories separated by pipe symbols).
base = pd.read_csv(data_source)['name'][0] #Name of base case for when diff='Yes'. Defaults to first case in reeds_scenarios.csv.
output_dir = f'{bokehpivot_dir}/out/reeds_report' #This is the directory that will be created to contain the report. If it already exists, the existing directory will be archived with a date.
data_type = 'ReEDS 2.0'
scenario_filter = 'all' #'all' or string of comma-separated names.
html_num = 'one' #'one' or 'multiple'. 'one' will create one html file with all sections, and 'multiple' will create a separate html file for each section
report_format = 'html,excel' #'html', 'excel', or 'csv', or any combination separated by commas
auto_open = 'Yes' #'Yes' or 'No'. Automatically open the resulting report excel and html files when they are created.

#DON'T EDIT THIS SECTION
report_dir = os.path.dirname(report_path)
sys.path.insert(1, report_dir)
report_name = os.path.basename(report_path)[:-3]
report = importlib.import_module(report_name)
rb.reeds_static(data_type, data_source, scenario_filter, diff, base, report.static_presets, report_path, report_format, html_num, output_dir, auto_open)
shutil.copy2(os.path.realpath(__file__), output_dir)

#CUSTOM POSTPROCESSING
#Any post-processing of the excel data that was produced. you can read excel data into dataframes by importing pandas and using pandas.read_excel()

#Read in value factors
df = pd.read_excel(f'{output_dir}/report.xlsx', sheet_name='vf')
df = df.rename(columns={'vf': 'value_factor'})
df = df[df['tech'].isin(['wind-ons','upv'])].copy()
df = df[df['year']>2025].copy()

#Merge with benchmark price
df_bench = pd.read_excel(f'{output_dir}/report.xlsx', sheet_name='elec_price')
df_bench = df_bench.rename(columns={'$':'benchmark_price'})
df_bench = df_bench.groupby(['scenario','year'], as_index=False)['benchmark_price'].sum()
df = df.merge(df_bench, on=['scenario','year'], how='left')

#Merge with LCOE_base
#LCOE_base uses default ATB 2024 techs: Tech 1 class 4 Moderate land-based wind and class 5 Moderate utility PV
df_lcoe_base = pd.read_csv(f'{bokehpivot_dir}/LCOE_base.csv')
df_lcoe_base['lcoe_base'] = df_lcoe_base['lcoe_base'] * 1.041 #Converted to 2023$ from 2022$ (2024 ATB)
df = df.merge(df_lcoe_base, on=['tech','year'], how='left')
ptc = 18.31481632 #11.36 2004$/MWh, converted to 2023$ (taken from ReEDS run ptc_value_scaled).
#If "_IRA" is in the scenario name, subtract the ptc from lcoe
df.loc[df['scenario'].str.contains('_IRA'), 'lcoe_base'] = df['lcoe_base'] - ptc

df['lvoe'] = df['value_factor'] * df['benchmark_price']
df['value_cost_factor'] = df['lcoe_base'] / df['benchmark_price']
df['cost_factor'] = df['lvoe'] / df['lcoe_base'] #Here we assume lcoe = lvoe, which is true on the margin.
df['lcoe_adder'] = df['lvoe'] - df['lcoe_base']
df['integration_cost'] = df['benchmark_price'] - df['lvoe']
df['value_cost_adder'] = df['benchmark_price'] - df['lcoe_base']

#Merge with generation
df_gen = pd.read_excel(f'{output_dir}/report.xlsx', sheet_name='gen')
df_gen = df_gen.rename(columns={'Generation (TWh)': 'gen_twh'})
df_gen = df_gen[['scenario','tech','year','gen_twh']].copy()
df = df.merge(df_gen, on=['scenario','tech','year'], how='left')

#Merge with generation fraction
df_gen_frac = pd.read_excel(f'{output_dir}/report.xlsx', sheet_name='gen_frac')
df_gen_frac = df_gen_frac.rename(columns={'Generation (TWh)': 'gen_frac'})
df_gen_frac = df_gen_frac[['scenario','tech','year','gen_frac']].copy()
df = df.merge(df_gen_frac, on=['scenario','tech','year'], how='left')

df.to_csv(f'{output_dir}/valcostfac.csv', index=False)
b()
