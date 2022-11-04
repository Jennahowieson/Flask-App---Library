from models.book import *
from models import library
from models.library import book_list
from app import app
from flask import render_template, request

@app.route ('/book_list')
def book_list():
    return render_template('book_list.html', book_list = library.book_list)