SET x1=4
SET x2=586
SET x3=239
SET x4=287
SET x5=68
SET x6=19
SET y1=366
SET y2=167
SET y3=6
SET y4=507
SET y5=570
SET y6=256
SET XSHIFT=0
SET YSHIFT=0
IF %1 == frma.tiff (
SET XSHIFT=83
)
IF %1 == ocgr.tiff (
SET XSHIFT=172
)
IF %1 == ocho.tiff (
SET XSHIFT=28
)
IF %1 == ochor.tiff (
SET XSHIFT=94
)
IF %1 == ocma.tiff (
SET XSHIFT=50
)
IF %1 == ocme.tiff (
SET XSHIFT=166
)
IF %1 == ocmi.tiff (
SET XSHIFT=166
)
IF %1 == ococ.tiff (
SET XSHIFT=172
)
IF %1 == octe.tiff (
SET XSHIFT=167
)
IF %1 == pema.tiff (
SET XSHIFT=67
)
IF %1 == phae.tiff (
SET XSHIFT=167
)
IF %1 == prae.tiff (
SET XSHIFT=94
)
IF %1 == prpa.tiff (
SET XSHIFT=167
)
IF %1 == pucr.tiff (
SET XSHIFT=167
)
IF %1 == pugr.tiff (
SET XSHIFT=167
)
IF %1 == pulh.tiff (
SET XSHIFT=16
)
IF %1 == sone.tiff (
SET XSHIFT=78
)
IF %1 == sugr.tiff (
SET XSHIFT=89
)
SET /a x1b=%XSHIFT%+%x1%
SET /a x2b=%XSHIFT%+%x2%
SET /a x3b=%XSHIFT%+%x3%
SET /a x4b=%XSHIFT%+%x4%
SET /a x5b=%XSHIFT%+%x5%
SET /a x6b=%XSHIFT%+%x6%
SET /a y1b=%YSHIFT%+%y1%
SET /a y2b=%YSHIFT%+%y2%
SET /a y3b=%YSHIFT%+%y3%
SET /a y4b=%YSHIFT%+%y4%
SET /a y5b=%YSHIFT%+%y5%
SET /a y6b=%YSHIFT%+%y6%
gdal_translate -of GTiff -gcp %x1b% %y1b% 498353 9.75475e+06 -gcp %x2b% %y2b% 1.13853e+06 9.99319e+06 -gcp %x3b% %y3b% 747172 1.01571e+07 -gcp %x4b% %y4b% 818043 9.6109e+06 -gcp %x5b% %y5b% 572611 9.5335e+06 -gcp %x6b% %y6b% 508386 9.87613e+06 "SHIFTED_655\%1" "TMP\%1"