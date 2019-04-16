import author
import csvreader

class AuthorList:

    def __init__(self, authors_filename):
        authors_csv_as_list = open_authors_csv(authors_filename)
        self.author_list = []
        for csv_line in authors_csv_as_list:
            add_author(csv_line)

    def open_authors_csv(authors_filename):
        return csvreader.get_csv_as_list(authors_filename)

    def add_author(self, author_info):
        new_author = author.Author(author_info)
        author_list.append(new_author)

    def get_author_list(self):
        return author_list
