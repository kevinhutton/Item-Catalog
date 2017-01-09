from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
from flask import make_response
import requests
import json

app = Flask(__name__)


# Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

# Show all categories and all items
@app.route('/')
@app.route('/catalog')
def catalog():
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(CategoryItem).order_by(asc(CategoryItem.name))
    return render_template('catalog.html',categories=categories,items=items)

@app.route('/catalog/JSON')
def catalogJSON():
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(CategoryItem).order_by(asc(CategoryItem.name))
    return jsonify(categories=[category.serialize for category in categories] , items = [item.serialize for item in items])

@app.route('/catalog/category/<int:category_id>')
def category(category_id):
    categories = session.query(Category).filter_by(id=category_id).order_by(asc(Category.name))
    items = session.query(CategoryItem).filter_by(category_id=category_id).order_by(asc(CategoryItem.name))
    return render_template('catalog.html',categories=categories,items=items)

@app.route('/catalog/category/<int:category_id>/JSON')
def categoryJSON(category_id):
    categories = session.query(Category).filter_by(id=category_id).order_by(asc(Category.name))
    items = session.query(CategoryItem).filter_by(category_id=category_id).order_by(asc(CategoryItem.name))
    return jsonify(categories=[category.serialize for category in categories] , items = [item.serialize for item in items])

@app.route('/catalog/newitem',methods=['GET', 'POST'])
def newItem():
    if request.method == 'POST':
        print "Post !"
        print request.form
        corresponding_category = session.query(Category).filter_by(name=request.form['category_select']).one()
        newItem = CategoryItem(name=request.form['name'], description=request.form['description'],
                     category=corresponding_category)
        session.add(newItem)
        session.commit()

        return redirect(url_for('catalog'))
    else:
        categories = session.query(Category).order_by(asc(Category.name))
        return render_template('newItem.html',categories=categories)

@app.route('/catalog/edititem/<int:item_id>', methods=['GET', 'POST'])
def editItem(item_id):
    if request.method == 'POST':
        print "Post !"
        print request.form
        item = session.query(CategoryItem).filter_by(id=item_id).one()
        item.name = request.form['name']
        item.description = request.form['description']
        item.category = session.query(Category).filter_by(name=request.form['category_select']).one()
        session.add(item)
        session.commit()
        return redirect(url_for('catalog'))
    else:
        currentItem = session.query(CategoryItem).filter_by(id=item_id).one()
        categories = session.query(Category).order_by(asc(Category.name))
        return render_template('editItem.html',categories=categories,item=currentItem)

@app.route('/catalog/deleteitem/<int:item_id>', methods=['GET'])
def deleteItem(item_id):
    item = session.query(CategoryItem).filter_by(id=item_id).one()
    session.delete(item)
    session.commit()
    return redirect(url_for('catalog'))

@app.route('/catalog/showitem/<int:item_id>', methods=['GET'])
def showItem(item_id):
        currentItem = session.query(CategoryItem).filter_by(id=item_id).one()
        return render_template('showItem.html',item=currentItem)

@app.route('/catalog/showitem/<int:item_id>/JSON', methods=['GET'])
def showItemJSON(item_id):
        currentItem = session.query(CategoryItem).filter_by(id=item_id).one()
        return jsonify(item=currentItem.serialize)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
