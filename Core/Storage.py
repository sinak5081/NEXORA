import json
import os
file_name = "users.json"

def save_data(users):
    with open(file_name,"w") as file:
        json.dump(users,file,indent=4)

def load_data():
    if os.path.exists(file_name):
        with open(file_name,"r") as file:
            data = json.load(file)
            return data
    else:
        return {}
