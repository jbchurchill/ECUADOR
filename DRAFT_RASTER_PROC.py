# Import system modules
# import sys, string, os, time, arcpy
import arcpy
# is this next part necessary ?
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
#arcpy.env.workspace = r"C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\ws2"
outws = r"C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\ws3"
inws = r"C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\GEOREF\OUTPUT_RENAMED"
theMask = r"C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\ws2\mask01"
arcpy.env.workspace = inws


try:
  rasterList = arcpy.ListRasters()
  neighborhood = NbrRectangle(5, 5, "CELL")
  for raster in rasterList:
    #testing
    print raster
    ConResult = Con(Raster(raster) < 255, Con(Raster(theMask) == 1, 1, 0), 0)
    for x in range(0, 3):
      outFM = "FM" + str(raster[:-6]) + str(x)
      outCon = str(raster[:-6]) + str(x)
      # RUN FOCAL MAJORITY
      FMresult = FocalStatistics(ConResult, neighborhood, "MAJORITY", "")
      ### Do I need to save it ?????
      # FMresult.save(outws + "\\" + outFM)
      ### Do I need to save it ?????
      # FMresult = ?????????
      # Con (in_conditional_raster, in_true_raster_or_constant, {in_false_raster_or_constant}, {where_clause})
      ConResult2 = Con(IsNull(FMresult), ConResult, FMresult)
      ConResult2.save(outws + "\\" + outCon)
      # CITI03B = Con(IsNull("CITI02F5"), "CITI02", "CITI02F5")
      # RUN CON

except:
    # If an error occurred print the message to the screen
    print arcpy.GetMessages()  
