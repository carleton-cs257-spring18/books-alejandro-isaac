
import booksdatasource
import unittest

class BooksDataSourceTest(unittest.TestCase):

    def setUp(self):
        self.books_data_source = booksdatasource.BooksDataSource('books.csv', 'authors.csv', 'books_authors.csv')
        pass

    def tearDown(self):
        pass

    def test_return_correct_book(self):
        self.assertEqual({'id':0, 'title':'All Clear', 'publication_year':2010},self.books_data_source.book(0))
        pass

    def test_invalid_book_id(self):
        self.assertRaises(ValueError, self.books_data_source.book, -3)
        pass

    def test_illegal_type_for_book(self):
        self.assertRaises(TypeError, self.books_data_source.book, 'hello')
        pass

    def test_books_all_parameters_none(self):
        self.assertEqual(47,len(self.books_data_source.books()))
        pass

    def test_books_search_by_author(self):
        book = self.books_data_source.books(author_id=10)
        self.assertEqual({'id':10,'title':'Main Street','publication_year':1920}, book[0])
        pass

    def test_books_invalid_author_id(self):
        self.assertRaises(ValueError, self.books_data_source.books, author_id = -3)
        pass

    def test_books_search_by_search_text(self):
        books = self.books_data_source.books(search_text='clear')
        for book in books:
            self.assertIn('clear',book['title'].lower())
        pass

    def test_books_search_by_end_year(self):
        books = self.books_data_source.books(end_year=1930)
        for book in books:
            self.assertTrue(book['publication_year'] <= 1930)
        pass

    def test_correct_author(self):
        austen_correct = {'id':4, 'last_name':'Austen', 'first_name':'Jane', 'birth_year':1775, 'death_year':1817}
        self.assertEqual(austen_correct, self.books_data_source.author(author_id=4))

    def test_invalid_author_id(self):
        self.assertRaises(ValueError, self.books_data_source.author, -3)
        pass

    def test_illegal_type_for_author(self):
        self.assertRaises(TypeError, self.books_data_source.author, 'hello')
        pass

    def test_authors_all_parameters_none(self):
        self.assertEqual(25, len(self.books_data_source.authors()))
        pass

    def test_authors_search_by_book_id(self):
        haruki_murakami = self.books_data_source.authors(book_id=30)
        self.assertEqual(16, haruki_murakami[0]['id'])
        pass

    def test_authors_search_by_seach_text(self):
        bronte_sisters = self.books_data_source.authors(search_text='Brontë')
        for sister in bronte_sisters:
            self.assertEqual('Brontë', sister['last_name'])
        pass

    def test_authors_search_by_start_year(self):
        authors_after_1875 = self.books_data_source.authors(start_year=1875)
        for author in authors_after_1875:
            try:
                self.assertTrue(author['death_year'] >= 1875)
            except TypeError:
                self.assertTrue(author['death_year'] == None)

    def test_authors_search_by_end_year(self):
        authors_before_1875 = self.books_data_source.authors(end_year=1875)
        for author in authors_before_1875:
            self.assertTrue(author['birth_year'] <= 1875)
        pass

    def test_authors_sort_by_last_name(self):
        authors_sorted_by_last_name = self.books_data_source.authors(sort_by="last_name")
        previous_author = authors_sorted_by_last_name[0]
        for author in authors_sorted_by_last_name:
            self.assertTrue(author['last_name'] >= previous_author['last_name'])
            previous_author = author
        pass

    def test_authors_sort_by_birth_year(self):
        authors_sorted_by_birth_year = self.books_data_source.authors(sort_by="birth_year")
        previous_author = authors_sorted_by_birth_year[0]
        for author in authors_sorted_by_birth_year:
            self.assertTrue(author['birth_year'] <= previous_author['birth_year'])
            previous_author = author
        pass

    def test_authors_invalid_book_id(self):
        self.assertRaises(ValueError, self.books_data_source.authors, book_id = -3)
        pass

    

if __name__ == '__main__':
    unittest.main()
