import clr
# Add Office reference
clr.AddReference('Microsoft.Office.Interop.Excel')

from Microsoft.Office.Interop import Excel

excel = Excel.ApplicationClass()

excel.Visible = True
excel.DisplayAlerts = False

workbook = excel.Workbooks.Add()
sheet = workbook.ActiveSheet

# Active cell
sheet.Cells(1,1).Value2 = "Hello World"