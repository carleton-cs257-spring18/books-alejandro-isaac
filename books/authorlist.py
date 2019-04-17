from author import *
from csvreader import *
from bookauthorlinklist import *

class AuthorList:

    def __init__(self, authors_filename):
        authors_csv_as_list = get_csv_as_list(authors_filename)
        self.author_list = []
        for csv_line in authors_csv_as_list:
            new_author = Author(csv_line)
            self.author_list.append(new_author)

    def get_author_from_id(self, id):
        for indexed_author in self.author_list:
            if indexed_author.get_id() == id:
                target_author = indexed_author.get_author()
        try:
            return target_author
        except:
            raise Exception(ValueError)

    def get_author_from_book_id(self, book_id, book_author_link_list, author_list=[]):
        books_authors_ids = book_author_link_list.get_author_from_book(book_id)
        for id in books_authors_ids:
            if self.author_list.get_author_from_id(id) not in author_list:
                author_list.append(author_list.get_author_from_id(id))
        return author_list

    def get_author_from_search_text(self, search_text, author_list=[]):
        search_text = search_text.lower()
        for indexed_author in self.author_list:
            if ((search_text in indexed_author.get_first_name().lower()
                or search_text in indexed_author.get_last_name().lower())
                and indexed_author.get_author() not in author_list):
                author_list.append(indexed_author.get_author())
        return author_list

    def get_author_from_start_year(self, start_year, author_list=[]):
        for indexed_author in self.author_list:
            if ((indexed_author.get_birth_year() >= start_year)
                and indexed_author.get_author() not in author_list):
                author_list.append(indexed_author.get_author())
        return author_list

    def get_author_from_end_year(self, end_year, author_list=[]):
        for indexed_author in self.author_list:
            if ((indexed_author.get_birth_year() <= end_year)
                and indexed_author.get_author() not in author_list):
                author_list.append(indexed_author.get_author())
        return author_list

    def sort_author_list(self, sort_by='last_name', author_list=[]):
        if not author_list:
            return []
        if sort_by == 'birth_year':
            author_list = sorted(author_list, key=lambda
                k: (-k['birth_year'], k['last_name'], k['first_name']))
        if sort_by == 'last_name':
            author_list = sorted(author_list, key=lambda
                k: (k['last_name'], k['first_name'], -k['birth_year']))
        return author_list
