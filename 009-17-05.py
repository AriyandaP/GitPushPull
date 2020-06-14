'''
MINGGU - 17 MEI 2020
'''

import math
import random

### 1 ###
'''
#soal jumlah kata
#fungsi jumlah kata

#input : masukin kalimat
#output : per kata berapa jumlahnya
# ' jumlah kata ' xx ' ada sebanyak yy

kata=[]
hitung={}
kalimat='ari 1 adalah 2 nama saya ARI'
# (input('Input kalimat : '))
kalimat=kalimat.lower()
for i in kalimat.split():
    kata.append(i)
# print(kata)
for j in kata:
    if j in hitung:
        hitung[j]+=1
    else:
        hitung[j]=1

# print(hitung)

for k in hitung:
    print("Jumlah kata '"+k+"' ada sebanyak '"+str(hitung.get(k))+"'")

# for j in kata:
#     print("Jumlah kata '"+str(j)+"' ada sebanyak '"+str(kata.count(j))+"'")

'''
### 2 ###
'''
#input angka
#ouput seven segment display clock

list_angka=[]
input_angka='1 2 3 4 5 6 7 8 9 0 10'
for i in input_angka.split():
    list_angka.append(int(i))
# print(list_angka)

xxx x_x x_x xxx x_x x_x x_x x_x x_x x_x
xx| x_| x_| |_| |_x |_x xx| |_| |_| |x|
xx| |_x x_| xx| x_| |_| xx| |_| x_| |_|

z=''
for atas in list_angka:
    if((atas==1) or (atas==4)):
        z+='     '
    else:
        z+='  _  '
z+='\n'
for tengah in list_angka:
    if((tengah==4) or (tengah==8) or (tengah==9)):
        z+=' |_| '
    elif((tengah==2) or (tengah==3)):
        z+='  _| '
    elif((tengah==5) or (tengah==6)):
        z+=' |_  '
    elif(tengah==0):
        z+=' | | '
    else:
        z+='   | '
z+='\n'
for bawah in list_angka:
    if((bawah==8) or (bawah==6) or (bawah==0)):
        z+=' |_| '
    elif((bawah==5) or (bawah==3) or (bawah==9)):
        z+='  _| '
    elif(bawah==2):
        z+=' |_  '
    else:
        z+='   | '
print(z)
'''
### 3 ###
'''
#input: ukuran matriks
#input2: angka urut atau random
#output matriks


# matrik_jadi=[
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]
# matrik=[]
# x=3
# print(matrik_jadi[1][1])
# print(matrik_jadi)

def urut(matrik):
    x=1
    m=''
    i=''
    for i in range(matrik):
        for i in range(matrik):
            m+=str(x)+' '
            x+=1
        m+='\n'
    return(m)

def acak(matrik):
    n=''
    j=''
    for j in range(matrik):
        for j in range(matrik):
            n+=str(random.randint(1,100))+' '
        m+='\n'
    return n

m=''
x=1
pilih=0
stop = False
while(not stop):
    matrik=int(input('Input ukuran matriks : '))
    print('1. Angka urut')
    print('2. Angka random')
    print('3. Berhenti')
    pilih=input('pilih angka yang dimasukkan ke matriks : ')
    if(pilih=='1'):
        print(urut(matrik))
    elif(pilih=='2'):
        print(acak(matrik))
    elif(pilih=='3'):
        stop=True

'''

### 4 ###

isi=[]
'''
def acak(x):
    i=0
    for i in range(x):
        isi.append(random.randint(0,100))
    return isi

def total():
    jumlah=0
    for j in isi:
        jumlah+=j
    return jumlah

def vardev():
    jumlah2=0
    for j in range(0,x):
        kuadrat=(isi[j]-ratarata)**2
        jumlah2+=kuadrat
    variansi=jumlah2/(x-1)
    print('Variansi dari data diatas adalah : '+str(variansi))
    deviasi=math.sqrt(variansi)
    print('Standar deviasi dari data diatas adalah : '+str(deviasi))

x=int(input('Berapa banyak angka acak yang akan dimasukan : '))

print(str(x)+' Angka acak yang dimasukan :'+str(acak(x)))

# print(total())

ratarata=(total()/x)

# print(ratarata)

vardev()
'''

### 5 ###
'''
angka=[]

def acak(x):
    i=0
    for i in range(x):
        angka.append(random.randint(0,100))
    return angka

def ascending(angka):
    for pertama in range(len(angka)):
        for berikutnya in range(pertama+1,len(angka)):
            if angka[pertama]>angka[berikutnya]:
                angka[pertama],angka[berikutnya]=angka[berikutnya],angka[pertama]
    return angka

def tengah_ganjil():
    print(angka[(len(angka)//2)])

def tengah_genap():
    print((angka[(len(angka)//2)]+angka[((len(angka)//2)-1)])/2)

q=int(input('Berapa banyak data random yang di input : '))
acak(q)
print('Data random yang didapatkan : '+str(angka))
ascending(angka)
# angka.sort
print(angka)
if(len(angka)%2==0):
    print('Median dari data-data diatas adalah : ')
    tengah_genap()
elif(len(angka)%2!=0):
    print('Median dari data-data diatas adalah : ')
    tengah_ganjil()

'''
### 6 ###
angka=[]
hitung={}

def acak(x):
    for i in range(x):
        angka.append(random.randint(0,10))
    return angka

def berapa(x):    
    for j in x:
        if j in hitung:
            hitung[j]+=1
        else:
            hitung[j]=1
    return hitung

q=int(input('Berapa banyak data random yang di input : '))
acak(q)
print(angka)
berapa(angka)
print(hitung)

print(max(hitung, key=hitung.get))