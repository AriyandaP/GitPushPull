'''
SENIN - 18 Mei 2020
'''

import math
import random

### TUPLES ###

#cannot be modified
'''
t = 1,2,3,4,5,'tes'
t1 = (1,2,3,4,5,'tes1')
t2 = 'string'
t3 = 'tuples',

print(t)
print(type(t))
print(t1)
print(type(t1))
print(t2)
print(type(t2))
print(t3)
print(type(t3))

tup = 1,'str', True, [2,'string', False,[2.5, 'list within list']],{'3': 3.2, '3.4': ['list within tuple']}
tupp = ('data tunggal',)

print(tup)
print(tup[0])
print(tup[3])
print(tup[3][2])
print(tup[3][3])
print(tup[3][3][1])
print(tup[4])
print(tup[4]['3.4'])
print(tupp)
'''
### SETS ###

#no duplicate
'''
s={1,3,2,4,2,2,1,1,0,'C','b','C','A','B','a',(1,2,3),(1,2,3),(6,5,4)}

print(s)
print(type(s))

setkosongsalah = {}
print(setkosongsalah)
print(type(setkosongsalah))
setkosongbenar = set()
print(setkosongbenar)
print(type(setkosongbenar))

mentah=[]
x=int(input('N angka random : '))
for i in range(x):
    mentah.append(random.randint(0,10))
print(mentah)
print('\n')
filtered=set(mentah)
print(filtered)

'''

### List Comprehension ###

'''
z=int(input('list mulai dari : '))
y=int(input('List sampai N ke : '))
listnum=[x for x in range(z,y+1)]
print('---list normal---')
print(listnum)
print('len list : '+str(len(listnum)))
print('---')
if(z%2==0):
    listganjil=[ganjil for ganjil in range(z+1,y+1,2)]
    print('---list ganjil---')
    print(listganjil)
    print('len list : '+str(len(listganjil)))
    print('---')
    listgenap=[genap for genap in range(z,y+1,2)]
    print('---list genap---')
    print(listgenap)
    print('len list : '+str(len(listgenap)))
    print('---')
else:
    listganjil=[ganjil for ganjil in range(z,y+1,2)]
    print('---list ganjil---')
    print(listganjil)
    print('len list : '+str(len(listganjil)))
    print('---')
    listgenap=[genap for genap in range(z+1,y+1,2)]
    print('---list genap---')
    print(listgenap)
    print('len list : '+str(len(listganjil)))
    print('---')
'''

### LAMBDA ###
'''
def square_sum(x,y):
    return x**2 + y**2

print(square_sum(5,4))

print((lambda x,y: x**2 + y**2)(5,4))

#((x**y//z)**w)/m
x=int(input('x : '))
y=int(input('y : '))
z=int(input('z : '))
w=int(input('w : '))
m=int(input('m : '))


def xyzwm(x,y,z,w,m):
    hasil=(((x**y//z)**w)/m)
    return hasil

print(xyzwm(x,y,z,w,m))

test = lambda x,y,z,w,m : ((x**y//z)**w)/m

print(test(x,y,z,w,m))

print(lambda x,y,z,w,m: ((x**y//z)**w)/m)(x,y,z,w,m)

'''

### Check ###
'''
cari = ''
cari=input('cari : ')
kalimat=['merdeka','hello','hellos','sohib','kari ayam']
filtered=[]

for kata in range(len(kalimat)):
    if cari in kalimat[kata] :
        filtered.append(kalimat[kata])
print(filtered)



cari = ''
pilih=''
kalimat=[]
kalimatlower=[]
filtered=[]
stop = False
i=1

while(not stop):
    isi=input('masukkan kata ke-'+str(i)+' : ')
    kalimat.append(isi)
    i+=1
    pilih=input('lanjut y/n : ')
    if((pilih=='y') or (pilih=='Y')):
        stop = False
    elif((pilih=='n') or (pilih=='N')):
        stop = True
print('---list kata yang dimasukkan---')
print(kalimat)
print('---')
cari=input('cari : ')
for kata in range(len(kalimat)):
    if cari in kalimat[kata] :
        filtered.append(kalimat[kata])
print('---hasil filter---')
print(filtered)
print('---')

'''