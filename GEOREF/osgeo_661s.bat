for /f %%f in ('dir /b *.tiff SHIFTED_661') do (
  echo "Processing %%f"
  gdtrans661s %%f
  gdwarp %%f
)