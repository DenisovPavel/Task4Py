
#  Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Заполните массив элементами арифметической прогрессии.
#  Каждое число вводится с новой строки.

first_number = int(input("Введите первый элемент: "))
raznost = int(input("Введите разность элементов: "))
kolichestvo = int(input("Введите количество  элементов: "))
i = kolichestvo
while i >= first_number:
   my_list = []
   d = first_number + (kolichestvo - i) * raznost
   my_list.append(d)
   print(f"{my_list}\n")
   i -= 1
  
# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

list = [int(input("Введите элемент: "))
        for i in range(int(input("Введите количество элементов: ")))]
index_list = []
min_element = int(input("Введите минимальный элемент диапазона - "))
max_element = int(input("Введите максимальный элемент диапазона - "))
for i in range(0, len(list)-1):
    if list[i] > min_element and list[i] < max_element:
     index_list.append(i)
print(index_list)







