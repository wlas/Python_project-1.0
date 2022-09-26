# модуль печати данных из базы

from dataclasses import dataclass
import export_db as ed

def read_db():
    data = ed.export_data()
    for row in data:
        print_line(row)

def print_line(line):
    surname, name, tel = line
    print(f'* {surname} {name}: {tel}')        