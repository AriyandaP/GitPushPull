### VARIABLE ###
kursi={
    'Alien':
    {   'Siang':
            [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]],
        'Malam':
            [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
    },
    'Community':
    {   'Siang':
            [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]],
        'Malam':
            [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
    }}
film={1:'Alien',2:'Community'}
jadwal={1:'Siang',2:'Malam'}
stop = False
pilih=0
pilih_film=0
pilih_jadwal=0
qtiket=0
belanja=[]
row=0
seat=0
### FUNCTION ###
def menu():
    print('\n')
    print('---MENU---')
    print('\n')
    print('1.Pesan tiket')
    print('2.Lihat history')
    print('3.Keluar')
    print('\n')

def filmfilm():
    print('---PILIH FILM---')
    print('\n')
    print('Film yang sedang tayang adalah : ')
    print('\n')
    for i in film:
        print(str(i)+'.'+film.get(i))
    print('3.Menu')
    print('\n')
    
def jadwaljadwal():
    print('---PILIH JADWAL---')
    print('\n')
    print('Jadwal tayang yang tersedia untuk film : '+film[int(pilih_film)])
    for i in jadwal:
        print(str(i)+'.'+jadwal.get(i))
    print('3.Menu')
    print('\n')

def print_kursi(film,jadwal):
    for i in kursi[film][jadwal]:
        print(' '.join(map(str,i)))

def isi_kursi(film,jadwal,row,seat):
    row-=1
    seat-=1
    kursi[film][jadwal][row][seat]='X'
    return kursi

def beli_tiket():
    berhenti = False
    while(not berhenti):
        print("Pembelian tiket untuk film '"+film[int(pilih_film)]+"' jadwal '"+jadwal[int(pilih_jadwal)]+"'")
        qtiket=input('Berapa banyak tiket yang akan dibeli : ')
        if(int(qtiket)<=10 and int(qtiket)>=1):
            berhenti = True
            for i in range(int(qtiket)):
                print('Pilih tempat duduk untuk tiket nomor.'+str(i+1))
                print_kursi(film[int(pilih_film)],jadwal[int(pilih_jadwal)])
                row=int(input('Baris ke : '))
                seat=int(input('Kursi ke : '))
                isi_kursi(film[int(pilih_film)],jadwal[int(pilih_jadwal)],row,seat)
                catat_belanja(row,seat)
            print_kursi(film[int(pilih_film)],jadwal[int(pilih_jadwal)])
        elif(int(qtiket)>10 or int(qtiket)<1):
            berhenti = False
            print('Jumlah tiket yang bisa dibeli dalam satu kali transaksi adalah kisaran 1 sampai 10 lembar tiket')
        else:
            berhenti = False
            tidak_dikenal()

def kembali_menu():
    print('\n')
    print('---kembali ke Menu---')

def tidak_dikenal():
    print('\n')
    print('Keyword yang dimasukkan tidak dikenal.')

def catat_belanja(row,seat):
    belanja.append("Nama film : '"+film[int(pilih_film)]+"' Untuk jadwal : '"+jadwal[int(pilih_jadwal)]+"' row:"+str(row)+' seat:'+str(seat))

def print_belanja():
    nomor=1
    print('Jumlah tiket yang dibeli : '+str(len(belanja))+' lembar')
    print('History belanja anda : ')
    for j in belanja:
        print(str(nomor)+'. '+j)
        nomor+=1

### PROGRAM ###
while(not stop):
    menu()
    pilih=input('Masukan pilihan : ')
    if(pilih=='1'):
        stop = False
        filmfilm()
        pilih_film=input('Pilih film : ')
        if(pilih_film=='1'):
            jadwaljadwal()
            pilih_jadwal=input('Pilih jadwal : ')
            if(pilih_jadwal=='1'):
                beli_tiket()
            elif(pilih_jadwal=='2'):
                beli_tiket()
            elif(pilih_jadwal=='3'):
                kembali_menu()
            else:
                tidak_dikenal()
        elif(pilih_film=='2'):
            jadwaljadwal()
            pilih_jadwal=input('Pilih jadwal : ')
            if(pilih_jadwal=='1'):
                beli_tiket()
            elif(pilih_jadwal=='2'):
                beli_tiket()
            elif(pilih_jadwal=='3'):
                kembali_menu()
            else:
                tidak_dikenal()
        elif(pilih_film=='3'):
            kembali_menu()
        else:
            tidak_dikenal()
    elif(pilih=='2'):
        print_belanja()
        stop = False
    elif(pilih=='3'):
        stop = True
        print('\n')
        print('---Terima Kasih---')
    else:
        tidak_dikenal()