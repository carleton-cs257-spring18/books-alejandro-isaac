import book
import csvreader

class BookList:

    # books_filename is a string passed from BooksDataSource constructor
    # books_filename should refer to a CSV file in the local folder
    # csv_line is a list
    def __init__(self, books_filename):
        books_csv_as_list = open_books_csv(books_filename)
        self.book_list = []
        for csv_line in books_csv_as_list:
            add_book(csv_line)

    # opens the CSV file and returns it as a list
    # row in list corresponds to a row in the CSV file
    def open_books_csv(books_filename):
        return csvreader.get_csv_as_list(books_filename)

    # book_info is a list [id, title, publication_year]
    def add_book(self, book_info):
        new_book = book.Book(book_info)
        book_list.append(new_book)

    def get_book_list(self):
        return book_list
