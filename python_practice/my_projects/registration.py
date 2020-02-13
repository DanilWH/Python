# В дальнейшем заного, с самого начала сделать программу для регистрации.
import json

def registration(users):
    f_n = False
    f_p = False
    while not f_n:
        name = input("What is your name:")
        # Проверка выхода.
        if name == 'q':
            break
        elif name in users.keys():
            print("This name is already taken! Try again!\n")
            f_n = False
            #continue
        else:
            f_n = True
            print('Complete!')

    while not f_p:
        if name != 'q':
            password = input("Create a password:")
            # Проверка выхода.
            if password == 'q':
                break
            password_second = input("Enter your password again:")
            # Проверка выхода.
            if password_second == 'q':
                break

            elif password != password_second:
                print('Passwords do not match! Try again!\n')
                f_p = False
                #continue
            else:
                f_p = True
                print('Complete!')

                users[name] = password # Add a user in dictonary.
                load_users(users)
                print("Registration is successful!\n")
        else:
            print('') # Сделано для отступа!
            break

def log_in(users):
    f_i = False
    while not f_i:
        name = input("Enter your name:")
        # Проверка выхода.
        if name == 'q':
            break
        password = input("Enter your password:")
        # Проверка выхода.
        if password == 'q':
            break

        elif name in users.keys() and users[name] == password:
            print('Log in complete!\n')
            f_i = True
        else:
            f_i = False
            print("Log in miss! Try again!\n")
            question = input("We offer free registration[y/n]:")
            if question == 'y':
                registration(users)
                break
            else:
                break

def load_users(users):
    with open('username.json', 'w') as file_dump:
        json.dump(users, file_dump)


with open('username.json', 'r') as file_read:
    users = json.load(file_read)

while True:

    question = input("What do you want to do? [log in/registration]")
    if question == 'q':
        break
    if question == 'log in':
        log_in(users)
    elif question == 'registration':
        registration(users)
