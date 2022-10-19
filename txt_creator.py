#import os

def record_contact(dict):
    with open('contacts.txt','a') as file:
        for value in dict.values():
            file.write(value+'\n')
        file.write('\n')

def read_contacts():
    with open('contacts.txt','r') as file:
        data = file.readlines()
        return data

def find_contact(name):
    with open('contacts.txt', 'r') as file:
        list_lines = file.readlines()
        split_list_lines = [list_lines[i:i+4] for i in range(0, len(list_lines),5)]
        for i in split_list_lines:
            if name+'\n' in i:
                return i



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
