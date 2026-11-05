from Core import auth
from commands import user_commands,guest_commands
from admin.admin_commands import admin_login
import os
while True:
    print("---------------User manager------------------")
    print("1.register")
    print("2.login")
    print("3.continue as guest")
    print("4.admin login")
    print("5.exit")

    choice = input("Enter your choice(1-5):")

    if choice == "1":
        os.system("cls")
        auth.register_user()

    elif choice == "2":
        os.system("cls")
        success,user,users = auth.login_user()
        if success:
            os.system("cls")
            user_commands.user_menu(user,users)
        else:
            print("username or password incorrect")
    elif choice == "3":
        os.system("cls")
        guest_commands.guest_menu()
    elif choice == "4":
        os.system("cls")
        admin_login()
    elif choice == "5":
        print("goodbye")
        break
    else:
        print("invalid choice")

