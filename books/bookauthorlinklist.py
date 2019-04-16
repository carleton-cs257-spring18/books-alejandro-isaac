import bookauthorlink
import csvreader

class BookAuthorLinkList:

    def __init__(self, book_author_link_filename):
        self.book_author_link_list = []
        '''
        reads the 'book_author.csv' file
        for each line in the file it creates a book_authors_link object
        '''

    def add_book_authors_link(self, book_authors_link_info):
        self.book_author_link_list.append(book_authors_link_info)

    def get_book_authors_link_list(self):
        return book_author_link_list
