#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018
    Modified by Eric Alexander, April 2019

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class.
'''

from booklist import BookList
from authorlist import AuthorList
from bookauthorlinklist import *
from book import *
from author import *

class BooksDataSource:
    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        self.all_books = BookList(books_filename)
        self.all_authors = AuthorList(authors_filename,books_authors_link_filename)
        self.all_book_author_links = BookAuthorLinkList(books_authors_link_filename)
        pass

    def test_function(self):
        print(self.all_authors.author_list2)

    def book(self, book_id):
        book = self.all_books.get_book_from_id(book_id)
        return book

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        book_list = []

        if author_id != None:
            book_list = self.all_books.get_book_from_author_id(author_id, self.all_book_author_links, book_list)
        if search_text != None:
            book_list = self.all_books.get_book_from_search_text(search_text, book_list)
        if start_year != None:
            book_list = self.all_books.get_book_from_start_year(start_year, book_list)
        if end_year != None:
            book_list = self.all_books.get_book_from_end_year(end_year, book_list)

        book_obj_list = self.all_books.book_list
        if (author_id and search_text and start_year and end_year) == None:
            for book_obj in book_obj_list:
                book_list.append(book_obj.get_book())

        book_list = self.all_books.sort_book_list(sort_by, book_list)

        return book_list

    def author(self, author_id):
        author = self.all_authors.get_author_from_id(author_id)
        return author

    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):
        ''' Returns a list of all the authors in this data source matching all of the
            specified non-None criteria.

                book_id - only returns authors of the specified book
                search_text - only returns authors whose first or last names contain
                    (case-insensitively) the search text
                start_year - only returns authors who were alive during or after
                    the specified year
                end_year - only returns authors who were alive during or before
                    the specified year

            Note that parameters with value None do not affect the list of authors returned.
            Thus, for example, calling authors() with no parameters will return JSON for
            a list of all the authors in the data source.

            The list of authors is sorted in an order depending on the sort_by parameter:

                'birth_year' - sorts by birth_year, breaking ties with (case-insenstive) last_name,
                    then (case-insensitive) first_name
                any other value - sorts by (case-insensitive) last_name, breaking ties with
                    (case-insensitive) first_name, then birth_year

            See the BooksDataSource comment for a description of how an author is represented.
        '''
        author_list = self.all_authors.author_list

        if book_id != None:
            author_list = self.all_authors.filter_authors_by_book_id(book_id, author_list)
        if search_text != None:
            author_list = self.all_authors.filter_authors_by_search_text(search_text, author_list)
        if start_year != None:
            author_list = self.all_authors.filter_authors_by_start_year(start_year, author_list)
        if end_year != None:
            author_list = self.all_authors.filter_authors_by_end_year(end_year, author_list)

        # author_list = self.all_authors.sort_authors(author_list, sort_by)
        #didn't finish sort method
        return author_list

        # return []
