for /f %%f in ('dir /b *.tiff SHIFTED_655') do (
  echo "Processing %%f"
  gdtrans655s %%f
  gdwarp %%f
)