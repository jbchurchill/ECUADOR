for /f %%f in ('dir /b *.tiff INPUT') do (
  echo "Processing %%f"
  gdtrans %%f
  gdwarp %%f
)