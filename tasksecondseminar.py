# Урок 2. Циклы (for, while)

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

from random import randint
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
    print("Знaчения совподают, повторите ввод еще раз!")









































# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.























# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.