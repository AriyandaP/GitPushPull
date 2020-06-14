import math

# #while loop

# angka=1
# while(angka<=10):
#     print(angka)
#     angka+=1
# else:
#     print('selesai')

#range(mulai dari sama dengan,sampai kurang dari,interval)

# listitem=list(range(1,11,2))
# print(listitem)
# for angka in range(1,11,2):
#     print(angka)

# for nomor_urut in range(1,11,1):
#     print('NOMOR URUT '+str(nomor_urut))

# angka=1
# while(angka<=10):
#     print('NOMOR URUT '+str(angka))
#     angka+=1

# for nomor_urut2 in range(0,51,5):
#     print('NOMOR URUT '+str(nomor_urut2))

# z=''
# for item in range(0,5):
#     for item in range(0,5):
#         z+=' * '
#     z+='\n'
# print(z)

# z=''
# for item in range(0,10,2):
#     for item1 in range(1)(item+2):
#         z+=' * '
#     z+='\n'
# print(z)

jumlah=0
jumlah1=0
data=int(input('input: '))

list=[]
for item in range(0,data,1):
    item1=int(input('Data No.'+str(item+1)+': '))
    list.append(item1)
    jumlah+=item1

print(str(list))
print(str(jumlah))
print(str(list[1]))
ratarata=jumlah/data
print(str(ratarata))

jumlah2=0

for item2 in range(0,data,1):
    kuadrat=(list[item2]-ratarata)**2
    jumlah2+=kuadrat
variansi=jumlah2/data
print(str(variansi))
