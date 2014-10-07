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
IF %1 == ocgr.tiff (
SET XSHIFT=172
SET /a x1b=%XSHIFT%+%x1%
SET /a x2b=%XSHIFT%+%x2%
SET /a x3b=%XSHIFT%+%x3%
SET /a x4b=%XSHIFT%+%x4%
SET /a x5b=%XSHIFT%+%x5%
SET /a x6b=%XSHIFT%+%x6%
echo ocgr %x1b% %x2b% %x3b% %x4b% %x5b% %x6b%
)