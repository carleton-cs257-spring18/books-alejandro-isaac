import sys
import csv

try:
    csv_file = sys.argv[1]
except IndexError:
    print("Error! Please provide the filename of the csv file.")
    exit(1)

try:
    action = sys.argv[2].lower()
except IndexError:
    print("Error! Please provide an action.")
    exit(1)

try:
    sort_direction = sys.argv[3].lower()
    if sort_direction == "forward":
        sortReverse= False
    else:
        sortReverse = True
except IndexError:
    sortReverse = False

with open(csv_file, newline = '') as csvfile:
    reader = csv.reader(csvfile)
    target_list = []
    if action == "books":
        item = 0
    elif action == "authors":
        item = 2
        
    for line in reader:
        target_list.append(line[item])
        
    print(sorted(target_list, reverse = sortReverse))


        
