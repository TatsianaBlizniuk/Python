# Вариант 1. Скопировать в файл F2 только четные строки из F1. Подсчитать размер файлов F1 и F2 (в байтах).

import os


file1 = open("f1.txt", "r", encoding="utf8")
file2 = open("f2.txt", "w", encoding="utf8")
try:

    all_lines = file1.readlines()

    # запись во второй файл четных строк
    file2.writelines(all_lines[1::2])

finally:
    file1.close()
    file2.close()


file1 = open("f1.txt", "r", encoding="utf8")
file2 = open("f2.txt", "r", encoding="utf8")
try:
    all_data = file1.read()
    all_data2 = file2.read()
    print(f'Все строки первого файла:\n {all_data}')
    print('************************************')
    print(f'Только четные строки из первого файла:\n {all_data2}')
    print('************************************')

    # подсчет размера файлов в байтах
    print(os.path.getsize("f1.txt"))
    print(os.path.getsize("f2.txt"))
finally:
    file1.close()
    file2.close()