for /f %%f in ('dir /b *.tiff INPUT') do (
  echo "Processing %%f"
  gdtrans2 %%f
  gdwarp %%f
)