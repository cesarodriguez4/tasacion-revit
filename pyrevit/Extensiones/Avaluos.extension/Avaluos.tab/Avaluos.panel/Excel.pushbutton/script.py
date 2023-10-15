"""Exporta el resultado de la tasacion a un archivo de Microsoft Excel."""
import clr
from avaluos import Avaluos
clr.AddReference('Microsoft.Office.Interop.Excel')
from config import Config
from rpw.ui.forms import (Alert)
from Microsoft.Office.Interop import Excel

conf = Config()
saved_values = conf.get_config_value('configuration')
vida_probable = None
antiguedad = None
area = None
coef_depreciacion = None

if 'vida_probable' in saved_values:
    vida_probable = float(saved_values['vida_probable'])
else:
    Alert('Debe registrar una vida probable a la vivienda en ajustes', "Atencion")
  
if 'antiguedad' in saved_values:
    antiguedad = float(saved_values['antiguedad'])
else:
    Alert('Debe registrar una antiguedad a la vivienda en ajustes', "Atencion")
    
if 'area' in saved_values:
    area = float(saved_values['area'])
else:
    Alert('Debe registrar un area a la vivienda en ajustes', "Atencion")
    
if 'depreciacion' in saved_values:
    coef_depreciacion = float(saved_values['depreciacion'])
else:
    Alert('Debe registrar un coeficiente de depreciacion a la vivienda en ajustes', "Atencion")
    
if 'costo_construccion' in saved_values:
    costo_construccion = float(saved_values['costo_construccion'])
else:
    Alert('Debe registrar un costo de paredes a la vivienda en ajustes', "Atencion")
    
# Current doc in Revit
doc = __revit__.ActiveUIDocument.Document
avaluo = Avaluos(doc, coef_depreciacion, antiguedad, vida_probable, area, costo_construccion)

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
 
# Blank space
row += 2

sheet.Cells(row, 1).Value2 = "Detalle"
sheet.Cells(row, 2).Value2 = "Area"
sheet.Cells(row, 3).Value2 = "Costo de construccion por m2"
sheet.Cells(row, 4).Value2 = "Coste Total"
sheet.Cells(row, 5).Value2 = "USD"

row += 1
    
# Print total cost at the end
total_cost = avaluo.get_total_cost_as_new()
sheet.Cells(row, 1).Value2 = "Costo construccion como nuevo"
sheet.Cells(row, 2).Value2 = avaluo.area
sheet.Cells(row, 3).Value2 = avaluo.costo_construccion
sheet.Cells(row, 4).Value2 = total_cost
sheet.Cells(row, 5).Value2 = ""

row +=1

# Print total with depreciation
total_costs = avaluo.get_total_cost_as_new() 
deprecation_cost = avaluo.ross_heidecke(total_costs)

sheet.Cells(row, 1).Value2 = "Valor actual (Formula Ross-Heidecke aplicada)"
sheet.Cells(row, 2).Value2 = avaluo.area
sheet.Cells(row, 3).Value2 = deprecation_cost / avaluo.area
sheet.Cells(row, 4).Value2 = deprecation_cost
sheet.Cells(row, 5).Value2 = ""

# Adjust the cell values to content
sheet.Columns.AutoFit()

