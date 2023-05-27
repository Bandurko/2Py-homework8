def fileread():
    return open('book.txt', 'r', encoding='utf-8')

def fileadd():
    return open('book.txt', 'a', encoding='utf-8')

def filewrite():
    return open('book.txt', 'w', encoding='utf-8')

def show_data() -> None:
    """Выводит информацию из справочника"""
    print(fileread().read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    fileadd().write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    data = fileread().read().split('\n')
    print('\n'.join(data))
    data_to_find = input('Введите данные для поиска: ')
    print(search(data, data_to_find))


def search(book: list[str], info: str) -> list[str] | str:
    """Находит в списке записи по определенному критерию поиска"""
    result = [contact for contact in book if info in contact]
    if not result:
        return 'Совпадений не найдено'
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('-------------------')
        print('\n'.join(result))
        new_info = input('Введите дополнительные данные для поиска: ')
        return search(result, new_info)


def change() -> None:
    """Изменение/удаление данных в справочнике"""
    data = fileread().read().split('\n')
    print('\n'.join(data))
    data_to_edit = input('Введите данные для поиска: ')
    data_to_edit = search(data, data_to_edit)
    mode = input('Удалить или изменить? 1 - удалить, 2 - изменить: ')
    if mode == '1':
        data.remove(data_to_edit)
    elif mode == '2':
        data[data.index(data_to_edit)] = enter_contact()

    filewrite().write('\n'.join(data))


def enter_contact() -> str:
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    return f'{fio} | {phone}'