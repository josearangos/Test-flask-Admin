from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import unittest


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/josearangos/Documentos/Universidad/2018-2/Dev componentes/categoryManagment-ComponentAdmin/category.db'
app.config['SECRET_KEY'] = 'mysecret'


db = SQLAlchemy(app)

admin = Admin(app)


class category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(5000))
 

admin.add_view(ModelView(category, db.session))

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True)
