import clr
# Add Office reference
clr.AddReference('Microsoft.Office.Interop.Excel')

from Microsoft.Office.Interop import Excel

logs = []

logs.append(path)

# Print hello world in the excel file
excel = Excel.ApplicationClass()

excel.Visible = True
excel.DisplayAlerts = False

# Open blank sheet
workbook = excel.Workbooks.Add()
sheet = workbook.ActiveSheet


logs.append(dir(excel))

OUT = logs

