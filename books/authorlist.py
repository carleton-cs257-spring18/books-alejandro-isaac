import author
import csvreader

class AuthorList:

    def __init__(self, authors_filename):
        authors_csv_as_list = csvreader.get_csv_as_list(authors_filename)
        self.author_list = []
        for csv_line in authors_csv_as_list:
            new_author = author.Author(csv_line)
            self.author_list.append(new_author)

    def get_author_list(self):
        author_list = []
        for an_author in self.author_list:
            author_list.append(an_author.get_author())
        return author_list

    def get_author_from_id(self, id):
        for an_author in self.author_list:
            if a_author.get_id() == id:
                target_author = a_author.get_author()
        return target_author
