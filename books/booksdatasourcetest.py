'''
    booksdatasourcetest.py | books phase 2
    Alejandro Gallardo & Isaac Reynaldo, 11 April 2019
    unit test for booksdatasource.py
    implements unittest
'''

import booksdatasource
import unittest

class BooksDataSourceTest(unittest.TestCase):
'''
initializers
'''
    def setUp(self):
        self.books_data_source = booksdatasource.BooksDataSource(
            books.csv, authors.csv, books_authors.csv)
        pass

    def tearDown(self):
        pass

'''
BooksDataSource.book() tests
'''

    def test_return_correct_book(self):
        self.assertEqual(
            {'id':0, 'title':'All Clear', 'publication_year':2010},
            self.books_data_source.book(0))
        pass



    def test_invalid_book_id(self):
        self.assertRaises(ValueError, self.books_data_source.book, -3)
        pass

    def test_illegal_type_for_book(self):
        self.assertRaises(TypeError, self.books_data_source.book, 'hello')
        pass

'''
BooksDataSource.books() tests
'''

	def test_books_all_parameters_none(self):
	#assumes 47 is correct length of returned list
		self.assertEqual(47,len(self.books_data_source.books()))
        pass

	def test_books_search_by_author(self):
		books = self.books_data_source.books(author_id=10)
		for book in books:
			self.assertTrue(book.id == 10)
		pass

	def test_books_search_by_search_text(self):
		books = self.books_data_source.books(search_text='clear')
		for book in books:
			self.assertIn('clear',book.title)
		pass

	def test_books_search_by_start_year(self):
		books = self.books_data_source.books(start_year='1930')
		for book in books:
			self.assertTrue(book.title >= 1930)
		pass

	def test_books_search_by_end_year(self):
		books = self.books_data_source.books(end_year='1930')
		for book in books:
			self.assertTrue(book.title <= 1930)
		pass

	def test_books_sort_by_year(self):
		books = self.books_data_source.books(sort_by='year')
		book_year = 1813 #assumes first book in sorted list is from 1813 and that order is ascending
		for book in books:
			self.assertTrue(book.publication_year >= book_year)
			book_year = book.publication_year
		pass

	def test_books_sort_by_default(self):
		books = self.books_data_source.books(sort_by='title')
		book_titles_test = []
		for book in books:
			book_titles_test.append(book.title)
		book_titles_correct = book_titles_test.sort()
		self.assertEqual(book_titles_correct, book_titles_test)
		pass


	def test_books_when_author_input_is_negative(self):
	    self.assertRaises(ValueError, self.books_data_source.books,-3)
	   	pass


'''
BooksDataSource.author() tests
'''
	def test_correct_author(self):
        austen_correct = {'id':0, 'last_name':'Austen', 'first_name':'Jane', 'birth_year'=1775, 'death_year':1817}
        austen_test = self.books_data_source.author(0)
        self.assertEqual(austen_correct,austen_test)
        pass



    def test_invalid_author_id(self):
        self.assertRaises(ValueError, self.books_data_source.author, -3)
        pass

    def test_illegal_type_for_author(self):
        self.assertRaises(TypeError, self.books_data_source.author, 'hello')
        pass


'''
BooksDataSource.authors() tests
'''
    def test_authors_all_parameters_none(self):
        self.assertEqual(47, len(self.books_data_source.authors(sort_by=None)))
        pass

    def test_authors_search_by_book_id(self):
        haruki_murakami = self.books_data_source.authors(book_id=30)
        self.assertEqual(16, haruki_murakami[0]['id'])
        pass

    def test_authors_search_by_seach_text(self):
        bronte_sisters = self.books_data_source.authors(last_name='Brontë')
        for sister in bronte_sisters:
            self.assertEqual('Brontë', sister['last_name'])
        pass

    def test_authors_search_by_start_year(self):
        authors_after_1875 = self.books_data_source.authors(start_year=1875)
        for author in authors_after_1875:
            self.assertTrue(author['death_year'] >= 1875)

    def test_authors_search_by_end_year(self):
        authors_before_1875 = self.books_data_source.authors(end_year=1875)
        for author in authors_before_1875:
            self.assertTrue(author['death_year'] <= 1875)
        pass

    def test_authors_sort_by_birth_year(self):
        authors = self.books_data_source.authors()
        previous_author = authors[0]
        current_author = authors[0]
        for author in authors:
            current_author = author
            self.assertTrue(previous_author['birth_year']>=current_author['birth_year'])
            self.assertTrue(previous_author['last_name']<=current_author['last_name'])
            self.assertTrue(previous_author['first_name']<=current_author['first_name'])
            previous_author = author
        pass

    def test_authors_sort_by_last_name(self):
        authors = self.books_data_source.authors()
        previous_author = authors[0]
        current_author = authors[0]
        for author in authors:
            current_author = author
            self.assertTrue(previous_author['last_name']<=current_author['last_name'])
            self.assertTrue(previous_author['first_name']<=current_author['first_name'])
            self.assertTrue(previous_author['birth_year']>=current_author['birth_year'])
            previous_author = author
        pass

    def test_authors_invalid_book_id(self):
        self.assertRaises(ValueError, self.books_data_source.authors, book_id = -3)
        pass

if __name__ == '__main__':
    unittest.main()
