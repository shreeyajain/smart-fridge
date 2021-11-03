from app import app, db, login_manager
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
from flask import abort, request, render_template, redirect
from app.models import Fridge, FridgeUser, Login, User
from sqlalchemy import text

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

@app.route("/fridge/<int:fid>")
@login_required
def fridge(fid):
    fridgeUser = Fridge.query.filter_by(fid=fid, uid=current_user.id).all()
    if len(fridgeUser) == 0:
        return redirect("/dashboard")
    
    query = text("SELECT stores.fid fid, stores.conid conid, stores.catid catid, content.name, stores.amount, stores.unit, stores.price, stores.store, category.name category from stores, content, category where stores.conid = content.conid and stores.catid = category.catid and fid={} order by category.name;".format(fid))
    data = db.session.execute(query)
    return render_template('fridge.html', data=data, fid=fid)

@app.route("/shopping/<int:fid>")
@login_required
def shopping(fid):
    fridgeUser = Fridge.query.filter_by(fid=fid, uid=current_user.id).all()
    if len(fridgeUser) == 0:
        return redirect("/dashboard")
    
    query = text("SELECT content.name, stores.amount, stores.unit, stores.price, stores.store, category.name from stores, content, category where stores.conid = content.conid and stores.catid = category.catid and fid={} order by category.name;".format(fid))
    data = db.session.execute(query)
    return render_template('shopping.html', data=data, fid=fid)

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

@app.route("/add/<int:fid>", methods=['GET', 'POST'])
@login_required
def add(fid):
    fridgeUser = Fridge.query.filter_by(fid=fid, uid=current_user.id).all()
    if len(fridgeUser) == 0:
        return redirect("/dashboard")
    
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        unit = request.form['unit']
        price = request.form['price']
        store = request.form['store']
        catid = request.form['category']

        if not catid.isnumeric():
            result = db.session.execute("INSERT INTO category(name) VALUES ('{}') RETURNING catid".format(catid))
            db.session.commit()
            catid = result.first()
        
        conid = db.session.execute("SELECT conid from content where LOWER(name)=LOWER('{}')".format(name)).first()
        if not conid:
            result = db.session.execute("INSERT INTO content(name, catid) VALUES ('{}', {}) RETURNING conid".format(name, catid))
            db.session.commit()
            conid = result.first()
        
        db.session.execute("INSERT INTO stores(fid, conid, catid, amount, unit, price, store) VALUES ({},{},{},{},'{}',{}, '{}');".format(fid, conid[0], catid, amount, unit, price, store))
        db.session.commit()
        return redirect("/fridge/{}".format(fid))

    categories = db.session.execute("SELECT name, catid from category;")
    return render_template('add.html', categories=categories, fid=fid)

@app.route("/edit", methods=['GET', 'POST'])
@login_required
def edit():
    fid = request.args.get('fid', default = None)
    conid = request.args.get('conid', default = None)
    catid = request.args.get('catid', default = None)
    
    if fid == None or catid == None or conid == None:
        return redirect("/dashboard")
    
    fridgeUser = Fridge.query.filter_by(fid=fid, uid=current_user.id).all()
    if len(fridgeUser) == 0:
        return redirect("/dashboard")
    
    if request.method == 'POST':
        amount = request.form['amount']
        price = request.form['price']
        unit = request.form['unit']

        query = text("UPDATE stores SET amount={}, price={}, unit='{}' where fid={} and conid={} and catid={};".format(amount, price, unit, fid, conid, catid))
        print(query)
        db.session.execute(query)
        db.session.commit()
        return redirect("/fridge/{}".format(fid))

    query = text("SELECT content.name, stores.amount, stores.unit, stores.price, stores.store, category.name category from stores, content, category where stores.conid = content.conid and stores.catid = category.catid and stores.fid={} and stores.conid={} and stores.catid={};".format(fid, conid, catid))
    data = db.session.execute(query).first()
    return render_template('edit.html', item=data, fid=fid, conid=conid, catid=catid)

@app.route("/delete", methods=['GET'])
@login_required
def delete():
    fid = request.args.get('fid', None)
    conid = request.args.get('conid', None)
    catid = request.args.get('catid', None)
    if fid == None or catid == None or conid == None:
        return redirect("/dashboard")
    
    fridgeUser = Fridge.query.filter_by(fid=fid, uid=current_user.id).all()
    if len(fridgeUser) == 0:
        return redirect("/dashboard")

    query = text("DELETE from stores where fid={} and conid={} and catid={};".format(fid, conid, catid))
    db.session.execute(query)
    db.session.commit()
    return redirect("/fridge/{}".format(fid))