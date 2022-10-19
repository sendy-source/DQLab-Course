#[Handling missing value]
'''
penanggulangan data yang hilang
saat berhubungan dengan data real, solusi pertama adalah
melakukan trace back ke sumber data atau memeriksa record (data human record)
'''

#[Pengecekan nilai null pada data]
print('Pengecekan nilai null pada data:')
import pandas as pd

csv_data = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/shopping_data_missingvalue.csv')

#[True] = terdapat data kosong
#[False] = data lengkap
print(csv_data.isnull().values.any())

#[Solusi missing value]
'''
Data Outlier merupakan data yang memiliki karakteristik yang berbeda jauh
dari observasi-observasi lainnya dan muncul dalam bentuk nilai ekstrim 
baik untuk variabel tunggal atau variabel kombinasi
'''

print() #[1. Mengisi dengan MEAN]
#Mean sendiri digunakan untuk data yang memiliki sedikit sifat outlier/noisy/anomali dalam sebaran datanya maupun isinya

print('Mengisi dengan MEAN:')
print(csv_data.mean())
print('Dataset yang masih terdapa nilai kosong !')
print(csv_data.head(10))

csv_data_avg = csv_data.fillna(csv_data.mean())
print('Dataset yang sudah diproses Handling Missing Value dengan MEAN:')
print(csv_data_avg.head(10))


print() #[2. Mengisi dengan Median]
#Median digunakan untuk data-data yang memiliki sifat outlier yang kuat

print('Mengisi dengan MEDIAN:')
print('Dataset yang masing terdapat nilai kosong !:')
print(csv_data.head(10))

csv_data_Med = csv_data.fillna(csv_data.median())
print('Dataset yang sudah diproses Handling Missing Value dengan MEDIAN :')
print(csv_data_Med.head(10))


print()
print() #[Normalisasi Data]
#[Fungsi] Mengatasi kasus 1 kolom dengan kolom yang lain, memiliki SKALA yang berbeda

print('Normalisasi menggunakan Scikitlearn:')
#import pandas ad pd
import numpy as np
from sklearn import preprocessing

#csv_data = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/shopping_data_missingvalue.csv')
#array disini : menggunakan data yang sudah dilakukan Handling Missing Values dengan AVERAGE
array = csv_data_avg.values 

X = array[:,2:5] #memisahkan fitur dari dataset
Y = array[:,0:1] #memisahkan class dari dataset

#memahami isi data yang di array
print(array[:3])
print(X[:3])
print(Y[:3])

dataset = pd.DataFrame({'Customer ID':array[:,0], 'Gender':array[:,1], 'Age':array[:,2], 'Income':array[:,3], 'Spending Score':array[:,4]})
print('dataset sebelum dinormalisasi :')
print(dataset.head())

#inisialisasi normalisasi MinMax
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
data = min_max_scaler.fit_transform(X)  #transformasi MinMax untuk fitur
dataset = pd.DataFrame({'Age':data[:,0], 'Income':data[:,1], 'Spending Score':data[:,2], 'Customer ID':array[:,0], 'Gender':array[:,1]})
print('Dataset setalah normalisasi :')
print(dataset.head(10))