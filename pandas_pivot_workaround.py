import pandas as pd
metadata=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/june_2018_figure_fixing/metadata_for_reshape_more_futz.txt', sep='\t')
metadata_melt=pd.melt(metadata,id_vars=['date','exp_day','carboy','dilution','pCO2_condition'])
metadata_melt_groupby=metadata_melt.groupby(['date','exp_day','carboy','dilution','variable'])['value'].sum().unstack('carboy')
