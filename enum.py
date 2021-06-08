names = ["Balaji", "Vasanthi", "Surya"]
ages  = [46,       39,         14]

for name, age in zip(names, ages):
    print(f'{name} is {age} years old')

lst_a = [4, 3, 7, 6, 5, 9, 2, 4]
lst_b = [1, 4, 6, 7, 4, 6]

for indx, a in enumerate(lst_a):
    print(indx, a)

acc = 0
for i, a, b in zip(range(len(lst_a)), lst_a, lst_b):
    acc += (a / b) ** i
print(acc)

for tup in zip(lst_a, lst_b):
    print(tup)

acc = 0
for tup in enumerate(zip(lst_a, lst_b)):
    print(tup)

