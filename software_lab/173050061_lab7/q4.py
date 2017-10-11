import pandas as pd
xls_file = pd.ExcelFile('India_Imports_2011-12_And_2012-13.xls')
dfi = xls_file.parse()

xls_file = pd.ExcelFile('India_Exports_2011-12_And_2012-13.xls')
dfe = xls_file.parse()

topI = dfi.groupby('Country')['Value-INR-2011-12'].sum()
topE = dfe.groupby('Country')['Value-INR-2011-12'].sum()


merge = pd.concat([topE, topI],axis=1)
merge.columns = ['exports', 'imports']

merge = merge.query('exports > 1e+11')
print (merge)


