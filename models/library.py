from models.book import *
from models.library import *

book1 = Book("Becoming","Michelle Obama","Autobiography",True)
book2 = Book("I am Malala","Malala Yousafzai","Autobiography",False)
book3 = Book("Bossypants","Tina Fey", "Autobiography",True)
book4 = Book("The Handmaids Tale", "Margaret Atwood", "Fiction",True)
book5 = Book("Milk and Honey", "Rupi Kaur", "Poetry",False)
book6 = Book("Girl, Woman, Other", "Bernardine Evaristo", "Fiction",False)
book7 = Book("Good Night Stories For Rebel Girls", "Francesca Cavallo", "Childrens",True)
book8 = Book("She Persisted", "Chelsea Clinton", "Childrens",True)

book_list = [book1, book2, book3, book4, book5, book6, book7, book8]

def return_book_by_title(book_title):
    for book in book_list:
        if book.title == book_title:
            return book

def add_new_book(new_book):
    book_list.append(new_book)

def del_new_book(del_book):
    book_list.remove(del_book)

def remove_book(old_book):
    for book in book_list:
        if book.title == old_book:
            book_list.remove(book)

