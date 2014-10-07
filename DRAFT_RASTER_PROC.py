import arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
outws = r"C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\ws4"
inws = r"C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\GEOREF\OUTPUT_655"
theMask = r"C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\ws2\mask02"
# was mask01 in ws3
arcpy.env.workspace = inws


try:
  rasterList = arcpy.ListRasters()
  neighborhood = NbrRectangle(5, 5, "CELL")
  for raster in rasterList:
    #testing
    print raster
    ConResult = Con(Raster(raster) < 255, Con(Raster(theMask) == 1, 1, 0), 0)
    for x in range(0, 4):
      outFM = "FM" + str(raster[:-5]) + str(x)
      outCon = str(raster[:-5]) + str(x)
      # RUN FOCAL MAJORITY
      FMresult = FocalStatistics(ConResult, neighborhood, "MAJORITY", "")
      # Con (in_conditional_raster, in_true_raster_or_constant, {in_false_raster_or_constant}, {where_clause})
      ConResult2 = Con(IsNull(FMresult), ConResult, FMresult)
      if (x == 3):
        ConResult2.save(outws + "\\" + outCon)

except:
    # If an error occurred print the message to the screen
    print arcpy.GetMessages()  
