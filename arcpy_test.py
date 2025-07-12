import sys
import arcpy

param = sys.argv[1]
print(f"You passed: {param}")

try:
    print(arcpy.GetCount_management(param).getOutput(0))
except Exception as e:
    raise e