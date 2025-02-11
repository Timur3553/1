month = int(input('Введіть номер місяця: '))

if month in [12, 1, 2]:
    print('Це зима')
elif month in [3, 4, 5]:
    print('Це весна')
elif month in [6, 7, 8]:
    print('Це літо')
elif month in [9, 10, 11]:
    print('Це осінь')
else:
    print('Невірний номер місяця.')


