'''
SENIN/SELASA - 18/19 Mei 2020
PR05 - MUHAMAD ARIYANDA PUTRA
'''
import math
import random

angka=[]
pilihfungsi=['SORT', 'MEAN', 'MEDIAN', 'MODE', 'VARIANCE', 'STDEV', 'SKEWNESS', 'KURTOSIS', 'LIHAT LIST']
pilihlist=['LIST BIASA','LIST TANPA DUPLIKAT']
n=0
pilih=0
bawah=0
atas=0
stop = False
pilih1=''
pilih2=''
x=[]

def urutnaik (urutan):
    for pertama in range(0,len(urutan)):
        for berikut in range(pertama+1,len(urutan)):
            if urutan[pertama]>urutan[berikut]:
                urutan[pertama],urutan[berikut]=urutan[berikut],urutan[pertama]
def urutturun (urutan):
    for pertama in range(0,len(urutan)):
        for berikut in range(pertama+1,len(urutan)):
            if urutan[pertama]<urutan[berikut]:
                urutan[pertama],urutan[berikut]=urutan[berikut],urutan[pertama]
def urut (urutan):
    pilihurut=0
    print('---SORT---')
    print('1. Urut naik / Ascending')
    print('2. Urut Turun / Descending')
    pilihurut=input('Pilih fungsi urut : ')
    if(pilihurut=='1'):
        urutnaik(urutan)
    elif(pilihurut=='2'):
        urutturun(urutan)
    else:
        print('---ERROR---')
        print('pilihan tidak dikenal!')
        print('---ERROR---')
    return(urutan)
# print(urut(x))
def total (urutan):
    jumlah=0
    for ke in range(len(urutan)):
        jumlah+=urutan[ke]
    return jumlah
# print(total(x))
def rata (urutan):
    ratarata=total(urutan)/len(urutan)
    return ratarata
# print(rata(x))
def tengah (urutan):
    angkamedian=0
    urutnaik(urutan)
    # print(urutan)
    if len(urutan)%2==0:
        angkamedian+=(urutan[int(len(urutan)/2)]+urutan[int((len(urutan)/2)-1)])/2
    elif len(urutan)%2!=0:
        angkamedian=urutan[(len(urutan)//2)]
    return angkamedian
# print(tengah(x))
def modus (urutan):
    hitung={}
    for j in x:
        if j in hitung:
            hitung[j]+=1
        else:
            hitung[j]=1
    maksimum = max(hitung.values())
    maksimums = [k for k, v in hitung.items() if v == maksimum]
    if len(maksimums)==len(x):
        print('Modus tidak ditemukan')
    else:
        for l in range(len(maksimums)):
            print('Modus ke-'+str(l+1)+' : '+str(maksimums[l]))
# modus(x)
def var (urutan):
    jumlah2=0
    for j in range(0,len(urutan)):
        kuadrat=(urutan[j]-rata(urutan))**2
        jumlah2+=kuadrat
    variansi=jumlah2/(len(urutan)-1)
    return variansi
# print(var(x))
def dev (urutan):
    deviasi=math.sqrt(var(urutan))
    return deviasi
# print(dev(x))
def skew (urutan):
    jumlah3=0
    for j in range(0,len(urutan)):
        pangkat3=(urutan[j]-rata(urutan))**3
        jumlah3+=pangkat3
    hasil=jumlah3/((len(urutan)-1)*dev(urutan))
    return hasil
# print(skew(x))
def kurt (urutan):
    jumlah4=0
    for j in range(0,len(urutan)):
        pangkat4=(urutan[j]-rata(urutan))**4
        jumlah4+=pangkat4
    hasil=jumlah4/((len(urutan)-1)*dev(urutan))
    return hasil
# print(kurt(x))
def namafungsilist(a,b):
    print("Hasil dari fungsi '"+pilihfungsi[(a-1)]+"' menggunakan '"+pilihlist[(b-1)]+"' adalah : ")

print('---MENU INPUT DATA---')
n=int(input('Input berapa N data yang ingin dimasukkan : '))
print('1. Masukan data secara manual')
print('2. Masukan data secara acak')
pilih=input('Silahkan pilih : ')
if pilih=='1':
    for i in range(n):
        tambah=int(input('masukan data ke-'+str(i+1)+' : '))
        angka.append(tambah)
elif pilih=='2':
    bawah=int(input('Batas bawah nilai acak : '))
    atas=int(input('Batas atas nilai acak : '))
    for i in range(n):
        angka.append(random.randint(bawah,atas))
else:
    print('---ERROR---')
    print('pilihan tidak dikenal!')
    print('---ERROR---')
print('---MENU INPUT DATA---')
print('---List Angka---')
print(angka)
nodup=set(angka)
noduplist=list(nodup)
print('---List Angka---')
while(not stop):
    print('---MENU FUNGSI---')
    print('1.   Sort list angka')
    print('2.   Rata-rata')
    print('3.   Median')
    print('4.   Modus')
    print('5.   Variansi')
    print('6.   Standar Deviasi')
    print('7.   Skewness')
    print('8.   Kurtosis')
    print('9.   Lihat list')
    print('10.  Keluar')
    pilih1=input('Silahkan pilih : ')
    print('---MENU FUNGSI---')
    if pilih1=='1':
        print('1. Gunakan list biasa')
        print('2. Gunakan list tanpa duplikat')
        pilih2=input('Silahkan pilih : ')
        if pilih2=='1':
            x=angka
        elif pilih2=='2':
            x=noduplist
        else:
            print('---ERROR---')
            print('pilihan tidak dikenal!')
            print('---ERROR---')
        namafungsilist(int(pilih1),int(pilih2))
        print(urut(x))
    elif pilih1=='2':
        print('1. Gunakan list biasa')
        print('2. Gunakan list tanpa duplikat')
        pilih2=input('Silahkan pilih : ')
        if pilih2=='1':
            x=angka
        elif pilih2=='2':
            x=noduplist
        else:
            print('---ERROR---')
            print('pilihan tidak dikenal!')
            print('---ERROR---') 
        namafungsilist(int(pilih1),int(pilih2))   
        print(rata(x))
    elif pilih1=='3':
        print('1. Gunakan list biasa')
        print('2. Gunakan list tanpa duplikat')
        pilih2=input('Silahkan pilih : ')
        if pilih2=='1':
            x=angka
        elif pilih2=='2':
            x=noduplist
        else:
            print('---ERROR---')
            print('pilihan tidak dikenal!')
            print('---ERROR---')
        namafungsilist(int(pilih1),int(pilih2))
        print(tengah(x))
    elif pilih1=='4':
        print('1. Gunakan list biasa')
        print('2. Gunakan list tanpa duplikat')
        pilih2=input('Silahkan pilih : ')
        if pilih2=='1':
            x=angka
        elif pilih2=='2':
            x=noduplist
        else:
            print('---ERROR---')
            print('pilihan tidak dikenal!')
            print('---ERROR---')
        namafungsilist(int(pilih1),int(pilih2))    
        modus(x)
    elif pilih1=='5':
        print('1. Gunakan list biasa')
        print('2. Gunakan list tanpa duplikat')
        pilih2=input('Silahkan pilih : ')
        if pilih2=='1':
            x=angka
        elif pilih2=='2':
            x=noduplist
        else:
            print('---ERROR---')
            print('pilihan tidak dikenal!')
            print('---ERROR---')
        namafungsilist(int(pilih1),int(pilih2))                
        print(var(x))
    elif pilih1=='6':
        print('1. Gunakan list biasa')
        print('2. Gunakan list tanpa duplikat')
        pilih2=input('Silahkan pilih : ')
        if pilih2=='1':
            x=angka
        elif pilih2=='2':
            x=noduplist
        else:
            print('---ERROR---')
            print('pilihan tidak dikenal!')
            print('---ERROR---')
        namafungsilist(int(pilih1),int(pilih2))    
        print(dev(x))
    elif pilih1=='7':
        print('1. Gunakan list biasa')
        print('2. Gunakan list tanpa duplikat')
        pilih2=input('Silahkan pilih : ')
        if pilih2=='1':
            x=angka
        elif pilih2=='2':
            x=noduplist
        else:
            print('---ERROR---')
            print('pilihan tidak dikenal!')
            print('---ERROR---')
        namafungsilist(int(pilih1),int(pilih2))    
        print(skew(x))
    elif pilih1=='8':
        print('1. Gunakan list biasa')
        print('2. Gunakan list tanpa duplikat')
        pilih2=input('Silahkan pilih : ')
        if pilih2=='1':
            x=angka
        elif pilih2=='2':
            x=noduplist
        else:
            print('---ERROR---')
            print('pilihan tidak dikenal!')
            print('---ERROR---')
        namafungsilist(int(pilih1),int(pilih2))    
        print(kurt(x))
    elif pilih1=="9":
        print('1. Lihat list biasa')
        print('2. Lihat list tanpa duplikat')
        pilih2=input('Silahkan pilih : ')
        if pilih2=='1':
            x=angka
        elif pilih2=='2':
            x=noduplist
        namafungsilist(int(pilih1),int(pilih2))
        print(x)
    elif pilih1=='10':
        stop = True
    else:
        print('---ERROR---')
        print('pilihan tidak dikenal!')
        print('---ERROR---')