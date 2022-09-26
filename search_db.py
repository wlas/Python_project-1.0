# модуль поиска данных

import export_db as ed
import user_interface as ui
import print_db as pd

def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None

def input_search():
    in_search = ui.get_input_user("Введите данные для поиска")
    data = ed.export_data()
    item = search_data(in_search, data)
    if item != None:
        pd.print_line(item)
    else:
        print("Данные не обнаружены")