import sys
import csv

try:
    csv_file = sys.argv[1]
except IndexError:
    print('Usage: python3 books1.py input-file action [sort-direction]', file=sys.stderr)
    print('At the very least, please include .csv file and an action!')
    exit(1)

try:
    action = sys.argv[2].lower()
except IndexError:
    print('Usage: python3 books1.py input-file action [sort-direction]', file=sys.stderr)
    print('At the very least, please include .csv file and an action!')
    exit(1)

try:
    sort_direction = sys.argv[3].lower()
    if sort_direction == "forward":
        sortReverse= False
    else:
        sortReverse = True
except IndexError:
    sortReverse = False

def createList():
    """
    Creates a sorted list of 
    """
    with open(csv_file, newline = '') as csvfile:
        reader = csv.reader(csvfile)
        target_list = []
        if action == "books":
            item = 0
        elif action == "authors":
            item = 2
            
        for line in reader:
            if action == "authors":
                author = line[item].split("(")[0]
                author_lastName = author.split(' ')[-2]
                if [author_lastName,author] not in target_list:
                    target_list.append([author_lastName,author])
            else:
                target_list.append(line[item])
        return sorted(target_list, reverse = sortReverse)

def printList(target_list):
    for item in target_list:
        if action == "books":
            print(item)
        elif action == "authors":
            print(item[1])

def main():
    target_list = createList()
    printList(target_list)

main()
        
#method below uses dictionaries as data structure instead of lists. 
#much simpler. 
# with open(csv_file, newline = '') as csvfile:
#     reader = csv.reader(csvfile)
#     target_dict = {}
        
#     for line in reader:
#         author = line[2].split("(")[0]
#         book_title = line[0]
#         target_dict[author] = [book_title]
#     if action == "books":
#         target_list = list(target_dict.values())
#     elif action == "authors":
#         target_list = list(target_dict.keys())
#     print(sorted(target_list, reverse = sortReverse))


        
