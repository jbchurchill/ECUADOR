for f in *.tif
do
  echo "Processing $f"
  gdal_translate -of GTiff -gcp 2.01299 182.543 498646 9.75808e+06 -gcp 293.113 83.5611 1.13967e+06 9.98832e+06 -gcp 117.885 2.24701 736633 1.01607e+07 -gcp 142.97 253.152 812548 9.61267e+06 -gcp 34.0952 284.723 576335 9.53561e+06 -gcp 8.80097 121.934 510282 9.88275e+06 $f "C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\TMP\$f"
  gdalwarp -r near -order 1 -co COMPRESS=NONE  "C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\TMP\$f" "C:\Users\jchurchill\TMP_WORK\TMP_BIRDSEYE\ECUADOR\OUTPUT\$f"
done