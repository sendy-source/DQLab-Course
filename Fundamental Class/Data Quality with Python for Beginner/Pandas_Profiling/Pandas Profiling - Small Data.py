# Doing Profiling on a smaller dataset: 
import pandas as pd
import pandas_profiling
df2 = pd.read_csv('D:\DQLab-course\Fundamental Class\Data Quality with Python for Beginner\Pandas_Profiling\corona_dataset')

profile2 = df2.profile_report(title="Corona Small dataset report")

# Export into an HTML report
profile2.to_file(output_file="Pandas Profiling Report Small Data.html")