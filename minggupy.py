''' 
soal 1 : class luas dan keliling layang-layang
Luas = 1/2 x d1 x d2
keliling = 2 x (sisi1 + sisi2) 

'''
import math
'''
class luaskelilingbangun():
    def __init__(self,diagonal1,diagonal2,sisi1,sisi2,jari,alas,tinggijajar,sisimiring,sisiketupat,diagonalketupat1,diagonalketupat2,sisisejajar1,sisisejajar2,tinggitrapesium,sisimiringtrapesium1,sisimiringtrapesium2):
        self.d1=diagonal1
        self.d2=diagonal2
        self.s1=sisi1
        self.s2=sisi2
        self.r=jari
        self.a=alas
        self.tj=tinggijajar
        self.sm=sisimiring
        self.sk=sisiketupat
        self.dk1=diagonalketupat1
        self.dk2=diagonalketupat2
        self.ss1=sisisejajar1
        self.ss2=sisisejajar2
        self.tt=tinggitrapesium
        self.smt1=sisimiringtrapesium1
        self.smt2=sisimiringtrapesium2
    def luaslayang(self):
        llayang=(self.d1*self.d2/2)
        return llayang
    def kelilinglayang(self):
        kellayang=(2*(self.s1+self.s2))
        return kellayang
    def luassetengahlingkaran(self):
        lsetlingkaran=((math.pi*self.r*self.r)/2)
        return lsetlingkaran
    def kelilingsetengahlingkaran(self):
        kelsetlingkaran=(math.pi*self.r)
        return kelsetlingkaran
    def luasjajargenjang(self):
        ljajar=(self.a*self.tj)
        return ljajar
    def kelilingjajargenjang(self):
        keljajar=(2*(self.a+self.sm))
        return keljajar
    def luasbelahketupat(self):
        lketupat=((self.dk1*self.dk2)/2)
        return lketupat
    def kelilingbelahketupat(self):
        kelketupat=(self.sk*4)
        return kelketupat
    def luastrapesium(self):
        ltrapesium=(((self.ss1+self.ss2)*self.tt)/2)
        return ltrapesium
    def kelilingtrapesium(self):
        keltrapesium=self.ss1+self.ss2+self.smt1+self.smt2
        return keltrapesium


print('1. Layang-layang')
diagonal1=int(input("Masukan ukuran diagonal 1 dari layang-layang : "))
diagonal2=int(input("Masukan ukuran diagonal 2 dari layang-layang : "))
sisi1=int(input("masukan ukuran sisi 1 dari layang-layang : "))
sisi2=int(input("masukan ukuran sisi 2 dari layang-layang : "))
print('---')

print('2. Setengah lingkaran')
jari=int(input('Masukan ukuran jari-jari dari setengah lingkaran : '))
print('---')

print('3. Jajar genjang')
alas=int(input("masukan ukuran alas dari jajar genjang : "))
tinggijajar=int(input("masukan ukuran tinggi dari jajar genjang : "))
sisimiring=int(input("masukan ukuran sisi miring dari jajar genjang : "))
print('---')

print('4. Belah ketupat')
sisiketupat=int(input("masukan ukuran sisi dari belah ketupat : "))
diagonalketupat1=int(input("masukan ukuran diagonal 1 dari belah ketupat : "))
diagonalketupat2=int(input("masukan ukuran diagonal 2 dari belah ketupat : "))
print('---')

print('5. Trapesium')
sisisejajar1=int(input("masukan ukuran sisi sejajar 1 dari trapesium  : "))
sisisejajar2=int(input("masukan ukuran sisi sejajar 2 dari trapesium : "))
tinggitrapesium=int(input("masukan ukuran tinggi dari trapesium : "))
sisimiringtrapesium1=int(input("masukan ukuran sisi miring 1 dari trapesium  : "))
sisimiringtrapesium2=int(input("masukan ukuran sisi miring 1 dari trapesium  : "))
print('---')


masukkan = luaskelilingbangun(diagonal1,diagonal2,sisi1,sisi2,jari,alas,tinggijajar,sisimiring,sisiketupat,diagonalketupat1,diagonalketupat2,sisisejajar1,sisisejajar2,tinggitrapesium,sisimiringtrapesium1,sisimiringtrapesium2)



print('1. Layang-layang')
print('Luas layang-layang dengan ukuran diagonal 1 "'+str(diagonal1)+'" dan diagonal 2 "'+str(diagonal2)+'" adalah : '+ str(masukkan.luaslayang()))
print('Keliling layang-layang dengan ukuran sisi 1 "'+str(sisi1)+'" dan sisi 2 "' +str(sisi2)+'" adalah : '+ str(masukkan.kelilinglayang()))
print('---')

print('2. Setengah lingkaran')
print('Luas setengah lingkaran dengan ukuran jari-jari "'+str(jari)+'" adalah : '+str(masukkan.luassetengahlingkaran()))
print('Keliling setengah lingkaran dengan ukuran jari-jari "'+str(jari)+'" adalah : '+str(masukkan.kelilingsetengahlingkaran()))
print('---')

print('3. Jajar genjang')
print('Luas jajar genjang dengan ukuran alas "'+str(alas)+'" dan tinggi "'+str(tinggijajar)+'" adalah : '+ str(masukkan.luasjajargenjang()))
print('Keliling jajar genjang dengan ukuran alas "'+str(alas)+'" dan sisi miring "' +str(sisimiring)+'" adalah : '+ str(masukkan.kelilingjajargenjang()))
print('---')

print('4. Belah ketupat')
print('Luas belah ketupat dengan ukuran diagonal 1 "'+str(diagonalketupat1)+'" dan diagonal 2 "'+str(diagonalketupat2)+'" adalah : '+ str(masukkan.luasbelahketupat()))
print('Keliling belah ketupat dengan ukuran sisi "'+str(sisiketupat)+'" adalah : '+ str(masukkan.kelilingbelahketupat()))
print('---')

print('5. Trapesium')
print('Luas trapesium dengan ukuran sisi sejajar 1 "'+str(sisisejajar1)+'", sisi sejajar 2 "'+str(sisisejajar1)+'" dan tinggi "'+str(tinggitrapesium)+'" adalah : '+ str(masukkan.luastrapesium()))
print('Keliling trapesium dengan ukuran sisi sejajar 1 "'+str(sisisejajar1)+'", sisi sejajar 2 "'+str(sisisejajar2)+'", sisi miring 1 "'+str(sisimiringtrapesium1)+'", sisi miring 2 "'+str(sisimiringtrapesium2)+'" adalah : '+ str(masukkan.kelilingtrapesium()))
print('---')
'''

'''
umurlist=list()
class murid():
    def __init__(self, a, b, c):
        self.nama=a
        self.nomor=b
        self.umur=c
    def tampilkan(self):
        print('Nama siswa : '+self.nama+', dengan nomor :'+str(self.nomor)+', dan berumur '+str(self.umur)+' tahun.')
        umurlist.append(self.umur)
        # print(umurlist)

murid1=murid('ari',10045,23)
murid2=murid('ira',10046,32)
murid3=murid('rai',10047,24)
murid4=murid('ria',10048,42)
murid5=murid('iar',10049,20)

murid1.tampilkan()
murid2.tampilkan()
murid3.tampilkan()
murid4.tampilkan()
murid5.tampilkan()

# print(umurlist)
total=0
for i in range(len(umurlist)):
    total+=umurlist[i]
# print(total)
rata=total/(len(umurlist))
# print(rata)
print('Rata-rata umur dari murid-murid diatas adalah : '+str(rata))
'''

'''
jamlist=list()

def konversidetik(detik):
    jam=detik//3600
    sisamenit=detik%3600
    menit=sisamenit//60
    sisadetik=sisamenit%60
    print(str(detik)+' detik adalah : '+str(jam)+' jam '+str(menit)+' menit dan '+str(sisadetik)+' detik.')
    nol=0
    if jam<10:
        jamlist.append(nol)
        jamlist.append(jam)
    else:
        jamlist.append(str(str(jam)[0]))
        jamlist.append(str(str(jam)[1]))
    if menit<10:
        jamlist.append(nol)
        jamlist.append(menit)
    else:
        jamlist.append(str(str(menit)[0]))
        jamlist.append(str(str(menit)[1]))
    if sisadetik<10:
        jamlist.append(nol)
        jamlist.append(sisadetik)
    else:
        jamlist.append(str(str(sisadetik)[0]))
        jamlist.append(str(str(sisadetik)[1]))
    print(str(jamlist[0]),str(jamlist[1])+' : '+str(jamlist[2]),str(jamlist[3])+' : '+str(jamlist[4]),str(jamlist[5]))
detik=int(input('Masukan detik : '))



# detik=7552

konversidetik(detik)

# jam=32
# menit=2
# sisadetik=52

# nol=0
# if jam<10:
#     jamlist.append(nol)
#     jamlist.append(jam)
# else:
#     jamlist.append(str(str(jam)[0]))
#     jamlist.append(str(str(jam)[1]))

# if menit<10:
#     jamlist.append(nol)
#     jamlist.append(menit)
# else:
#     jamlist.append(str(str(menit)[0]))
#     jamlist.append(str(str(menit)[1]))

# if sisadetik<10:
#     jamlist.append(nol)
#     jamlist.append(sisadetik)
# else:
#     jamlist.append(str(str(sisadetik)[0]))
#     jamlist.append(str(str(sisadetik)[1]))

# print(jamlist)
# print(str(jamlist[0]),str(jamlist[1])+' : '+str(jamlist[2]),str(jamlist[3])+' : '+str(jamlist[4]),str(jamlist[5]))
'''

### output 
#list inside a list [1],[3,5],[7,9,11],...
#piramid
#total list terakhir

'''
n=10
start=1
listluar=[]

for i in range(1,n+1):
    listdalam=[]
    for j in range(i):
        listdalam.append(start)
        start+=2
    listluar.append(listdalam)

print(listluar)

x=''

# print(listluar[0][0])
# print(listluar[1][0])

for a in range(1,n+1):
    for b in range(0,n-a,1):
        x+='  '
    for c in range(0,a,1):
        x+='  '+str(listluar[(a-1)][c])+' '
    x+='\n'
print(x)

total=0
for zz in range(len(listluar[n-1])):
    total+=listluar[(n-1)][zz]
# print(total)
rata=total/len(listluar[n-1])
# print(rata)

print(str(listluar[n-1])+' = '+str(total))

totallist=''

for zzz in range(len(listluar[n-1])):
    print(listluar[n-1][zzz])
    totallist+=(listluar[n-1][zzz])
'''

### apabila diatas 5 huruf dibalik

'''
textlist=list()

text = 'tes kalimat percobaan keempat'

pisah = text.split()

kalimatbaru=[]
katabaru=[]

for i in range(len(pisah)):
    if len(pisah[i])>5:
        kata=list(pisah[i])
        xx=len(kata)
        for j in range(xx):
            katabaru.append(kata[xx-1])
            xx-=1
        kalimatbaru.append(''.join(map(str,katabaru)))
        katabaru.clear()
    else:
        kalimatbaru.append(pisah[i])

print(' '.join(map(str,kalimatbaru)))
'''

'''

listlist=[False,1,0,4,'b',0,'Z',5,0,0,2,0,False]

print(listlist)

xx=len(listlist)

# print(xx)

for i in range(xx):
    if type(listlist[i])==type(False):
        continue
    elif listlist[i]==0:
        listlist.pop(i)
        listlist.append(0)
    else:
        continue
        
print(listlist)

for i in range(xx):
    if type(listlist[i])==type(False):
        continue
    elif listlist[i]==0:
        listlist.pop(i)
        listlist.append(0)
    else:
        continue

print(listlist)

# listbaru=[]
# listtemp=[]
# nol=0

# for i in range(xx):
#     if listlist[i]==False:
#         listbaru.append(False)
#     elif listlist[i]==0:
#         listtemp.append(nol)
#     else:
#         listbaru.append(listlist[i])

# print(listbaru)
# print(listtemp)

# listbaru.extend(listtemp)

# print(listbaru)
'''


pop=1000
growth=2
migration=50
maks=1100
year=0

def pertumbuhan(pop,growth,migration,maks,year):
    while pop<maks:
        pop+=(pop*growth/100)+migration
        year+=1
    print(year)

pertumbuhan(pop,growth,migration,maks,year)

# year+=1
# print(year)
# pop+=(pop*growth/100)+migration
# print(pop)

# year+=1
# print(year)
# pop+=(pop*growth/100)+migration
# print(pop)

# year+=1
# print(year)
# pop+=(pop*growth/100)+migration
# print(pop)

# year+=1
# print(year)
# pop+=(pop*growth/100)+migration
# print(pop)