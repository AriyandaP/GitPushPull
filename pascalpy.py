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



x=int(input('Piramida paskal hingga baris ke N : '))
satu=1
dua=2
pascallis=[]
temp=[]
kiri=1
kanan=0
jumlah=0

#pascal list
for i in range (x):
    if i == 0:
        temp.append(satu)
        pascallis.append(temp)
        temp=[]
    elif i == 1:
        temp.append(satu)
        temp.append(dua)
        temp.append(satu)
        pascallis.append(temp)
        temp=[]
    elif i>1:       
        temp.append(satu)
        for j in range(i):
            jumlah+=int(pascallis[kiri][kanan])
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

print(piramid)