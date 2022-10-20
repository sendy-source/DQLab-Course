#[Python Operator]
'''
1. Arithmetic operator 
melakukan operasi matematika sederhana
    penambahan 3 + 2, output: 5
    pengurangan 4 -2, output: 2
    perkalian 3 * 2, output: 6
    Modulus	3 % 2, output: 1
    Pangkat	3 ** 2, output: 9
    Pembagian dengan pembulatan ke bawah 3 // 2, output: 1
'''

'''
2. Assignment operator
mendeklerasikan nilai secara langsung
x = 3
    penambahan x += 2 ekivalen dengan x = x + 2, output: 5
    pengurangan x -= 2 ekivalen dengan x = x - 2, output: 1
    perkalian x *= 2 ekivalen dengan x = x * 2, output: 6
    pembagian x /= 2 ekivalen dengan x = x / 2, output: 1.5
    modulus x %= 2 ekivalen dengan x = x % 2, output: 1
    pangkat x **= 2 ekivalen dengan x = x ** 2, output: 9
    pembagian dengan pembulatan ke bawah x //= 2 ekivalen dengan x = x // 2, output: 1
'''

'''
3. Comparison operator
membandingkan dua buah nilai
    persamaan 33 == 33, output = True
              34 == 33, output = False
    pertidaksamaan 34 != 33, output = True
                   33 != 33, output = False
    lebih besar dari 34 > 33, output = True
                     33 > 34, output = False
    lebih kecil dari 33 < 34, output = True
                     34 < 33, output = False
    lebih besar atau sama dengan 34 >= 33, output = True
                                 34 >= 34, output = True
                                 33 >= 34, output = False
    lebih kecil atau sama dengan 33 <= 34, output = True
                                 33 <= 33, output = True
                                 34 <= 33, output = False
'''

'''
4. Logical operators
menggabungkan beberapa nilai kebenaran atas suatu statement logika
    And - mengembalikan nilai benar jika keduanya benar
        x = 5
        x >= 1 and x <= 10, output = True
        x >= 1 and x <= 4, output = False
    Or - mengembalikan nilai benar jika salah satu benar
        x = 3
        x >= 1 or x <= 2, output = True
        x >= 5 or x <= 0, output = False
    Not - mengembalikan komplemennya
        x = 7
        not(x == 7), output = True
        not(x >= 10), output = False
'''

'''
5. Identity operator
membandingkan identitas dari dua buah variable
operator identitas sering digunakan bersamaan dengan fungsi type()
Is - mengembalikan nilai True ketika keduanya merujuk pada objek yang sama dan False dalam kondisi lainnya
Is not - mengembalikan nilai True ketika keduanya merujuk pada objek yang berbeda dan False jika sama
'''
x = 3
print(type(x) is int)
x /= 3
print(type(x) is int)
print(type(x) is float)


'''
6. Membership operator
digunakan untuk memeriksa anggota dari sebauh tipe data sequence/set
    In - mengembalikan True ketika objek merupakan anggota dari sequence/set, dan False ketika bukan
    Not in - mengembalikan True ketika objek bukan merupakan anggota dari sequence/set, dan False sebaliknya
'''
x = ["Ani", "Budi", "Cici"]
y = "Cici"
z = "Dodi"
print(y in x)
print(x in x)
print(y not in x)
print(z not in x)


print()
# Menulis dengan Predensi (urutan eksekusi)
# menuliskan operasi-operasi variabel yang bersifat ekspresif dan ringkas
# Kode awal
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = 1 - potongan_harga # baris pertama
harga_bayar *= total_harga # baris kedua
pajak_bayar = pajak * harga_bayar # baris ketiga
harga_bayar += pajak_bayar # baris ke-4
print("Kode awal - harga_bayar=", harga_bayar)

# Penyederhanaan baris kode dengan menerapkan prioritas operator
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = (1 - potongan_harga) * total_harga #baris pertama 
harga_bayar += harga_bayar * pajak # baris kedua
print("Penyederhanaan kode - harga_bayar=", harga_bayar)


'''
Nilai Prioritas operator dalam Python (tinggi ke rendah)
    () - Grouping
    x[index] - Mengakses elemen array
    **
    +x, -X
    *, /, %
    +, -
    is, is not, in, not in, <=, <, >=, >, ==, !=
    not
    and
    or
'''


print()
# Tugas Praktek : Penyederhanaan kode, mengolah data type : Dict
sepatu = { "nama" : "Sepatu Niko", "harga": 150000, "diskon": 30000 }
baju = { "nama" : "Baju Unikloh", "harga": 80000, "diskon": 8000 }
celana = { "nama" : "Celana Lepis", "harga": 200000, "diskon": 60000 }
harga_sepatu = sepatu["harga"] - sepatu["diskon"]
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
total_harga = (harga_sepatu+harga_baju+harga_celana) * 1.1 
print(total_harga)


#[Pythons Conditioning]
print()
# Python conditioning : if, elif, else, nested if
# Tugas praktek : memahami struktur pyhton
# Statement if elif else
x = 4
if x % 2 == 0: # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua") # statemen aksi lebih menjorok ke dalam
# Statement if ... elif ... else
x = 7
if x % 2 == 0: # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua")
elif x % 3 == 0: # jika sisa bagi x dengan 3 sama dengan 0
    print("x habis dibagi tiga")
elif x % 5 == 0: # jika sisa bagi x dengan 5 sama dengan 0
    print("x habis dibagi lima")
else:
    print("x tidak habis dibagi dua, tiga ataupun lima")


# Tugas praktek : program ucapan sapaan - selamat pagi - malam
# menggunakan nested if, operator python
jam = 13
if jam >= 5 and jam < 12: # selama jam di antara 5 s.d. 12
    print("Selamat pagi!")
elif jam >= 12 and jam < 17: # selama jam di antara 12 s.d. 17
    print("Selamat siang!")
elif jam >=17 and jam < 19: # selama jam di antara 17 s.d. 19
    print("Selamat sore!")
else: # selain kondisi di atas
    print("Selamat malam!")


print()
#[Tugas Praktek : Kalkulator tagihan pembayaran]
tagihan_ke = 'Mr. Yoyo'
warehousing = { 'harga_harian': 1000000, 'total_hari':15 } 
cleansing = { 'harga_harian': 1500000, 'total_hari':10 } 
integration = { 'harga_harian':2000000, 'total_hari':15 } 
transform = { 'harga_harian':2500000, 'total_hari':10 }
sub_warehousing = warehousing['harga_harian'] * warehousing['total_hari'] 
sub_cleansing = cleansing['harga_harian']  * cleansing['total_hari']
sub_integration = integration['harga_harian'] * integration['total_hari']
sub_transform = transform['harga_harian'] * transform['total_hari']
total_harga = sub_warehousing+sub_cleansing+sub_integration+sub_transform
print("Tagihan kepada:") 
print(tagihan_ke)
print("Selamat pagi, anda harus membayar tagihan sebesar:") 
print(total_harga)


#[Tugas Praktek : Kalkulator tagihan pembayaran + program ucapan sapaan]
jam = 17
tagihan_ke = 'Mr. Yoyo'
warehousing = { 'harga_harian': 1000000, 'total_hari':15 } 
cleansing = { 'harga_harian': 1500000, 'total_hari':10 } 
integration = { 'harga_harian':2000000, 'total_hari':15 } 
transform = { 'harga_harian':2500000, 'total_hari':10 }
sub_warehousing = warehousing['harga_harian']*warehousing['total_hari'] 
sub_cleansing = cleansing['harga_harian']*cleansing['total_hari'] 
sub_integration = integration['harga_harian']*integration['total_hari'] 
sub_transform = transform['harga_harian']*transform['total_hari']
total_harga = sub_warehousing+sub_cleansing+sub_integration+sub_transform
print("Tagihan kepada:")
print(tagihan_ke)
if jam > 19:
    print("Selamat malam, anda harus membayar tagihan sebesar:")
elif jam > 17:
    print("Selamat sore, anda harus membayar tagihan sebesar:") 
elif jam > 12:
    print("Selamat siang, anda harus membayar tagihan sebesar:")
else :
    print("Selamat pagi, anda harus membayar tagihan sebesar:") 
print(total_harga)


#[Python Primitive Loop Control]
print()
# Python loop control : [WHILE loops]
# Tugas Praktek : Pertambahan dengan while
# Tagihan
tagihan = [50000, 75000, 125000, 300000, 200000]
# Tanpa menggunakan while loop
total_tagihan = tagihan[0]+tagihan[1]+tagihan[2]+tagihan[3]+tagihan[4]
print(total_tagihan)
# Dengan menggunakan while loop
i = 0 # sebuah variabel untuk mengakses setiap elemen tagihan satu per satu
jumlah_tagihan = len(tagihan) # panjang (jumlah elemen dalam) list tagihan
total_tagihan = 0 # mula-mula, set total_tagihan ke 0
while i < jumlah_tagihan: # selama nilai i kurang dari jumlah_tagihan
    total_tagihan += tagihan[i] # tambahkan tagihan[i] ke total_tagihan
    i += 1 # tambahkan nilai i dengan 1 untuk memproses tagihan selanjutnya.
print(total_tagihan)


# Tugas Praktek : Pertambahan dengan while - break
# perintah [break] untuk keluar dari struktur pengulangan
tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # pengulangan akan dihentikan
    if tagihan[i] < 0:
        total_tagihan = -1
        print("terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan += tagihan[i]
    i += 1
print("While loops with break")
print(total_tagihan)


print()
# Tugas Praktek : Pertambahan dengan while - continue
# perintah [continue] untuk melanjutkan proses pengulangan berikutnya
tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # abaikan tagihan ke-i dan lanjutkan ke tagihan berikutnya
    if tagihan[i] < 0:
        i += 1
        continue
    total_tagihan += tagihan[i]
    i += 1
print("While loops with continue")
print(total_tagihan)


# Python loop control : [FOR loops]
# Tugas Praktek : Pertambahan dengan for
list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
total_tagihan = 0
for tagihan in list_tagihan: # untuk setiap tagihan dalam list_tagihan
    total_tagihan += tagihan # tambahkan tagihan ke total_tagihan
print(total_tagihan)


print()
# Tugas Praktek : Pertambahan dengan for - break & continue
list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]

# For loops with break
print("For loops with break")
total_tagihan_break = 0
for tagihan in list_tagihan:
    if tagihan < 0:
        print("Terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan_break += tagihan
print("Total tagihan %d." % total_tagihan_break)
print()

# For loops with continue
print("For loops with continue")
total_tagihan_continue = 0
for tagihan in list_tagihan:
    if tagihan < 0:
        print("Terdapat angka minus dalam tagihan, tagihan %d dilewati!" %tagihan)
        continue
    total_tagihan_continue += tagihan
print("Total tagihan %d." % total_tagihan_continue)


# Tugas Praktek : Nested loops
# aku dapat mengkombinasikan (menambahkan) struktur pengulangan lain di dalamnya
list_daerah = ['Malang', 'Palembang', 'Medan']
list_buah = ['Apel', 'Duku', 'Jeruk']
for nama_daerah in list_daerah:
    for nama_buah in list_buah:
        print(nama_buah+" "+nama_daerah)


print()
#[Tugas Praktek : program menghitung total_pengeluaran & total_pemasukan dari list_cash_flow]
# list_cash_flow berisikan pengeluaran (bil. negatif) dan pemasukan perusahaan (bil. positif)
list_cash_flow = [
2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
-5000000, 7500000, 10000000, -1500000, 25000000, -2500000
]
total_pengeluaran, total_pemasukan = 0, 0
for dana in list_cash_flow:
    if dana > 0:
        total_pemasukan += dana
    else:
        total_pengeluaran += dana
total_pengeluaran *= -1
print(total_pengeluaran) 
print(total_pemasukan)


print()
#[Study Kasus : Ekspedisi Pamanku]
# menghitung total pengeluaran per bulan karena adanya aturan ganjil-genap yang membuat pengoperasian mobil yang berbeda
# Data
uang_jalan = 1500000
jumlah_hari = 31
list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]
# Pengecekan kendaraan dengan nomor pelat ganjil atau genap 
# Deklarasikan kendaraan_genap dan kendaraan_ganjil = 0
kendaraan_genap = 0 
kendaraan_ganjil = 0
for plat_nomor in list_plat_nomor:
    if plat_nomor%2==0:
        kendaraan_genap +=1 
    else:
        kendaraan_ganjil +=1

# Total pengeluaran untuk kendaraan dengan nomor pelat ganjil 
# dan genap dalam 1 bulan
i = 1
total_pengeluaran = 0
while i <= jumlah_hari:
    if i % 2 == 0:
        total_pengeluaran += (kendaraan_genap * uang_jalan)
    else:
        total_pengeluaran += (kendaraan_ganjil * uang_jalan) 
    i += 1
# Cetak total pengeluaran
print(total_pengeluaran)
