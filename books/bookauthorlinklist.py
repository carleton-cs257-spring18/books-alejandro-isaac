from csvreader import *

class BookAuthorLinkList:

    def __init__(self, book_author_link_filename):
        book_author_link_csv_as_list = get_csv_as_list(book_author_link_filename)
        self.book_to_author_link = {}
        self.author_to_book_link = {}
        for link in book_author_link_csv_as_list:
            book_id = int(link[0])
            author_id = int(link[1])
            if book_id not in self.book_to_author_link:
                self.book_to_author_link[book_id] = [author_id]
            elif author_id not in self.book_to_author_link[book_id]:
                self.book_to_author_link[book_id].append(author_id)

            if author_id not in self.author_to_book_link:
                self.author_to_book_link[author_id] = [book_id]
            elif book_id not in self.author_to_book_link[author_id]:
                self.author_to_book_link[author_id].append(book_id)
        #for csv_line in book_author_link_csv_as_list:


    def get_author_from_book(self, book_id):
        author_ids = self.book_to_author_link[book_id]
        return author_ids

    def get_book_from_author(self, author_id):
        book_ids = self.author_to_book_link[author_id]
        return book_ids
