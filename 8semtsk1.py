# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines 
# (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:

def vvod_strok():
    num_lines = input("Введите количество строк: ")
    while not num_lines.isdigit():
        num_lines = input("Неккоректный ввод. Введите другое количество строк: ")
    return int(num_lines)


def chtenie_strok(lines, file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        amount_lines = len(text)
        start = amount_lines - lines
        for i in text[start:]:
            print(i)


article_file = "Pushkin.txt"
last_lines = vvod_strok()
chtenie_strok(last_lines, article_file)