'''
This file creates a figure with subfigures of LCOE_base vs year (upper left), cost-value factor vs. market share (upper right), and example PLCOE vs market share curves for select years (bottom), with lines for each tech.

Run this file on the reeds2 conda environment.
'''
import pandas as pd
import os
from pdb import set_trace as b

years = [2030,2040,2050]

this_dir = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(f'{this_dir}/valcostfac_core.csv')
df['cost_value_factor'] = 1 / df['value_cost_factor']

df_lcoe = pd.read_csv(f'{this_dir}/LCOE_base.csv')
df_lcoe_sel = df_lcoe[df_lcoe['year'].isin(years)].copy()
df_lcoe_sel = df_lcoe_sel.pivot_table(index='tech', columns='year', values='lcoe_base')
df_lcoe_sel.columns = ['lcoe_base_' + str(c) for c in df_lcoe_sel.columns]
df_lcoe_sel.reset_index(inplace=True)

df = df.merge(df_lcoe_sel, how='left', on='tech')

for year in years:
    df[f'plcoe_{year}'] = df[f'lcoe_base_{year}'] * df['cost_value_factor']

#Create the figure. Note that market share is the 'gen_frac' column in df.
b()