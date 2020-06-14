import random
import math

#0           1
#1       1   2   1
#2     1   3   3   1
#3   1   4   6   4   1
#4  1   5   10  10  5   1

#[[1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 0 [[1]]
# 1 [1,2,1]            = [x[0][0]    x[0][0]+x[0][0]                                    x[0][0]]
# 2 [1,3,3,1]          = [x[1][0]    x[1][0]+x[1][1]  x[1][1]+x[1][0]                   x[1][0]]
# 3 [1,4,6,4,1]        = [x[2][0]    x[2][0]+x[2][1]  x[2][1]+x[2][2]  x[2][2]+x[2][3]  x[2][0]]
# 4 [1,5,10,10,5,1]    = [x[]] 
# 5 [1,6,15,20,15,6,1] = 



x=4
y=''
start=1
isi=0
satu=1
dalam=[[1],[1,2,1]]
temp=[]
kiri=1
kanan=0
jumlah=0


#loop baris 3
#   2 kali loop
#   0   1
#   or
#   1   2

kanan=0
temp.append(satu)

jumlah+=int(dalam[kiri][kanan])
kanan+=1
jumlah+=int(dalam[kiri][kanan])
temp.append(jumlah)
jumlah=0

jumlah+=int(dalam[kiri][kanan])
kanan+=1
jumlah+=int(dalam[kiri][kanan])
temp.append(jumlah)
jumlah=0

temp.append(satu)
dalam.append(temp)
temp=[]

print(dalam)
kiri+=1

kanan=0
temp.append(satu)

jumlah+=int(dalam[kiri][kanan])
kanan+=1
jumlah+=int(dalam[kiri][kanan])
temp.append(jumlah)
jumlah=0

jumlah+=int(dalam[kiri][kanan])
kanan+=1
jumlah+=int(dalam[kiri][kanan])
temp.append(jumlah)
jumlah=0

jumlah+=int(dalam[kiri][kanan])
kanan+=1
jumlah+=int(dalam[kiri][kanan])
temp.append(jumlah)
jumlah=0

temp.append(satu)
dalam.append(temp)
temp=[]

print(dalam)

''' 
for i in range(2, x+1):
    temp = []
    for j in range(i):
        jumlah+=int(dalam[kiri][kanan])
        kanan+=1
        jumlah+=int(dalam[kiri][kanan])
        temp.append(jumlah)
    dalam.append(temp)
    temp.clear
    kiri+=1
    kanan=0

print(dalam)
'''

'''
tickets1=[25,25,50]
tickets2=[25,100]
tickets3=[25,25,50,50,100]


def tickets(customer):
    kas=0
    tiket=25
    no=0
    for i in range(len(customer)):
        if customer[i]==tiket:
            kas+=tiket
        elif customer[i]>tiket:
            if (kas-(customer[i]-tiket))>=0:
                kas-=(customer[i]-tiket)
            else:
                kas-=(customer[i]-tiket)
                no+=1
        print(str(i+1)+' : '+str(kas))
    print('no count : '+str(no))
    yesorno=''
    if no>0:
        yesorno+='NO'
    else:
        yesorno+='YES'
    return yesorno


print(tickets(tickets3))
'''