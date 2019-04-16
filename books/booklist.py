import book
import csvreader

class BookList:

    # books_filename is a string passed from BooksDataSource constructor
    # books_filename should refer to a CSV file in the local folder
    # csv_line is a list
    def __init__(self, books_filename):
        books_csv_as_list = csvreader.get_csv_as_list(books_filename)
        self.book_list = []
        for csv_line in books_csv_as_list:
            new_book = book.Book(csv_line)
            self.book_list.append(new_book)

    def get_book_list(self):
        book_list = []
        for a_book in self.book_list:
            book_list.append(a_book.get_book())
        return book_list

    def get_book_from_id(self, id):
        for a_book in self.book_list:
            if a_book.get_id() == id:
                target_book = a_book.get_book()
        return target_book
