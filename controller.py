import view
#import txt_creator as tc
import csv_creator as cc
def start():
    action = view.get_type_action()
    if action == 1:
        dict_contacts = {'Фамилия':' ',
                         'Имя':' ',
                         'Телефон':' ',
                         'Описание':' '}
        for key in dict_contacts.keys():
            dict_contacts[key] = view.get_info(key)
        cc.record_contact(dict_contacts)
    elif action == 2:
        data = cc.read_contacts()
        view.show_data(data)
    elif action == 3:
        last_name = view.get_last_name()
        found_contact = cc.find_contact(last_name)
        view.show_data(found_contact)
    #elif action == 4:
        #del_con = view.get_del_con()
        #cc.delete_contact(del_con)