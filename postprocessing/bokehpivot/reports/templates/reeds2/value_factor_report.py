'''
This makes a report of value and value factor outputs. Gen Frac is included
so that the value factors can be compared to market share. See comments in
in reeds2.py for a description of each preset.
'''
storage_techs = ['pumped-hydro','pumped-hydro-flex','battery', 'battery_2', 'battery_4', 'battery_6', 'battery_8', 'battery_10']

static_presets = [
    {'name': 'Generation (TWh)', 'sheet_name':'gen', 'result': 'Generation National (TWh)', 'preset': 'Stacked Bars'},
    {'name': 'Capacity (GW)', 'sheet_name':'cap', 'result': 'Capacity National (GW)', 'preset': 'Stacked Bars'},
    {'name': 'New Annual Capacity (GW)', 'sheet_name':'cap_new_ann', 'result': 'New Annual Capacity National (GW)', 'preset': 'Stacked Bars'},
    {'name': 'Annual Retirements (GW)', 'sheet_name':'retire_ann', 'result': 'Annual Retirements National (GW)', 'preset': 'Stacked Bars'},
    # {'name': 'Final Gen by timeslice (GW)', 'sheet_name':'gen_final_timeslice', 'result': 'Gen by timeslice national (GW)', 'preset': 'Stacked Bars Final'},
    {'name': 'Bulk System Electricity Price ($/MWh)', 'sheet_name':'elec_price', 'result': 'Requirement Prices and Quantities National', 'preset': 'Bulk System Electricity Price ($/MWh)'},
    {'name': 'Present Value of System Cost through 2050 (Bil $)', 'sheet_name':'sys_cost', 'result': 'Sys Cost Annualized (Bil $)', 'preset': 'Discounted through 2050'},
    {'name': 'Emissions National (metric tons)', 'sheet_name':'emissions', 'result': 'Emissions National (metric tons)', 'preset': 'Scenario Lines Over Time'},
    {'name': 'Runtime (hours)', 'sheet_name':'runtime', 'result': 'Runtime', 'preset': 'Stacked Bars'},
    {'name': 'Full Value New Techs', 'sheet_name':'vf_full', 'result': 'Value New Techs', 'download_full_source': True},
    {'name': 'Gen Frac', 'sheet_name':'gen_frac', 'result': 'Generation National (TWh)', 'preset': 'Stacked Bars Gen Frac', 'config':{'filter':{'tech':{'exclude':storage_techs}}}},
    {'name': 'Cap Frac', 'sheet_name':'cap_frac', 'result': 'Capacity National (GW)', 'preset': 'Stacked Bars Cap Frac'},
    {'name': 'LVOE by Year', 'sheet_name':'lvoe', 'result': 'Value New Techs', 'preset': 'LVOE by Year'},
    {'name': 'LVOE Energy by Year', 'sheet_name':'lvoe_energy', 'result': 'Value New Techs', 'preset': 'LVOE Energy by Year'},
    {'name': 'LVOE Firm Capacity by Year', 'sheet_name':'lvoe_resmarg', 'result': 'Value New Techs', 'preset': 'LVOE Firm Capacity by Year'},
    {'name': 'LVOE Operating Reserves by Year', 'sheet_name':'lvoe_opres', 'result': 'Value New Techs', 'preset': 'LVOE Operating Reserves by Year'},
    {'name': 'LVOE State RPS by Year', 'sheet_name':'lvoe_rps', 'result': 'Value New Techs', 'preset': 'LVOE State RPS by Year'},
    {'name': 'VF by Year', 'sheet_name':'vf', 'result': 'Value New Techs', 'preset': 'VF by Year'},
    {'name': 'VF Energy by Year', 'sheet_name':'vf_energy', 'result': 'Value New Techs', 'preset': 'VF Energy by Year'},
    {'name': 'VF Firm Capacity by Year', 'sheet_name':'vf_firmcap', 'result': 'Value New Techs', 'preset': 'VF Firm Capacity by Year'},
    {'name': 'VF Spatial by Year', 'sheet_name':'vf_spatial', 'result': 'Value New Techs', 'preset': 'VF Spatial by Year'},
    {'name': 'VF Temporal by Year', 'sheet_name':'vf_temporal', 'result': 'Value New Techs', 'preset': 'VF Temporal by Year'},
    {'name': 'VF Interaction by Year', 'sheet_name':'vf_interaction', 'result': 'Value New Techs', 'preset': 'VF Interaction by Year'},
]
