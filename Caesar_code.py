print('\nЭта программа поможет вам создать Шифр Цезаря, а также дешифровать его!\n')
print('''Шифр Цезаря - это метод шифрования,
при котором каждая буква текста заменяется другой, 
отстоящей на фиксированное количество позиций правее по алфавиту.
Например, при шаге равном 3, «А» превращается в «Г»,
При дешифровке «Г» превращается в «А».''')

def caesar():
    is_code = input('\nНапишите "1", если нужно зашифровать текст, или "2",если нужно его дешифровать\n\n')
    while is_code != '1' and is_code != '2':
        is_code = input('''\nНеподходящий ответ.\nНапишите "1", если нужно зашифровать текст, или "2",если нужно его дешифровать\n\n''')
    is_language = input('\nНа каком языке текст? "1" - русский, "2" - английский\n\n')
    while is_language != '1' and is_language != '2':
        is_language = input('\nНеподходящий ответ.\nНа каком языке текст? "1" - русский, "2" - английский\n\n')
    is_step = input('\nВведите шаг сдвига (любое число от 1 до 26)\n\n')
    while is_step.isdigit() == False or int(is_step) > 26 or int(is_step) < 1:
        is_step = input('\nНеподходящий ответ.\nВведите любое число от 1 до 26\n\n')

    text = input('\nВведите текст\n\n')

    low_eng_chars = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    up_eng_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_rus_chars = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
    up_rus_chars = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ''

    for i in text:
        if i.isalpha():
            if is_language == '1':
                if i not in low_rus_chars and i not in up_rus_chars:
                    print('\nТекст содержит буквы другого языка! Запускаю программу заного')
                    caesar()
                if is_code == '1':
                    if i.isupper():
                        x = up_rus_chars.index(i)
                        result += up_rus_chars[x + int(is_step)]
                    else:
                        x = low_rus_chars.index(i)
                        result += low_rus_chars[x + int(is_step)]
                if is_code == '2':
                     if i.isupper():
                        x = up_rus_chars.index(i)
                        result += up_rus_chars[x - int(is_step)]
                     else:
                        x = low_rus_chars.index(i)
                        result += low_rus_chars[x - int(is_step)]
            if is_language == '2':
                if i not in up_eng_chars and i not in low_eng_chars:
                    print('\nТекст содержит буквы другого языка! Запускаю программу заного')
                    caesar()
                if is_code == '1':
                    if i.isupper():
                        x = up_eng_chars.index(i)
                        result += up_eng_chars[x + int(is_step)]
                    else:
                        x = low_eng_chars.index(i)
                        result += low_eng_chars[x + int(is_step)]
                if is_code == '2':
                    if i.isupper():
                        x = up_eng_chars.index(i)
                        result += up_eng_chars[x - int(is_step)]
                    else:
                        x = low_eng_chars.index(i)
                        result += low_eng_chars[x - int(is_step)]
        else:
            result += i

    print('\nВаш результат:', result)
    repeat = input('\nНажмите "1", если хотите повторить операцию, или "2", чтобы закрыть программу\n\n')
    while repeat != '1' and repeat != '2':
        repeat = input('\nНеподходящий ответ.\nНажмите "1", если хотите повторить операцию, или "2", чтобы закрыть программу\n\n')
    if repeat == '1':
        caesar()
    else:
        return

caesar()






