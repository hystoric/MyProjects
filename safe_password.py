from random import randint, choice

print('\nПривет! Эта программа поможет тебе создать безопасные пароли для твоих аккаунтов и приложений\n')
print('Причем сделает их такими, как ты захочешь')

def generate():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    answers = ['да', 'д', 'da', 'd', 'y', 'yes', 'yep', 'yea']
    chars = ''
    passwords = []
    symbols = [digits, lowercase_letters, uppercase_letters, punctuation]

    count = int(input('\nСколько паролей требуется создать?\n\n'))
    lenght = int(input('\nТребуемая длина паролей?\n\n'))
    is_digit = input('\nДобавить ли в пароль цифры?\n\n').lower()
    is_lowercase_letters = input('\nДобавить ли в пароль маленькие буквы?\n\n').lower()
    is_uppercase_letters = input('\nДобавить ли в пароль большие буквы?\n\n').lower()
    is_punctuation = input('\nДобавить ли в пароль различные знаки?\n\n').lower()
    is_the_same = input('\nДобавить ли в пароль неоднозначные символы, такие как "i, I, l, L, o, O, 0"?\n\n').lower()
    answers2 = [is_digit, is_lowercase_letters, is_uppercase_letters, is_punctuation]

    for i in range (len(answers2)):
        if answers2[i] in answers:
            chars += symbols[i]

    if is_the_same not in answers:
        for j in 'i, I, l, L, o, O, 0':
            if j in chars:
                chars = chars.replace(j, '')

    for i in range (count):
        if chars == '':
            print('\nТы не добавил в выборку ни одного вида символов =(')
            again = input('\nСоздать новый список паролей?\n\n').lower()
            if again in answers:
                generate()
            else:
                return
        password = ''
        for j in range (lenght):
            password += choice(chars)
        passwords.append(password)
    print('\nТвои пароли готовы! Пусть они тебя защитят от киберзлодеев!', *passwords, sep = '\n\n')
    again = input('\nСоздать новый список паролей?\n\n').lower()
    if again in answers:
        generate()
    else:
        return

generate()




