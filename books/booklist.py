from book import *
from csvreader import *
from bookauthorlinklist import *

class BookList:

    def __init__(self, books_filename):
        books_csv_as_list = get_csv_as_list(books_filename)
        self.book_list = []
        for csv_line in books_csv_as_list:
            new_book = Book(csv_line)
            self.book_list.append(new_book)

    def get_book_from_id(self, id):
        for indexed_book in self.book_list:
            if indexed_book.get_id() == id:
                target_book = indexed_book.get_book()
        try:
            return target_book
        except:
            raise Exception(ValueError)

    def get_book_from_author_id(self, author_id, book_author_link_list, book_list=[]):
        authors_books_ids = book_author_link_list.get_book_from_author(author_id)
        for id in authors_books_ids:
            if self.get_book_from_id(id) not in book_list:
                book_list.append(self.get_book_from_id(id))
        return book_list

    def get_book_from_search_text(self, search_text, book_list=[]):
        search_text = search_text.lower()
        for indexed_book in self.book_list:
            if ((search_text in indexed_book.get_title().lower())
                and indexed_book.get_book() not in book_list):
                book_list.append(indexed_book.get_book())
        return book_list

    def get_book_from_start_year(self, start_year, book_list=[]):
        for indexed_book in self.book_list:
            if ((indexed_book.get_publication_year() >= start_year)
                and indexed_book.get_book() not in book_list):
                book_list.append(indexed_book.get_book())
        return book_list

    def get_book_from_end_year(self, end_year, book_list=[]):
        for indexed_book in self.book_list:
            if ((indexed_book.get_publication_year() <= start_year)
                and indexed_book.get_book() not in book_list):
                book_list.append(indexed_book.get_book())
        return book_list

    def sort_book_list(self, sort_by='title', book_list=[]):
        if not book_list:
            return []
        if sort_by == 'title':
            book_list = sorted(book_list, key=lambda
                k: (k['title'], -k['publication_year']))
        if sort_by == 'publication_year':
            book_list = sorted(book_list, key=lambda
                k: (-k['publication_year'], k['title']))
        return book_list
