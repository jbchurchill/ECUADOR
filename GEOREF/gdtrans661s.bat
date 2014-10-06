SET y1=366
SET y2=167
SET y3=6
SET y4=507
SET y5=570
SET y6=256
IF %1 == daca.tiff (
SET x1=9
SET x2=591
SET x3=245
SET x4=292
SET x5=73
SET x6=24

)
IF %1 == phir.tiff (
SET x1=170
SET x2=752
SET x3=405
SET x4=453
SET x5=234
SET x6=185
)
gdal_translate -of GTiff -gcp %x1% %y1% 498646 9.75808e+06 -gcp %x2% %y2% 1.13967e+06 9.98832e+06 -gcp %x3% %y3% 736633 1.01607e+07 -gcp %x4% %y4% 812548 9.61267e+06 -gcp %x5% %y5% 576335 9.53561e+06 -gcp %x6% %y6% 510282 9.88275e+06 "SHIFTED_661\%1" "TMP\%1"