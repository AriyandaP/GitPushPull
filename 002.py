# usia_andi=40
# usia_budi=20

# # * perkalian
# # / pembagian
# # % sisa pembagian
# # // pembagian pembulatan kebawah

# # print(math.fabs([pembuat absolut]))
# # print(math.pow(angka,pangkat))
# # print(math.sqrt(angka,akar))

# #soal
# #8^5
# #pembulatan 9.9
# #-9.5 x 7
# #sisa pembagian 100/70

# import math

# angka1=-9.5
# angka2=7
# angka3=100
# angka4=70

# print(math.pow(8,5))
# print(round(9.9))
# print(angka1*angka2)
# print(angka3%70)

# angka5=12
# angka6=9
# angka7=3

# print(angka5+angka6/angka7)


# #string
# x='Hello World'

# #jumlah karakter pada var string
# print(len(x))

# print(x.index('World'))

# print(x.split(' '))

# print(x.lower())

# print(x.upper())

# print(x.capitalize())


# text="I'm Baron, nice to meet you"

# print(text[0])
# print(text[1])
# print(text[2:])
# print(text[:4])
# print(text[2:5])
# print(text[:])


# #input dengan type yang sudah di pilih

# a=(input('masukan angka a : '))
# print(a)
# print(type(a))
# b=(input('masukan angka b : '))
# print(b)
# print(type(b))
# print(a+b)
# print((int)(a)+(int)(b))


# c=str(24.77)
# c1=float(c)
# c2=int(c1)
# print(c)
# print(c1)
# print(c2)
# print(type(c))
# print(type(c1))
# print(type(c2))

# #beda type data
# usia=28
# nama='ari'
# print((nama)+' '+str(usia))

# #input : nama , jenis kelamin, umur, umur 3 tahun kedepan
# #output : nama saya adalah ... berjenis kelamin ... berusia ... di 3 tahun mendatang

# nama=input('nama : ')
# jenis_kelamin=input('jenis kelamin : ')
# umur=int(input('umur : '))

# print('nama saya adalah '+nama+' berjenis kelamin '+jenis_kelamin+' berusia '+(str(umur+3))+' di 3 tahun mendatang')

# #solve1

# x=4
# y=3
# z=2
# w=math.pow((x+y*z)/(x*y),z)
# print(w)
# print(type(w))

# #solve2
# print('solve 2')
# berapapun=(int)(input('silahkan masukan angka berapapun : '))
# kuadrat=berapapun*berapapun
# print('kuadrat dari '+str(berapapun)+' adalah '+str(kuadrat))

# #solve3
# print('solve 3')
# total=(int)(input('masukan total hari : '))
# tahun=total//360
# sisa1=total%360
# bulan=(sisa1//30)
# sisa2=sisa1%30
# minggu=(sisa2//7)
# sisa3=sisa2%7

# print(str(tahun)+' tahun')
# print(str(bulan)+' bulan')
# print(str(minggu)+' minggu')
# print(str(sisa3)+' hari')

# print(str((tahun*360)+(bulan*30)+(minggu*7)+sisa3)+' total hari = '+str(tahun)+' tahun '+str(bulan)+' bulan '+str(minggu)+' minggu '+str(sisa3)+' hari')