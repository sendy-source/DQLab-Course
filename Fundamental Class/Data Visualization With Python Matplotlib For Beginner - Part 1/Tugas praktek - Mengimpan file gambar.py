'''
Tugas Praktek : Menyimpan Hasil Plot Menjadi File Image
1. Ketahui format lengkap yang bisa digunakan untuk menyimpan
# Melihat Format Lengkap yang bisa di gunakan
plt.gcf().canvas.get_supported_filetypes()
2. Pengaturan parameter untuk menyimpan gambar - Bentuk PNG
'''

import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

# Mengubah figure size
fig = plt.figure(figsize=(15,5))
# Menampilkan & Memodifikasi Line and Point
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)
# Menambahkan & Memodifikasi Title dan Axis labels
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
# Menambahkan Grid
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
# Batas Minimum : sumbu-y nya dimulai dari 0
plt.ylim(ymin=0)
# Modifikasi list tiks labels di sumbu y
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
# Menambahkan Informasi Pada Plot 
plt.text(0.45, 0.72, 'The GMV increased significantly on October 2019', transform=fig.transFigure, color='red')

# Menyimpan dan pengaturan parameter gambar - bentuk PNG
'''
1. dpi: Resolusi gambar (dots per inch). 
2. quality: Kualitas gambar (hanya berlaku jika formatnya jpg atau jpeg), bisa diisi nilai 1 (paling buruk) hingga 95 (paling bagus).
3. facecolor: Memberikan warna bagian depan figure, di luar area plot 
4. edgecolor: Memberikan warna pinggiran gambar
5. transparent: Jika nilainya True, maka gambarnya jadi transparan (jika file-nya png)
'''
plt.savefig('monthly_gmv.png')
plt.show()
