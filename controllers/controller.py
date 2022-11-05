from models.book import *
from models import library
from models.library import *
from app import app
from flask import render_template, request, redirect, Flaskwtf,
from models.book import *

@app.route ('/book_list')
def book_list():
    return render_template('book_list.html', book_list = library.book_list)

@app.route ('/book_list/<book_title>')
def single_book_page(book_title):
    for book in library.book_list:
        if book.unspace_title(book.title) == book_title:
            return render_template('single_book.html', book = book)

@app.route('/book_list', methods=["POST"])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    book_status = False
    if 'checked_in' in request.form['status']:
        book_status = True
    else:
        book_status = False
    new_book = Book(book_title, book_author, book_genre, book_status)
    library.add_new_book(new_book)
    return render_template('book_list.html', book_list = library.book_list)

@app.route('/status', methods=["POST"])
def update_status():
    
    if 'checked_in' in request.form['status']:
        book_status = True
    else:
        book_status = False
    return render_template('book_list.html', book_list = library.book_list)


@app.route('/book_list/delete/<title>', methods=["GET","POST"])
def delete(title):
    library.remove_book(title)
    return render_template('book_list.html', book_list = library.book_list)

