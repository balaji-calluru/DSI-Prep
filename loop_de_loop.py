selections = []
more_food = True
menu_str = '''Select from this list:
   1 : Bread
   2 : Butter
   3 : Potatoes
   4 : Chicken'''

while more_food:
    print(menu_str)

    inp = int(input('Please make a selection, 1-4: '))

    if inp in [1,2,3,4]:
        selections.append(inp)
        inp2 = input('More Food [y/n]?')
        if inp2 not in ['y','Y']:
            more_food = False
    else:
        print('--- Your selection was not understood ---')

print(selections)