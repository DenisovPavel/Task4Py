# Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
# Пример
# Ввод

# 8-5+2-1
# Вывод
# 4

input_str = '8-5+2-1'
sum_number = int(input_str[0])
for i in range(2, len(input_str)):
    if input_str[i-1] == '-':
        sum_number -= int(input_str[i])
    elif input_str[i-1] == '+':
        sum_number += int(input_str[i])
print(sum_number)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задача 2
# Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)

# Формат ввода
# Вводится строка.

# Формат вывода
# Выведите слова из строки по одному.

# Пример 1
# Ввод

# Hello, world!
# Вывод
# Hello,
# world!
# Пример 2
# Ввод

# My heart in the Highland
# Вывод
# My
# heart
# in
# the
# Highland 


message = input("Введите предложение: ")
probel= " "
message = message.replace(probel,"\n")
print(message)

#--------------------------------------------------------------
# побуквенный перенос!!

# message = input("Введите предложение: ")
# probel = " "
# for c in message:
#     if c == probel:
#         print()
#     else:
#      print(c)



    





