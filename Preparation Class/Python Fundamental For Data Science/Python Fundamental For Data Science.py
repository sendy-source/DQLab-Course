#[Data type python]
#Berikut adalah data type pada Python:

#tipe data Boolean
print(True)

#tipe data String
print("Ayo belajar Python")
print('Belajar Python Sangat Mudah di DQLAB')

#tipe data Integer
print(20)

#tipe data Float
print(3.14)

#tipe data List
print([1,2,3,4,5])
print(["satu", "dua", "tiga"])

#tipe data Dictionary
print({"nama":"Budi", "umur":20})
print()


#[Checking data type Python]
var_string="Belajar Python DQLab"
var_int=10
var_float=3.14
var_list=[1,2,3,4,5]
var_tuple=("satu","dua","tiga")
var_dict={"nama":"Ali", "umur":20}

print(var_string)
print(type(var_string))
print(var_int)
print(type(var_int))
print(var_float)
print(type(var_float))
print(var_list)
print(type(var_list))
print(var_tuple)
print(type(var_tuple))
print(var_dict)
print(type(var_dict))
print()


#[IF Statement]
i = 10 #Inisialisasi variabel yang memiliki nilai 10
if(i==10): #pengecekan nilai i apakah sama dengan 10
    print("ini adalah angka 10") #jika True maka akan mencetak kalimat ini

#[IF... ELSE... Statement]
i = 5 #inisialisasi variabel
if(i==10): #pengecekan nilai
    print('ini adalah angka 10')
else:
    print('bukan angka 10')

#[IF... ELIF... ELSE...]
i = 3
if(i==5):
    print('ini adalah angka 5')
elif(i>5):
    print('lebih besar dari 5')
else: #memeriksa apakah kondisi i tidak memenuhi 2 kondisi diatas
    print('lebih kecil dari 5')

#[Nested IF]
i = 5
if(1<7):
    print('nilai kurang dari 7')
    if(i<3):
        print('nilai i kurang dari 7 dan kurang dari 3')
    else:
        print('nilai i kurang dari 7 tapi lebih dari 3')


#[Operasi Matematika Sederhana]
a=10
b=5

selisih = a-b
jumlah = a+b
kali = a*b
bagi = a/b

print("Hasil penjumlahan a dan b adalah", jumlah)
print("Selisih a dan b adalah :",selisih)
print("Hasil perkalian a dan b adalah :",kali)
print("Hasil pembagian a dan b adalah:",bagi)

#[Operasi Modulus]
c=10
d=3

modulus=c%d
print("Hasil modulus", modulus)

#[Tugas program menentukan bil  genap atau ganjil]
angka=10

modulus=angka%2
if(modulus==0):
    print('angka termasuk bilangan genap')
else:
    print('angka termasuk bilangan ganjil')


#[Konsep WHILE]
#nilai awal j = 0
j=0

#ketika j kurang dari 6 lakukan perulangan, jika tidak stop perulangan
while j<6:
	#lakukan perintah ini ketika perulangan
	print("ini adalah perulangan ke -",j)
	#setiap kali diakhiri perulangan update nilai dengan ditambah 1
	j=j+1

#[Konsep FOR]
for i in range(1,6): #perulangan for sebagai inisialisasi dari angka 1 hingga angka yang lebih kecil daripada 6
	print("ini adalah perulangan ke -", i) #perintah jika looping akan tetap berjalan

#[Konsep FOR with access element]
count=[1,2,3,4,5] #elemen list

for number in count: #looping untuk menampilkan semua elemen pada count
    print("Ini adalah element count : ", number) #menampilkan elemen list pada count

#[Konsep FOR: Tugas Praktek]
for angka in range(1,11):
	if(angka%2==0):
		print('Angka Genap', angka)
	else:
		print('Angka Ganjil', angka)


#[FUNCTION]
#[Membuat dan Memanggil Fungsi]
# membuat fungsi
def salam():
	print("Hello, Selamat Pagi")
	
## Pemanggilan Fungsi
salam()

#[Menambah Parameter pada fungsi]
def luas_segitiga(alas, tinggi): #alas dan tinggi merupakan parameter yang masuk
	luas = (alas * tinggi) / 2
	#sintaks %0.2f" % untuk menampilkan dua angka pecahan dibelakang koma, jika tidak ini akan sangat panjang
	print("Luas segitiga: %0.2f" % luas);
	
#pemanggilan fungsi
## 4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga
luas_segitiga(4,6)

#[Fungsi dengan Return Value]
#mengembalikan nilai adalah menggunakan kata kunci return
#alas dan tiggi segitiga merupakan parameter yang masuk
def luas_segitiga(alas, tinggi):
	luas = (alas*tinggi)/2
	return luas

#pemanggilan fungsi
##4 dan 6 merupakan parameter yang diinputkan ke dalam fungsi luas segitiga
print("Luas segitiga : %d" % luas_segitiga(4,6))


#[Modul dan Package]
#[Import Package dan Menggunakan modul]
import math
print("Nilai pi adalah:", math.pi) #math.pi merupakan sintak memanggil fungsi pi

#[Import dengan Module Rename atau Alias]
#menggunakan m sebagai modole rename atau alias
import math as m

#m.pi merupakan sintak untuk memanggil fungsi
print("Nilai pi adalah:", m.pi)

#[Import Sebagian Fungsi]
from math import pi

print("Nilai pi adalah", pi)

#[Import Semua isi Moduls]
from math import *

print("Nilai e adalah:", e)
