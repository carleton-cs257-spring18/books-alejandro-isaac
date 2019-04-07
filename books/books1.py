'''
books1.py
Alejandro Gallardo & Isaac Reynaldo, April 7 2018

Phase one of the 'books' project. Handles command line input to print
a sorted list of authors or book titles.
'''

import sys
import csv

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
        print('No CSV file.')
        sys.exit()

    return f_ls

# checks if the user specifies an action and sort order
# prints a list based on user input
def sortnprint(ls):
    try:
        item = 0
        if sys.argv[2].lower() == 'authors':
            item = 2
    except:
        item = 0

    target_list = []
    for line in ls:
        if line[item] not in target_list:
            target_list.append(line[item])

    try:
        if sys.argv[3].lower() == 'reverse':
            sortReverse = True
    except IndexError:
        if sys.argv[2].lower() == 'reverse':
            sortReverse = True
        else:
            sortReverse = False
    except:
        sortReverse = True

    target_list = sorted(target_list, reverse = sortReverse)
    for thing in target_list:
        print(thing)

def main():
    file_list = import_csv()
    sortnprint(file_list)

if __name__ == '__main__':
    main()
