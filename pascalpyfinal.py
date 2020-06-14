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

# piramid 
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
