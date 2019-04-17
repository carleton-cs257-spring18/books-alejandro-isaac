import csv

def get_csv_as_list(file):
    csv_as_list = []

    with open(file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            csv_as_list.append(row)
    return csv_as_list

def csv_line_to_author(csv_line):
    new_author = {
            'id':int(csv_line[0]), 'last_name':csv_line[1],
            'first_name':csv_line[2], 'birth_year':int(csv_line[3]),
            'death_year': None
        }
        
    try:
    	if type(int(csv_line[4])) is int:
        	    new_author['death_year'] = csv_line[4]
    except ValueError as e:
    	pass
    
    return new_author

def create_author_list(authors_csv_as_list):
	author_list = []
	for csv_line in authors_csv_as_list:
		new_author = csv_line_to_author(csv_line)
		author_list.append(new_author)
	return author_list
