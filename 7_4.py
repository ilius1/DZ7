a=int(input('Введите первое число '))
b=int(input('Введите второе число '))
while (a==7 or b==7):
    print('Good bay')
    break
else:
    if a>b:
        print('максимальное число ',a,'сумма ',a+b)
    elif b>a:
        print('максимальное число ', b, 'сумма ', a + b)
    elif b==a:
        print('Числа равны' , b, 'сумма ', a + b)