import csv

def get_csv_as_list(file):
    csv_as_list = []

    with open(file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            csv_as_list.append(row)

    return csv_as_list
