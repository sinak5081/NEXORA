import os
from Core.Storage import save_data
def show_profile(user):
    if user["is_verified"]:
        print("🍓 Verified User 🍓")

    print(f'"username": "{user["username"]}"')
    print(f'"is_verified": {user["is_verified"]}')
    print(f'"skills": {user["skills"]}')
    print('"profile": {')
    print(f'    "name": "{user["profile"]["name"]}"')
    print(f'    "age": {user["profile"]["age"]}')
    print(f'    "city": "{user["profile"]["city"]}"')


def user_menu(user,users):
    while True:

        print("---------user menu---------")
        print("1.show profile")
        print("2.edit profile")
        print("3.manage skills")
        print("4.logout")

        user_choice = input("Enter your choice(1-4):")

        if user_choice == "1":
            os.system("cls")
            show_profile(user)
        elif user_choice == "2":
            os.system("cls")
            edit_profile(user,users)
        elif user_choice == "3":
            os.system("cls")
            manage_skills(user,users)
        elif user_choice == "4":
            os.system("cls")
            print("logged out")
            break
        else:
            print("invalid choice")


def edit_profile(user,users):
    print("-------------edit profile----------------")
    print("1.edit name")
    print("2.edit age")
    print("3.edit city")
    print("4.edit skills")
    user_choice = input("Enter your choice(1-4):")
    if user_choice == "1":
        new_name = input("Enter new name:")
        user["profile"]["name"] = new_name
        print()
    elif user_choice == "2":
        new_age = input("Enter new age:")
        user["profile"]["age"] = new_age
    elif user_choice == "3":
        new_city = input("Enter new city:")
        user["profile"]["city"] = new_city
    elif user_choice == "4":
        new_skills = input("Enter new skills(separate with spaces):")
        new_skills = new_skills.split()
        user["skills"] = new_skills

    else:
        print("invalid choice")
        return
    save_data(users)
    print("🍓 Profile edited successfully!")



def manage_skills(user,users):
    print("1.add skills")
    print("2.remove skills")
    choice = input("Enter your choice(1-2):")
    if choice == "1":
        skills_name = input("Enter skills name:(separate with spaces):)")
        skills_name = skills_name.split()
        added = False
        for skill in skills_name:
            if skill not in user["skills"]:
                user["skills"].append(skill)
                added = True
            else:
                print("skills already exist")
        if added:
            print("🍓 Skills added successfully!")
            save_data(users)
        else:
            print("Skills not added")

    elif choice == "2":
        skill_name = input("Enter skill name to delete:")
        if skill_name in user["skills"]:
            user["skills"].remove(skill_name)
            print("Skill removed successfully!")
            save_data(users)
        else:
            print("Skill not exist")
    else:
        print("invalid choice")