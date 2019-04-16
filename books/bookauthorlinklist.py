import bookauthorlink
import csvreader

class BookAuthorLinkList:

    def __init__(self, book_author_link_filename):
        book_author_link_csv_as_list = open_books_csv(book_author_link_filename)
        self.book_author_link_list = []
        for csv_line in book_author_link_csv_as_list:
            add_

    def add_book_authors_link(self, book_authors_link_info):
        self.book_author_link_list.append(book_authors_link_info)

    def get_book_authors_link_list(self):
        return book_author_link_list
