'''
RABU - 20 Mei 2020
'''

import math
import random

## FIBONACCI ###
'''
bilfibo=[1,2,2,3,5,8,13,21]

def fibo(urut):
    listdata=[1,1]
    for i in range(0,urut):
        listdata.append(listdata[i]+listdata[i+1])
    return listdata[urut-1]

print(fibo(8))

## --- ###

1,1,2,3,4,6
0,1,2,3,4,5
 , , ,1+2,1+3,2+4
 , , ,[0]+[2],[1]+[3],[2]+[4]

def lompat(urut):
    listdata=[1,1,2]
    for i in range(0,urut):
        listdata.append(listdata[i]+listdata[i+2])
    return listdata[urut-1]
listdata=[1,1,2]
print(lompat(4))
print(lompat(5))
print(lompat(6))
print(lompat(7))
print(lompat(8))
x=int(input('Bil lompat sampai N ke-'))
for j in listdata:
    print(j)
for k in range(4,x+1):
    print(lompat(k))
'''

### REVERSE LIST ###
'''
random0=random.randint(0,30)
random1=random.randint(0,30)

def fibolist(urut,random0,random1):
    fibo=[random0,random1]
    for i in range(0,urut):
        fibo.append(fibo[i]+fibo[i+1])
    return fibo

print(fibolist(10,random0,random1))

def balik(normal):
    for j in range(0,(len(normal)//2)):
        temp=normal[j]
        normal[j]=normal[len(normal)-1-j]
        normal[len(normal)-1-j]=temp
    return normal

print(balik(fibolist(10,random0,random1)))
'''

### BUBBLE SORT ###
'''
a=[]
x=int(input('N : '))
for i in range(x):
    a.append(random.randint(0,30))
print(a)
for pertama in range(len(a)):
    for berikut in range(pertama+1,len(a)):
        if a[pertama]>a[berikut]:
            a[pertama],a[berikut]=a[berikut],a[pertama]
print(a)


3,1,5,4,7,8,13
w,x,y,z,w+z,x+7,y+8
normal
balik
descending
'''

random0=random.randint(0,30)
random1=random.randint(0,30)
random2=random.randint(0,30)
random3=random.randint(0,30)

x=int(input('N='))

def fibolist(urut,random0,random1,random2,random3):
    fibo=[random0,random1,random2,random3]
    for i in range(0,urut-4):
        fibo.append(fibo[i]+fibo[i+3])
    return fibo

print(fibolist(x,random0,random1,random2,random3))

def balik(normal):
    for j in range(0,(len(normal)//2)):
        temp=normal[j]
        normal[j]=normal[len(normal)-1-j]
        normal[len(normal)-1-j]=temp
    return normal

print(balik(fibolist(x,random0,random1,random2,random3)))


def besarkecil(a):
    for pertama in range(len(a)):
        for berikut in range(pertama+1,len(a)):
            if a[pertama]<a[berikut]:
                a[pertama],a[berikut]=a[berikut],a[pertama]
    return a

print(besarkecil(fibolist(x,random0,random1,random2,random3)))