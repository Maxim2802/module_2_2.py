# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

first = int(input())
second = int(input())
third = int(input())
if first == second and first == third :
    print(3)
elif first == second or first == third or second == third :
    print(2)
else:
    print(0)