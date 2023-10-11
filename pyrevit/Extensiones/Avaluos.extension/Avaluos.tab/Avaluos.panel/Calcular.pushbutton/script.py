# coding: utf8

from avaluos import Avaluos
from config import Config
from rpw.ui.forms import (Alert)

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
  
    
# Current doc in Revit
doc = __revit__.ActiveUIDocument.Document
avaluo = Avaluos(doc, coef_depreciacion, antiguedad, vida_probable, area)

# now that results are collected, print the total
print(avaluo.print_costs_as_new_table())
print(avaluo.print_deprecation_table())