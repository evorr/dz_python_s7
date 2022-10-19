#import os

def record_contact(dict):
    with open('contacts.txt','a') as file:
        for value in dict.values():
            file.write(value+';')
        file.write('\n')

def read_contacts():
    with open('contacts.txt','r') as file:
        data = file.readlines()
        res=[]
        for row in data:
            new_row = row.rstrip('\n')
            items = new_row.split(';')
            for item in items:
                res.append(item)
        return res

def find_contact(name):
    with open('contacts.txt', 'r') as file:
        list_lines = file.readlines()
        for i in list_lines:
            if name in i:
                res = i.split(';')
                return res


#def delete_contact(del_con):
    #file = open('contacts.csv','r')
    #temp_file = open('temp.csv','w')
    #all_lines = file.readlines()
    #for line in all_lines:
        #if del_con not in line:
            #temp_file.write(line)
    #file.close()
    #temp_file.close()
    #os.remove('contacts.csv')
    #os.rename('temp.csv','contacts.csv')
