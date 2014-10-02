for /f %%f in ('dir /b *.tiff INPUT_655') do (
  echo "Processing %%f"
  gdtrans655 %%f
  gdwarp %%f
)