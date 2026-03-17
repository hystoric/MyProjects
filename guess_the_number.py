import tkinter as tk
from random import randint, choice
from tkinter import messagebox

win = tk.Tk()
win.title ('Угадайка чисел')
win.geometry ('700x500+500+300')
win.resizable (False, False)
win.config (bg='#00ccff')

too_low = ['Пока что маловато', 'Маловато, давай еше', 'Бери выше', 'Нет, я загадал число побольше']
too_high = ['Тихо, тихо, не так много', 'Что-то ты лишканул немножко', 'Давай-ка поменьше', 'Многовато', 'Бери ниже']
congrats = ['Красавчик, это оно!', 'В точку. Ты победил!', 'Число угадано! Поздравляю!', 'Это победа. Ура!']
very_near_high = ['Очень близко! Давай ниже', 'Еще чуть-чуть! Ниже', 'Горячо! Чуть ниже']
very_near_low = ['Совсем рядом! Возьми выше', 'Почти у цели! Возьми чуть больше', 'Почти угадал, чуть выше!']

def again():
    clear_all()
    label = tk.Label (win, width = 25, height = 1, text = 'Отлично! Играем снова...', bg = '#00ccff', fg = '#ffffff',
        font = ('Arial', 20, 'bold'))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
    win.after(3000, game)

def end():
    clear_all()
    label = tk.Label (win, width = 25, height = 1, text = 'Спасибо тебе за игру!', bg = '#00ccff', fg = '#ffffff',
        font = ('Arial', 20, 'bold'))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
    win.after(3000, win.destroy)

def clear_all():
    for widget in win.winfo_children():
        widget.destroy()

def clear_input():
    entry.delete(len(entry.get()) - 1)

def calc():
    global count

    if entry.get().isdigit() == False:
        messagebox.showinfo('Ошибка ввода!', 'Для ввода допускаются только цифры')
        entry.delete(0, tk.END)

    elif int(entry.get()) < 1 or int(entry.get()) > 100:
        messagebox.showinfo('Ошибка ввода!', 'Подходят только числа от 1 до 100')
        entry.delete(0, tk.END)

    else:
        count -= 1
        if int(entry.get()) == num:
            if count > 4:
                clear_all()
                label = tk.Label (win, width = 30, height = 1, text = 'ТАК БЫСТРО УГАДАЛ!', bg = '#00ccff', fg = '#ffffff',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.3, anchor = 'c')

                label = tk.Label (win, width = 20, height = 2, text = f'Это было число: {num}', bg = '#ffff99', fg = '#000000',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.45, anchor = 'c')

                label = tk.Label (win, width = 30, height = 1, text = 'Cыграем снова?', bg = '#00ccff', fg = '#ffffff',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.6, anchor = 'c')

                button = tk.Button (win, relief = tk.RAISED, bd = 5, width = 7, height = 1, text = 'Не хочу', bg = '#339933', fg = '#ffffff',
                font = ('Arial', 20, 'bold'), command = end)
                button.place(relx = 0.35, rely = 0.75, anchor = 'c')

                button = tk.Button (win, relief = tk.RAISED, bd = 5, width = 7, height = 1, text = 'Давай!', bg = '#339933', fg = '#ffffff',
                font = ('Arial', 20, 'bold'), command = again)
                button.place(relx = 0.65, rely = 0.75, anchor = 'c')

            else:
                clear_all()
                label = tk.Label (win, width = 30, height = 1, text = choice(congrats), bg = '#00ccff', fg = '#ffffff',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.3, anchor = 'c')

                label = tk.Label (win, width = 20, height = 2, text = f'Это было число: {num}', bg = '#ffff99', fg = '#000000',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.45, anchor = 'c')

                label = tk.Label (win, width = 30, height = 1, text = 'Cыграем снова?', bg = '#00ccff', fg = '#ffffff',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.6, anchor = 'c')

                button = tk.Button (win, relief = tk.RAISED, bd = 5, width = 7, height = 1, text = 'Не хочу', bg = '#339933', fg = '#ffffff',
                font = ('Arial', 20, 'bold'), command = end)
                button.place(relx = 0.35, rely = 0.75, anchor = 'c')

                button = tk.Button (win, relief = tk.RAISED, bd = 5, width = 7, height = 1, text = 'Давай!', bg = '#339933', fg = '#ffffff',
                font = ('Arial', 20, 'bold'), command = again)
                button.place(relx = 0.65, rely = 0.75, anchor = 'c')

        elif count == 0:
            clear_all()
            label = tk.Label (win, width = 30, height = 1, text = 'У тебя закончились попытки', bg = '#00ccff', fg = '#ffffff',
            font = ('Arial', 20, 'bold'))
            label.place(relx = 0.5, rely = 0.3, anchor = 'c')

            label = tk.Label (win, width = 20, height = 2, text = f'Это было число: {num}', bg = '#ffff99', fg = '#000000',
            font = ('Arial', 20, 'bold'))
            label.place(relx = 0.5, rely = 0.45, anchor = 'c')

            label = tk.Label (win, width = 30, height = 1, text = f'Cыграем снова?', bg = '#00ccff', fg = '#ffffff',
            font = ('Arial', 20, 'bold'))
            label.place(relx = 0.5, rely = 0.6, anchor = 'c')

            button = tk.Button (win, relief = tk.RAISED, bd = 5, width = 7, height = 1, text = 'Не хочу', bg = '#339933', fg = '#ffffff',
            font = ('Arial', 20, 'bold'), command = end)
            button.place(relx = 0.35, rely = 0.75, anchor = 'c')

            button = tk.Button (win, relief = tk.RAISED, bd = 5, width = 5, height = 1, text = 'Давай!', bg = '#339933', fg = '#ffffff',
            font = ('Arial', 20, 'bold'), command = again)
            button.place(relx = 0.65, rely = 0.75, anchor = 'c')

        elif int(entry.get()) > num:
            if (int(entry.get()) - num) <= 5:
                label = tk.Label (win, width = 30, height = 1, text = choice(very_near_high), bg = '#00ccff', fg = '#ffffff',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.7, anchor = 'c')

                label = tk.Label (win, width = 20, height = 1, text = f'Осталось попыток: {count}', bg = '#00ccff', fg = '#ffffff',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.8, anchor = 'c')

            else:
                label = tk.Label (win, width = 30, height = 1, text = choice(too_high), bg = '#00ccff', fg = '#ffffff',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.7, anchor = 'c')

                label = tk.Label (win, width = 20, height = 1, text = f'Осталось попыток: {count}', bg = '#00ccff', fg = '#ffffff',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.8, anchor = 'c')

        elif int(entry.get()) < num:
            if (num - int(entry.get())) <= 5:
                label = tk.Label (win, width = 30, height = 1, text = choice(very_near_low), bg = '#00ccff', fg = '#ffffff',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.7, anchor = 'c')

                label = tk.Label (win, width = 20, height = 1, text = f'Осталось попыток: {count}', bg = '#00ccff', fg = '#ffffff',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.8, anchor = 'c')

            else:
                label = tk.Label (win, width = 30, height = 1, text = choice(too_low), bg = '#00ccff', fg = '#ffffff',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.7, anchor = 'c')

                label = tk.Label (win, width = 20, height = 1, text = f'Осталось попыток: {count}', bg = '#00ccff', fg = '#ffffff',
                font = ('Arial', 20, 'bold'))
                label.place(relx = 0.5, rely = 0.8, anchor = 'c')

def game():
    global num
    global count
    global entry
    num = randint(1, 100)
    print (num)
    count = 8
    clear_all()

    label = tk.Label (win, text = 'Введи любое число', bg = '#00ccff', fg = '#ffffff',
    font= ('Arial', 20, 'bold'), width = 17, height = 1)
    label.place(relx = 0.5, rely = 0.2, anchor = 'center')

    label = tk.Label (win, text = 'от 1 до 100', bg = '#00ccff', fg = '#ffffff',
    font= ('Arial', 20, 'bold'), width = 11, height = 1)
    label.place(relx = 0.5, rely = 0.3, anchor = 'center')

    button = tk.Button (win, relief = tk.RAISED, bd = 5, width = 4, height = 1, text = 'Ввод', bg = '#339933', fg = '#ffffff',
    font= ('Arial', 20, 'bold'), command = calc)
    button.place(relx = 0.6, rely = 0.55, anchor = 'center')

    button = tk.Button (win, relief = tk.RAISED, bd = 5, width = 4, height = 1, text = '<', bg = '#339933', fg = '#ffffff',
    font= ('Arial', 20, 'bold'), command=clear_input)
    button.place(relx = 0.4, rely = 0.55, anchor = 'center')

    entry = tk.Entry (win, width = 7, justify = tk.CENTER, font = ('Arial', 20))
    entry.place(relx = 0.5, rely = 0.4, anchor = 'center')

label = tk.Label (win, text = 'Привет! Это угадайка чисел',
bg = '#00ccff', fg = '#ffffff', font = ('Arial', 20, 'bold'))
label.place(relx = 0.5, rely = 0.2, anchor = 'center')

label = tk.Label (win, text = 'Я загадываю случайное число от 1 до 100',
bg = '#00ccff', fg = '#ffffff', font = ('Arial', 20, 'bold'))
label.place(relx = 0.5, rely = 0.35, anchor = 'center')

label = tk.Label (win, text = '''А ты пытаешься его угадать
и вводишь свои варианты''', bg = '#00ccff', fg = '#ffffff', font = ('Arial', 20, 'bold'))
label.place(relx = 0.5, rely = 0.5, anchor = 'center')

label = tk.Label (win, text = 'У тебя 8 попыток. Готов?',
bg = '#00ccff', fg = '#ffffff', font = ('Arial', 20, 'bold'))
label.place(relx = 0.5, rely = 0.65, anchor = 'center')

button = tk.Button (win, relief = tk.RAISED, bd = 5, text = 'Начать игру', bg = '#339933', fg = '#ffffff', font = ('Arial', 20, 'bold'),
width = 15, height = 1, command = game)
button.place(relx = 0.5, rely = 0.8, anchor = 'center')

win.mainloop ()
