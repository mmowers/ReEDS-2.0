# This script contains dictionaries mapping the definitions of pivot tables
# to be included in an export to Tableau's .hyper file format.
# 
# Users can specify the keys of all the pivot dictionaries (the outermost dictionary)
# to be included in a Tableau export by including them as a Python list
# input to postprocess_for_tableau.py with, e.g.
# 
# python postprocess_for_tableau.py -p ['standard','plexos'] ... <other required flags>

# Create a dict of pivoted csvs/Tableau tables with the concatenated csvs from above that they pull data from:
PIVOT_DEFS = {'standard':          {'scen_i_r_t':             {'id_columns':  ['scenario','i','r','t'],
                                                               'csvs':        ['gen_ivrt','gen_ann','stor_inout','cap_ivrt','cap_new_ivrt','cap_upgrade_ivrt','ret_ivrt','stor_energy_cap',
                                                                               'curt_all_ann','opRes_supply','emit_irt','emit_captured_irt','lcoe','lcoe_fullpol','lcoe_nopol','prod_cap','prod_produce_ann','bioused','repgasquant_irt'],
                                                               'operation':   ['sum','sum','sum','sum','sum','sum','sum','sum',
                                                                               'mean','sum','sum','sum','mean','mean','mean','sum','sum','sum','sum']},
                                    'scen_i_r_szn_t':         {'id_columns':  ['scenario','i','r','szn','t'],
                                                               'csvs':        ['cap_firm','cc_new'],
                                                               'operation':   ['sum','mean']},
                                    'scen_r_t':               {'id_columns':  ['scenario','r','t'],
                                                               'csvs':        ['load_rt','emit_irt','emit_captured_irt','emit_r','emit_captured_r','prod_load_ann','prod_smr_emit','repbioprice','repgasprice_r','repgasquant_r'],
                                                               'operation':   ['sum','sum','custom','sum','custom','sum','sum','mean','mean','sum']},
                                    'scen_i_h_r_t':           {'id_columns':  ['scenario','i','h','r','t'],
                                                               'csvs':        ['gen_h','reqt_quant','stor_in','opRes_supply_h','stor_level','prod_load','prod_produce'],
                                                               'operation':   ['sum','sum','load_only','sum','sum','sum','custom','sum']},
                                    'scen_t':                 {'id_columns':  ['scenario','t'],
                                                               'csvs':        ['cap_ivrt','gen_ivrt','co2_cap','co2_price','RE_gen_price_nat','tran_mi_out','prod_h2_price','prod_h2ct_cost'],
                                                               'operation':   ['sum','sum','sum','mean','mean','sum','custom','custom']},
                                    'scen_rf_rt_trtype_t':    {'id_columns':  ['scenario','rf','rt','trtype','t'],
                                                               'csvs':        ['tran_mi_out_detail','tran_flow_rep_ann','opres_trade'],
                                                               'operation':   ['sum','sum','sum']},
                                    'scen_rf_rt_trtype_szn_t':{'id_columns':  ['scenario','rf','rt','trtype','szn','t'],
                                                               'csvs':        ['captrade'],
                                                               'operation':   ['sum']},
                                    'scen_rf_rt_h_trtype_t':  {'id_columns':  ['scenario','rf','rt','h','trtype','t'],
                                                               'csvs':        ['losses_tran_h','tran_flow_rep'],
                                                               'operation':   ['sum','sum']},
                                    'costs_r_t':              {'id_columns':  ['scenario','r','t','cost_cat_display','cost_cat'],
                                                               'csvs':        ['systemcost_ba'],
                                                               'operation':   ['custom']},
                                    'value_streams':          {'id_columns':  ['scenario','i','r','t','var_name','con_name'],
                                                               'csvs':        ['valuestreams_chosen'],
                                                               'operation':   ['sum']},
                                    'retail_rates':           {'id_columns':  ['scenario','st','t','price_component'],
                                                               'csvs':        ['retail'],
                                                               'operation':   ['custom']},
                                    'region_mapping':         {'id_columns':  ['r'],
                                                               'csvs':        ['region_mapping'],
                                                               'operation':   ['custom']},
                                    'line_mapping':           {'id_columns':  ['rf','rt'],
                                                               'csvs':        ['line_mapping'],
                                                               'operation':   ['custom']},
                                    'runtimes':               {'id_columns':  ['scenario','t','process','subprocess','starttime','stoptime'],
                                                               'csvs':        ['meta'],
                                                               'operation':   ['custom']},
                                    'metadata':               {'id_columns':  ['scenario','machine','repo','branch','commit'],
                                                               'csvs':        ['meta'],
                                                               'operation':   ['custom']}
             },
              'ctus':              {'line_mapping':           {'id_columns':  ['rf','rt'],
                                                               'csvs':        ['line_mapping'],
                                                               'operation':   ['custom']},
                                    'ctus_scen_r_cs_t':       {'id_columns':  ['scenario','r','cs','t'],
                                                               'csvs':        ['CO2_SPURLINE_INV_out','CO2_CAPTURED_out_ann','CO2_STORED_out_ann'],
                                                               'operation':   ['sum','sum','sum']},
                                    'ctus_scen_r_cs_h_t':     {'id_columns':  ['scenario','r','cs','h','t'],
                                                               'csvs':        ['CO2_CAPTURED_out','CO2_STORED_out'],
                                                               'operation':   ['sum','sum']},
                                    'ctus_scen_rf_rt_t':      {'id_columns':  ['scenario','rf','rt','t'],
                                                               'csvs':        ['CO2_TRANSPORT_INV_out','CO2_FLOW_out_ann','CO2_FLOW_pos_out_ann','CO2_FLOW_neg_out_ann','CO2_FLOW_net_out_ann',],
                                                               'operation':   ['sum','sum','sum','sum','sum']},
                                    'ctus_scen_rf_rt_h_t':    {'id_columns':  ['scenario','rf','rt','h','t'],
                                                               'csvs':        ['CO2_FLOW_out','CO2_FLOW_pos_out','CO2_FLOW_neg_out','CO2_FLOW_net_out'],
                                                               'operation':   ['sum','sum','sum','sum']},
                                    'ctus_r_cs_mapping':      {'id_columns':  ['r','cs'],
                                                               'csvs':        ['ctus_r_cs_mapping'],
                                                               'operation':   ['custom']},
                                    'ctus_cs_mapping':        {'id_columns':  ['cs'],
                                                               'csvs':        ['ctus_cs_mapping'],
                                                               'operation':   ['custom']}
             },
              'geometries':        {'geometries_cendiv':      {'id_columns':  ['cendiv'],
                                                                'csvs':       ['cendiv'],
                                                                'operation':  ['custom']},
                                    'geometries_country':     {'id_columns':  ['country'],
                                                                'csvs':       ['country'],
                                                                'operation':  ['custom']},
                                    'geometries_interconnect':{'id_columns':  ['interconnect'],
                                                                'csvs':       ['interconnect'],
                                                                'operation':  ['custom']},
                                    'geometries_nercr':       {'id_columns':  ['nercr'],
                                                                'csvs':       ['nercr'],
                                                                'operation':  ['custom']},
                                    'geometries_rto':         {'id_columns':  ['rto'],
                                                                'csvs':       ['rto'],
                                                                'operation':  ['custom']},
                                    'geometries_st':          {'id_columns':  ['st'],
                                                                'csvs':       ['st'],
                                                                'operation':  ['custom']},
                                    'geometries_transreg':    {'id_columns':  ['transreg'],
                                                                'csvs':       ['transreg'],
                                                                'operation':  ['custom']},
                                    'geometries_usda':        {'id_columns':  ['usda'],
                                                                'csvs':       ['usda'],
                                                                'operation':  ['custom']}
             },
              'costs_i_t':         {'costs_i_t':              {'id_columns':  ['scenario','i','t','cost_cat_display','cost_cat'],
                                                               'csvs':        ['systemcost_ba'],
                                                               'operation':   ['custom']}
             },
              'plexos':            {'plexos_scen_i_r_t':          {'id_columns':  ['scenario','plexos_scenario','i','r','t'],
                                                                    'csvs':       ['plexos_capacity','plexos_generation','plexos_emissions','plexos_availableenergy','plexos_pumpload'], #plexos_storage_maxvolume
                                                                    'operation':  ['sum','sum','sum','sum','sum']},
                                    'plexos_scen_r_t':            {'id_columns':  ['scenario','plexos_scenario','r','t'],
                                                                    'csvs':       ['plexos_load','plexos_lmp','plexos_use'],
                                                                    'operation':  ['sum','mean','sum']},
                                    'plexos_scen_8760_r_t':       {'id_columns':  ['scenario','plexos_scenario','8760','r','t'],
                                                                    'csvs':       ['plexos_load','plexos_losses'],
                                                                    'operation':  ['sum','sum']},
                                    'plexos_scen_i_8760_state_t': {'id_columns':  ['scenario','plexos_scenario','i','8760','r','t'],
                                                                    'csvs':       ['plexos_generation','plexos_pumpload'],
                                                                    'operation':  ['sum','sum']}
             }
}

pivots_without_csvs = [
    'retail_rates',
    'region_mapping',
    'line_mapping',
    'ctus_r_cs_mapping',
    'ctus_cs_mapping',
    'plexos_scen_i_r_t',
    'plexos_scen_8760_r_t',
    'plexos_scen_r_t',
    'plexos_scen_i_8760_state_t',
    'runtimes',
    'metadata'
    ]