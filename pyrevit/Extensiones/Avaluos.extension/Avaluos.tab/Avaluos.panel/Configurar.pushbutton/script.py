from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox, TextBox, Separator, Button)

components = [Label('Estado:'),  ComboBox('depreciacion', 
                                                         {
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
                                                         ),
              Label("Vida probable (Years):"),
              TextBox('vida_probable', Text="75"),
              Label("Antiguedad (Years):"),
              TextBox('antiguedad', Text="43"),
              Separator(),
               Button('Aceptar')
            ]
form = FlexForm('Configurar parametros del avaluo', components)
form.show()
