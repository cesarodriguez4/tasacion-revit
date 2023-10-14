# coding: utf8

from config import Config
from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox, TextBox, Separator, Button, Alert)

conf = Config()
saved_values = conf.get_config_value('configuration')

vida_probable = "Sin definir"
antiguedad = "Sin definir"
area = "Sin definir"
depreciacion = None
costo_paredes = "Sin definir"
costo_techo = "Sin definir"
estado = {
            'Optimo': 0.0,
            'Muy bueno': 0.032,
            'Bueno': 2.52,
            'Intermedio': 8.09,
            'Regular': 18.10,
            'Deficiente': 32.20,
            'Malo': 52.60,
            'Muy malo': 72.20,
            'Demolicion': 100
        }

if 'vida_probable' in saved_values:
    vida_probable = saved_values['vida_probable']
if 'antiguedad' in saved_values:
    antiguedad = saved_values['antiguedad']
if 'area' in saved_values:
    area = saved_values['area']
if 'depreciacion' in saved_values:
    depreciacion = list(estado.keys())[list(estado.values()).index(saved_values['depreciacion'])]
if 'costo_paredes' in saved_values:
    costo_paredes = saved_values['costo_paredes']
if 'costo_techo' in saved_values:
    costo_techo = saved_values['costo_techo']

components = [
              Label('Estado de conservación:'),
              ComboBox('depreciacion', estado, depreciacion),
              Label("Vida probable (Años):"),
              TextBox('vida_probable', Text=vida_probable),
              Label("Antigüedad (Años):"),
              TextBox('antiguedad', Text=antiguedad),
              Label("Área tapada (m3):"),
              TextBox('area', Text=area),
              Label("Costo de paredes por m2:"),
              TextBox('costo_paredes', Text=costo_paredes),
              Label("Costo de techo por m2:"),
              TextBox('costo_techo', Text=costo_techo),
              Separator(),
              Button('Aceptar')
            ]
form = FlexForm('Configurar parametros del avalúo', components)
form.show()
values = form.values
if len(values) != 0:
    conf.set_config_value('configuration', values)
    Alert('Configuración guardada', "Ajustes")

