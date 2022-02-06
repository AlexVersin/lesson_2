# 1) Создать список, содержащий цены на товары (10 – 20 товаров)
list_cash = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12, 1508.5, 800900, 4.000007, 56.911, 29.0596, 481, 0.925]
print("Исходный список:")
print(list_cash)

# 2) Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
print()
print("Цены через запятую:")
for x in list_cash:
    number_1 = int(x)
    number_2 = str(int((x * 100) - (number_1 * 100)))
    if len(number_2) == 1:
        print(str(number_1), "руб", "0" + number_2, "коп, ", end="")
    else:
        print(str(number_1), "руб", number_2, "коп, ", end="")
print()
print()

# 3) Вывести на экран цены(как числа), отсортированные по возрастанию,
# новый список для этого не создавать (доказать,
# что объект списка после сортировки остался тот же).
print("Доказательство операции in place:")
print("id перед сортировкой", id(list_cash), list_cash)
list_cash.sort()
print("id после сортировкои", id(list_cash), list_cash)
print()

# 4) Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Показать, что это другой список, другой объект,
print("Доказательство отсутствия операции in place:")
list_cash_new_reverse = sorted(list_cash, reverse=True)
print("id перед сортировкой", id(list_cash), (list_cash))
print("id после сортировкои", id(list_cash_new_reverse), (list_cash_new_reverse))

# 5)Вывести цены пяти самых дорогих товаров
print()
print("5 самых дорогих товаров:")
for x in list_cash_new_reverse[:5]:
    print(x)