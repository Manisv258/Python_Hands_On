
import pandas as pd
import numpy as np

"""
To read the excel file using Pandas, we need to install (optional) dependency module "xlrd". Otherwise we will
receive this error - "ImportError: Missing optional dependency 'xlrd'"

To install xlrd use this command - pip install xlrd

Use cases:
1. Duplicate the original sheet and keep the content in new sheet within a same excel file.
2. Create new sheet and copy only any two columns from the original sheet
3. Create new sheet and copy contents from original sheet with reordered columns
4. Create new sheet and keep the content which met the certain conditions. eg) year > 2009 or without empty values, etc
5. Create new sheet and concatenate two column values and keep it in single column.
6. Format the any number column as currency

Try all the above with different excel or any other file types.
"""

filename = "Employee_Data1.xlsx"
df = pd.read_excel(filename)
#print(df.keys())

#Use Case 1:
# To fetch the sheet names in an excel file.
sheets = pd.ExcelFile(filename).sheet_names
print(sheets)

df2 = df.copy()
#print(df2)
#df2.to_excel(filename, sheet_name='Test Sheet')

with pd.ExcelWriter(filename, mode='a', if_sheet_exists="replace") as writer:
  #df.to_excel(writer, sheet_name='Original', index=False)
  df2.to_excel(writer, sheet_name='Test Sheet', index=False)

#Use Case 2:
#2. Create new sheet and copy only any two columns from the original sheet
  # Get columns from excel
print(df.columns)
df3 = pd.read_excel(filename, usecols=['Employee Id','Salary'])

with pd.ExcelWriter(filename, mode='a', if_sheet_exists="replace") as writer:
  df3.to_excel(writer, sheet_name='New Test Sheet', index=False)

#Use case 3:
#3. Create new sheet and copy contents from original sheet with reordered columns

df4 = df.iloc[:,[0,3,1,2,4,5,6]]

with pd.ExcelWriter(filename, mode='a', if_sheet_exists="replace") as writer:
  df4.to_excel(writer, sheet_name='Reordered', index=False)

#4. Create new sheet and keep the content which met the certain conditions. eg) year > 2009 or without empty values, etc

# Select rows where Dept is not null
df5 = df[df['Department'] > '']

with pd.ExcelWriter(filename, mode='a', if_sheet_exists="replace") as writer:
  df5.to_excel(writer, sheet_name='Conditions', index=False)

#5. Create new sheet and concatenate two column values and keep it in single column.

# concatenating the DataFrames
df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
print(df['Full Name'])


