import pandas as pd
xls_file = pd.ExcelFile('India_Imports_2011-12_And_2012-13.xls')
dfi = xls_file.parse()

xls_file = pd.ExcelFile('India_Exports_2011-12_And_2012-13.xls')
dfe = xls_file.parse()

topI = dfi.groupby('Country')['Value-INR-2011-12'].sum()
topE = dfe.groupby('Country')['Value-INR-2011-12'].sum()
# .sort_values(ascending=False).head()
# print (topE)

ii = pd.concat([topI, topE],axis=1)
ii.columns = ['imports','exports']
ii['ie_ratio'] = ii['exports'] / ii['imports']
print (ii)

# coI = dfi.groupby('Commodity')['Value-INR-2011-12'].count().sort_values(ascending=False).head()
# coE = dfe.groupby('Commodity')['Value-INR-2011-12'].count().sort_values(ascending=False).head()

# print (coI)
# print (coE)