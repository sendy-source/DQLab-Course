'''
Tugas Praktek : Membuat quick summary
1. membuat quick summary dari segi kuantitas, harga, freight value dan weight yang dibeli konsumen
2. menghitung median dari total pembelian konsumen per transaksi
'''
import pandas as pd

order_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/order.csv')
# Quick summary dari segi kuantitas, harga, freight value, dan weight (type:numeric)
print(order_df.describe())
# Median dari total pembelian konsumen per transaksi
print(order_df.loc[:, 'price'].median())


'''
Tugas Praktek : Membuat price distribusi dari pembelian produk dari data order.csv
Tugas ini dapat diartikan : membuat histogram price
Menggunakan jumlah bins 10
'''
import matplotlib.pyplot as plt
# menggunakan data order.csv yang sudah diimport
# membuat plot histogram kolom: price
order_df[['price']].hist(figsize=(4,5), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()


'''
Tugas Praktek : Groupby dengan Pandas
Cobalah untuk mencari rata rata dari price per payment_type dari dataset order_df
'''
# Data sudah di-import diatas
rata_rata = order_df['price'].groupby(order_df['payment_type']).mean()
print(rata_rata)


'''
Tugas Praktek : Sorting Pandas
Tolong cari berapa harga maksimum pembelian customer di dataset order_df
'''
# Data sudah di-import diatas
sort_harga = order_df.sort_values(by='price', ascending=False)
print(sort_harga['price'])