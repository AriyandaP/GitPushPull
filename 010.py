import math

### LIST

# mobil=['alya','xenia',86]
# print(mobil)
# motor=[
#     'revo',
#     'mio',
#     'pulsar'
# ]
# print(motor)
# print('mobil 0 :'+mobil[0])
# print('motor 2 :'+motor[2])

# #bisa call dari belakang [-1] = [terakhir]
# print(motor[-1])
# print('mobil -2 : '+mobil[-2])

# print(mobil[:])


###


#list nama lebih dari 5
#output 1 = list indeks no 3 dan 5
#output 2 = list kebawah
#output 3 = 2 nama teman
#output 4 = panjang list

# nama_teman=[
# 'Andry',
# 'Obie',
# 'Lika',
# 'Indra',
# 'Andre',
# 'Icha'
# ]
# #output 1
# print('\n')
# print('Output 1')
# print('Nama teman saya di indeks ke-3 adalah : '+nama_teman[3])
# print('Nama teman saya di indeks ke-5 adalah : '+nama_teman[5])
# print('\n')
# #output 2
# print('Output 2')
# for nama in nama_teman:
#     print(nama)
# print('\n')
# #output 3
# print('Output 3')
# print('Nama teman kedua teman saya adalah : '+nama_teman[-2]+' dan '+nama_teman[3])
# print('\n')
# #output 4
# print('Output 4')
# print('Saya memiliki '+str(len(nama_teman))+' teman')


###

# buah=['jeruk','nanas','apel','mangga']
# buah.append('kelapa')
# print(buah)
# #.append menambah dibelakang
# buah.pop()
# print(buah)
# buah.pop(1)
# print(buah)
# #pop() menghapus paling belakang
# #pop(1) menghapus indeks 1
# buah.insert(1,'anggur')
# print(buah)
# buah.insert(0,'kurma')
# print(buah)
# buah.remove('apel')
# print(buah)

###

# hobi=[]
# ke=1
# lanjut=''
# hobi_pertama=input('Apa hobimu? ')
# hobi.append(hobi_pertama)
# lanjut=input('Mau isi lagi? (y/t): ')
# while(lanjut=='y' or lanjut=='Y'):
#     ke+=1
#     tambahan=input('Masukkan hobimu yang ke-'+str(ke)+' : ')
#     hobi.append(tambahan)
#     lanjut=input('Mau isi lagi? (y/t): ')
# print('kamu memiliki '+str(len(hobi))+' hobi')
# for item in hobi :
#     print(('-')+item)


# stop=False
# while(not stop):
#     tambahan=input('Masukkan hobimu yang ke-'+str(ke)+' : ')
#     hobi.append(tambahan)
#     ke+=1
#     lanjut=input('Mau isi lagi? (y/t): ')
#     if(lanjut == 'y' or lanjut == 'Y' ):
#         stop=False
#     elif(lanjut=='t' or lanjut=='T'):
#         stop=True
#     else:
#         stop=True
#         print('Keyword yang dimasukkan salah!')
# print('kamu memiliki '+str(len(hobi))+' hobi')
# for item in hobi :
#     print(('-')+item)

###

#buatlah algoritma mengurutkan
#input  x=[40,100,1,5,25,10]
#output x=[1,5,10,25,40,100]

# angka=[40,100,1,5,25,10]

# for pertama in range(len(angka)):
#     for berikutnya in range(pertama+1,len(angka)):
#         if angka[pertama]<angka[berikutnya]:
#             angka[pertama],angka[berikutnya]=angka[berikutnya],angka[pertama]

# print(angka)


###


# angka=[40,100,1,5,25,10]

# def ascending():
#     for pertama in range(len(angka)):
#         for berikutnya in range(pertama+1,len(angka)):
#             if angka[pertama]>angka[berikutnya]:
#                 angka[pertama],angka[berikutnya]=angka[berikutnya],angka[pertama]
#     return angka

# def descending():
#     for pertama in range(len(angka)):
#         for berikutnya in range(pertama+1,len(angka)):
#             if angka[pertama]<angka[berikutnya]:
#                 angka[pertama],angka[berikutnya]=angka[berikutnya],angka[pertama]
#     return angka

# ascending()
# print(str(angka[0]))

# ascending()
# print(str(angka[-1]))
    

###


#fungsi bilangan ganjil dan bilangan genap

angka=[1,2,3,4,5,6,7,8,9,10]
ganjil=[]
genap=[]

for i in range(0,len(angka)):
    if angka[i]%2==0:
        genap.append(angka[i])
    else:
        ganjil.append(angka[i])

print(ganjil)

print(genap)