import pandas as pd
import numpy as np
xls_file = pd.ExcelFile('India_Imports_2011-12_And_2012-13.xls')
dfi = xls_file.parse()

xls_file = pd.ExcelFile('India_Exports_2011-12_And_2012-13.xls')
dfe = xls_file.parse()

co12I = dfi.groupby('Commodity')['Value-INR-2011-12'].sum().sort_values(ascending=False)
co12E = dfe.groupby('Commodity')['Value-INR-2011-12'].sum().sort_values(ascending=False)
co13I = dfi.groupby('Commodity')['Value-INR-2012-13'].sum().sort_values(ascending=False)
co13E = dfe.groupby('Commodity')['Value-INR-2012-13'].sum().sort_values(ascending=False)




merge12 = pd.concat([co12E, co12I],axis=1)
merge12.columns = ['exports', 'imports']
temp = pd.DataFrame(merge12.index.values, index = np.arange(merge12.index.values.size))
merge12 = merge12.set_index(np.arange(merge12.index.values.size))
merge12 = pd.concat([temp, merge12],axis=1)
merge12.columns = ['Commodity', 'Exports', 'Imports']




merge13 = pd.concat([co13E, co13I],axis=1)
merge13.columns = ['exports', 'imports']
temp = pd.DataFrame(merge13.index.values, index = np.arange(merge13.index.values.size))
merge13 = merge13.set_index(np.arange(merge13.index.values.size))
merge13 = pd.concat([temp, merge13],axis=1)
merge13.columns = ['Commodity', 'Exports', 'Imports']


merge = pd.concat([merge12, merge13],axis=0)


merge = merge.groupby('Commodity').sum()
# print (merge)
# print (merge13)

merge = merge.query('Exports > 0')
merge = merge.query('Imports > 0')
print (merge)
