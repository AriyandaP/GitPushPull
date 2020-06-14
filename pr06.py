# PR Rabu 10 06 2020 - Kamis 11 06 2020


print('1. Piramida 1 3 5 7 9 ... dst.')
print('2. Piramida 1 3 4 5 6 ... dst.')
pilih=input('Piramida nomor : ')
baris=int(input('Hingga n baris ke : '))

def pilihpiramid(pilih,baris):
    if pilih == '1':
        print(lompat(baris))
    elif pilih =='2':
        print(tidaklompat(baris))
    else:
        print('Pilihan tidak dikenal')        


#           1
#       2   3   5
#     4  5  6  7  22
# 8  9  10  11  12  13 63    
# dst


def lompat (baris):
    x = ''
    hitung=1
    lompat=0
    jumlah=0
    for a in range(0,(baris),1):
        for b in range(0,(baris-a),1):
            x+='    '
        if a == 0:
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
    return x


#        1
#     2  3  5
#    4  5  6  16
#   7  8  9 10 34
# 11 12 13 14 15 65    
# dst


def tidaklompat (baris):
    x = ''
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
    return x


pilihpiramid(pilih,baris)

