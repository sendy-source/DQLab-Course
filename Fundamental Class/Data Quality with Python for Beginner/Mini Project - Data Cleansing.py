# Data Cleansing Part 1 - Dataset uncleaned_raw
# Data cleansing dilakukan setelah semua Missing Value di treatment

# Mengetahui kolom yang memiliki outliers dengan boxplot
import pandas as pd
import numpy as np
import io
import pandas_profiling
import matplotlib.pyplot as plt

plt.style.use('default')

uncleaned_raw = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/uncleaned_raw.csv')
uncleaned_raw['Quantity'] = uncleaned_raw['Quantity'].fillna(uncleaned_raw['Quantity'].mean())

# Mengetahui kolom yang memiliki outliers!
# Outliers adalah titik di luar range
# Mean adalah yang garis berwarna merah.
# Median adalah garis yang berwarna Biru Tua.
fig, ax = plt.subplots()
uncleaned_raw.boxplot(vert=True, showmeans=True, patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'blue'},
           meanprops={'linewidth': 2, 'color': 'red'})
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000).astype(int))
plt.show()


# Data Cleansing Part 2 - Dataset uncleaned_raw

# Melakukan proses removing outliers pada kolom UnitPrice.
#Check IQR
Q1 = uncleaned_raw['UnitPrice'].quantile(0.25)
Q3 = uncleaned_raw['UnitPrice'].quantile(0.75)
IQR = Q3 - Q1

#removing outliers
uncleaned_raw = uncleaned_raw[~((uncleaned_raw[['UnitPrice']] < (Q1 - 1.5 * IQR)) | (uncleaned_raw[['UnitPrice']] > (Q3 + 1.5 * IQR)))]

# Checking duplikasi dan melakukan deduplikasi dataset tersebut!
#check for duplication
print(uncleaned_raw.duplicated(subset=None))

#remove duplication
uncleaned_raw = uncleaned_raw.drop_duplicates()
