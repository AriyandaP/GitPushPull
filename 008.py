import math

'''
function & list

FUNCTION
def nama_fungsi(parameter atau variable, ... , ... ,):
    program

#calling list: nama_fungsi
'''

###

# def fungsi_print():
#     print('tes fungsi print')
#     print('print tes fungsi')

# fungsi_print()

# # def for_saya(x):
# #     for saya in range(0,x,1):
# #         print('Saya anak rajin '+str(saya+1))

# # for_saya(5)

# for saya in range(0,5,1):
#             print('Saya anak rajin '+str(saya+1))


# fungsi_print()


### FUNCTION AND PARAMTER

# def nama_panjang(nama_depan):
#     print(nama_depan+' susilo')

# nama_panjang('ari')

# def lima_pangkat(x):
#     print(str(5**x))

# y=int(input('masukan pangkat berapa :'))

# lima_pangkat(y)


### PARAMETERS

# def vol_balok(p,l,t):
#     print(('Volume dari balok tersebut adalah : '+str(p*l*t)+' cm^3'))

# a=int(input('Masukan panjang balok dalam CM : '))
# b=int(input('Masukan lebar balok dalam CM : '))
# c=int(input('Masukan tinggi balok dalam CM : '))

# vol_balok(a,b,c)

### RETURN

# def jumlah(a,b):
#     c=a+b
#     print(c)
# jumlah(4,5)

# #tanpa fungsi return, maka fungsi tidak bisa berinteraksi dengan yang lain

# def total(x,y):
#     z=x+y
#     return z
# print(total(4,5))

# pangkat2=total(4,5)**2

# pangkat3=total(4,5)**3

# print(pangkat2)

# print(pangkat3)

# x=int(input('Masukan jari-jari dari sebuah lingkaran dalam CM : '))
# def luas_lingkaran(r):
#     luas=math.pi*r**2
#     return luas
# print('Luas dari lingkaran tersebut adalah : '+str(round(luas_lingkaran(x),2))+' CM^2')

# # def vol_tabung(luas,t):
# #     vol=luas*t
# #     return vol
# # y=int(input('masukan tinggi dalam CM : '))
# # print('Volume dari tabung dengan jari-jari dan tinggi diatas adalah : '+str(round(vol_tabung(luas_lingkaran(x),y),2))+' CM^3')

# y=int(input('Masukan panjang sisi kubus : '))
# def vol_kubus(sisi):
#     vol=sisi**3
#     return vol
# print('Volume dari kubus tersebut adalah ; '+str(vol_kubus(y))+' cm^3')

# print('Apabila kedua hasil dikalikan maka didapatkan nilai : '+str(luas_lingkaran(x)*vol_kubus(y)))

### FUNCTION INSIDE FUNCTION

# def kali(x):
#     if(x<2):
#         return 1
#     else:
#         return(x*tiga())
# def tiga():
#     return 3

# print(kali(7))

# x=1.5
# y=5
# c=8
# d=3

# def luas_persegi(sisi):
#     if(sisi<2):
#         return sisi*sisi
#     else:
#         return sisi*sisi*fungsi_sisi(c,d)

# def fungsi_sisi(a,b):
#     return a%b

# print(luas_persegi(y))

# # apabila y yang digunakan, y = 5 , lanjut ke else , 5 x 5 x fungsi sisi dengan nilai (8,3) , 8 mod 3 = 2 , hasil akhir 5 x 5 x 2 = 50
# # apabila x yang digunakan, x = 1 , lanjut ke if , hasil akhir  1,5 x 1,5 = 2,25

### DEFAULT PARAMETER

# def kali(angka1=5,angka2=2):
#     return angka1*angka2
# print(kali())
# print(kali(angka2=4))
# print(kali(angka2=1,angka1=2))
# print(kali(2,3))

### LIST