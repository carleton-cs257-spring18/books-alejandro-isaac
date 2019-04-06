import sys
import csv

try:
    csv_file = sys.argv[1]
except IndexError:
    print("Error! Please provide the filename of the csv file.")
    exit(1)

try:
    action = sys.argv[2]
except IndexError:
    print("Error! Please provide an action.")
    exit(1)
    
with open(csv_file, newline = '') as csvfile:
    reader = csv.reader(csvfile)
    target_list = []
    if action.lower() == "books":
        item = 0
    elif action.lower() == "authors":
        item = 2
        
    for line in reader:
        target_list.append(line[item])

    print(target_list)
        
