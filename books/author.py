class Author:

    # author_details is a list
    # [int (id), string (last_name), string (first_name), int (birth_year), int (death_year)]
    def __init__(self, author_info):
        self.author = {
            'id':int(author_info[0]), 'last_name':author_info[1],
            'first_name':author_info[2], 'birth_year':int(author_info[3]),
            'death_year':int(author_info[4])
        }

    def get_author(self):
        return self.author

    def get_id(self):
        return self.author['id']

    def get_last_name(self):
        return self.author['last_name']

    def get_first_name(self):
        return self.author['first_name']

    def get_birth_year(self):
        return self.author['birth_year']

    def get_death_year(self):
        return self.author['death_year']
