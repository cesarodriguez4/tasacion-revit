from avaluos import Avaluos

# Current doc in Revit
doc = __revit__.ActiveUIDocument.Document
avaluo = Avaluos(doc, 1, 1, 1, 1)

# now that results are collected, print the total
print(avaluo.print_table())