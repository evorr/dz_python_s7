import csv

def record_contact(dict):
    with open('contacts.csv','a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for value in dict.values():
            spamwriter.writerow([value])
        spamwriter.writerow(' ')

def read_contacts():
    with open('contacts.csv','r',newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        list_csv = []
        for row in spamreader:
            for value in row:
                list_csv.append(value)
        return list_csv

def find_contact(name):
    with open('contacts.csv','r',newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        list_csv = []
        for row in spamreader:
            for value in row:
                list_csv.append(value)
        split_list_csv = [list_csv[i:i+4] for i in range(0, len(list_csv),5)]
        for el in split_list_csv:
            if name in el:
                return el