import sys
import csv

def import_csv(action='books'):
    try:
        assert(len(sys.argv)>1)
        f_ls = []
        with open(sys.argv[1], newline='') as f:
            books_csv = csv.reader(f)
            for row in books_csv:
                f_ls.append(row)
    except:
        print("No CSV file.")
        sys.exit()

def sortnprint(ls):
    

def main():
    file_list = import_csv()
    sortnprint(file_list)


if __name__ == '__main__':
    main()
