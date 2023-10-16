# coding: utf8
from pyrevit import script

output = script.get_output()
output.print_md("## Acerca de")
output.print_md("Trabajo de grado para optar al título de ingeniero civil")
output.print_image(r'C:\Users\cesar\source\repos\tasacion-revit\pyrevit\Extensiones\Avaluos.extension\Avaluos.tab\Avaluos.panel\Acerca.pushbutton\uc_logo.png')
output.print_md("Universidad de Carabobo")
output.print_md("Todos los derechos reservados")
output.print_md("Valencia, octubre de 2023")
output.print_md("## Contacto")
output.print_md("Email: cesarodriguez4@gmail.com")

