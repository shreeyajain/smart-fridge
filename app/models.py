from app import app, db
from flask_login import UserMixin, current_user
from sqlalchemy import Column
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import CheckConstraint, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.sql.sqltypes import VARCHAR, TIMESTAMP, Integer
import inspect
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

class MyAdminIndexView(AdminIndexView):
	def is_accessible(self):
		return current_user.is_authenticated

admin = Admin(app, name='Smart Fridge', template_mode='bootstrap3',
	index_view=MyAdminIndexView())

# A decorator to automagically assign init variables.
def instanceVariables(func):
    def returnFunc(*args, **kwargs):
        self_var = args[0]
        arg_spec = inspect.getargspec(func)
        argument_names = arg_spec[0][1:]
        defaults = arg_spec[3]
        if defaults is not None:
            default_argdict = dict(zip(reversed(argument_names), reversed(defaults)))
            self_var.__dict__.update(default_argdict)

        arg_dict = dict(zip(argument_names, args[1:]))
        self_var.__dict__.update(arg_dict)

        valid_keywords = set(kwargs)&set(argument_names)
        kwarg_dict = {k: kwargs[k] for k in valid_keywords}
        self_var.__dict__.update(kwarg_dict)

        func(*args, **kwargs)

    return returnFunc

class CRUD():
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

    def rollback(self):
        db.session.rollback()

class Base(db.Model, CRUD):
    __abstract__ = True

class Users(Base):
    __table_args__ = (
        CheckConstraint("email LIKE '%_@__%.__%'"),
        CheckConstraint('budget >= 0')
    )

    uid = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50), nullable=False)
    email = Column(VARCHAR(50), unique=True, nullable=False)
    address = Column(VARCHAR(100), default=None, nullable=False)
    countrycode = Column(Integer, default=1)
    phone = Column(VARCHAR(15), default=None, nullable=False, unique=True)
    budget = Column(Integer, default=0)
    
    @instanceVariables
    def __init__(self, name, email, address, countrycode, phone, budget):
        pass

    def __repr__(self):
        return "<User(username:%s)>"%self.name

class UserAdmin(ModelView):
    column_display_pk = True
    form_columns = ['uid', 'name', 'email', 'address', 'countrycode', 'phone', 'budget']

class Login(Base):
    __table_args__ = (
        CheckConstraint("password ~ '^.*(?=.{8,255})(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).*$'"),
        PrimaryKeyConstraint('uid', 'loginid', name='Login_PK'),
    )

    uid = Column(Integer, unique=True, nullable=False)
    loginid = Column(VARCHAR(50), unique=True, nullable=False)
    password = Column(VARCHAR(50), nullable= False)
    ForeignKeyConstraint(['uid'], ['users.uid'])

    @instanceVariables
    def __init__(self, uid, loginid, password):
        pass

    def __repr__(self):
        return "<Login(loginid:%s)>"%self.loginid

class LoginAdmin(ModelView):
    column_display_pk = True
    form_columns = ['uid', 'loginid', 'password']

class Fridge(Base):
    __table_args__ = (
        CheckConstraint("model ~ '^[a-zA-Z]{5}[0-9]{5}$'"),
    )

    fid = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(VARCHAR(10))
    since = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    nickname = Column(VARCHAR(25))
    uid = Column(Integer, nullable=False)
    ForeignKeyConstraint(['uid'], ['users.uid'])

    @instanceVariables
    def __init__(self, uid, model, nickname):
        pass

    def __repr__(self):
        return "<Fridge(fid:%s)>"%self.fid

class FridgeAdmin(ModelView):
    column_display_pk = True
    form_columns = ['fid', 'model', 'since', 'nickname', 'uid']

class FridgeUser(UserMixin):
    def __init__(self, id, name, password, email):
        self.id = id
        self.name = name
        self.password = password
        self.email = email

    @staticmethod
    def get(uid=None, loginid=None):
        login, user = None, None
        if loginid:
            login = Login.query.filter_by(loginid = loginid).first()
        
        if uid:
            login = Login.query.filter_by(uid=uid).first()

        if login:
            user = Users.query.filter_by(uid = login.uid).first()

        if user and login:
            return FridgeUser(user.uid, user.name, login.password, user.email)
        return None

class Category(Base):
    catid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50), nullable=False)

    def __repr__(self):
        return "<Category(name:%s)>"%self.name

class CategoryAdmin(ModelView):
    column_display_pk = False
    form_columns = ['catid', 'name']

class Content(Base):
    conid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50), nullable=False)
    catid = Column(Integer, nullable=False)
    ForeignKeyConstraint(['catid'], ['category.catid'])

    def __repr__(self):
        return "<Content(name:%s)>"%self.name

class ContentAdmin(ModelView):
    column_display_pk = True
    form_columns = ['conid', 'name', 'catid']

class Stores(Base):
    __table_args__ = (
        CheckConstraint('amount > 0'),
        CheckConstraint("unit in ('unit', 'kg', 'g', 'mg', 'l', 'ml', 'oz')"),
        CheckConstraint('price > 0'),
        PrimaryKeyConstraint('fid', 'conid', 'catid'),
    )

    fid = Column(Integer, nullable=False)
    conid = Column(Integer, nullable=False)
    catid = Column(Integer, nullable=False)
    amount = Column(Integer)
    unit = Column(VARCHAR(10))
    price = Column(Integer)
    store = Column(VARCHAR(50))
    expiry = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    ForeignKeyConstraint(['fid', 'conid', 'catid'], ['fridge.fid', 'content.conid', 'category.catid'])

    def __repr__(self):
        return "<Stores(fid:%s, conid: %s, catid: %s)>"%(self.fid, self.conid, self.catid)

class StoresAdmin(ModelView):
    column_display_pk = True
    form_columns = ['fid', 'conid', 'catid', 'amount', 'unit', 'price', 'store', 'expiry']

class CreateSList(Base):
    __table_args__ = (
        PrimaryKeyConstraint('fid', 'conid'),     
        UniqueConstraint('fid', 'conid', 'catid'),
    )

    fid = Column(Integer, nullable=False)
    conid = Column(Integer, nullable=False)
    catid = Column(Integer, nullable=False)
    date = Column(TIMESTAMP, server_default=db.func.current_timestamp())
    ForeignKeyConstraint(['fid', 'conid', 'catid'], ['fridge.fid', 'content.conid', 'category.catid'])

    def __repr__(self):
        return "<CreateSList(fid:%s, conid: %s, catid: %s)>"%(self.fid, self.conid, self.catid)

class CreateSListAdmin(ModelView):
    column_display_pk = True
    form_columns = ['fid', 'conid', 'catid', 'date']

class Settings(Base):
    __table_args__ = (
        PrimaryKeyConstraint('locid', 'fid'),
    )

    locid = Column(Integer)
    fid = Column(Integer, nullable=False)
    name = Column(VARCHAR(20))
    temp = Column(Integer, default=4)
    ForeignKeyConstraint(['fid'], ['fridge.fid'])

    @instanceVariables
    def __init__(self, fid, locid, name):
        pass

class SettingsAdmin(ModelView):
    column_display_pk = True
    form_columns = ['locid', 'fid', 'name', 'temp']

class Log(Base):
    lid = Column(Integer, primary_key=True, autoincrement=True)
    fid = Column(Integer, nullable=False)
    time = Column(TIMESTAMP, default=db.func.current_timestamp())
    message = Column(VARCHAR)
    ForeignKeyConstraint(['fid'], ['fridge.fid'])        

class LogAdmin(ModelView):
    column_display_pk = True
    form_columns = ['lid', 'fid', 'time', 'message']

admin.add_view(UserAdmin(Users, db.session))
admin.add_view(LoginAdmin(Login, db.session))
admin.add_view(FridgeAdmin(Fridge, db.session))
admin.add_view(CategoryAdmin(Category, db.session))
admin.add_view(ContentAdmin(Content, db.session))
admin.add_view(StoresAdmin(Stores, db.session))
admin.add_view(CreateSListAdmin(CreateSList, db.session))
admin.add_view(SettingsAdmin(Settings, db.session))
admin.add_view(LogAdmin(Log, db.session))
