#[Membaca file menggunakan Pandas]
import csv
import pandas as pd

csv_data = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/shopping_data.csv')
print(csv_data)


#[Membaca file dengan fungsi Head()]
#[Fungsi] menampilkan sebagian data awal tabel
print(csv_data.head())


#[Melakukan akses KOLOM]
#[Fungsi] mengetahui semua nama KOLOM
print(csv_data.columns)

#[Fungsi] mengakses data KOLOM
print(csv_data['Age'])


#[Melakukan akses BARIS]
#[Mengakses semua data pada indeks BARIS]
print(csv_data.iloc[5])


#[Menampilkan suatu data dari BARIS dan KOLOM tertentu]
print(csv_data['Age'].iloc[1])
print('bisa di cek pada cuplikan data set, KOLOM Age & BARIS 1')


#[Menampilkan data dalam RANGE tertentu]
#[Akses RANGE pada suatu kolom dan baris]
print(csv_data['Age'].iloc[5:10])

#[Akses RANGE pada suatu BARIS saja]
print(csv_data.iloc[5:10])


#[Menampilkan INFO STATISTIK dengan NUMPY]
#[Menampilkan semua informasi]
print(csv_data.describe(include='all'))

#[Menampilkan informasi: NUMERICAL saja]
print(csv_data.describe(exclude=['O']))
