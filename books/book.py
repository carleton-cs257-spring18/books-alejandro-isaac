class Book:

    # book_details is a list
    # [int (id), string (title), int (publication_year)]
    def __init__(self, book_info):
        self.book = {
            'id':int(book_info[0]), 'title':book_info[1],
            'publication_year':int(book_info[2])
        }

    def get_book(self):
        return self.book

    def get_id(self):
        return self.book['id']

    def get_title(self):
        return self.book['title']

    def get_publication_year(self):
        return self.book['publication_year']
