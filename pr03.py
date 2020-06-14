### PR 13 - 14 MAY 2020 MUHAMAD ARIYANDA PUTRA

#main menu
#1. isi
#2. lihat
#3. sort
#   1. ascending
#   2. descending
#4. min/max
#   1. min
#   2. max
#5. ganjil/genap
#   1.ganjil
#   2.genap
#6. keluar

import math


### VARIABLES


angka=[]
ganjil=[]
genap=[]
terbesar=0
terkecil=0
pilih=0
banyak=0
stop = False


### FUNCTIONS


def kecil_besar():
    for pertama in range(len(angka)):
        for berikutnya in range(pertama+1,len(angka)):
            if angka[pertama]>angka[berikutnya]:
                angka[pertama],angka[berikutnya]=angka[berikutnya],angka[pertama]
    return angka

def besar_kecil():
    for pertama in range(len(angka)):
        for berikutnya in range(pertama+1,len(angka)):
            if angka[pertama]<angka[berikutnya]:
                angka[pertama],angka[berikutnya]=angka[berikutnya],angka[pertama]
    return angka

def pilih_genap():
    genap.clear()
    for i in range(0,len(angka)):
        if angka[i]%2==0:
            genap.append(angka[i])
    return genap

def pilih_ganjil():
    ganjil.clear()
    for i in range(0,len(angka)):
        if angka[i]%2!=0:
            ganjil.append(angka[i])
    return ganjil

def maks():
    kecil_besar()
    print(angka[-1])

def mins():
    besar_kecil()
    print(angka[-1])


### PROGRAM


while(not stop):
    print('---Main menu--- \n')
    print('1. Input data')
    print('2. Lihat array')
    print('3. Sort array')
    print('4. Nilai maksimum dan minimum')
    print('5. Angka ganjil atau genap')
    print('6. Keluar program \n')
    pilih=input('Silahkan pilih menu : ')
    if(pilih=='1'):
        banyak=int(input('Banyak data yang akan diinput : '))
        for i in range(banyak):
            tambah=float(input('Input data ke-'+str(i+1)+' : '))
            angka.append(tambah)
    elif(pilih=='2'):
        stop = False
        print('Array yang anda telah masukan adalah : ')
        print(angka)
        print('Jumlah item dalam array tersebut adalah : '+str(len(angka)))
    elif(pilih=='3'):
        print('---Main menu--- \n')
        print('1. Input data')
        print('2. Lihat array')
        print('3. Sort array')
        print('     a. Sort dari KECIL ke BESAR')
        print('     b. Sort dari BESAR ke KECIL')
        print('4. Nilai maksimum dan minimum')
        print('5. Angka ganjil atau genap')
        print('6. Keluar program \n')
        pilih=input('Silahkan pilih menu : ')
        if(pilih=='a' or pilih=='A'):
            print(kecil_besar())
        elif(pilih=='b' or pilih=='B'):
            print(besar_kecil())
        elif(pilih=='6'):
            stop = True
            print('\n')
            print('Terima kasih telah menggunakan program ini')
            print('---sampai jumpa lagi---')
        else:
            print('\n')
            print('Keyword yang di masukkan tidak dikenal')
            print('\n')
    elif(pilih=='4'):
        print('---Main menu--- \n')
        print('1. Input data')
        print('2. Lihat array')
        print('3. Sort array')
        print('4. Nilai maksimum dan minimum')
        print('     a. Angka paling BESAR')
        print('     b. Angka paling KECIL')
        print('5. Angka ganjil atau genap')
        print('6. Keluar program \n')
        pilih=input('Silahkan pilih menu : ')
        if(pilih=='a' or pilih=='A'):
            print('Angka paling BESAR di dalam array yang ada adalah: ')
            maks()
        elif(pilih=='b' or pilih=='B'):
            print('Angka paling KECIL di dalam array yang ada adalah: ')
            mins()
        elif(pilih=='6'):
            stop = True
            print('\n')
            print('Terima kasih telah menggunakan program ini')
            print('---sampai jumpa lagi---')    
        else:
            print('\n')
            print('Keyword yang di masukkan tidak dikenal')
            print('\n')
    elif(pilih=='5'):
        print('---Main menu--- \n')
        print('1. Input data')
        print('2. Lihat array')
        print('3. Sort array')
        print('4. Nilai maksimum dan minimum')
        print('5. Angka ganjil atau genap')
        print('     a. Tampilkan hanya angka GANJIL')
        print('     b. Tampilkan hanya angka GENAP')
        print('6. Keluar program \n')
        pilih=input('Silahkan pilih menu : ')
        if(pilih=='a' or pilih=='A'):
            print('Hanya angka GANJIL')
            print(pilih_ganjil())
        elif(pilih=='b' or pilih=='B'):
            print('Hanya angka GENAP')
            print(pilih_genap())
        elif(pilih=='6'):
            stop = True
            print('\n')
            print('Terima kasih telah menggunakan program ini')
            print('---sampai jumpa lagi---')
        else:
            print('\n')
            print('Keyword yang di masukkan tidak dikenal')
            print('\n')
    elif(pilih=='6'):
        stop = True
        print('\n')
        print('Terima kasih telah menggunakan program ini')
        print('---sampai jumpa lagi---')
    else:
        stop = False
        print('\n')
        print('Keyword yang di masukkan tidak dikenal!')
        print('\n')
        