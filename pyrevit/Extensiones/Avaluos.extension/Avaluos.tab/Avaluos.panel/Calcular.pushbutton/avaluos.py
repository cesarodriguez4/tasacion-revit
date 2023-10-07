class Avaluos:
    def __init__(self, coef, antiguedad, vida_probable, long_paredes):
        self.coef = coef
        self.antiguedad = antiguedad
        self.vida_probable = vida_probable
        self.long_paredes = long_paredes   
    @staticmethod
    def calculate_total_price(doc):
        # Obtenemos todos los tipos de familia en Revit
        family_types = FilteredElementCollector(doc).OfClass(FamilySymbol)
        
        # Crear un diccionario para guardar el parametro de costo para cada tipo de familia
        cost_parameter_dict = {}
        
        # Iterar sobre todas los tupos de familia y guardar el parametro de costo
        for family_type in family_types:
            cost_parameter = family_type.LookupParameter("Cost")
            if cost_parameter:
                cost_parameter_dict[family_type.Id] = cost_parameter.AsDouble()
        
        # Iterar sobre todos los elementos de familia en el documento y calcular el precio total
        total_price = 0
        family_instances = FilteredElementCollector(doc).OfClass(FamilyInstance)
        for family_instance in family_instances:
            family_type_id = family_instance.Symbol.Id
            if family_type_id in cost_parameter_dict:
                cost_parameter_value = cost_parameter_dict[family_type_id]
                total_price += cost_parameter_value
        
        return total_price
        
    
    def costo_depreciado(self):
        return 0
    
    def hello_world(self):
        print("Hello World loco!")