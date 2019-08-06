

def sort_ascending(x):
    for a in range (0,len(x)):
        for b in range (a+1,len(x)):
            if (x[b] < x[a]):
                x[a],x[b] = x[b],x[a]
    return x

def sort_descending(x):
    for a in range (0,len(x)):
        for b in range (a+1,len(x)):
            if (x[b] > x[a]):
                x[a],x[b] = x[b],x[a]
    return x
 
def min(x):
    z = sort_ascending(x)[0]
    return z

def max(x):
    z = sort_descending(x)[0]
    return z

def minmaxx(x): # - alternte
    minx = sort_ascending(x)[0]
    maxx = sort_descending(x)[0]
    return print('Nilai tertingi adalah {} dan nilai terendah adalah {}'.format(maxx,minx))

def genap(x):
    genapx = 0
    for loop2 in range (0,len(x)):
        if x[loop2]%2 == 0:
            genapx += 1
    return genapx

def ganjil(x):
    ganjilx = 0
    for loop3 in range (0,len(x)):
        if x[loop3]%2 == 1:
            ganjilx += 1
    return ganjilx

def ganjilxgenap(x): #alternate
    ganjil1 = 0
    genap1 = 0
    for loop3 in range (0,len(x)):
        if x[loop3]%2 == 0:
            genap1 += 1
        else:
            ganjil1 += 1
    return print('Jumlah angka genap adalah {} dan jumlah angka ganjil adalah {}'.format(genap1,ganjil1))

def mainmenu():
    array = []
    angka = True
    while(angka <=  5):
        print('''Selamat datang di aplikasi pengolah array
    Silahkan pilih :
    1. Isi Array
    2. Lihat Array
    3. Sort Array
    4. Nilai tertinggi dan terendah
    5. Jumlah ganjil dan genap
    6. keluar
    ''')
        angka = int(input('Masukkin angka : '))
        if angka == 1:
            panjang = int(input('Masukkan panjang array : '))
            for loop1 in range (0,panjang):
                isi = int(input('Masukkan angka : '))
                array.append(isi)
        elif angka == 2:
            print(array)
        elif angka == 3:
            print('''Silahkan pilih :
        1. Ascending
        2. Descending
        ''')
            sort = int(input('Masukkan angka : '))
            if sort == 1:
                print(sort_ascending(array))
            elif sort == 2:
                print(sort_descending(array))
            else:
                print('Bodo lu bambang :(')
        elif angka == 4:
            print('''Silahkan pilih :
        1. Tertinggi
        2. Terendah
        3. Keduanya
        ''')
            minmax = int(input('Masukkan angka : '))
            if minmax == 1:
                print(max(array))
            elif minmax ==2:
                print(min(array))
            elif minmax == 3:
                minmaxx(array)
            else:
                print('Masukin yang bener dong bambang :(')
        elif angka == 5:
            ganjilxgenap(array)
        elif angka == 6:
            print('Terima Kasih!')
        else:
            print('Masukin yang bener dong bambang :(')
            
    
            return 

mainmenu()