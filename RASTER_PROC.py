import arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
#outws = r"C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\ws4b"
outws = r"C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR2\TEST_OUT"
#inws = r"C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\GEOREF\OUTPUT_655"
inws = r"C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR2\TEST_IN"
theMask = r"C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\ws2\mask04"
# was mask01 in ws3
arcpy.env.workspace = inws
arcpy.env.extent = theMask
arcpy.env.cellSize = theMask
arcpy.env.snapRaster = theMask



try:
  rasterList = arcpy.ListRasters("*", "TIFF")
  neighborhood = NbrRectangle(5, 5, "CELL")
  for raster in rasterList:
    #testing
    print raster
    ConResultA = Con(Raster(raster) < 255, Con(Raster(theMask) == 1, 1, 0), 0)
    ConResultB = Con(Raster(raster) > 5, Con(Raster(theMask) == 1, 1, 0), 0)
    ConResultC = ConResultA + ConResultB
    ConResult = Con(ConResultC == 2, 1, 0)
    
    for x in range(0, 6):
      outFM = "FM" + str(raster[:-5]) + str(x)
      outCon = str(raster[:-5]) + str(x)
      # RUN FOCAL MAJORITY
      FMresult = FocalStatistics(ConResult, neighborhood, "MAJORITY", "")
      # Con (in_conditional_raster, in_true_raster_or_constant, {in_false_raster_or_constant}, {where_clause})
      ConResult2 = Con(IsNull(FMresult), ConResult, FMresult)
      if (x == 5):
        OutPlus = Plus(theMask, ConResult2) # Adding values and then going back to 0, 1 seems to work
        OutCon3 = Con(IsNull(OutPlus), 0, Con(OutPlus == 2, 1, 0))
        OutCon3.save(outws + "\\" + outCon[:-1])

except:
    # If an error occurred print the message to the screen
    print arcpy.GetMessages()  
