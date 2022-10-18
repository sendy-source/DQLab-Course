#[Membaca Teks File (CSV) - Onilne]
import requests
from contextlib import closing
import csv

# tentukan lokasi file, nama file, dan inisialisasi csv
url = 'https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv'

# baca file secara streaming
with closing(requests.get(url, stream=True)) as r:
	f = (line.decode('utf-8') for line in r.iter_lines())
	
	reader = csv.reader(f, delimiter=',')
	
	#membaca baris per baris
	for row in reader:
		print(row)


#MEMBACA FILE DARI DIREKTORI LOCAL KOMPUTER]
import csv

# tentukan lokasi file, nama file, dan inisialisasi csv
f = open('D:\Dataset\diabetes.csv', 'r')
reader = csv.reader(f)

# membaca baris per baris
for row in reader:
     print (row)

# menutup file csv
f.close()


#[Membaca file CSV dengan menggunakan PANDAS]
import pandas as pd
pd.set_option("display.max_columns",50)

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
print(table)
