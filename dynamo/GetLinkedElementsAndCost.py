active_view = doc.ActiveView

elements = FilteredElementCollector(doc, active_view.Id).WhereElementIsNotElementType()

for element in elements:
  if (element.Name == 'Genérico - 200 mm'):
    elementType = doc.GetElement(element.GetTypeId())
    # print elementType properties
    for parameter in elementType.Parameters:
      if (parameter.Definition.Name == 'Costo'):
        print('Costo:', parameter.AsValueString())