import math

# #solve4

# print('solve 4')

# #a+b=49
# #a=0.4b
# #0.4b+b=49
# #1.4b=49

# #total=49
# total=int(input('total umur andi dan budi adalah : '))
# #rasio=0.4
# rasio=float(input('rasio umur andi dan budi adalah : '))
# budi=total/(1+rasio)
# andi=budi*rasio
# andi=int(andi)
# budi=int(budi)
# print('umur andi dan budi untuk 2 tahun kedepan adalah '+str(andi+2)+' dan '+str(budi+2))


# #soal1

# print('soal 1')

# angka=(input('masukan 4 digit angka : '))
# print(angka[2:4]+angka[0:2])


# #soal2

# print('soal 2')

# #area=pi*r^2

# radius=(int)(input('masukan radius dari sebuah lingkaran : '))
# jarijari=radius/2
# area=math.pi*(jarijari*jarijari)
# print('luas dari lingkaran dengan radius '+str(radius)+' adalah '+str(round(area)))


# #soal3

# print('soal 3')

# #input1:34
# #input2:98
# #output:3948
# #ab dan cd menjadi acbd

# digit1=str(input('1. masukan 2 digit angka : '))
# digit2=str(input('2. masukan 2 digit angka : '))
# print(digit1[0]+digit2[0]+digit1[1]+digit2[1])


# #soal4

# print('soal 4')

# #remove all input specific character from input string sentence

# kalimat=input('silahkan tulis kalimat : ')
# huruf=input('huruf yang ingin dihilangkan : ')
# print(kalimat.replace(huruf,''))


# #soal5

# print('soal 5')

# #input 2 kata yang dipisahkan oleh spasi A spasi B
# #output kata diputar dan di print sebagagai B spasi A

# dua_kata=str(input('silahkan masukkan 2 kata yang dipisahkan oleh spasi : '))
# kata_satu,kata_dua=dua_kata.split()
# print('dibalik menjadi : '+kata_dua+' '+kata_satu)

# x=int(input('Piramida paskal hingga baris ke N : '))


x=int(input('Piramida paskal hingga baris ke N : '))
satu=1
pascallis=[]
temp=[]
kiri=0
kanan=0
jumlah=0


#pascal list
for i in range (x):
    if i == 0:
        temp.append(satu)
        pascallis.append(temp)
        temp=[]
    elif i > 0:       
        temp.append(satu)
        for j in range(i):
            jumlah+=int(pascallis[kiri][kanan])
            if (kanan+1) == len(pascallis[kiri]):
                kanan+=0
            else:
                kanan+=1
            jumlah+=int(pascallis[kiri][kanan])
            temp.append(jumlah)
            jumlah=0
            if kanan==(len(pascallis[(kiri)])-1):
                kanan=0
            else:
                continue
        temp.append(satu)
        pascallis.append(temp)
        kiri+=1
        temp=[]

print(pascallis)

piramid=''

kiri=0
kanan=0
for a in range(x+2):
    if a == 0:
        for b in range(x+1-a):
            piramid+='  '
        piramid+='     '+str(pascallis[a][a])
    elif a <=2:
        continue
    else:
        for b in range(x+2-a):
            piramid+='  '
        for c in range(a):
            if (pascallis[(a-2)][c])<10:
                piramid+='    '
            elif (pascallis[(a-2)][c])>=10 and (pascallis[(a-2)][c])<100:
                piramid+='   '
            elif (pascallis[(a-2)][c])>100 and (pascallis[(a-2)][c])<1000:
                piramid+='  '
            elif (pascallis[(a-2)][c])>=1000:
                piramid+=' '
            piramid+=str(pascallis[(a-2)][c])
    piramid+='\n'

print('\n')
print(piramid)
