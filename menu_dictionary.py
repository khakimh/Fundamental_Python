# d = {}

# def isi_dictionary():
#     print('''Pilih jenis value :
#     1. String
#     2. Number
#     ''')
#     angka = int(input('Masukkan Menu = '))
#     panjang = int(input('Masukkan panjang dictionary = '))     
#     for loop1 in range (panjang):
#         keyx = str(input('Masukkan Key = '))
#         if angka == 1:
#             valx = str(input('Masukkan Value = '))
#             d[keyx] = (valx)
#         elif angka == 2:
#             valx = int(input('Masukkan Value = '))
#             d[keyx] = (valx)
#         else:
#             print ('Masukkin angka yang bener dong bambang :(')
#     return d.items()

# def cari_dictinarty():
#     dy = []
#     dz = {}
#     carix = str(input('Search = '))
#     print('''___________________________
# |____KEY____|____VALUE____|''')
#     for key,val in d.items():
#         dy.append(key)
#     for loop1 in range (len(dy)):
#         if carix in dy[loop1]:
#             dz[dy[loop1]] = d[dy[loop1]]
#     for key,val in dz.items():
#         if type(dz[key]) == type (1):
#             print("|    '{}'    |    {}    |".format(key,val))
#         else:
#             print("|    '{}'    |    '{}'    |".format(key,val))
#     return

# def lihat_dictionary():
#     for key,val in d.items():
#         if type(d[key]) == type (1):
#             print("|    '{}'    |    {}    |".format(key,val))
#         else:
#             print("|    '{}'    |    '{}'    |".format(key,val))
#     return

# def mainmenu():
#     angka = True
#     while (angka < 4):
#         print('''Selamat datang di aplikasi pengolah dictionary
#     Menu :
#     1. Lihat Full Dictionary
#     2. Isi Dictionary
#     3. Searching Dictionary
#     4. Keluar
#     ''')
#         angka = int(input('Masukkan Menu : '))
#         if angka == 1:
#             print('''___________________________
# |____KEY____|____VALUE____|''')
#             lihat_dictionary()
#         elif angka == 2:
#             isi_dictionary()
#         elif angka == 3:
#             cari_dictinarty()
#         elif angka == 4:
#             print('Terima kasih sudah mencoba, silahkan datang kembali!')
#         else:
#             print('Masukkan angka yang bener dong bambang :(')
#             return

# mainmenu()