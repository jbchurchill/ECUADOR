for /f %%f in ('dir /b *.tiff INPUT_661') do (
  echo "Processing %%f"
  gdtrans661 %%f
  gdwarp %%f
)