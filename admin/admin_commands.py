import os

from Core.Storage import load_data,save_data

def admin_login():
    print("----------admin login---------")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "admin1234":
        print("Login Successful")
        admin_menu()
    else:
        print("Login Failed")


def admin_menu():
    while True:
        print("----------admin panel---------")
        print("1.show users")
        print("2.searche user")
        print("3.delete user")
        print("4.Logout")

        admin_choice = input("Enter your choice(1-4): ")

        if admin_choice == "1":
            os.system("cls")
            show_users()


        elif admin_choice == "2":
         os.system("cls")
         search_user()

        elif admin_choice == "3":
            os.system("cls")
            delete_user()

        elif admin_choice == "4":
            break
        else:
            print("Invalid choice")


def show_users():
    users = load_data()

    if  not users:
        print("No users found")
    else:
        for username in users:
            user = users[username]
            print(username)
            print(f"is verified :{user["is_verified"]}")
            print(f"skills:{user["skills"]}")
            print(f"name:{user["profile"]["name"]}")
            print(f"age:{user["profile"]["age"]}")
            print(f"city:{user["profile"]["city"]}")
            print()
            print("___________________________________________________")



def search_user():
    users = load_data()
    user_to_found = input("Enter username to search: ")
    if not users:
        print("No users exist")
    elif user_to_found in users:
        user = users[user_to_found]
        print(user["username"])
        print(f"is verified :{user['is_verified']}")
        print(f"skills:{user['skills']}")
        print(f"name:{user['profile']['name']}")
        print(f"age:{user['profile']['age']}")
        print(f"city:{user['profile']['city']}")
        print()
    else:
        print("user not found")


def delete_user():
    users = load_data()
    user_to_delete = input("Enter username to delete: ")

    if user_to_delete in users:
        users.pop(user_to_delete)
        print("user deleted")
    else:
        print("user not found")

    save_data(users)