import math

# #PR1

# #USING NUMERICAL METHOD

# #soal3

# #4 digit angka abcd menjadi cdab

# angka=(input('masukan 4 digit angka : '))
# print(angka[2:4]+angka[0:2])
# angka=int(angka)
# cd=angka%100
# ab=angka//100
# print(cd)
# print(ab)
# print(cd*100+ab)

#soal3

#input1:34
#input2:98
#output:3948
#ab dan cd menjadi acbd

# digit1=str(input('1. masukan 2 digit angka : '))
# digit2=str(input('2. masukan 2 digit angka : '))
# print(digit1[0]+digit2[0]+digit1[1]+digit2[1])

# digit1=int(digit1)
# digit2=int(digit2)

# a=digit1//10
# b=digit1%10
# c=digit2//10
# d=digit2%10

# print(a*1000+c*100+b*10+d)

###

# #soal2

# print('soal 2')

# #area=pi*r^2

# radius=(float)(input('masukan radius dari sebuah lingkaran : '))
# jarijari=radius/2
# area=math.pi*(jarijari*jarijari)
# print('luas dari lingkaran dengan radius '+str(radius)+' adalah '+str(area))

# soal4

# print('soal 4')

# #remove all input specific character from input string sentence

# kalimat=input('silahkan tulis kalimat : ')
# huruf=input('huruf yang ingin dihilangkan : ')
# besar=huruf.upper()
# kecil=huruf.lower()
# kalimatbaru1=kalimat.replace(besar,'')
# kalimatbaru2=kalimatbaru1.replace(kecil,'')
# print(kalimatbaru2)

# kalimat=input('silahkan tulis kalimat : ')
# huruf=input('huruf yang ingin dihilangkan : ')
# kalimatbaru=kalimat.lower()
# hurufbaru=huruf.lower()
# print(kalimatbaru)

###

#input hari
#output tahun bulan minggu hari
#if string or negative = masukan jumlah hari yang benar

# total=int(input('Silahkan masukan jumlah hari : '))
# if(total>=0):
#     tahun=total//360
#     sisa1=total%360
#     bulan=sisa1//30
#     sisa2=sisa1%30
#     minggu=sisa2//7
#     sisahari=sisa2%7
#     print(str(total)+' hari = '+str(tahun)+' tahun '+str(bulan)+' bulan '+str(minggu)+' minggu'+str(sisahari)+' hari ')
# else:
#     print('masukan jumlah hari yang benar')

###

#input range
#output print range
# output print rata-rata

# a=int(input('Masukan range : '))
# arange=a+1
# b=0
# listitem=list(range(0,arange,1))
# print(str(listitem))
# for item in range(0,arange,1):
#     b+=item
# print('rata-rata dari 0 hingga '+str(a)+' adalah '+str(b/(a)))

# a=int(input('masukan range : '))
# arange=a+1
# itemlist=list(range(0,arange,1))
# print(str(sum(itemlist)))
# print(str(len(itemlist)-1))

###

#count huruf

# kalimat=input('Masukan kalimat apa saja : ')
# kalimat1=kalimat.lower()
# huruf=input('Huruf yang akan dihitung jumlahnya : ')
# kecil=huruf.lower()
# besar=huruf.upper()
# k=kalimat1.count(kecil)
# b=kalimat.count(besar)
# print("Kalimat '"+kalimat+"' memiliki huruf atau kata '"+huruf+"' sebanyak "+str(k+b)+" buah")

###

#jarak 120km
#a 60km/h
#b 40km/h
#start 9.00

# jarak=120
# a=60
# b=40
# mulai=9
# jam=120//(a+b)
# # print(str(jam))
# sisajarak=120%(a+b)
# # print(str(sisajarak))
# sisajam=sisajarak/(a+b)
# # print(str(sisajam))
# menit=sisajam*60
# menit=int(menit)
# # print(str(menit))
# # print('tabrakan terjadi setelah '+str(jam)+(' jam dan ')+str(menit)+' menit')
# print('mobil A dan mobil B akan bertabrakan pada pukul '+str(mulai+jam)+' lebih '+str(menit)+' menit WIB.')

###

# x=''
# y=int(input('Masukan jumlah baris bintang yang diinginkan : '))
# for item in range(0,y,1):
#     for item1 in range(0,item+1,1):
#         x+=' * '
#     x+='\n'
#     x+='\n'
# print(x)

###

#input masukkan banyaknya data
#input data ke-1 :
#output rata-rata

# z=0
# x=int(input('Masukkan banyaknya data : '))
# for item in range (0,x,1):
#     y=int(input('Data No.'+str(item+1)+': '))
#     z+=y
# # print(str(x))
# # print(str(z))
# print('Rata-rata nilai tersebut adalah '+str(z/x))

###

#multiply of 3 fizz
#multiply of 5 buzz
#multiply of 3 and 5 fizzbuzz
#print list number

# x=int(input('input number : '))


#output 4 pilihan: luas persegi panjang, lingkaran, rata2, variasi dan standar deviasi
#input pilih dari 4 pilihan

# print('Pilih dari 4 pilihan dibawah ini: \n')
# print('Pilihan ke 1 : Rumus luas permukaan tabung')
# print('Pilihan ke 2 : Rumus volume tabung')
# print('Pilihan ke 3 : Rata-rata dari data-data yang dimasukan')
# print('pilihan ke 4 : Variansi dan standar deviasi dari data-data yang dimasukkan')
# Pilih=input('Silahkan pilih : ')
# if(Pilih=='1'):
#     d=int(input('Masukan nilai diameter tabung dalam cm : '))
#     t=int(input('Masukan nilai tinggi tabung dalam cm : '))
#     r=d/2
#     lpt=(2*math.pi*(r**2))+(2*math.pi*r*t)
#     print('Luas permukaan dari tabung tersebut adalah '+str(lpt)+' cm^2')
# elif(Pilih=='2'):
#     d1=int(input('Masukan nilai diameter tabung dalam cm : '))
#     t1=int(input('Masukan nilai tinggi tabung dalam cm : '))
#     r1=d1/2
#     vt=(math.pi*(r1**2)*t1)
#     print('volume dari tabung tersebut adalah '+str(vt)+' cm^3')
# elif(Pilih=='3'):
#     z=0
#     x=int(input('Masukkan banyaknya data : '))
#     for item in range (0,x,1):
#         y=int(input('Data No.'+str(item+1)+': '))
#         z+=y
#     print('Rata-rata nilai tersebut adalah '+str(z/x))
# elif(Pilih=='4'):
#     jumlah=0
#     jumlah1=0
#     jumlah2=0
#     data=int(input('Masukkan banyaknya data : '))
#     list=[]
#     for item in range(0,data,1):
#         item1=int(input('Data No.'+str(item+1)+': '))
#         list.append(item1)
#         jumlah+=item1
#     ratarata=jumlah/data
#     for item2 in range(0,data,1):
#         kuadrat=(list[item2]-ratarata)**2
#         jumlah2+=kuadrat
#     variansi=jumlah2/(data-1)
#     print('variansi dari data yang dimasukan adalah : '+str(variansi))
#     deviasi=math.sqrt(variansi)
#     print('standar deviasi dari data yang dimasukan adalah : '+str(deviasi))
# else:
#     print('Masukkan pilihan yang benar')

###

n = int (input ('Masukkan Banyaknya Data: '))
jumlah = 0
atas = 0
for i in range (1,n+1) :
    x = int (input('data ke - ' + str(i) + ': '))
    jumlah = jumlah + x
    rata2 = jumlah/n
    a = x**2
    atas = atas+a
    bawah = n-1
    variansi = (atas-(n*(rata2**2)))/bawah
    stdev = math.sqrt(variansi)
print ('Varian Data Tersebut Adalah : ' + str(variansi))
print ('Standar Deviasi Data Tersebut Adalah : '+str(stdev))