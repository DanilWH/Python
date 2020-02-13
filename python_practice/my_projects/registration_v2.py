
def registration(users):
    while True:
        name = input("Your name: ")
        if name in users.keys():
            print("This name is exists! Try again!")
            continue
        else:
            break
    while True:
        password = input("Your password: ")
        password_one = input("Enter password yet time: ")
        if password != password_one:
            print("Passwords are not match! Try again!")
            continue
        else:
            break
    users[name] = password

def log_in(users):
    while True:
        name = input("Enter your name:")
        password = input("Enter your password:")
        if name in users.keys() and users[name] == password:
            print("Success!")
            break
        else:
            print("Username or password is incorrect! Try again!")
            answer = input('registration? [y/n]')
            if answer == 'y':
                registration(users)
                break
            else:
                break

users = {}
while True:
    answer = input("reg or log?")
    if answer == 'reg':
        registration(users)
    elif answer == 'log':
        log_in(users)
    elif answer == 'q':
        break
