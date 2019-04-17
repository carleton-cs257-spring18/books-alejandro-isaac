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
        self.all_authors = AuthorList(authors_filename)
        self.all_book_author_links = BookAuthorLinkList(books_authors_link_filename)
        pass

    def book(self, book_id):
        # if book_id isn't an integer, raise TypeError
        if type(book_id) != int:
            raise TypeError

        book = self.all_books.get_book_from_id(book_id)

        # if book_id doesn't return a book, raise ValueError
        if book == {}:
            raise ValueError

        return book

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        # create master book_list of all books
        book_list = []
        book_obj_list = self.all_books.book_list
        for book_obj in book_obj_list:
            book_list.append(book_obj.get_book())

        # filter_list is a list of books to filter from master book_list
        filter_list = []

        # if search parameter is specified, gets those books
        # filters other books from master list
        if author_id != None:
            filter_list = self.all_books.get_book_from_author_id(author_id, self.all_book_author_links)
            book_list = self.all_books.filter_book_list(book_list, filter_list)
        if search_text != None:
            filter_list = self.all_books.get_book_from_search_text(search_text)
            book_list = self.all_books.filter_book_list(book_list, filter_list)
        if start_year != None:
            filter_list = self.all_books.get_book_from_start_year(start_year)
            book_list = self.all_books.filter_book_list(book_list, filter_list)
        if end_year != None:
            filter_list = self.all_books.get_book_from_end_year(end_year)
            book_list = self.all_books.filter_book_list(book_list, filter_list)

        # sorts book_list by sort_by
        book_list = self.all_books.sort_book_list(sort_by, book_list=book_list)

        return book_list

    def author(self, author_id):
        # if author_id not an integer, raise TypeError
        if type(author_id) != int:
            raise TypeError

        author = self.all_authors.get_author_from_id(author_id)

        # if author_id didn't return an author, raise ValueError
        if author == {}:
            raise ValueError

        return author

    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):
        # creates a master author_list of all authors
        author_list = []
        author_obj_list = self.all_authors.author_list
        for author_obj in author_obj_list:
            author_list.append(author_obj.get_author())

        # filter_list is a list of authors to filter from master list
        filter_list = []

        # if search parameter is specified, gets those authors
        # filters other authors from master list
        if book_id != None:
            filter_list = self.all_authors.get_author_from_book_id(book_id, self.all_book_author_links)
            author_list = self.all_authors.filter_author_list(author_list, filter_list)
        if search_text != None:
            filter_list = self.all_authors.get_author_from_search_text(search_text)
            author_list = self.all_authors.filter_author_list(author_list, filter_list)
        if start_year != None:
            filter_list = self.all_authors.get_author_from_start_year(start_year)
            author_list = self.all_authors.filter_author_list(author_list, filter_list)
        if end_year != None:
            filter_list = self.all_authors.get_author_from_end_year(end_year)
            author_list = self.all_authors.filter_author_list(author_list, filter_list)

        # sorts author_list by sort_by
        author_list = self.all_authors.sort_author_list(sort_by, author_list=author_list)

        return author_list
