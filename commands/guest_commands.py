from Core.auth import register_user,login_user
from commands import user_commands
import os

def about_application():
    print("🍓 USER MANAGEMENT 🍓")
    print("This application allows you to:")
    print("- Create an account")
    print("- Login to your account")
    print("- Manage your profile")
    print("- Add and remove skills")
    input("\nPress Enter to return to the guest menu...")
    os.system("cls")
def guest_menu():
    os.system("cls")
    demo_user = None
    while True:
        print("----------Guest Profile Manager----------")
        print("1.About this application")
        print("2.Register")
        print("3.login")
        print("4.Create Demo Profile")
        print("5.show demo profile")
        print("6.manage demo skills")
        print("7.Back to main menu")

        guest_choice = input("Enter your choice(1-7): ")
        if guest_choice == "1":
            os.system("cls")
            about_application()
            print()
        elif guest_choice == "2":
            os.system("cls")
            register_user()
        elif guest_choice == "3":
            os.system("cls")
            success , user,users = login_user()
            if success:
                print("login successful")
                user_commands.user_menu(user,users)
            else:
                print("login failed")

        elif guest_choice == "4":
            os.system("cls")
            demo_user = create_demo_profile()

        elif guest_choice == "5":
            os.system("cls")
            if demo_user is not None:
                show_demo_profile(demo_user)
            else:
                print("No demo profile found")

        elif guest_choice == "6":
            os.system("cls")
            if demo_user is not None:
                manage_demo_skill(demo_user)
            else:
                print("No demo profile found")


        elif guest_choice == "7":
            os.system("cls")
            break
        else:
            print("invalid choice")



def create_demo_profile():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    city = input("Please enter your city: ")
    skill = input("Please enter your skills(seperated by space): ")

    skills = []

    for skil in skill.split():
        if skil not in skills:
            skills.append(skil)
        else:
            print("Skill already exists")


    demo_user = {
        "name":name,
        "age":age,
        "city":city,
        "skills":skills
    }

    print("create demo profile successfully")
    return demo_user

def show_demo_profile(demo_user):
    print(f"name: {demo_user['name']}")
    print(f"age: {demo_user['age']}")
    print(f"city: {demo_user['city']}")
    print(f"skills: {demo_user['skills']}")



def manage_demo_skill(demo_user):
    while True:
        print("1.add skill")
        print("2.remove skill")
        print("3.exit")

        demo_user_choice = input("Enter your choice(1-3): ")
        if demo_user_choice == "1":
            new_skill = input("Please enter your new skill(separated by space): ")
            for skill in new_skill.split():
                if skill not in demo_user["skills"]:
                    demo_user["skills"].append(skill)
                    print("skill added")
                else:
                    print("Skill already exists")
        elif demo_user_choice == "2":
            delete_skill = input("please enter skill you want to delete: ")
            if delete_skill in demo_user["skills"]:
                demo_user["skills"].remove(delete_skill)
                print("skill deleted")
            else:
                print("Skill does not exist")


        elif demo_user_choice == "3":
            os.system("cls")
            break



        else:
            print("invalid choice")