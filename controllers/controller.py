from models.book import *
from models import library
from models.library import book_list
from app import app
from flask import render_template, request

@app.route ('/book_list')
def book_list():
    return render_template('book_list.html', book_list = library.book_list)

@app.route ('/book_list/<book_title>')
def single_book_page(book_title):
    for book in library.book_list:
        if book_title in library.book_list:
            return render_template('single_book.html', book = book_list.index(book.title))

# @app.route ('/book_list/<book_num>')
# def single_book_page(book_num):
#     return render_template('single_book.html', book=library.book_list[int(book_num)])

# book_title_index = book_list.index(book.title)
