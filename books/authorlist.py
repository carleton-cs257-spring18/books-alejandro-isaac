from author import *
from csvreader import *
from bookauthorlinklist import *

class AuthorList:

    def __init__(self, authors_filename, books_authors_link_filename):
        authors_csv_as_list = get_csv_as_list(authors_filename)
        self.author_list = create_author_list(authors_csv_as_list)
        self.all_book_author_links = BookAuthorLinkList(books_authors_link_filename)

    def filter_authors_by_book_id(self, book_id, input_authors):
        filtered_authors = []
        target_authors_id = self.all_book_author_links.get_author_from_book(book_id)
        for author in input_authors:
            if author["id"] in target_authors_id:
                filtered_authors.append(author)
        return filtered_authors

    def filter_authors_by_search_text(self, search_text, input_authors):
        filtered_authors = []
        search_text = search_text.lower()
        for author in input_authors:
            if (search_text in author["last_name"].lower() or
                search_text in author["first_name"].lower()):
                filtered_authors.append(author)
        return filtered_authors
            
    def filter_authors_by_start_year(self,start_year,input_authors):
        filtered_authors = []
        for author in input_authors:
            if(author["birth_year"] >= start_year):
                filtered_authors.append(author)
        return filtered_authors
    
    def filter_authors_by_end_year(self,end_year,input_authors):
        #assumes that end year is never the current global year
        filtered_authors = []
        for author in input_authors:
            if( author["death_year"] is not None and 
                int(author["death_year"]) <= end_year ):
                filtered_authors.append(author)
        return filtered_authors

    def get_birth_year(author):
        return author["birth_year"]

        

    def get_author_from_id(self, id):
        author_list = []
        for author in self.author_list:
            if author.get_id() == id:
                target_author = author.get_author()
                author_list.append(author_list)
            # print(author.get_id())
        return self.author_list        

    def get_author_from_book_id(self, book_id, book_author_link_list, author_list=[]):
        books_authors_ids = book_author_link_list.get_author_from_book(book_id)
        author_list.append(self.get_author_from_id(id))
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

    def grab_last_name(author):
        return author.get_last_name()

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

