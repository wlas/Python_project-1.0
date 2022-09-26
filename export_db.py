# Модуль экспорта данныйх

def export_data():
    with open('db.csv', 'r') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                ln = line.strip().split(',')
                data.append(ln)
            elif ';' in line:
                ln = line.strip().split(';')
                data.append(ln)
            elif ':' in line:
                ln = line.strip().split(':')
                data.append(ln)
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t = []
    return data