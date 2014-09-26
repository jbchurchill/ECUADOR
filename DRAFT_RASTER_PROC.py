# Import system modules
# import sys, string, os, time, arcpy
import arcpy
# is this next part necessary ?
from arcpy.sa import *
arcpy.env.workspace = "C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\ws2\"

try:
  rasterList = arcpy.ListRasters()
  for raster in rasterList:
    #testing
    print raster
    ConResult = Con(Raster(raster) < 255, Con("mask01" == 1, 1, 0), 0)
    for x in range(0, 3):
      outname = "XXXX" + x
      # RUN FOCAL MAJORITY
      # FMresult = ?????????
      # Con (in_conditional_raster, in_true_raster_or_constant, {in_false_raster_or_constant}, {where_clause})
      ConResult = Con(IsNull(FMresult), ConResult, FMresult)
      ConResult.save(arcpy.env.workspace + outname)
      # CITI03B = Con(IsNull("CITI02F5"), "CITI02", "CITI02F5")
      # RUN CON

except:
    # If an error occurred print the message to the screen
    print arcpy.GetMessages()  