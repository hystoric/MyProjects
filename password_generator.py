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


import customtkinter as ctk
from random import choice
from tkinter import messagebox

ctk.set_appearance_mode ("dark")

app = ctk.CTk()
app.title ('your_password')
app.geometry ('500x700+900+300')
app.resizable (False, False)
app.config (bg='#ffcc66')
app.attributes ('-alpha', 0.8)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
waitings = ['Мне нужно\n несколько секунд...', 'Дайте мне\n немного времени...', 'Почти готово...']


def clear_all():
    for widget in app.winfo_children():
        widget.destroy()

def select_all(box1, box2, box3, box4, box5):
    for check in [box1, box2, box3, box4, box5]:
        check.select()

def deselect_all(box1, box2, box3, box4, box5):
    for check in [box1, box2, box3, box4, box5]:
        check.deselect()

def result():
    clear_all()
    label = ctk.CTkLabel (master = app, text = 'Пароли', bg_color = '#ffcc66',
    text_color = '#000000', font = ('Arial', 30, 'bold'))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')

def create(check1, check2, check3, check4, check5, count, lenght):
    clear_all()

    chars = ''
    symbols = [digits, lowercase_letters, uppercase_letters, punctuation]
    count = 0

    for i in [check1, check2, check3, check4]:
        if i == 1:
            chars += symbols[count]
        count += 1

    if check5 == 1:
         for j in 'i, I, l, L, 1, !, o, O, 0':
            if j in chars:
                chars = chars.replace(j, '')

    print(chars)

    #for j in range (lenght):
    #        password += choice(chars)
    #    passwords.append(password)

    label = ctk.CTkLabel (master = app, text = choice(waitings), bg_color = '#ffcc66',
    text_color = '#000000', font = ('Arial', 30, 'bold'))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
    app.after (5000, result)

def check_input(check1, check2, check3, check4, check5, count, lenght):
    if count.isdigit() == False or lenght.isdigit() == False:
        messagebox.showinfo ('Ошибочка', 'Для ввода допускаются только циферки')
    elif int(count) < 1:
        messagebox.showinfo ('Ошибочка', 'Нужен хотя бы 1 пароль')
    elif int(lenght) < 5:
        messagebox.showinfo ('Ошибочка', 'Недостаточная длина пароля')
    elif int(count) > 10:
        messagebox.showinfo ('Ошибочка', 'Слишком много паролей')
    elif int(lenght) > 20:
        messagebox.showinfo ('Ошибочка', 'Слишком длинный пароль')
    else:
        create(check1, check2, check3, check4, check5, count, lenght)

def filters():
    clear_all()

    label = ctk.CTkLabel (master = app, text = 'Сколько паролей\n нужно сгенерировать?', bg_color = '#ffcc66',
    text_color = '#000000', font = ('Arial', 30))
    label.place(relx = 0.5, rely = 0.1, anchor = 'c')

    label = ctk.CTkLabel (master = app, text = '(Введите значение от 1 до 10)', bg_color = '#ffcc66',
    text_color = '#000000', height = 5, font = ('Arial', 15))
    label.place(relx = 0.5, rely = 0.16, anchor = 'c')

    label = ctk.CTkLabel (master = app, text = 'Необходимая длина пароля?', bg_color = '#ffcc66',
    text_color = '#000000', font = ('Arial', 30))
    label.place(relx = 0.5, rely = 0.3, anchor = 'c')

    label = ctk.CTkLabel (master = app, text = '(Введите значение от 5 до 20)', bg_color = '#ffcc66',
    text_color = '#000000', height = 5, font = ('Arial', 15))
    label.place(relx = 0.5, rely = 0.35, anchor = 'c')

    label = ctk.CTkLabel (master = app, text = 'Какие символы использовать?', bg_color = '#ffcc66',
    text_color = '#000000', font = ('Arial', 30))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    entry1 = ctk.CTkEntry (master = app, width = 100, height = 30, border_width = 0,  corner_radius = 40, justify = 'c',
    fg_color = '#ffffff', bg_color = '#ffcc66', text_color = '#000066', font = ('Arial', 20, 'bold'))
    entry1.place(relx = 0.5, rely = 0.2, anchor = 'c')

    entry2 = ctk.CTkEntry (master = app, width = 100, height = 30, border_width = 0,  corner_radius = 40, justify = 'c',
    fg_color = '#ffffff', bg_color = '#ffcc66', text_color = '#000066', font = ('Arial', 20, 'bold'))
    entry2.place(relx = 0.5, rely = 0.4, anchor = 'c')

    check1 = ctk.BooleanVar()
    check2 = ctk.BooleanVar()
    check3 = ctk.BooleanVar()
    check4 = ctk.BooleanVar()
    check5 = ctk.BooleanVar()

    box1 = ctk.CTkCheckBox (master = app, text = '1 2 3', bg_color = '#ffcc66', fg_color = '#000000', hover_color = '#ffffff',
    text_color = '#000000', border_color = '#000000', font = ('Arial', 30), variable = check1)
    box1.place(relx = 0.2, rely = 0.6, anchor = 'c')

    box2 = ctk.CTkCheckBox (master = app, text = 'a b c', bg_color = '#ffcc66', fg_color = '#000000', hover_color = '#ffffff',
    text_color = '#000000', border_color = '#000000', font = ('Arial', 30), variable = check2)
    box2.place(relx = 0.5, rely = 0.6, anchor = 'c')

    box3 = ctk.CTkCheckBox (master = app, text = 'A B C', bg_color = '#ffcc66', fg_color = '#000000', hover_color = '#ffffff',
    text_color = '#000000', border_color = '#000000', font = ('Arial', 30), variable = check3)
    box3.place(relx = 0.8, rely = 0.6, anchor = 'c')

    box4 = ctk.CTkCheckBox (master = app, text = '# % &', bg_color = '#ffcc66', fg_color = '#000000', hover_color = '#ffffff',
    text_color = '#000000', border_color = '#000000', font = ('Arial', 30), variable = check4)
    box4.place(relx = 0.35, rely = 0.7, anchor = 'c')

    box5 = ctk.CTkCheckBox (master = app, text = 'l i I', bg_color = '#ffcc66', fg_color = '#000000', hover_color = '#ffffff',
    text_color = '#000000', border_color = '#000000', font = ('Arial', 30), variable = check5)
    box5.place(relx = 0.75, rely = 0.7, anchor = 'c')

    button = ctk.CTkButton (master = app, width = 300, height = 30, corner_radius = 20, text = 'Дальше', text_color = '#000000',
    bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command=lambda: check_input(check1.get(), check2.get(), check3.get(), check4.get(), check5.get(), entry1.get(), entry2.get()))
    button.place(relx = 0.5, rely = 0.9, anchor = 'c')

    button = ctk.CTkButton (master = app, width = 100, height = 30, corner_radius = 20, text = 'Выбрать все', text_color = '#000000',
    bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command = lambda: select_all(box1, box2, box3, box4, box5))
    button.place(relx = 0.3, rely = 0.8, anchor = 'c')

    button = ctk.CTkButton (master = app, width = 100, height = 30, corner_radius = 20, text = 'Убрать все', text_color = '#000000',
    bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#996633', font= ('Arial', 20, 'bold'), command = lambda: deselect_all(box1, box2, box3, box4, box5))
    button.place(relx = 0.7, rely = 0.8, anchor = 'c')

label = ctk.CTkLabel (master = app, text = 'Приветствую тебя!', bg_color = '#ffcc66',
text_color = '#0000ff', font = ('Arial', 30, 'bold'))
label.place(relx = 0.5, rely = 0.1, anchor = 'c')

label = ctk.CTkLabel (master = app, height = 70, text = 'Это генератор паролей', corner_radius = 50, fg_color = '#990000', bg_color = '#ffcc66',
text_color = '#ffffff', font = ('Arial', 30, 'bold'))
label.place(relx = 0.5, rely = 0.25, anchor = 'c')

label = ctk.CTkLabel (master = app, text = 'Он поможет тебе\n надежно защитить\n твои аккаунты и данные', bg_color = '#ffcc66',
text_color = '#ff6600', font = ('Arial', 30, 'bold'))
label.place(relx = 0.5, rely = 0.45, anchor = 'c')

label = ctk.CTkLabel (master = app, height = 100, corner_radius = 50, fg_color = '#0066ff', text = 'И сделает это так\n как ты хочешь', bg_color = '#ffcc66',
text_color = '#ffff00', font = ('Arial', 30, 'bold'))
label.place(relx = 0.5, rely = 0.65, anchor = 'c')

button = ctk.CTkButton (master = app, width = 300, height = 70, corner_radius = 20, text = 'Отлично!', text_color = '#000066',
bg_color = '#ffcc66', fg_color = '#ffffff', hover_color = '#9966ff', font= ('Arial', 20, 'bold'), command = filters)
button.place(relx = 0.5, rely = 0.85, anchor = 'c')

app.mainloop()

