#[Struktur Program Python]
'''
Struktur Program Python: statement, variabel & literals, operator
Struktur Program Python: reserved words, whitespace, single line comment
multi line comment
'''
# 1. Statement
print('Belajar Python Menyenangkan')
print('Halo Dunia')
# 2. Variabels & Literals
bilangan1 = 5
bilangan2 = 10
kalimat1 = 'Belajar Bahasa Python'
# 3. Operators
print(bilangan1+bilangan2)


print()
#[Tugas Praktek : Penggunaan Operator]
print('Tugas praktek : penggunaan operator')
harga_asli = 20000
potongan = 2000
harga_setelah_potongan = harga_asli - potongan
harga_final = harga_setelah_potongan*1.1
print(harga_final)


print()
#[Tipe Data Dasar]
'''
Null type : None
Boolean type : True, False
Numeric type : Int (bil. bulat), float (bil. riil)
Text type : str
'''

print()
#[Sequence type]

#[sequence type : List]
#list menggunakan  kurung siku
contoh_list = [1, 'dua', 3, 4, 0, 5]
#pemanggilan list menggunakan indeks; dimulai dari 0
print(contoh_list[0])
print(contoh_list[3])
#list bersifat Mutable
contoh_list[3] = 'empat'
print(contoh_list[3])

#[sequence type : Tuple]
#Tuple menggunakan tanda kurung
contoh_tuple = ('Januari', 'Februari', 'Maret', 'April')
#pemanggilan menggunakan indeks; dimulai dari 0
print(contoh_tuple[0])
#Tuple bersifat Immutable
#contoh_tuple[0] = 'Desember' ; jika diaktifkan akan eror
print(contoh_tuple[0])


print()
#[Set type]
#List memperbolehkan duplikasi nilai
#List memperdulikan urutan elemen saat di deklarasi
contoh_list = ['Dewi', 'Budi', 'Cici', 'Linda', 'Cici']
print('Data List :')
print(contoh_list)

#Set tidak memperbolehkan duplikasi
#Set tidak memperdulikan urutan elemen
contoh_set = {'Dewi', 'Budi', 'Cici', 'Linda', 'Cici'}
print('Data Set  dan Frozen Set :')
print(contoh_set)

#Frozenset tidak dapat diubah setelah proses deklarasinya
contoh_frozen_set = ({'Dewi', 'Budi', 'Cici', 'Linda', 'Cici'})
print(contoh_frozen_set)


print()
#[Mapping type - Dictionary]
person = {'nama':'Jhon Doe', 'pekerjaan':'programmer'}
print('Data Dictionary :')
print(person['nama'])
print(person['pekerjaan'])


print()
#[Tugas Praktek : Kalkulator Potongan Harga]
#Data yang dinyatakan di dalam dictionary

print('Tugas praktek :')
# Data yang dinyatakan ke dalam dictionary
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000} 
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000} 
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000}
# Hitunglah harga masing-masing data setelah dikurangi diskon
harga_sepatu = sepatu["harga"] - sepatu["diskon"] 
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
# Hitung harga total
total_harga = harga_sepatu + harga_baju + harga_celana
# Hitung harga kena pajak
total_pajak = total_harga * 0.1
# Cetak total_harga + total_pajak
print(total_harga + total_pajak)
