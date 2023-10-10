"""Calculates total volume of all walls in the model."""
from avaluos import Avaluos
import clr
clr.AddReference('Microsoft.Office.Interop.Excel')
from Microsoft.Office.Interop import Excel
doc = __revit__.ActiveUIDocument.Document
avaluo = Avaluos(doc, 1, 1, 1, 1)

cost_values = avaluo.get_family_instances_with_costs()

excel = Excel.ApplicationClass()

excel.Visible = True
excel.DisplayAlerts = False

workbook = excel.Workbooks.Add()
sheet = workbook.ActiveSheet

# # Active cell
# sheet.Cells(1,1).Value2 = "Hello World"
sheet.Cells(1,1).Value2 = "Elemento"
sheet.Cells(1,1).Font.Bold = True
sheet.Cells(1,2).Value2 = "Cantidad"
sheet.Cells(1,2).Font.Bold = True
sheet.Cells(1,3).Value2 = "Costo"
sheet.Cells(1,3).Font.Bold = True
sheet.Cells(1,4).Value2 = "Total"
sheet.Cells(1,4).Font.Bold = True

# From cell 2 start printing cost_values
# cost_values has this shape [['Puerta abatible con ventana', 1, 950.0, 950.0], ...]
row = 2
for cost_value in cost_values:
    sheet.Cells(row,1).Value2 = cost_value[0]
    sheet.Cells(row,2).Value2 = cost_value[1]
    sheet.Cells(row,3).Value2 = cost_value[2]
    sheet.Cells(row,4).Value2 = cost_value[3]
    row += 1

# Adjust the cell values to content
sheet.Columns.AutoFit()

