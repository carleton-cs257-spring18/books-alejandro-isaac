import author
import csvreader

class AuthorList:

    def __init__(self, authors_filename):
        self.author_list = []
        '''
        reads the 'authors.csv' file
        for each line in the file it creates a author object
        '''

    def add_author(self, author_info):
        self.author_list.append(author_info)

    def get_author_list(self):
        return author_list
