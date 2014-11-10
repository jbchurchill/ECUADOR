for /f %%f in ('dir /b *.tiff INPUT_NEW') do (
  echo "Processing %%f"
  gd3trans655s %%f
  gdwarp %%f
)