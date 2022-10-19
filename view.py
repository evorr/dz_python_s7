
def get_type_action():
    return int(input('Нажмите 1 - чтобы ввести контакт, \n'
                     'нажмите 2 - чтобы посмотреть контакты все \n'
                     'нажмите 3 - чтобы найти контакт \n'
                     ': '))

def get_info(parametr):
    return input(f'{parametr}: ')

def show_data(data):
    for i in data:
        print(i.rstrip('\n'))

def get_last_name():
    return input('Фамилия: ')




#def get_del_con():
    #return input('Кого удалить: ')