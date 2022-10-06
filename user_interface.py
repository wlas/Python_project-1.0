def get_menu():
    print('Выберите пункт из меню: \n\
        1 - Вывести все контакты. \n\
        2 - Добавить контакт. \n\
        3 - Поиск контакта.\n\
        0 - Завершение работы.')

def get_main():
    print('Телефонный справочник')

def get_result_user():
    return int(input('Укажите цифру: '))

def get_input_user(str):
    return input(f'{str}: ')    