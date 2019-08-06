def listx(x):
    y = []
    for a in range (1,((x**2)+1)):
        y.append(a)
    return y 

def normal(x):
    z = ''
    for loop1 in range (1,len(listx(x))+1):
        z += ' {} '.format(loop1)
        if loop1 % x == 0:
            z += '\n'
    return print(z)

def kebalik(x):
    z = ''
    for loop1 in range (len(listx(x)),0,-1):
        z += ' {} '.format(loop1)
        if (loop1+(x-1)) % x == 0:
            z += '\n'
    return print(z)

def putar_kanan(x):
    z = ''
    for b in range ((((x-1)*x)+1),(len(listx(x))+1)):
        for a in range (x):
            z += ' {} '.format(b-(x*a))
        z += '\n'
    return print(z)

def putar_kiri(x):
    z = ''
    for b in range (x,0,-1):
        for a in range (x):
            z += ' {} '.format(b+(x*a))
        z += '\n'
    print(z)

def mainmenu():
    jalan = 'y'
    while (jalan == 'y' ):
        x = int(input('Masukkan ukuran = '))
        normal(x)
        putarx = input('Pilih putar ke kanan atau ke kiri = ').lower()
        kalix = int(input('Pilih mau putar berapa kali = '))
        if putarx == 'kanan' and kalix%4 == 1:
            putar_kanan(x)
        elif putarx == 'kanan' or putarx == 'kiri' and kalix%4 == 2:
            kebalik(x)
        elif putarx == 'kanan' and kalix%4 == 3:
            putar_kiri(x)
        elif putarx == 'kanan' or putarx == 'kiri' and kalix%4 == 0:
            normal(x)
        elif putarx == 'kiri' and kalix%4 == 1:
            putar_kiri(x)
        elif putarx == 'kiri' and kalix%4 == 3:
            putar_kanan(x)
        jalan = input('Main lagi ? (y/n) : ')
         

mainmenu()