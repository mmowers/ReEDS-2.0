'''
This makes a report of value and value factor outputs. Gen Frac is included
so that the value factors can be compared to market share. See comments in
in reeds2.py for a description of each preset.
'''
storage_techs = ['pumped-hydro','pumped-hydro-flex','battery', 'battery_2', 'battery_4', 'battery_6', 'battery_8', 'battery_10']

static_presets = [
    {'name': 'Full Value New Techs', 'sheet_name':'vf_full', 'result': 'Value New Techs', 'download_full_source': True},
    {'name': 'Generation (TWh)', 'sheet_name':'gen', 'result': 'Generation National (TWh)', 'preset': 'Stacked Bars'},
    {'name': 'Capacity (GW)', 'sheet_name':'cap', 'result': 'Capacity National (GW)', 'preset': 'Stacked Bars'},
    {'name': 'Gen Frac', 'sheet_name':'gen_frac', 'result': 'Generation National (TWh)', 'preset': 'Stacked Bars Gen Frac', 'config':{'filter':{'tech':{'exclude':storage_techs}}}},
    {'name': 'Cap Frac', 'sheet_name':'cap_frac', 'result': 'Capacity National (GW)', 'preset': 'Stacked Bars Cap Frac'},
    {'name': 'VF by Year', 'sheet_name':'vf', 'result': 'Value New Techs', 'preset': 'VF by Year'},
    {'name': 'VF Energy by Year', 'sheet_name':'vf_energy', 'result': 'Value New Techs', 'preset': 'VF Energy by Year'},
    {'name': 'VF Firm Capacity by Year', 'sheet_name':'vf_firmcap', 'result': 'Value New Techs', 'preset': 'VF Firm Capacity by Year'},
    {'name': 'Bulk System Electricity Price ($/MWh)', 'sheet_name':'elec_price', 'result': 'Requirement Prices and Quantities National', 'preset': 'Bulk System Electricity Price ($/MWh)'},
]
