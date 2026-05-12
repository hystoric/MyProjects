import customtkinter as ctk
from random import choice

class GreetingsPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = controller.main_color)
        self.controller = controller

        label_data = [('Приветствую!', '#ffcc66'), ('Это игра "Викторина"', '#ffffff'), ('Сыграем?', '#ffcc66')]

        for idx, (text, color) in enumerate (label_data):
            label = ctk.CTkLabel(self, text = text, font = ('Constantia', 27), text_color = color)
            label.place(relx = 0.5, rely = 0.3 + (0.15 * idx), anchor = 'c')

        button_data = [('Не сейчас', self.controller.to_end), ('Давай!', lambda: self.controller.switch_to('RulesPage'))]

        for idx, (text, command) in enumerate (button_data):
            button = ctk.CTkButton (self, height = 50, corner_radius = 50, text = text, fg_color = '#ffcc66',
            hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 20), command = command)
            button.place(relx = 0.35 + (idx * 0.3), rely = 0.8, anchor = 'c')

class RulesPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = controller.main_color)
        self.controller = controller

        label_data = [('Правила очень просты:', '#66ff33'), ('Я задам тебе несколько вопросов', '#ffffff'), ('на самые разные темы', '#ffcc66'),
('а тебе нужно выбрать правильный ответ', '#ffffff'), ('за каждый из которых', '#ffcc66'), ('тебе начисляется балл', '#ffffff'),
('По итогу: считаем баллы', '#ffcc66'), ('Начнём?', '#ffffff')]

        for idx, (text, color) in enumerate (label_data):
            label = ctk.CTkLabel(self, text = text, font = ('Constantia', 27), text_color = color)
            label.place(relx = 0.5, rely = 0.05 + (idx * 0.1), anchor = 'c')

        button_data = [('Не сейчас', self.controller.to_end), ('Погнали', self.controller.create_game)]

        for idx, (text, command) in enumerate (button_data):
            button = ctk.CTkButton (self, height = 50, corner_radius = 50, text = text, fg_color = '#ffcc66',
            hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 20), command = command)
            button.place(relx = 0.35 + (idx * 0.3), rely = 0.9, anchor = 'c')

class QuizPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = controller.main_color)
        self.controller = controller

        self.setup_data()
        self.setup_variables()
        self.setup_ui()

    def setup_data(self):
        self.right_comments = ['Верно!', 'Отлично!', 'Так держать!', 'Прямо в точку', 'Угадал!']
        self.wrong_comments = ['Мимо', 'Не верно', 'Не угадал', 'Не-а', 'Не то']
        self.questions = [

            {   'question': 'Какая река считается самой длинной в мире?',
                'options': ['А) Амазонка', 'Б) Нил', 'В) Миссисипи'],
                'answer': 0   },

            {   'question': 'Какой фильм получил\n самую первую премию «Оскар»\n в номинации «Лучший фильм» в 1929 году?',
                'options': ['А) «Унесенные ветром»', 'Б) «Крылья»',  'В) «Огни большого города»'],
                'answer': 1   },

            {   'question': 'Какой химический элемент обозначается\n символом Fe в таблице Менделеева?',
                'options': ['А) Фтор', 'Б) Свинец', 'В) Железо'],
                'answer': 2     },

            {   'question': 'В каком году произошло\n падение Берлинской стены?',
                'options': ['А) 1987', 'Б) 1989', 'В) 1991'],
                'answer': 1   },

            {   'question': 'Какое животное способно\n развивать самую высокую\n скорость бега на короткие дистанции?',
                'options': ['А) Гепард', 'Б) Антилопа гну', 'В) Лев'],
                'answer': 0   }

                                           ]

    def setup_variables(self):
        self.index = 0
        self.boxes = []
        self.user_answers = []

    def setup_ui(self):
        self.question_frame = ctk.CTkFrame(self, fg_color = 'transparent')
        self.question_frame.place(relx = 0, rely = 0.2, relwidth = 1.0, relheight = 0.3)

        self.box_frame = ctk.CTkFrame(self, fg_color = 'transparent')
        self.box_frame.place(relx = 0, rely = 0.5, relwidth = 1.0, relheight = 0.3)

        self.x = ctk.IntVar(value = 0)

        for i in range (3):
            box = ctk.CTkRadioButton (self.box_frame, font = ('Calibri', 23), variable = self.x, value = i, text_color = '#FFFFFF', fg_color = '#FFFFFF',
            border_color = '#FFFFFF', hover_color = '#ffcc66', text_color_disabled = '#FFFFFF', border_width_checked = 5, border_width_unchecked = 1)
            box.pack(pady = 10, anchor='c')
            self.boxes.append(box)

        self.question_label = ctk.CTkLabel (self.question_frame, text = None,
        font = ('Constantia', 27), text_color = '#ffcc66')
        self.question_label.pack(pady = 10, fill = 'y', expand = True, anchor='c')

        self.step_label = ctk.CTkLabel (self, text = None,
        font = ('Constantia', 27), text_color = '#ffffff')
        self.step_label.place(relx = 0.25, rely = 0.1, anchor = 'c')

        self.score_label = ctk.CTkLabel (self, text = None,
        font = ('Constantia', 27), text_color = '#ffcc66')
        self.score_label.place(relx = 0.7, rely = 0.1, anchor = 'c')

        self.comment_label = ctk.CTkLabel (self, text = '',
        font = ('Constantia', 27), text_color = '#ffcc66')
        self.comment_label.place(relx = 0.5, rely = 0.9, anchor = 'c')

        self.back_button = ctk.CTkButton (self, height = 50, corner_radius = 50, text = 'Назад', fg_color = '#ffcc66',
        hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 20), command = self.go_back)

        self.go_button = ctk.CTkButton (self, height = 50, corner_radius = 50, text = 'Далее', fg_color = '#ffcc66',
        hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 20), command = self.give_feedback)

    def give_feedback(self):

        self.user_answers.append(self.x.get())

        for i in self.boxes:
            i.configure(state = 'disabled')
            if i.cget('value') == self.q['answer']:
                i.configure(border_color = '#ffcc66', fg_color = '#ffcc66', border_width_unchecked = 5)
            elif i.cget('value') != self.q['answer'] and i.cget('value') == self.x.get():
                i.configure(border_color = 'red', fg_color = 'red', border_width_unchecked = 5)

        self.back_button.place_forget()
        self.go_button.place_forget()

        if self.x.get() == self.q['answer']:
            self.controller.score += 1
            self.score_label.configure(text = f'Твои баллы: {self.controller.score}')
            self.comment_label.configure(text = f'{choice(self.right_comments)}\nПравильный ответ: {self.r}')
        else:
            self.comment_label.configure(text = f'{choice(self.wrong_comments)}\nПравильный ответ: {self.r}')

        self.after(3000, self.next_question)

    def update_data(self):
        self.index = 0
        self.user_answers = []
        self.refresh_page()

    def go_forward(self):
        self.index += 1
        self.refresh_page()

    def go_back(self):
        if self.index == 0:
            self.controller.switch_to('RulesPage')
        elif self.index > 0:
            self.index -= 1
            self.refresh_page()

    def next_question(self):
        self.index += 1
        if self.index < len(self.questions):
            self.refresh_page()
        else:
            self.controller.switch_to('FinalPage')

    def refresh_page(self):
        self.q = self.questions[self.index]
        self.r = self.q['options'][self.q['answer']]
        is_answered = self.index < len(self.user_answers)

        current_value = self.user_answers[self.index] if is_answered else 2
        self.x.set(current_value)

        new_command = self.go_forward if self.index < len(self.user_answers) else self.give_feedback
        self.go_button.configure(command = new_command)

        for idx, btn in enumerate(self.boxes):
            if is_answered and idx == self.q['answer']:
                color, width = '#ffcc66', 5
            elif is_answered and idx == current_value:
                color, width = 'red', 5
            else:
                color, width = '#ffffff', 1

            btn.configure(state='normal' if not is_answered else 'disabled', text = self.q['options'][idx], fg_color = color,
            border_color = color, border_width_unchecked = width)

        self.score_label.configure(text = f'Твои баллы: {self.controller.score}')
        self.step_label.configure(text = f'Вопрос номер: {self.index + 1}')
        self.question_label.configure(text = self.q['question'])
        self.comment_label.configure(text = '')
        self.back_button.place(relx = 0.35, rely = 0.9, anchor = 'c')
        self.go_button.place(relx = 0.65, rely = 0.9, anchor = 'c')

class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = controller.main_color)
        self.controller = controller

        self.repeating = ['Генерирую цикл...', 'Создаю всё с нуля...', 'Очищаю всё лишнее...', 'Отлично! Начинаем...', 'Дай мне пару секундочек...']
        self.farewell = ['До новых встреч!', 'Заглядывай ко мне ещё!', 'Был рад поработать с тобой!', 'Ты это, заходи, если что...', 'Надеюсь, еще увидимся!']

        self.label = ctk.CTkLabel (self, text = '',
        font = ('Constantia', 27), text_color = '#ffcc66')
        self.label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    def set_text(self, mode):
        if mode == 'loading':
            self.label.configure(text=choice(self.repeating))
        else:
            self.label.configure(text=choice(self.farewell))

class FinalPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = controller.main_color)
        self.controller = controller

        self.label = ctk.CTkLabel (self, text = '',
        font = ('Constantia', 27), text_color = '#ffcc66')
        self.label.place(relx = 0.5, rely = 0.35, anchor = 'c')

        label = ctk.CTkLabel (self, text = 'Хочешь сыграть снова?',
        font = ('Constantia', 27), text_color = '#ffcc66')
        label.place(relx = 0.5, rely = 0.5, anchor = 'c')

        self.back_button = ctk.CTkButton (self, height = 50, corner_radius = 50, text = 'Не сейчас', fg_color = '#ffcc66',
        hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 20), command = self.controller.to_end)
        self.back_button.place(relx = 0.35, rely = 0.75, anchor = 'c')

        self.go_button = ctk.CTkButton (self, height = 50, corner_radius = 50, text = 'Давай!', fg_color = '#ffcc66',
        hover_color = '#FFFFFF', text_color = '#000000', font= ('Constantia', 20), command = self.restart_game)
        self.go_button.place(relx = 0.65, rely = 0.75, anchor = 'c')

    def restart_game(self):
        self.controller.pages["QuizPage"].user_answers = []
        self.controller.create_game()

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Моя Викторина')
        self.geometry ('600x500+800+450')
        self.resizable (False, False)
        self.attributes ('-alpha', 0.9)

        self.main = ctk.CTkFrame(self)
        self.main.pack(fill = 'both', expand = True)

        self.main_color = '#0d0d0d'
        self.score = 0
        self.pages = {}
        self.current_frame = None

        for F in (GreetingsPage, RulesPage, QuizPage, MessagePage, FinalPage):
            page_name = F.__name__
            self.pages[page_name] = F(master = self.main, controller=self)

        self.switch_to("GreetingsPage")

    def switch_to(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.pages[page_name]
        if page_name == "FinalPage":
            self.current_frame.label.configure(text=f'Ты набрал: {self.score} баллов из 5')
        self.current_frame.pack(fill="both", expand=True)

    def to_end(self):
        self.pages["MessagePage"].set_text('farewell')
        self.switch_to("MessagePage")
        self.after(3000, self.destroy)

    def create_game(self):
        quiz = self.pages["QuizPage"]
        if not quiz.user_answers:
            self.pages["MessagePage"].set_text('loading')
            self.switch_to("MessagePage")
            self.score = 0
            self.pages["QuizPage"].update_data()
            self.after(3000, lambda: self.switch_to("QuizPage"))
        else:
            self.switch_to("QuizPage")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()