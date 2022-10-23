'''
Tugas Praktek :  Menghitung rata-rata pengeluaran dan pemasukanku
merapikan struktur data menjadi dict
menggunakan for
'''
# Data keuangan
keuangan = {
'pengeluaran': [2, 2.5, 2.25, 2.5, 3.2, 2.5, 3.5, 4, 3],
'pemasukan': [7.8, 7.5, 9, 7.6, 7.2, 7.5, 7, 10, 7.5]
}
# Perhitungan rata-rata pemasukan dan rata-rata pengeluaran
total_pengeluaran = 0
total_pemasukan = 0
for biaya in keuangan['pengeluaran']: 
    total_pengeluaran += biaya
for biaya in keuangan['pemasukan']: 
    total_pemasukan += biaya
rata_rata_pengeluaran = total_pengeluaran/len(keuangan['pengeluaran']) 
rata_rata_pemasukan = total_pemasukan/len(keuangan['pemasukan'])
print(rata_rata_pengeluaran) 
print(rata_rata_pemasukan)


'''
Tugas Praktek-1 : Menentukan Popularitas buah berdasarkan judul artikel di majalah buah sehat
Tugas Praktek-2 : Menghitung jumlah kemunculan kata_positif bagi tiap artikel jeruk dan salak
Langkah pertama adalah menghitung jumlah kemunculan kata jeruk dan salak di tiap judul artikel
Kata positif yang dicari : Kaya, Baik, Mencegah, Memperkuat
Kata positif dicari untuk mengetahui sudut pandang pemilik majalah
'''
judul_artikel = [
"Buah Salak Baik untuk Mata", "Buah Salak Kaya Potasium", 
"Buah Jeruk Kaya Vitamin C", "Buah Salak Kaya Manfaat", 
"Salak Baik untuk Jantung", "Jeruk dapat Memperkuat Tulang", 
"Jeruk Mencegah Penyakit Asma", "Jeruk Memperkuat Gigi", 
"Jeruk Mencegah Kolesterol Jahat", "Salak Mencegah Diabetes", 
"Salak Memperkuat Dinding Usus", "Salak Baik untuk Darah",
"Jeruk Kaya Manfaat untuk Jantung", "Salak si Kecil yang Baik", 
"Jeruk dan Salak Buah Kaya Manfaat", "Buah Jeruk Enak",
"Tips Panen Jeruk Ribuan Kilo", "Tips Bertanam Salak", 
"Salak Manis untuk Berbuka", "Jeruk Baik untuk Wajah"
]
jumlah_artikel_jeruk = 0
jumlah_artikel_salak = 0
for judul in judul_artikel:
    if judul.count("Jeruk") > 0: 
        jumlah_artikel_jeruk += 1
    if judul.count("Salak") > 0:
        jumlah_artikel_salak += 1
print(jumlah_artikel_jeruk) 
print(jumlah_artikel_salak)

kata_positif = ["Kaya", "Baik", "Mencegah", "Memperkuat"]
kata_positif_jeruk = 0
kata_positif_salak = 0
for judul in judul_artikel: 
    for kata in kata_positif:
        if judul.count("Jeruk") > 0 and judul.count(kata) > 0: 
            kata_positif_jeruk += 1
        if judul.count("Salak") > 0 and judul.count(kata) > 0:
            kata_positif_salak += 1
print('kata positif jeruk', kata_positif_jeruk)
print('kata positif salak', kata_positif_salak) 


'''
Tugas Praktek-1 : Membuat Fungsi menghitung rata-rata dari sebuah list of numeric
Tugas Praktek-2 : Membuat fungsi menghitung standar devasi suatu list of numeric
Tugas praktek-3 : membuat fungsi menghitung rata-rata dan standar deviasi dari data berbentuk tabel atau ber- type dict
Data dalam bentuk tabel = data type Dict.
'''
# Tugas Praktek-1
# Dua buah data yang tersimpan dalam tipe list
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]
# Definisikan fungsi hitng_rata_rata
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata
# Hitung nilai rata-rata dari kedua data yang dimiliki
print('Rata-rata data1:')
print(hitung_rata_rata(data1))
print('Rata-rata data2:')
print(hitung_rata_rata(data2))

# Tugas Praktek-2
# Dua buah data yang tersimpan dalam tipe list
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]
# Fungsi rata-rata data
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata
# Definisikan fungsi hitung_standar_deviasi
def hitung_standar_deviasi(data):
    rata_rata_data = hitung_rata_rata(data)
    varians = 0
    for item in data:
        varians += (item - rata_rata_data) ** 2
    varians /= len(data)
    standar_deviasi = varians ** (1/2)
    return standar_deviasi
# Hitung nilai standar deviasi dari kedua data yang dimiliki
print('Standar deviasi data1:')
print(hitung_standar_deviasi(data1))
print('Standar deviasi data2:')
print(hitung_standar_deviasi(data2))

# Tugas Praktek-3
# Data properti
tabel_properti = {
'luas_tanah': [70, 70, 70, 100, 100, 100, 120, 120, 150, 150],
'luas_bangunan': [50, 60, 60, 50, 70, 70, 100, 80, 100, 90],
'jarak': [15, 30, 55, 30, 25, 50, 20, 50, 50, 15],
'harga': [500, 400, 300, 700, 1000, 650, 2000, 1200, 1800, 3000]
}
# Fungsi rata-rata data
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata
# Fungsi hitung_standar_deviasi
def hitung_standar_deviasi(data):
    rata_rata_data = hitung_rata_rata(data)
    varians = 0
    for item in data:
        varians += (item - rata_rata_data) ** 2
        varians /= len(data)
    standar_deviasi = varians ** (1/2)
    return standar_deviasi
# Definisikan fungsi untuk menghitung rata-rata dan standar deviasi
# setiap kolom pada tabel_properti yang diberikan oleh key dict.
def deskripsi_properti(tabel):
    for key in tabel.keys():
        print('Rata-rata ' + key + ':')
        print(hitung_rata_rata(tabel[key])) 
        print('Standar deviasi ' + key + ':')
        print(hitung_standar_deviasi(tabel[key]))
        print('')
# Panggil fungsi deskripsi_properti untuk menghitung rata-rata 
# dan standar deviasi setiap kolom pada tabel_properti
deskripsi_properti(tabel_properti)
