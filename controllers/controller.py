from app import app
from flask import render_template
# from models.book import Book
from models.books_list_test_data import book_list

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/full_book_list')
def index():
    return render_template('index.html', book_list=book_list)

@app.route('/view_book/<index>')
def show(index):
    return render_template('index.html', book=book_list[int(index)])