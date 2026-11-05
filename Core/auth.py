
from Core.Storage import load_data, save_data

def register_user():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    users = load_data()
    if username in users:
        print("username already taken")
    else:
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        city = input("Please enter your city: ")
        role = "user"
        verify = input("user is verified? y/n: ")
        if verify == "y":
            is_verified = True
        else:
            is_verified = False

            
        skill = input("Please enter your skills (separate with spaces): ")
        skills = skill.split(" ")

        user = {
            "username": username,
            "password": password,
            "is_verified": is_verified,
            "skills": skills,
            "profile": {
                "name": name,
                "age": age,
                "city": city
            }
        }

        users[username] = user
        save_data(users)

        print("Registration successful!")


def login_user():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    users = load_data()
    if username in users and password == users[username]["password"]:
        return True,users[username],users
    else:
        return False,None,None