# Rabu 10 06 2020


# HH:MM:SS
# if HH>99 "invalid input"


'''
seconds = 14251
hour = seconds // 3600
hourleft = seconds % 3600
minute = hourleft // 60
minuteleft = hourleft % 60

# hour = 9
# minute = 9
# minuteleft = 9

# print(hour)
# print(hourleft)
# print(minute)
# print(minuteleft)

hh = []
mm = []
ss = []
zero = 0

if hour<100 :
    if hour<10:
        hour = str(hour)
        hh.append(zero)
        hh.append(hh.append(hour[0]))
    elif hour>=10:
        hour = str(hour)
        hh.append(hour[0])
        hh.append(hour[1])
    if minute<10:
        minute=str(minute)
        mm.append(zero)
        mm.append(minute[0])
    elif minute>=10:    
        minute = str(minute)
        mm.append(minute[0])
        mm.append(minute[1])
    if minuteleft<10:
        minuteleft=str(minuteleft)
        ss.append(zero)
        ss.append(minuteleft[0])
    elif minuteleft>=10:
        minuteleft = str(minuteleft)
        ss.append(minuteleft[0])
        ss.append(minuteleft[1])
if int(hour)>100:
    print('Invalid Input')


print(seconds)
print(str(hh[0])+str(hh[1])+':'+str(mm[0]+str(mm[1]))+':'+str(ss[0])+str(ss[1]))


# print(hh)
# print(mm)
# print(ss)
'''

# if > 5 pindah ke belakang
'''
isi = [False, 4, 10, 2251, 'True', 223, 'A', True, False, 66, 6]
temp= []
new = []

def belakang(isi):
    for i in range(len(isi)):
        if isinstance(isi[i],int):
            if isi[i] > 5 :
                temp.append(isi[i])
            else:
                new.append(isi[i])
        else:
            new.append(isi[i])
    # print(temp)
    # print(new)
    for depan in range (len(temp)):
        for belakang in range (depan+1,len(temp)):
            if temp[depan]>temp[belakang]:
                temp[depan],temp[belakang]=temp[belakang],temp[depan]
    # print(temp)
    new.extend(temp)
    # print(new)
    return new

print(isi)
print(belakang(isi))
# belakang(isi)
'''

#           1
#       2   3   5
#     4  5  6  7  22
# 8  9  10  11  12  13 63    

baris=int(input('N baris : '))
normal = []
jumlah = []
x = ''
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


# zzzz=0
# for a in range(0,baris+1):
#     for b in range(0,(baris-a),1):
#         x+='  '
#     for c in range(0,(a+zzzz),1):
#         if c<(len(normal[a-1])):    
#             x+='  '+str(normal[(a-1)][c])+''
#         else:
#             continue
#     if a>1 :
#         x+='  '+str(jumlah[(a-2)][0])+''
#     x+='\n'
#     zzzz+=1
# print(x)

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