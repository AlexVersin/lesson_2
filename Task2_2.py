list_one = ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
print("Исходный список:")
print(list_one)
list_x = []
for x in list_one:
    if x[0] == "+":
        if len(x) <= 2:
            x = "+0" + x[1:]
        list_x.append('"')
        list_x.append(x)
        list_x.append('"')

    elif x[0] == "-":
        if len(x) <= 2:
            x = "-0" + x[1:]
        list_x.append('"')
        list_x.append(x)
        list_x.append('"')

    elif x.isnumeric() == True:
        if len(x) <= 1:
            x = "0" + x[0:]
        list_x.append('"')
        list_x.append(x)
        list_x.append('"')

    else:
        list_x.append(x)
print()
print("Новый список + добавление элементов-кавычек:")
print(list_x)

print()
print("Строка:")
for l in list_x:
    if l[0] == "+":
        print(l, end="")

    elif l[0] == "-":
        print(l, end="")

    elif l.isnumeric() == True:
        print(l, end="")

    elif l[0] == '"':
        print(l, end="")

    else:
        print(" " + l + " ", end="")
