#Перевод из любой "СС" в 10 "СС"
def from_any_to_10(num, from_where):
    num = list(num)
    x = 0

    for j in range(len(num)):
        if num[j] == 'A':
            num[j] = '10'
        if num[j] == 'B':
            num[j] = '11'
        if num[j] == 'C':
            num[j] = '12'
        if num[j] == 'D':
            num[j] = '13'
        if num[j] == 'E':
            num[j] = '14'
        if num[j] == 'F':
            num[j] = '15'

    for i in range(len(num)):
        x += int(num[i]) * int(from_where) ** (len(num) - 1 - i)

    return x

#Перевод из 10 "СС" в любую "СС"
def from_10_to_any(num, to_where):
    x = []
    num = int(num)
    to_where = int(to_where)

    while num > 0:
        x.append(str(num % to_where))
        num //= to_where

    for i in range(len(x)):
        if x[i] == '10':
            x[i] = 'A'
        if x[i] == '11':
            x[i] = 'B'
        if x[i] == '12':
            x[i] = 'C'
        if x[i] == '13':
            x[i] = 'D'
        if x[i] == '14':
            x[i] = 'E'
        if x[i] == '15':
            x[i] = 'F'

    return ''.join (x[::-1])

#Приветствие и ввод данных
def greetings():
    from_where = input('''\nНапишите, из какой системы счисления перевести ваше число.
"2" - двоичная, "8" - восьмеричная, "10" - десятичная, "16" - шестнадцатеричная\n\n''')
    while from_where.isdigit() == False or from_where not in ['2', '8', '10', '16']:
        from_where = input('''\nНеверное значение. Введите одну из систем.
"2" - двоичная, "8" - восьмеричная, "10" - десятичная, "16" - шестнадцатеричная\n\n''')

    to_where = input('''\nНапишите в какую систему нужно перевести ваше число?
"2" - двоичная, "8" - восьмеричная, "10" - десятичная, "16" - шестнадцатеричная\n\n''')
    while to_where.isdigit() == False or to_where not in ['2', '8', '10', '16']:
        to_where = input('''\nНеверное значение. Введите одну из систем.
"2" - двоичная, "8" - восьмеричная, "10" - десятичная, "16" - шестнадцатеричная\n\n''')

    return from_where, to_where

#Проверка ввода числа
def check_num(from_where):
    num = input('\nВведите ваше число\n\n').upper()
    flag = True

    for i in num:
        if from_where == '16' and i.isalnum() == False or (i.isalpha() and i not in 'ABCDEF'):
            flag = False
            break
        if from_where == '10' and i.isdigit() == False:
            flag = False
            break
        if from_where == '8' and (i.isdigit() == False or int(i) > 7):
            flag = False
            break
        if from_where == '2' and (i.isdigit() == False or int(i) > 1):
            flag = False
            break

    while from_where == '2' and flag == False:
        print('\nВ двоичной системе допускаются только цифры "0" и "1"', end = '')
        num = input('\nВведите ваше число"\n\n').upper()

        flag = True

        for i in num:
            if i.isdigit() == False or int(i) > 1:
                flag = False
                break

    while from_where == '8' and flag == False:
        print('\nВ восьмеричной системе допускаются только цифры от 0 до 7 включительно', end = '')
        num = input('\nВведите ваше число\n\n').upper()

        flag = True

        for i in num:
            if i.isdigit() == False or int(i) > 7:
                flag = False
                break

    while from_where == '10' and flag == False:
        print('\nВ десятичной системе допускаются только цифры', end = '')
        num = input('\nВведите ваше число\n\n').upper()

        flag = True

        for i in num:
            if i.isdigit() == False:
                flag = False
                break

    while from_where == '16' and flag == False:
        print('\nВ шестнадцатеричной системе допускаются только все цифры и буквы "ABCDEF"', end = '')
        num = input('\nВведите ваше число\n\n').upper()

        flag = True

        for i in num:
            if i.isalnum() == False or (i.isalpha() and i not in 'ABCDEF'):
                flag = False
                break

    return num

#Основной цикл программы
def starting():
    from_where, to_where = greetings()
    num = check_num(from_where)

    if from_where == to_where:
        print('Ваш результат:', num)

    if from_where != to_where:
        if to_where == '10':
            first_step = from_any_to_10(num, from_where)
            print('Ваш результат:',first_step)

        if from_where == '10':
            second_step = from_10_to_any(num, to_where)
            print('Ваш результат:',second_step)

        if from_where != '10' and to_where != '10':
            first_step = from_any_to_10(num, from_where)
            second_step = from_10_to_any(first_step, to_where)
            print('Ваш результат:',second_step)

    repeat = input('''\nХотите повторить операцию?
Нажмите "1", чтобы повторить, или "2", чтобы завершить программу\n\n''')
    while repeat != '1' and repeat != '2':
        repeat = input('''\nНеверное значение.
Нажмите "1", чтобы повторить, или "2", чтобы завершить программу\n\n''')

    if repeat == '1':
        starting()
    else:
        return

print('''\nЭто калькулятор систем счисления.
Он поможет вам преобразовать числа
из одной системы счисления - в любую другую!''')
starting()

