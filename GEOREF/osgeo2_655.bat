for /f %%f in ('dir /b *.tiff INPUT_655') do (
  echo "Processing %%f"
  gd2trans655s %%f
  gdwarp %%f
)