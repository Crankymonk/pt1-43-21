lst = []
a = input('Введите сторону а:')
b = input('Введите сторону b:')
c = input('Введите сторону c:')
lst.append(a)
lst.append(b)
lst.append(c)

lst.sort()
# print(lst)

x = lst[2]
# print(x)

if lst[2] < lst[1] + lst[0]:

    p = (a + b + c) / 2
    s = ((p * ((p - a) * (p - b) * (p - c))) ** 0.5)  # Формула Герона для площади треугольника
    print('Площадь треугольника: ' + str(s))
else:
    print('Треугольника с заданными сторонами не существует.')