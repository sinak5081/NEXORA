from flask import Flask, render_template,request,flash,redirect,url_for,session
from Core import Storage
app = Flask(__name__)
app.secret_key = "1234"

    
@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username:
            flash("username empty")
            return redirect(url_for('login'))
        
        if not password:
            flash("password is empty")
            return redirect(url_for('login'))
       
        users = Storage.load_data()

        if username not in users:
            flash("User does not exist")
            return redirect(url_for('login'))
        if users[username]["password"] != password:
            flash("Incorrect password")
            return redirect(url_for('login'))
        session["username"] = username
        session["role"] = users[username]["role"]
        if session["role"] == "admin":
            flash("Welcome admin")
            return redirect(url_for("admin"))
        else:
            flash("Login successful")
            return redirect(url_for('index'))
        
@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if not username:
            flash("username emopty")
            return redirect(url_for('register'))

        if not password:
            flash("password is empty")
            return redirect(url_for('register'))

        if password != confirm_password:
            flash("paswword and confirm passwodr not match")
            return redirect(url_for('register'))
        if username in Storage.load_data():
            flash("username already exist")
            return redirect(url_for('register'))
        user = {
    "username": username,
    "password": password,
    "role":"user",
    "is_verified": False,
    "skills": [],
    "profile": {
        "name": "",
        "age": None,
        "city": ""
    }


}
        users= Storage.load_data()
        users[username] = user
        Storage.save_data(users)
        flash("create account succssfully")
        return redirect(url_for("profile"))
        
@app.route("/skills",methods = ["GET","POST"])
def skills():
    if "username" not in session:
        return redirect(url_for("login"))
    users = Storage.load_data()
    user = session["username"]
    user = users[user]

    if request.method == "POST":
        delete_skill = request.form.get("delete_skill", "").strip()
        if delete_skill:
            if delete_skill in user["skills"]:
                user["skills"].remove(delete_skill)
                flash("Skill removed successfully", "success")
                Storage.save_data(users)
                return redirect(url_for("skills"))
            else:
                flash("Skill not found", "error")
                return redirect(url_for("skills"))
        skill = request.form.get("skill", "").strip()
        if skill:
            if skill in user["skills"]:
                flash("skills is exist", "error")
                return redirect(url_for("skills"))
            user["skills"].append(skill)
            Storage.save_data(users)
            flash("Skill added successfully", "success")
            return redirect(url_for("skills"))
    else:
        return render_template("skills.html",user = user)


@app.route("/profile",methods = ["GET","POST"])
def profile():
    if "username" not in session:
        return redirect(url_for("login"))
    users = Storage.load_data()
    username = session["username"]
    user = users[username]
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        city = request.form.get("city")
        if not age.isdigit():
            flash("age is not digit")
            return redirect(url_for("profile"))
        age = int(age)
        if not 0<age<100:
            flash("age is not valid")
            return redirect(url_for("profile"))

        user["profile"]["name"] = name
        user["profile"]["age"] = age
        user["profile"]["city"] = city
        Storage.save_data(users)


        flash("profile saved")
        return redirect(url_for("index"))


    return render_template("profile.html",user = user)

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully", "success")
    return redirect(url_for("login"))

@app.route("/admin")
def admin():
    users = Storage.load_data()
    total_users = 0
    verified_users = 0
    unverified_users = 0
    for user in users.values():
        if user["role"] == "user":
            total_users += 1
            if user["is_verified"] == True:
                verified_users += 1
            else:
                unverified_users  += 1
    
    return render_template("admin_dashboard.html",users = users,total_users = total_users,verified_users = verified_users,unverified_users = unverified_users)

@app.route("/admin/verify/<username>",methods = ["POST"])
def toggle_verify(username):
    users = Storage.load_data()
    user = session["username"]
    if users[user]["role"] == "admin":
        if username in users:
            target_user = users[username]
            if target_user["role"] == "user":
                target_user["is_verified"] = not target_user["is_verified"]
                Storage.save_data(users)
                return redirect(url_for("admin"))



@app.route("/")
def index():
    missing = []
    completion = 0
    user = None
    if "username" in session:
        users = Storage.load_data()
        user = users[session["username"]]


        name = user["profile"]["name"].strip()
        age = user["profile"]["age"]
        city = user["profile"]["city"].strip()
        if name:
            completion += 1

        if age:
            completion += 1

        if city:
            completion += 1

        completion = (completion/3) * 100

        if not name:
            missing.append("name")
        if not age:
            missing.append("age")
        if not city:
            missing.append("city")

        
    return render_template("index.html",user=user,completion = completion,missing = missing)





if __name__ == "__main__":
    app.run(debug=True)