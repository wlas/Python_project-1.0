import user_interface as ui
import print_db as pd
import search_db as sd
import export_db as ed
import import_db as id


def start_menu():
    ui.get_main()
    while True:
        ui.get_menu()
        result = ui.get_result_user()
        if result == 1:
            pd.read_db()
        elif result == 2:
            row_data = id.input_data()
            separ = id.choice_sep()
            id.import_data(row_data, separ)
        elif result == 3:
            sd.input_search()
        elif result == 0:
            break