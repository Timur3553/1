a=int(input ('введіть довжину a '))
b=int(input ('введіть довжину b '))
c=int(input ('введіть довжину c '))

if a+b>c and a+c>b and b+c>a:
    print('трикутник правильний')
    if a==b==c:
        print('та є рівностороннім')
    elif a==b or a==c:
        print('та є рівнобедренним')
    else:
        print('та є різностороннім')
else:
    print('трикутник неправильний')

