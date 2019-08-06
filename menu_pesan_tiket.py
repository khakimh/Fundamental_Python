x = [[],[],[],[],[],[],[],[]]
dictionary = {'Avengers: Endgame' : {'siang' : {1:x[0],2:x[1]},'malam': {1:x[2],2:x[3]}},'Spider-Man: Far From Home' : {'siang' : {1:x[4],2:x[5]},'malam': {1:x[6],2:x[7]}}}
tempat_duduk = [[],[],[],[],[]]
for d in range (5):
    for c  in range (2):
        tempat_duduk[d].append([' O ',' O ',' O ',' O ',' O ',' O ' ,' O ',' O ',' O ',' O '])

def print_kursi(x):
    z = ''
    for a in range (2):
        for b in range (len(x[a])):
            z += x[a][b]
        z += '\n'
    return print(z)

def pesan_tiket():
    film = int(input("\n Daftar Fiilm \n 1. 'Avengers: Endgame' \n 2. 'Spider-Man: Far From Home' \n Masukkan Pilihan : "))
    if film == 1:
        z = 'Avengers: Endgame'
    elif film == 2:
        z = 'Spider-Man: Far From Home'
    jadwal = 0 + int(input("\n Pilih Jadwal Film '{}' \n 1. Siang \n 2. Malam \n Masukkan Pilihan : ".format(z)))
    jumlah = int(input('\n Pesan Tiket Berapa Kali :' ))
    for loop in range (jumlah):
        row = int(input('\n Pilih Row : '))
        seat = int(input('\n Pilih Seat : '))
        if tempat_duduk[((film**2)+1)-jadwal][row-1][seat-1] == ' - ':
            print(' Maaf tempat duduk tersebut telah dipesan, Silahkan pilih tempat duduk lain!')
            print_kursi(tempat_duduk[((film**2)+1)-jadwal])
        else:
            tempat_duduk[((film**2)+1)-jadwal][row-1][seat-1] = ' - '
            print_kursi(tempat_duduk[((film**2)+1)-jadwal]) 
            if film ==1 and jadwal ==1 and row ==1:
                x[0].append(seat)
            elif film ==1 and jadwal ==1 and row ==2:
                x[1].append(seat)
            elif film ==1 and jadwal ==2 and row ==1:
                x[2].append(seat)
            elif film ==1 and jadwal ==2 and row ==2:
                x[3].append(seat)
            elif film ==2 and jadwal ==1 and row ==1:
                x[4].append(seat)
            elif film ==2 and jadwal ==1 and row ==2:
                x[5].append(seat)
            elif film ==2 and jadwal ==2 and row ==1:
                x[6].append(seat)
            elif film ==2 and jadwal ==2 and row ==2:
                x[7].append(seat)
            else:
                print('Masukkin yang bener dong bambang!')
    return

def lihat_history(d):
    for key in d.keys():
        for keyx in d[key].keys():
            for keyy,valy in d[key][keyx].items():
                for loop in range (len(valy)):
                    if valy != []:
                        print (" Film '{}' jadwal {} row {} seat {}". format(key,keyx,keyy,valy[loop]))

def mainmenu():
    menu = True
    while (menu <= 2):
        menu = int(input('Menu : \n 1. Pesan Tiket \n 2. Lihat History \n 3. Keluar \n Masukkan Pilihan : '))
        if menu == 1:
            pesan_tiket()
        elif menu == 2:
            lihat_history(dictionary)
        elif menu == 3:
            print(' Terima Kasih!')
        else:
            print(' Masukkin yang bener dong bambang!')

mainmenu()