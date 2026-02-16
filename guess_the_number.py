#Вызов рандом модуля
from random import randint, choice

#Ответы
too_low = ['Пока что маловато',  'Маловато, еще давай :3', 'Бери выше', 'Нет, я загадал число побольше :)']
too_high = ['Тихо, тихо, не так много', 'Что-то ты лишканул немножко', 'Давай-ка поменьше :3', 'Многовато', 'Бери ниже :)']
congrats = ['Красавчик, это оно!', 'В точку. Ты победил!', 'Число угадано! Поздравляю!', 'Это победа. Ура!']
wrong_symbol = 'Это не число. Давай еще раз :3'
wrong_num = 'Введи число не меньше 1 и не больше 100 :)'
one_shot = 'ДА ТЫ ВОЛШЕБНИК, ТАК БЫСТРО УГАДАЛ!'
very_near_high = ['Очень близко! Давай ниже :0', 'Еще чуть-чуть! Ниже', 'Горячо! Чуть ниже']
very_near_low = ['Совсем рядом! Возьми выше', 'Почти у цели! Возьми чуть больше', 'Почти угадал, чуть выше!']

#Приветствие
print('Привет! Это угадайка чисел\n')
print('Я загадываю случайное число от 1 до 100\n')
print('А ты пытаешься его угадать и вводишь свои варианты\n')
print('Ах да. У тебя 8 попыток :)\n')

#Основной цикл
def game():
    count = 0
    print('Поехали! Напиши число\n')
    num = randint(1, 100)
    while num:
        if count == 8:
            print('\nТы потратил свои 8 попыток =(\n')
            game_repeat()
            break
        new_word = input()
        if new_word.isdigit():
            if 1 <= int(new_word) <= 100:
                if int(new_word) > num:
                    if count < 7:
                        if int(new_word) - num <= 5:
                            print(choice(very_near_high), end = '\n'*2)
                        else:
                            print(choice(too_high), end = '\n'*2)
                    count += 1
                if int(new_word) < num:
                    if count < 7:
                        if num - int(new_word) <= 5:
                            print(choice(very_near_low), end = '\n'*2)
                        else:
                            print(choice(too_low), end = '\n'*2)
                    count += 1
                if int(new_word) == num and count <= 2:
                    print(one_shot, end = '\n'*2)
                    game_repeat()
                    break
                if int(new_word) == num:
                    print(choice(congrats), end = '\n'*2)
                    game_repeat()
                    break
            else:
                print(wrong_num, end = '\n'*2)
        else:
            print(wrong_symbol, end = '\n'*2)

#Повтор игры
def game_repeat():
    question = input('Напиши "да" если хочешь сыграть снова :)\n\n').lower()
    if question == 'да':
        game()
    else:
        game_repeat()

#Вызов основного цикла
game()


