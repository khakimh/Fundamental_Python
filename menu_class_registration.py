user_pass = {}
user_classs = {}
username_global = []

def register():
    username = input('Username : ')
    password = input('Password : ')
    if username not in user_pass.keys():
        user_pass[username] = password
        user_classs[username] = []
        print('Log in Sucessfully')
        if username_global == []:
            username_global.append(username)
        else:
            username_global[0] = username
    else:
        print('Username Already Exist')


def login(username_global):
    username = input('Username : ')
    password = input('Password : ')

    for key in user_pass.keys():
        if username == key:
            if password == user_pass[username]:
                print('Log in Successfully')
                if username_global == []:
                    username_global.append(username)
                else:
                    username_global[0] = username
            else:
                print('username or password might be wrong')

def class_registration(username):
    kelas = int(input('Avalaible Class : \n 1.Data Science \n 2.Web and Mobile Development \n 3.Digital Marketing \n 4.UI/UX Designer \n Choose : '))
    if kelas == 1:
        user_classs[username].append('Data Science Class')
    elif kelas == 2:
        user_classs[username].append('Web and Mobile Development')
    elif kelas == 3:
        user_classs[username].append('Digital Marketing')
    elif kelas == 4:
        user_classs[username].append('UI/UX Designer')
    else:
        print('Masukkan Pilihan dengan benar!')

def History(username):
    history_class = []
    for loop in range (len(user_classs[username])):
        history_class.append(user_classs[username][loop])

    if len(history_class) == 1:
        print('Class taken by {} is {}'.format(username,history_class[0]))
    elif len(history_class) == 2:
        print('Class taken by {} are {} and {}'.format(username,history_class[0],history_class[1]))
    elif len(history_class) >= 3:
            x = 'Class taken by ' +  str(username) + ' are '
            y = ''
            for loop in range ((len(history_class)-1)):
                if loop == 0:
                    y += str(history_class[loop])
                else:
                    y += ',' + str(history_class[loop])
            z = ' and ' + str(history_class[-1])
            print(x+y+z)


def mainmenu():
    menu = True
    while(menu <= 5):
        if username_global != []:
            print('\nCurrent User is {}'.format(username_global[0]))
        menu = int(input('Welcome to the Purwadhika Class Registration! Please choose your selection: \n 1.Register \n 2.Login \n 3.Class registration \n 4.History \n 5.Log out \n 6.Exit \n Choose : '))
        if menu == 1:
            register()
        elif menu == 2:
            if username_global != []:
                print('You already login!')
            elif user_pass == {}:
                print('There is no account avalaible, please register first!')
            else:
                login(username_global)
        elif menu == 3:
            if username_global == []:
                print('Login required!')
            else:
                class_registration(username_global[0])
                print(user_classs)
        elif menu == 4:
            if username_global == []:
                print('Login required!')
            else:
                History(username_global[0])
        elif menu == 5:
            if username_global == []:
                print('You are not log in yet!')
            else:
                username_global.pop()
        elif menu == 6:
            print('Thank You!')

mainmenu()