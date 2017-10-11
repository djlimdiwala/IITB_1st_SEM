import pandas as pd
xls_file = pd.ExcelFile('India_Imports_2011-12_And_2012-13.xls')
dfi = xls_file.parse()

xls_file = pd.ExcelFile('India_Exports_2011-12_And_2012-13.xls')
dfe = xls_file.parse()

topI = dfi.groupby('Country')['Value-INR-2011-12'].sum().sort_values(ascending=False).head()
topE = dfe.groupby('Country')['Value-INR-2011-12'].sum().sort_values(ascending=False).head()

topI.columns = ['imports']
topE.columns = ['exports']
print (topI)
print (topE)