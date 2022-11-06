# Doing Profiling on a Largest dataset: 
import pandas as pd
import pandas_profiling

# Read Dataset
df = pd.read_csv("D:\DQLab-course\Fundamental Class\Data Quality with Python for Beginner\Pandas_Profiling\worldometer_coronavirus_daily_data.csv")

# Generating Profile Report for Large Dataset
profile = df.profile_report(title="Pandas Profiling Report")

# Export this into an HTML report
profile.to_file(output_file="Pandas Profiling Report:Corona Case.html")

'''
Hasil masih belum keluar seperti pandas profiling Small data
1. Mungkin data terlalu besar
2. Mungkin file csv-nya bermasalah
3. Perlu dipelajari lagi
'''