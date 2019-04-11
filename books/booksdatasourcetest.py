'''
    booksdatasourcetest.py
    Alejandro Gallardo & Isaac Reynaldo, 11 April 2019
'''

import booksdatasource
import unittest

class BooksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.books_data_source = booksdatasource.BooksDataSource(books.csv, authors.csv, books_authors.csv)
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
