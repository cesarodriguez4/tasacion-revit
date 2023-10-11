# coding: utf8

from Autodesk.Revit.DB import FilteredElementCollector, FamilySymbol, FamilyInstance, BuiltInCategory
from pyrevit import script

class Avaluos:
    
    def __init__(self, doc, coef, antiguedad, vida_probable, area):
        self.coef = coef
        self.antiguedad = antiguedad
        self.vida_probable = vida_probable
        self.area = area
        self.doc = doc
        self.usd_ves = 33
           
    def get_family_instances_with_costs(self):
        # Obtenemos todos los tipos de familia en Revit
        family_types = FilteredElementCollector(self.doc).OfClass(FamilySymbol)
        # Crear un diccionario para guardar el parametro de costo para cada tipo de familia
        cost_parameter_dict = {}
        # Iterar sobre todas los tupos de familia y guardar el parametro de costo
        # instances_with_costs = [Name, Number of items, Cost, total cost]
        instances_with_costs = []
        for family_type in family_types:
            # Show all available parameters
            cost_parameter = family_type.LookupParameter("Costo")
            if cost_parameter:
                cost_parameter_dict[family_type.Id] = cost_parameter.AsDouble()
        
        # Iterar sobre todos los elementos de familia en el documento y calcular el precio total
        family_instances = FilteredElementCollector(self.doc).OfClass(FamilyInstance)
        for family_instance in family_instances:
            family_type_id = family_instance.Symbol.Id
            family_name = family_instance.Symbol.FamilyName
            if family_type_id in cost_parameter_dict:
                cost_parameter_value = cost_parameter_dict[family_type_id]
                family_name = family_instance.Symbol.FamilyName
                # If there is an element in instances_with_costs with the same name
                # then add the cost to the total
                found = False
                for instance_with_cost in instances_with_costs:
                    if instance_with_cost[0] == family_name:
                        instance_with_cost[1] += 1
                        instance_with_cost[3] += cost_parameter_value
                        found = True
                        break
                if not found:
                    instances_with_costs.append([family_name, 1, cost_parameter_value, cost_parameter_value])
        return instances_with_costs
    
    
    
    def get_walls_length(self):
        # Obtenemos todas las paredes en el documento
        walls = FilteredElementCollector(self.doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
        # Sumar la longitud de todas las paredes
        total_length = 0
        print(walls[0].LookupParameter("Length"))
        
        
    def get_total_cost_as_new(self, data):
        total_costs = 0
        for instance_with_cost in data:
            total_costs += instance_with_cost[3]
        return total_costs
          
    def print_costs_as_new_table(self):
        data = self.get_family_instances_with_costs()
        total_costs = self.get_total_cost_as_new(data)   
        output = script.get_output()    
        output.print_table(data, title='Resúmen de costos' , columns=["Elemento", "Cantidad", "Costo", "Total"])
        output.print_md("Total VES: **{}** VES".format(total_costs * self.usd_ves))
        output.print_md("Total USD: **{}** USD".format(total_costs))
        
    def print_deprecation_table(self):
        data = self.get_family_instances_with_costs()
        total_costs = self.get_total_cost_as_new(data)   
        deprecation_cost = self.ross_heidecke(total_costs)
        output = script.get_output()
        output.print_md("**Cálculo de depreciación por Ross-Heidecke**")
        output.print_image(r'C:\Users\cesar\source\repos\tasacion-revit\pyrevit\Extensiones\Avaluos.extension\Avaluos.tab\Avaluos.panel\Calcular.pushbutton\rossheidecke.png')
        output.print_md("Valor actual VES: **{}** VES".format(deprecation_cost * self.usd_ves))
        output.print_md("Valor actual USD: **{}** USD".format(deprecation_cost))
        output.print_md("Costo por metro cuadrado: **{}** USD".format(deprecation_cost / self.area))
        
    
        
    def ross_heidecke(self, value_as_new):
        e_factor = (100 - self.coef) / 100
        x = self.antiguedad
        n = self.vida_probable
        return value_as_new *(1 - 1/2*((x/n)+(x**2/n**2))) * e_factor
    
        
