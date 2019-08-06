bintang = int(input('Masukkan Besar Bintang : '))
y=''
z=''
for item1 in range (bintang,0,-1):
    for a in range (0,item1):
        y += ' a '
    for b in range (0,bintang-item1):
        y += ' - '
    for c in range (0,(bintang-1)-item1):
        y += ' + '
    for d in range (0,item1-1):
        y += ' * '
    if (item1==bintang):
        y += ''
    else:
        y += ' * '
    y += '\n'
for item2 in range (0,(bintang-1)):
    for e in range (0,item2+2):
        z += ' * '
    for f in range (0,(bintang-2)-item2):
        z += '   '
    for g in range (0,(bintang-3)-item2):
        z += '   '
    for h in range (0,item2+1):
        z += ' * '
    if (item2==(bintang-2)):
        z += ''
    else:
        z += ' * '
    z += '\n'
print(y+z)