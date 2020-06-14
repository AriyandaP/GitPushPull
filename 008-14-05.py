'''
KAMIS - 14 MEI 2020
'''

import math

### DICTIONARIES

#List dengan nama kunci

# d={'key':'item1','key2':'item2',"kata_kunci":[3,'contoh_isi']}

# print(d['kata_kunci'])
# print(d['kata_kunci'][1])

###

#Buat dictionary : nama, tempat lahir, tanggal lahir, hobi, alamat

# biodata={'NAMA':'M ARIYANDA P','TEMPAT LAHIR':'JAKARTA','TANGGAL LAHIR':'26 NOVEMBER','HOBI':'NONTON','ALAMAT':'BEKASI'}

# print(biodata['NAMA'])
# print(biodata['TEMPAT LAHIR'])
# print(biodata['TANGGAL LAHIR'])
# print(biodata['HOBI'])
# print(biodata['ALAMAT'])

### DICTIONARIES INSIDE DICTIONARIES

# biodata={'NAMA':{'PANJANG':'M ARIYANDA P','PENDEK':'ARI'},'TEMPAT LAHIR':'JAKARTA','TANGGAL LAHIR':'26 NOVEMBER','HOBI':'NONTON','ALAMAT':'BEKASI','SEKOLAH':{'SMA':'SMA LABSCHOOL RAWAMANGUN','S1':'PPM SCHOOL OF MANAGEMENT','S2':'FUJEN CATHOLIC UNIVERSITY'},'MEDIA SOSIAL':{'FACEBOOK':'ARIYANDAPUTRA91','LINKEDIN':'ARIYANDAPUTRA91'}}

# # print(biodata['NAMA']['PANJANG'])
# # print(biodata['NAMA']['PENDEK'])

# for  i in biodata :
#     print(biodata[i])

# print('nama saya adalah %s' % biodata['NAMA'])

# print('nama saya adalah %s' % biodata.get('NAMA'))

### 


#fungsi dengan pilihan:
#1. identitas = nama,ttl,alamat,pekerjaan []
#2. pendidikan = sd sampai s1 get
#3. portofolio = 

# identitas={'nama':'M Ariyanda P','ttl':'Jakarta, 26 November','alamat':'Bekasi Barat'}

# pendidikan={'sd':'SDI Al-Azhar','smp':'SMPI Al-Azhar 8','sma':'SMA Labschool Rawamangun','kuliah':'PPM School of Management'}

# portofolio={'organisasi':'CIMA, CGMA, AIBMS', 'proyek':'Kayula, Youth in Lane'}

# def ID():
#     for i in identitas:
#         print(str(i)+' : '+identitas[i])
#         print('\n')

# def SEKOLAH():
#     for j in pendidikan:
#         print(str(j)+' : '+pendidikan.get(j))
#         print('\n')

# def WORK():
#     for k in portofolio:
#         print(str(k)+' : '+portofolio.get(k))
#         print('\n')

# stop = False
# pilih=0

# while(not stop):
#     print('1. Identitas')
#     print('2. Pendirikan')
#     print('3. Portofolio')
#     print('4. Keluar')
#     pilih=(input('masukan pilihan : '))
#     if(pilih=='1'):
#         stop = False
#         print('Identitas saya : \n')
#         ID()
#     elif(pilih=='2'):
#         print('Pendidikan saya : \n')
#         stop = False
#         SEKOLAH()
#     elif(pilih=='3'):
#         print('portofolio saya : \n')
#         stop = False
#         WORK()
#     elif(pilih=='4'):
#         stop = True
#         print('Program berhenti')
#         print('\n')
#     else:
#         stop=False
#         print('masukan pilihan yang benar')
#         print('\n')

# kamus={'buah':'apel','sayur':'kol'}

# for a in kamus:
#     print(str(a)+' : '+kamus.get(a))
# print('\n')

# kamus['buah']='leci'

# for a in kamus:
#     print(str(a)+' : '+kamus.get(a))
# print('\n')

# # GANTI KEYWORD TIDAK DISARANKAN DAN JARANG DIPAKAI
# # kamus['sayur mayur']=kamus.pop(sayur)

# # for a in kamus:
# #     print(str(a)+' : '+kamus.get(a))

###

#1.pesan tiket
#   list film:
#   1.
#       1.siang
#           pesan berapa tiket? (maks 10)
#               tentukan row (2)
#               tentukan seat (10)
#                   tempat duduk
#                       0000000000
#                       000000000x
#       2.malam
#   2.
#2.lihat history
#3.keluar

film={1:'The Matrix',2:'The Lord of the Ring'}
jadwal={1:'Jadwal Siang',2:'Jadwal Malam'}
kursi_history={}
kursi=''
stop = False
pilih=0
pilih_film=0
qtiket=0

def menu():
    print('1.Pesan tiket')
    print('2.Lihat history')
    print('3.Keluar')

def filmfilm():
    for i in film:
        print(str(i)+'.'+film.get(i))
    print('3.Keluar')

kursi=[
[0,0,0,0,0],
[0,0,0,0,0]
]

for i in kursi:
    print(' '.join(map(str,i)))

# row=2
# seat=4

x=2
y=4

x-=1
y-=1

#expected result:
# 1 0 0 0 0 0
# 2 0 0 0 X 0
#   1 2 3 4 5

def taken(row,seat):
    kursi[row][seat]='X'
    return kursi

print('\n')

taken(x,y)
for i in kursi:
    print(' '.join(map(str,i)))

# print(taken(2,4))

# while(not stop):
#     menu()
#     pilih=input('Masukan pilihan : ')
#     if(pilih=='1'):
#         stop = False
#         print('Film yang sedang tayang adalah : ')
#         filmfilm()
#         pilih_film=input('Pilih film : ')
#         if(pilih_film=='1'):
#             qtiket=int(input('Berapa banyak tiket yang akan dibeli : '))
#             print(str(qtiket))
#         elif(pilih_film=='2'):
#             qtiket=int(input('Berapa banyak tiket yang akan dibeli : '))
#             print(str(qtiket))
#         elif(pilih=='3'):
#             stop = True
#             print('\n')
#             print('---Terima Kasih---')
#         else:
#             print('\n')
#             print('Keyword yang dimasukkan tidak dikenal.')
#     elif(pilih=='2'):
#         print('pilihan 2')
#         stop = False
#     elif(pilih=='3'):
#         stop = True
#         print('\n')
#         print('---Terima Kasih---')
#     else:
#         print('\n')
#         print('Keyword yang dimasukkan tidak dikenal.')