import book
import csvreader

class BookList:

    def __init__(self, books_filename):
        self.books_csv_as_list = open_books_csv(books_filename)
        self.book_list = []



    def open_books_csv(books_filename):
        books_csv_as_list = csvreader.get_csv_as_list(books_filename)
        return books_csv_as_list

    def add_book(self, book_info):
        self.book_list.append(book_info)

    def get_book_list(self):
        return book_list
