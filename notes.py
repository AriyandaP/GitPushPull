'''
1 HARI

1,5 JAM

1 JAM

SELASA - 19 Mei 2020

SENIN/SELASA - 18/19 Mei 2020
PR05 - MUHAMAD ARIYANDA PUTRA


759 063 2858

BelajarDS

raihan 085261477003
prissilya 081510908848


PRINT
print('string')
print(str(int))
print(( )+....)


FUNCTION
def nama_fungsi(parameter atau variable, ... , ... ,):
    program

#calling list: nama_fungsi

#using: return untuk bisa berinteraksi dengan fungsi lain atau operasi lain diluar

LIST
list[x,y,z]
#calling list: list[0]=x, ... ,list[2]=z


'''

x=[5,4,1,6,4,3,0]

def sortascending(x):
    for pertama in range(len(x)):
        for kedua in range(pertama,len(x)):
            if x[pertama]>x[kedua]:
                x[pertama],x[kedua]=x[kedua],x[pertama]
    return x

def onlyeven(x):
    for i in range(len(x)):
        if x[i]==0:
            x[i]=' '
        elif x[i]%2!=0:
            x[i]=' '
    return x

print(sortascending(x))
print(onlyeven(sortascending(x)))