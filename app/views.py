from app import app, db, login_manager
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
from flask import abort, request, render_template, redirect
from app.models import Fridge, FridgeUser, Login, User

def checkUserAuth(func):
    @wraps(func)
    def returnFunc(*args, **kwargs):
        if not current_user.is_authenticated:
            abort(405)

        return func(*args, **kwargs)

    return returnFunc

@login_manager.user_loader
def load_user(id):
    return FridgeUser.get(id)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not current_user.is_authenticated:
            user = FridgeUser.get(loginid=username)
            
            if user and password == user.password:
                login_user(user, remember=True)
            else:
                return render_template('login.html', error='Username or password incorrect!')

    if current_user.is_authenticated:
        return redirect("/dashboard")
    else:
        return render_template('login.html')

@app.route("/")
def landing():
    return render_template('landing.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        country_code = request.form['country_code']
        phone = request.form['phone']
        budget = request.form['budget']
        loginid = request.form['loginid']
        password = request.form['password']

        user = User(name=name, email=email, address=address, countrycode=country_code, phone=phone, budget=budget)
        user.add(user)
        login = Login(uid=user.uid, loginid=loginid, password=password)
        login.add(login)
        return redirect("/login")

    else:
        return render_template('register.html')

@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        uid = current_user.id
        model = request.form['model']
        fridge = Fridge(uid=uid, model=model)
        fridge.add(fridge)
    fridges = Fridge.query.filter_by(uid=current_user.id)
    return render_template('dashboard.html', username=current_user.name, fridges=fridges)