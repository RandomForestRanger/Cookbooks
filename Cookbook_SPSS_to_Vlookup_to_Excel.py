import pandas as pd
import numpy as np
import pyreadstat

wb1 = 'Wave1.xlsx'
#wb2 = 'B2.xlsx'
wb2, meta = pyreadstat.read_sav("Wave1_3.sav")
wb3 = 'Product.xlsx'

df_wb1 = pd.read_excel(wb1)
#df_wb2 = pd.read_excel(wb2)
df_wb2 = wb2

#print(df_wb1.columns)
#print(df_wb2.columns)

# frmat of below                 ['Thing to look for in both', 'Thing to add to output'], on 'Thing to look for in both'
df_wb3 = pd.merge(df_wb2, df_wb1[['uniqueid','Theme']], on='uniqueid', how='left')
##print(df_wb3)

# this works, but concatenates ALL   df_wb3 = df_wb2.merge(df_wb1, on="uniqueid", how='left')


df_wb3.to_excel("output4.xlsx", index=False)
