import pandas as pd
import numpy as np
xls_file = pd.ExcelFile('India_Imports_2011-12_And_2012-13.xls')
dfi = xls_file.parse()
xls_file = pd.ExcelFile('India_Exports_2011-12_And_2012-13.xls')
dfe = xls_file.parse()

topI = dfi.groupby('Country')['Value-INR-2011-12'].sum()
topE = dfe.groupby('Country')['Value-INR-2011-12'].sum()


merge = pd.concat([topE, topI],axis=1)
merge.columns = ['exports', 'imports']

merge = merge.query('exports > 1e+11')


temp = pd.DataFrame(merge.index.values, index = np.arange(merge.index.values.size))
merge = merge.set_index(np.arange(merge.index.values.size))
merge = pd.concat([temp, merge],axis=1)
merge.columns = ['Country', 'Exports', 'Imports']
# print (merge)


melted = pd.melt(merge, id_vars = ['Country'], var_name = 'Transaction', value_name = 'Value').sort_values(['Value'],ascending = False).head(n=10)

print (melted)