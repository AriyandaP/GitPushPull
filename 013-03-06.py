'''
RABU - 03 Juni 2020
'''

import math
import random

# class namakelas ():
#     def __init__(self,parameter1,parameter2):
#         isi yang akan dimasukkan
#     def metode1 (self,parameter1,parameter2):
#         mirip fungsi
#     def metode2 (self,parameter1,parameter2):
#         mirip fungsi

# class classkeren:
#     halo = 5
#     hello = 10

# obj1 = classkeren()
# print(obj1.halo)
# print(obj1.hello)

# class manusia:
#     def __init__(self,name,age):
#         self.nama = name
#         self.umur = age

# manusia1 = manusia('ari',28)

# print(manusia1)
# print(manusia1.nama)
# print(manusia1.umur)
# print(manusia1.__dict__)

# class ari:
#     def __init__(self,name,age,job,birthplace):
#         self.nama = name
#         self.umur = age
#         self.pekerjaan = job
#         self.tempatlahir = birthplace

# saya = ari('Muhamad Ariyanda Putra',28,'freelancer','Jakarta')

# print(saya)
# print(saya.nama)
# print(saya.umur)
# print(saya.pekerjaan)
# print(saya.tempatlahir)
# print(saya.__dict__)
# print(saya.__dict__['nama'])
# print(saya.__dict__['umur'])
# print(saya.__dict__['pekerjaan'])
# print(saya.__dict__['tempatlahir'])

# class manusia :
#     def __init__ (self,name,age) :
#         self.nama = name
#         self.umur = age

# manusia1 = manusia('Ari',28)
# print(manusia1.nama)
# print(manusia1.umur)
# print(manusia1.__dict__)
# manusia1.nama = 'Andi'
# print(manusia1.nama)
# print(manusia1.umur)
# print(manusia1.__dict__)
# manusia1.pekerjaan = 'Guru'
# print(manusia1.__dict__)

# class identitas : 
#     def __init__ (self,name,sex,age):
#         self.nama = name 
#         self.kelamin = sex 
#         self.umur = age
#     def tulis (self):
#         print('Nama saya adalah : "'+ self.nama +'" yang berjenis kelamin : "'+ self.kelamin +'" dan berumur : "'+ str(self.umur)+'".')

# saya = identitas('Ari','Laki-laki',29)

# saya.tulis()
# print(saya.__dict__)
# print('\n')

# saya.nama = 'Bintang'
# saya.kelamin = 'Perempuan'
# saya.umur = 24
# saya.pekerjaan = 'Dosen'
# saya.tulis()
# print(saya.__dict__)

# class manusia :
#     def __init__ (self,name,age) :
#         self.nama = name
#         self.umur = age
#     def salamkenal (self,kalimatsalam) :
#         print('Halo, nama saya ' + self.nama + ' ,' + kalimatsalam)

# halo = manusia('Ari',28)
# halo.salamkenal('Siapa namamu?')

# class human(manusia) : 
#     def __init__(self,name,age,gender):
#         super().__init__(name,age)
#         self.kelamin = gender

# hello = human('Brian',27,'Male')
# hello.salamkenal('What is your name?')
# print(hello.__dict__)

# class utama : 
#     def __init__ (self,name,sex,birthplace):
#         self.nama = name
#         self.jeniskelamin = sex
#         self.tempatlahir = birthplace
#     def tampilkan (self):
#         print('Halo, nama saya "'+self.nama+'" ,berjenis kelamin "'+self.jeniskelamin+'" ,lahir di kota "'+self.tempatlahir+'". \n')

# parent = utama('Brian','Pria','Bandung')
# print(parent.__dict__)
# parent.tampilkan()


# class tambahan(utama) : 
#     def __init__ (self,name,sex,birthplace,age,job):
#         super().__init__(name,sex,birthplace)
#         self.umur = age
#         self.pekerjaan = job
#     def tampilkantambahan (self):
#         print('Halo, nama saya "'+self.nama+'" ,berjenis kelamin "'+self.jeniskelamin+'" ,lahir di kota "'+self.tempatlahir+'" , umur saya 2 tahun kedepan "'+str(self.umur+2)+'" , dan terakhir pekerjaan saya adalah "'+self.pekerjaan+'". \n')
    # def fungsitambahan (self, kalimattambahan):
    #     self.tampilkan()+kalimattambahan

# child = tambahan('Rindu', 'Perempuan', 'Solo', 26, 'Manajer')
# print(child.__dict__)
# child.tampilkantambahan()

# child.fungsitambahan('Umur saya 2 tahun kedepan adalah :'+str(self.umur+2)+' dan saya berprofesi sebagai : '+ self.pekerjaan)

teks = 'Selamat Ulang Tahun Kami Ucapkan'



# def hitunga(teks) :
#     counta=0
#     lista=[]
#     for i in teks:
#         lista.append(i)    
#     for huruf in teks:
#         if huruf == 'a' or huruf == 'A':
#             counta = counta+1
#     print(counta)

# hitunga(teks)

class hitunghuruf:
    def __init__ (self, teks):
        self.kalimat = teks
        self.lista=[]
        self.hitunga = 0
        self.hitungi = 0
        self.hitungu = 0
        self.hitunge = 0
        self.hitungo = 0
    def hurufa(self):
        for i in self.kalimat:
            self.lista.append(i)
        for huruf in self.lista:
            if huruf == 'a' or huruf == 'A':
                self.hitunga+=1
        print('A : '+str(self.hitunga))

# teks = input('Ketik kalimat yang akan dihitung : ')

test1 = hitunghuruf(teks)
test1.hurufa()




