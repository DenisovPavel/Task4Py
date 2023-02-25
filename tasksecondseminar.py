# Урок 2. Циклы (for, while)

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
#  а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
#  чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
#  которые нужно перевернуть

# В ПЕРВОМ СЛУЧАЕ У НАС ВЫВОДИТСЯ КОЛИЧЕСТВО МОНЕТ В ВИДЕ ЦИФР

eagle_coins = int(randint(1, 10)) # OREL monetki
tails_coins = int(randint(1, 10)) # RESHKA monetki

print(f"Орел:", eagle_coins)
print(f"Решка:", tails_coins)

if eagle_coins!=tails_coins:

    if eagle_coins<tails_coins:
      print(f"Минимальное количество монет стороной 'ОРЕЛ', которые нужно перевернуть :",eagle_coins) #nuzno povernut' OREL monetki - minimalnoe kol monet
    else:
        print(f"Минимальное количество монет стороной 'РЕШКА', которые нужно перевернуть :",tails_coins) #nuzno povernut' RESHKA monetki - minimalnoe kol monet
else:
    print("Знaчения совпадают, повторите ввод еще раз!")


# ВТОРОЙ СЛУЧАЙ В ВИДЕ 0 И 1

# import random
# num = int(input("Задайте количество монет: "))
# coins = []
# for i in range(num):
#    coins.append(random.randint(0, 1))
# print(f"Случайный разброс монет по заданому размеру:{coins}")

# Reshka = 0  # Решка
# Orel =  0  # орел

# for j in coins:
#   if j == 0:
#    Reshka += 1
#   else:
#      Orel += 1

# print(f' Орлов : {Orel} и Решек: {Reshka}')

# if Orel==Reshka:
#   print("Монеты совподают!")
# elif Orel >= Reshka:
#  print(f'Развернем {Reshka} выпавших Решкой !')
# else:
#     print(f'Развернем {Orel} выпавших Орлом !')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

Summa = int(input("Введите сумму чисел: "))
Proizvedenie = int(input("Введите произведение чисел: "))
numberX = 1
numberY = Summa - 1
while (numberX * numberY < Proizvedenie):
   numberX +=1
   numberY -=1
print(f'Задуманные  числа Пети:  X = {numberX} , Y = {numberY}')


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N. 
# 2 в 4 степени = 2*2*2*2 записать и вывезти : 10 -> 1 ,2,4,8,

number = int(input("Введите целое число для проверки степени двойки: "))
count = 1 
while count <= number:   
    print(count, end = "  ") 
    count*=2 