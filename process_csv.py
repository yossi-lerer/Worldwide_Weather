import csv

def create_csv(filename, fields):
    with open(filename, 'w+', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

def add_row(filename, row):
    data_row = []
    for i in row:
        data_row.append(row[i])
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data_row)
    data_file = read_csv(filename)
    if data_row in data_file:
        return True
    else:
        return False

def read_csv(filename):
    data_list = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data_list.append(row)
    return data_list