# 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку

# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

n = int(input("Введите количество элементов первого множества "))
num_1 = set()
for i in range(n):
    el_1 = int(input("Введите элемент первого множества "))
    num_1.add(el_1)

m = int(input("Введите количество элементов второго множества "))
num_2 = set()
for i in range(m):
    el_2 = int(input("Введите элемент второго множества "))
    num_2.add(el_2)

u = num_1.union(num_2)
lst1=list(u)
lst1.sort()
if len(lst1) == (n+m):
    print("Повторяющихся чисел нет")
else:
    for i in lst1:
        print(i, end = ' ')