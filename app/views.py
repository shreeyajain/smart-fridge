from app import app, db, login_manager
from flask_login import current_user, login_user, logout_user, login_required
from flask import request, render_template, redirect
from app.models import FridgeUser
from sqlalchemy import text

def check_fridge_authorization(func):
    def inner(fid):
        fridgeUser = db.session.execute("SELECT * from fridge where uid={} and fid={}".format(current_user.id, fid)).all()
        if len(fridgeUser) == 0:
            return redirect("/dashboard")
        return func(fid)
    inner.__name__ = func.__name__
    return inner

@login_manager.user_loader
def load_user(id):
    return FridgeUser.get(id)

@app.route("/")
def landing():
    return render_template('landing.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            print(username, password)
            if not current_user.is_authenticated:
                user = FridgeUser.get(loginid=username)
                print(user)
                if user and password == user.password:
                    login_user(user, remember=True)
                else:
                    return render_template('login.html', error='Username or password incorrect!')
        
        except Exception as e:
            print(e)
            return render_template('login.html', error='Server encountered an error. Please try again later.')

    if current_user.is_authenticated:
        return redirect("/dashboard")
    else:
        return render_template('login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            address = request.form['address']
            country_code = request.form['country_code']
            phone = request.form['phone']
            budget = request.form['budget']
            loginid = request.form['loginid']
            password = request.form['password']

            user = db.session.execute("INSERT INTO users(name,email,address,countrycode,phone,budget) VALUES ('{}', '{}', '{}', {}, {}, {}) RETURNING uid".format(name, email, address, country_code, phone, budget))
            db.session.execute("INSERT INTO login(uid, loginid, password) VALUES ({}, '{}', '{}')".format(user.first()[0], loginid, password))
            db.session.commit()
            return redirect("/login")

        except Exception as e:
            print(e)
            db.session.rollback()
            return render_template('register.html', error='Server encountered an error. Please try again later.')
    else:
        return render_template('register.html')

@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    user = db.session.execute("SELECT * FROM users WHERE uid={}".format(current_user.id)).first()
    try:
        if request.method == 'POST':
            name = request.form['name']
            if name == "":
                name = user.name
            email = request.form['email']
            if email == "":
                email = user.email
            address = request.form['address']
            if address == "":
                address = user.address
            country_code = request.form['country_code']
            if country_code == "":
                country_code = user.countrycode
            phone = request.form['phone']
            if phone == "":
                phone = user.phone
            budget = request.form['budget']
            if budget == "":
                budget = user.budget
            
            update_query = text("update users set name = '{}', email = '{}', address = '{}', countrycode = {}, \
                                phone = {}, budget = {} where uid = {}".format(name, email, address, country_code,
                                phone, budget, current_user.id))
            db.session.execute(update_query)
            db.session.commit()

            return redirect("/dashboard")
    
    except Exception as e:
        print(e)
        db.session.rollback()
        return render_template('profile.html', error='Server encountered an error. Please try again later.')

    else:
        return render_template('profile.html', user=user)

@app.route("/fridge/<int:fid>", methods=['GET', 'POST'])
@login_required
@check_fridge_authorization
def fridge(fid):
    if request.method == 'POST':
        try:
            for key in request.form:
                locid = key
                temp = request.form[key]
                query = "UPDATE settings SET temp={} WHERE locid={} and fid={}".format(temp, locid, fid)
                db.session.execute(query)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return render_template('fridge.html', error='Server encountered an error. Please try again later.')

    query = "SELECT locid, name, temp from settings where fid={}".format(fid)
    settings = db.session.execute(query)
    query = text("SELECT stores.fid fid, stores.conid conid, stores.catid catid, content.name, stores.amount, stores.unit, stores.price, stores.store, category.name category from stores, content, category where stores.conid = content.conid and stores.catid = category.catid and fid={} order by category.name;".format(fid))
    data = db.session.execute(query)
    nickname = db.session.execute("SELECT nickname from fridge where fid={}".format(fid)).first()
    return render_template('fridge.html', data=data, settings=settings, fid=fid, nickname=nickname[0])

@app.route("/shopping/<int:fid>")
@login_required
@check_fridge_authorization
def shopping(fid):
    query = text("SELECT content.name, stores.amount, stores.unit, stores.price, stores.store, category.name from stores, content, category where stores.conid = content.conid and stores.catid = category.catid and fid={} order by category.name;".format(fid))
    data = db.session.execute(query)
    return render_template('shopping.html', data=data, fid=fid)

@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    try:
        if request.method == 'POST':
            uid = current_user.id
            model = request.form['model']
            nickname = request.form['nickname']
            db.session.execute("INSERT INTO fridge(uid, model, nickname) VALUES ({},'{}','{}')".format(uid, model, nickname))
            db.session.commit()
        fridges = db.session.execute("SELECT * FROM fridge WHERE uid={}".format(current_user.id)).all()  

        total_spending_query = text("select round(sum(price), 2) from stores where fid in (select fid from fridge where uid={})".format(current_user.id))
        total_spending = db.session.execute(total_spending_query)

        spending_query = text("select stores.fid as fid, fridge.nickname as nick, round(sum(price), 2) as sum from stores join fridge on stores.fid=fridge.fid where uid={} group by stores.fid, fridge.nickname".format(current_user.id))
        spending = db.session.execute(spending_query)

        spending_cat_query = text("select category.name as cat, round(sum(price), 2) as sum from category left outer join stores on stores.catid=category.catid where fid in (select fid from fridge where uid={}) group by category.name".format(current_user.id))
        spending_cat = db.session.execute(spending_cat_query)

        not_spent_cat_query = text("select name from category where name not in (select category.name from category left outer join stores on stores.catid=category.catid where fid in (select fid from fridge where uid={}))".format(current_user.id))
        not_spent_cat = db.session.execute(not_spent_cat_query)
        
        return render_template('dashboard.html', username=current_user.name, fridges=fridges, total_spending=total_spending, 
                                spending=spending, spending_cat=spending_cat, not_spent=not_spent_cat)
    except Exception as e:
        print(e)
        return render_template('dashboard.html', error='Server encountered an error. Please try again later.')

@app.route("/add/<int:fid>", methods=['GET', 'POST'])
@login_required
@check_fridge_authorization
def add(fid):
    error = ''
    try:
        if request.method == 'POST':
            conid = request.form['content']
            amount = request.form['amount']
            unit = request.form['unit']
            price = request.form['price']
            store = request.form['store']
            expiry = request.form['expiry']

            catid = None
            if not conid.isnumeric():
                category = request.form['category']
                result = db.session.execute("INSERT INTO category(name) VALUES ('{}') RETURNING catid".format(category))
                catid = result.first()[0]
                result = db.session.execute("INSERT INTO content(name, catid) VALUES ('{}', {}) RETURNING conid".format(conid, catid))
                conid = result.first()[0]
            else:
                result = db.session.execute("SELECT catid from content where conid={}".format(conid))
                catid = result.first()[0]
            db.session.execute("INSERT INTO stores(fid, conid, catid, amount, unit, price, store, expiry) VALUES ({},{},{},{},'{}',{}, '{}', DATE('{}'));".format(fid, conid, catid, amount, unit, price, store, expiry))
            db.session.commit()
            return redirect("/fridge/{}".format(fid))
    except Exception as e:
        print(e)
        error = 'Server encountered an error. Please try again later.'

    contents = db.session.execute("SELECT content.name as content, content.conid, content.catid, category.name as category from content, category where category.catid=content.catid order by content.name;")
    return render_template('add.html', contents=contents, fid=fid, error=error)

@app.route("/edit", methods=['GET', 'POST'])
@login_required
def edit():
    error = ''
    fid = request.args.get('fid', default = None)
    conid = request.args.get('conid', default = None)
    catid = request.args.get('catid', default = None)
    
    if fid == None or catid == None or conid == None:
        return redirect("/dashboard")
    
    fridgeUser = db.session.execute("SELECT * from fridge where uid={} and fid={}".format(current_user.id, fid)).all()
    if len(fridgeUser) == 0:
        return redirect("/dashboard")
    
    if request.method == 'POST':
        try:
            amount = request.form['amount']

            query = text("UPDATE stores SET amount={} where fid={} and conid={} and catid={};".format(amount, fid, conid, catid))
            db.session.execute(query)
            db.session.commit()
            return redirect("/fridge/{}".format(fid))
        except Exception as e:
            print(e)
            db.session.rollback()
            error = 'Server encountered an error. Please try again later'

    query = text("SELECT content.name, stores.amount, stores.unit, stores.price, stores.store, category.name category from stores, content, category where stores.conid = content.conid and stores.catid = category.catid and stores.fid={} and stores.conid={} and stores.catid={};".format(fid, conid, catid))
    data = db.session.execute(query).first()
    return render_template('edit.html', item=data, fid=fid, conid=conid, catid=catid, error=error)

@app.route("/delete", methods=['GET'])
@login_required
def delete():
    fid = request.args.get('fid', None)
    conid = request.args.get('conid', None)
    catid = request.args.get('catid', None)
    if fid == None or catid == None or conid == None:
        return redirect("/dashboard")
    
    fridgeUser = db.session.execute("SELECT * from fridge where uid={} and fid={}".format(current_user.id, fid)).all()
    if len(fridgeUser) == 0:
        return redirect("/dashboard")

    try:
        query = text("DELETE from stores where fid={} and conid={} and catid={};".format(fid, conid, catid))
        db.session.execute(query)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    
    return redirect("/fridge/{}".format(fid))
