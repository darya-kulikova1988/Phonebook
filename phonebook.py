# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# 1. Показать искомый контакт
# 2. Добавить новый контакт
# 3. Изменить контакт
# 4. Удалить контакт
# 5. Экспорт выбранного контакта в файл
# 6. Выход из меню

def read_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        return file.readlines()


def find_cont(data, name):
    all_lines = ''
    for line in data:
        if name in line.lower() and len(line) > 3:
            all_lines += line
    return all_lines


def write_file(path, data, key):
    with open(path, key, encoding='UTF-8') as file:
        if len(data) > 3:
            file.write('\n'+data)


def change_delete_file(path, name, new_data):
    data_file = read_file(path)
    check = True
    for index, line in enumerate(data_file):
        if name in line.lower() and len(line) > 3:
            data_file[index] = new_data
            with open(path, 'w', encoding='UTF-8') as file:
                for line in data_file:
                    file.write(line)
            check = False
    if check:
        print('Name not found')


path_phbook = 'phonebook.txt'
path_result = 'result.txt'
while True:
    menu = int(input('Choose your doing\n'
                     '1. Show contact\n'
                     '2. Add new contact\n'
                     '3. Change contact\n'
                     '4. Delete contact\n'
                     '5. Export contact at file\n'
                     '6. Exit from menu\n: '))

    if menu != 2 and menu != 6:
        name = input('Input name: ')

    if menu == 1:
        data_file = read_file(path_phbook)
        print(find_cont(data_file, name))

    if menu == 2:
        new_contact = input(
            'Input Last name, First name and phone using space: \n')
        write_file(path_phbook, new_contact, 'a')

    if menu == 3:
        new_data = input(
            'Input Last name, First name and phone using space: \n')
        change_delete_file(path_phbook, name, new_data)

    if menu == 4:
        new_data = ''
        change_delete_file(path_phbook, name, new_data)

    if menu == 5:
        data_file = read_file(path_phbook)
        result = find_cont(data_file, name)
        write_file(path_result, result, 'w')

    if menu == 6:
        break
