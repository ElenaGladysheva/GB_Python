def write_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for c in contacts:
            file.write(c['name'] + ', ' + c['surname'] + ', ' + c['patronymic'] + ', ' + c['phone'] + '\n')


def read_contacts(filename):
    contacts = []
    with open(filename, 'r') as file:
        for line in file:
            name, surname, patronymic, phone = line.strip().split(',')
            contact = {
                'name' : name.strip(),
                'surname' : surname.strip(),
                'patronymic' : patronymic.strip(),
                'phone' : phone.strip()
            }
            contacts.append(contact)
    return contacts

def search_contacts(contacts):
    query = input('Введите строку для поиска: ')
    result = []
    for c in contacts:
        if query == c['name'] or query == c['surname'] or query == c['patronymic']:
            result.append(c)
    return result

def print_contacts(contacts):
    n = 0
    for c in contacts:
        print(n, c['name'], c['surname'], c['patronymic'], c['phone'], sep=', ')
        n = n + 1
    print()

def add_contact(contacts):
    c = {}
    c['surname'] = input('Фамилия: ')
    c['name'] = input('Имя: ')
    c['patronymic'] = input('Отчество: ')
    c['phone'] = input('Телефон: ')
    contacts.append(c)

def del_contact(contacts):
    res = search_contacts(contacts)
    if len(res) == 0:
        print('Запись не найдена')
    elif len(res) == 1:
        contacts.remove(res[0])
        print('Запись удалена')
    else:
        print('Выберите запись для удаления:')
        print_contacts(res)
        n = int(input())
        if n < len(res):
            contacts.remove(res[n])               
            print('Запись удалена')
        else:
            print('Номер введен неверно')

def change_contact(contacts):
    res = search_contacts(contacts)
    if len(res) == 0:
        print('Запись не найдена')
    else:
        if len(res) == 1:
            contacts.remove(res[0])
            add_contact(contacts)
        else:
            print('Выберите запись для изменения:')
            print_contacts(res)
            n = int(input())
            if n < len(res):
                contacts.remove(res[n])               
                add_contact(contacts)
            else:
                print('Номер введен неверно')

filename = 'book.txt'
conts = read_contacts(filename)
n = 0
while (n != 7):
    print('1. Вывод', '2. Добавление данных', '3. Поиск', '4. Изменение', '5. Удаление', '6. Сохранить', '7. Выход', sep='\n')
    n = int(input())
    if n == 1:
        print_contacts(conts)
    elif n == 2:
        add_contact(conts)
    elif n == 3:
        print_contacts(search_contacts(conts))
    elif n == 4:
        change_contact(conts)
    elif n == 5:
        del_contact(conts)
    elif n == 6:
        write_contacts(filename, conts)
    
    
