#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018
    Modified by Eric Alexander, April 2019

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class.
'''

import bookslist
import authorlist
import bookauthorlinklist

class BooksDataSource:
    '''
    A BooksDataSource object provides access to data about books and authors.
    The particular form in which the books and authors are stored will
    depend on the context (i.e. on the particular assignment you're
    working on at the time).

    Most of this class's methods return Python lists, dictionaries, or
    strings representing books, authors, and related information.

    An author is represented as a dictionary with the keys
    'id', 'last_name', 'first_name', 'birth_year', and 'death_year'.
    For example, Jane Austen would be represented like this
    (assuming her database-internal ID number is 72):

        {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}

    For a living author, the death_year is represented in the author's
    Python dictionary  as None.

        {'id': 77, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': None}

    Note that this is a simple-minded representation of a person in
    several ways. For example, how do you represent the birth year
    of Sophocles? What is the last name of Gabriel García Márquez?
    Should we refer to the author of "Tom Sawyer" as Samuel Clemens or
    Mark Twain? Are Voltaire and Molière first names or last names? etc.

    A book is represented as a dictionary with the keys 'id', 'title',
    and 'publication_year'. For example, "Pride and Prejudice"
    (assuming an ID of 132) would look like this:

        {'id': 193, 'title': 'A Wild Sheep Chase', 'publication_year': 1982}

    '''

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        self.all_books = booklist.BookList(books_filename)
        self.all_authors = authorlist.AuthorList(authors_filename)
        self.all_book_author_links = bookauthorlinklist.BookAuthorLinkList(books_authors_link_filename)
        pass

    def book(self, book_id):
        ''' Returns the book with the specified ID. (See the BooksDataSource comment
            for a description of how a book is represented.)

            Raises ValueError if book_id is not a valid book ID.
        '''
        return {}

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        ''' Returns a list of all the books in this data source matching all of
            the specified non-None criteria.

                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year

            Note that parameters with value None do not affect the list of books returned.
            Thus, for example, calling books() with no parameters will return JSON for
            a list of all the books in the data source.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year

            See the BooksDataSource comment for a description of how a book is represented.

            QUESTION: Should Python interfaces specify TypeError?
            Raises TypeError if author_id, start_year, or end_year is non-None but not an integer.
            Raises TypeError if search_text or sort_by is non-None, but not a string.
				OUR ANSWER: Not for this assignment.

            QUESTION: How about ValueError? And if so, for which parameters?
            Raises ValueError if author_id is non-None but is not a valid author ID.
				OUR ANSWER: Yes, but just for author_id.

             

The following conceptual framework can be applied to all methods
 --------------------------------------------
                all possible situations

                arguments == [0, 0, 0 ,0]
                arguments == [0, 0, 0 ,1]
                arguments == [0, 0, 1 ,0]
                arguments == [0, 0, 1 ,1]

                arguments == [0, 1, 0 ,0]
                arguments == [0, 1, 0 ,1]
                arguments == [0, 1, 1 ,0]
                arguments == [0, 1, 1 ,1]

                arguments == [1, 0, 0 ,0]
                arguments == [1, 0, 0 ,1]
                arguments == [1, 0, 1 ,0]
                arguments == [1, 0, 1 ,1]

                arguments == [1, 1, 0 ,0]
                arguments == [1, 1, 0 ,1]
                arguments == [1, 1, 1 ,0]
                arguments == [1, 1, 1 ,1]
                
--------------------------------------------
main books() method: dealing with all possible situations
--------------------------------------------                
#[author_id, search_text, start_year, end_year] 
#with corresponding indices [0,1,2,3]

                provided_arguments = [author_id, search_text, start_year, end_year]

                index_corresponding_to_argument = 0
                for item in provided_arguments:
                    if item == 1:
                        filtered_books = all_books.filterBooks(index_corresponding_to_argument):
                    index_corresponding_to_argument++


--------------------------------------------
1 filterBooks method: highest level of abstraction
--------------------------------------------    
filter books will exist
inside the class books_list


                filterBooks(self, index_input):

                """
                filters book by author, search text, start year, end year, respectively corresponding with 
                an index inputs of 0, 1, 2, 3

                """
                    if index_input = 0:
                        filtered_books = book_list.filter_by_author_id() 
                        ##since we are already inside the book_list class, book_list within the class might
                        ## just be a list. In that case, we could do filter_by_author_id(book_list)

                    if index_input = 1:
                        filtered_books = book_list.filter_by_search_text()

                    if index_input = 2:
                        filtered_books = book_list.filter_by_start_year()
                    
                    if index_input = 3:
                        filtered_books = book_list.filter_by_end_year()

                    return filtered_books


--------------------------------------------
4 filter methods: lower level of abstraction
--------------------------------------------  

                filter_by_author_id():
                    for book in books_list

                filter_by_search_text():

                filter_by_start_year():

                filter_by_end_year():



                

        '''
        return []

    def author(self, author_id):
        ''' Returns the author with the specified ID. (See the BooksDataSource comment for a
            description of how an author is represented.)

            Raises ValueError if author_id is not a valid author ID.
        '''
        return {}

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
        return []
