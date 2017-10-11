import pandas as pd
xls_file = pd.ExcelFile('India_Imports_2011-12_And_2012-13.xls')
dfi = xls_file.parse()

xls_file = pd.ExcelFile('India_Exports_2011-12_And_2012-13.xls')
dfe = xls_file.parse()

topI = dfi.groupby('Country')['Value-INR-2011-12'].sum()
topE = dfe.groupby('Country')['Value-INR-2011-12'].sum()

cat = pd.concat([topI, topE],axis=1)
cat.columns = ['Total_Imports','Total_Exports']
cat['Exp/imp_ratio'] = cat['Total_Exports'] / cat['Total_Imports']
cat['Trade deficit'] = cat['Total_Exports'] - cat['Total_Imports']

print (cat)