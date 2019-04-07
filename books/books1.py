'''
books1.py
Alejandro Gallardo & Isaac Reynaldo, April 7 2018

Phase one of the 'books' project. Handles command line input to print
a sorted list of authors or book titles.
'''

import sys
import csv

# handles action input: if user specifies authors, the program sorts by authors
# no input or other input assumes a sort by books
try:
    if sys.argv[2].lower() == 'authors':
        action = 'authors'
        item = 2
    else:
        action = 'books'
        item = 0
except:
    action = 'books'
    item = 0

# sorts normally unless specified 'reverse' by user
# also sorts reverse if 'reverse' specified in sys.argv[2]
try:
    if sys.argv[3].lower() == 'reverse':
        sortReverse = True
except IndexError:
    try:
        if sys.argv[2].lower() == 'reverse':
            sortReverse = True
        else:
            sortReverse = False
    except:
        sortReverse = False

# checks if there is a CSV file referenced in the command line
# returns the lines of the CSV file as elements in a list
def import_csv(action='books'):
    try:
        f_ls = []
        with open(sys.argv[1], newline='') as f:
            books_csv = csv.reader(f)
            for row in books_csv:
                f_ls.append(row)
    except:
        print('Usage: python3 books1.py input-file [action] [sort-direction]', file=sys.stderr)
        print('At the very least, please include .csv file!')
        sys.exit()

    return f_ls

# checks if the user specifies an action and sort order
# prints a list based on user input
def sort_list(csv_rows):

    target_list = []
    for line in csv_rows:
        if item == 2:
            author = line[item].split("(")[0]
            author_lastName = author.split(' ')[-2]
            if [author_lastName,author] not in target_list:
                target_list.append([author_lastName,author])
        elif line[item] not in target_list:
            target_list.append(line[item])

    return sorted(target_list, reverse = sortReverse)

def print_list(sorted_list):
    for thing in sorted_list:
        if action == 'books':
            print(thing)
        else:
            print(thing[1])

def main():
    file_list = import_csv()
    print_list(sort_list(file_list))

if __name__ == '__main__':
    main()
