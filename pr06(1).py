# PR Rabu 10 06 2020 - Kamis 11 06 2020


#           1
#       2   3   5
#     4  5  6  7  22
# 8  9  10  11  12  13 63    

baris=int(input('N baris : '))
x = ''

'''
normal = []
jumlah = []
z=2
satu=[1]
zz=0
zzz=0


normal.append(satu)
for i in range(2, baris+1):
    temp = []
    for j in range((i+zzz)):
        temp.append(z)
        z+=1
    zzz+=1
    normal.append(temp)
    temp.clear

print(normal)

for k in range(1,len(normal)):
    jumlahtemp = []
    for l in range(len(normal[k])):
        zz+=normal[k][l]
    jumlahtemp.append(zz)
    zz=0
    jumlah.append(jumlahtemp)
    jumlahtemp.clear

print(jumlah)


#                                                 normal[0][0]
#                                 normal[1][0]    normal[1][1]    jumlah[0]
#                 normal[2][0]    normal[2][1]    normal[2][2]    normal[2][3]    jumlah[1]
# normal[3][0]    normal[3][1]    normal[3][2]    normal[3][3]    normal[3][4]    normal[3][5]    jumlah[2]


zzzz=0
for a in range(0,baris+1):
    for b in range(0,(baris-a),1):
        x+='    '
    for c in range(0,(a+zzzz),1):
        if c<(len(normal[a-1])): 
            if normal[(a-1)][c]<10:
                x+=' '   
            x+='  '+str(normal[(a-1)][c])+''
        else:
            continue
    if a>1 :
        x+='  '+str(jumlah[(a-2)][0])+''
    x+='\n'
    zzzz+=1
print(x)
'''


#        1
#     2  3  5
#    4  5  6  16
#   7  8  9 10 34
# 11 12 13 14 15 65    


'''
start = 1
total = 0
for i in range((baris+1)):
    for j in range((baris-i)):
        x+='  '
    for k in range(i):
        if start==1:
            x+='     '
        elif start<10:
            x+='   '
        elif start>=10 and start<100:
            x+='  '
        elif start>=100:
            x+=' '
        x+=str(start)
        total+=start
        start+=1
    if i<=1:
        x+='\n'
    elif i>1:
        if total<10:
            x+='   '
        elif total>=10 and start<100:
            x+='   '
        elif total>=100:
            x+=' '
        x+=str(total)
        x+='\n'
    total=0
print(x)
'''


hitung=1
lompat=0
jumlah=0
for a in range(0,(baris),1):
    for b in range(0,(baris-a),1):
        x+='    '
    if hitung == 1:
        x+='   '+str(hitung)
        hitung+=1
    else:
        for c in range(0,(a+lompat),1):
            if hitung<10:
                x+='   '
            elif hitung>=10 and hitung<100:
                x+='  '
            elif hitung>100:
                x+=' '
            x+=str(hitung)
            jumlah+=hitung
            hitung+=1
        if jumlah<10:
            x+='   '
        elif jumlah>=10 and jumlah<100:
            x+='  '
        elif jumlah>100:
            x+=' '
        x+=str(jumlah)
        jumlah=0
    lompat+=1
    x+='\n'
print(x)


