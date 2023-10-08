from Autodesk.Revit.DB import FilteredElementCollector, FamilySymbol, FamilyInstance, BuiltInCategory
from pyrevit import script

class Avaluos:
    
    def __init__(self, doc, coef, antiguedad, vida_probable, long_paredes):
        self.coef = coef
        self.antiguedad = antiguedad
        self.vida_probable = vida_probable
        self.long_paredes = long_paredes
        self.doc = doc
           
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
          
    def print_table(self):
        data = self.get_family_instances_with_costs()
        # instances_with_costs = [Name, Number of items, Cost, total cost]
        # sum all total cost in instances_with_costs
        total_costs = 0
        for instance_with_cost in data:
            total_costs += instance_with_cost[3]
    
        output = script.get_output()    
        output.print_table(data, title='Resumen de costos' , columns=["Elemento", "Cantidad", "Costo", "Total"])
        print("Costos totales", total_costs, ' USD')
