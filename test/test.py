# import csv
# file =open("Stars.csv", "a")
# name = input("Введите вашу имя: ")
# surname = input("Введите вашу фамилию: ")
# phone = input("Введите ваш телефон: ")
# newRecord = name + ','+ surname + ',' + phone + '\n'
# file.write(str(newRecord))
# file. close

import csv
with open("classmates.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Вывод строк
            print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
        count += 1
    print(f'Всего в файле {count} строк.')