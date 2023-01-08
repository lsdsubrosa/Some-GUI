import tkinter as tk
from tkinter import ttk, messagebox

font_family = {
    1: 'Calibri',
    2: 'Courier',
    3: 'Arial',
    4: 'Times',
    5: 'Times New Roman',
    6: 'Verdana',
    7: 'Terminal',
    8: 'Modern',
    9: 'Roman',
    10: 'Malgun Gothic',
    11: 'Symbol',
    12: 'Helvetica',
    13: 'Bahnschrift'
}

font_size = {
    1: '10',
    2: '11',
    3: '12',
    4: '14',
    5: '16',
    6: '18'
}


def prog1():
    # Главное окно программы 1
    win_1 = tk.Tk()
    win_1.title('Вычислить Процент от')

    width = 350
    height = 400
    position_x = 700
    position_y = 300
    color_bg = 'burlywood'

    win_1['bg'] = color_bg
    win_1.geometry(f'{width}x{height}+{position_x}+{position_y}')

    win_1.maxsize(width, height)
    win_1.minsize(width, height)

    img = tk.PhotoImage(file='img/percent.png')
    win_1.iconphoto(False, img)

    # Ф-ции
    def find_res():
        number, percent = float(number_entry.get()), float(percent_entry.get())
        result = number * (percent / 100)
        show_res.delete(0, tk.END)
        show_res.insert(0, round(result, 2))

    def clear():
        number_entry.delete(0, tk.END)
        percent_entry.delete(0, tk.END)
        show_res.delete(0, tk.END)
        number_entry.insert(0, '0')
        percent_entry.insert(0, '0')

    def back():
        win_1.destroy()
        choose_prog()

    def close():
        win_1.destroy()

    # Инициализация переменных
    prog_name = tk.Label(text='Вычислить число\nзная процент', bg=color_bg,
                         font=(font_family[11], font_size[5], 'bold'))
    number = tk.Label(text='Число', bg=color_bg, font=(font_family[11], font_size[3], 'bold'))
    percent_num = tk.Label(text='Процент', bg=color_bg, font=(font_family[11], font_size[3], 'bold'))
    find_res = tk.Button(text='Вычислить', bg='beige', font=(font_family[6], font_size[3], 'bold italic'),
                         command=find_res)

    number_entry = tk.Entry()
    percent_entry = tk.Entry()
    number_entry.insert(0, '0')
    percent_entry.insert(0, '0')
    show_res = tk.Entry()

    clear_btn = tk.Button(text='Очистить поля ввода', bg='beige', font=(font_family[6], font_size[3], 'bold italic'),
                          command=clear)
    back_btn = tk.Button(text='Назад в меню', bg='beige', font=(font_family[6], font_size[3], 'bold italic'),
                         command=back)
    close_btn = tk.Button(text='Закрыть программу', bg='beige', font=(font_family[6], font_size[3], 'bold italic'),
                          command=close)

    # Расположение элементов
    prog_name.grid(row=0, column=0, padx=width * 0.22)

    number.grid(row=1, column=0, pady=(15, 0))
    number_entry.grid(row=2, column=0)
    percent_num.grid(row=3, column=0, pady=(15, 0))
    percent_entry.grid(row=4, column=0)

    find_res.grid(row=5, column=0, pady=(15, 0))
    show_res.grid(row=6, column=0, pady=(5, 0))

    clear_btn.grid(row=7, column=0, pady=(15, 0))
    back_btn.grid(row=8, column=0, pady=(15, 0))
    close_btn.grid(row=9, column=0)

    win_1.mainloop()


def prog2():
    # Главное окно программы 1
    win_1 = tk.Tk()
    win_1.title('Вычислить процент, зная число')

    width = 350
    height = 400
    position_x = 700
    position_y = 300
    color_bg = 'burlywood'

    win_1['bg'] = color_bg
    win_1.geometry(f'{width}x{height}+{position_x}+{position_y}')

    win_1.maxsize(width, height)
    win_1.minsize(width, height)

    img = tk.PhotoImage(file='img/question.png')
    win_1.iconphoto(False, img)

    # Ф-ции
    def find_res():
        num1, num2 = float(number_entry.get()), float(percent_entry.get())
        if num1 == 0:
            return messagebox.showinfo('ZeroDivisionError', 'Деление на 0 -_-')
        else:
            result = (100 * num2) / num1
            show_res.delete(0, tk.END)
            show_res.insert(0, f'{round(result, 2)}%')

    def clear():
        number_entry.delete(0, tk.END)
        percent_entry.delete(0, tk.END)
        show_res.delete(0, tk.END)
        number_entry.insert(0, '0')
        percent_entry.insert(0, '0')

    def back():
        win_1.destroy()
        choose_prog()

    def close():
        win_1.destroy()

    # Инициализация переменных
    prog_name = tk.Label(text='Вычислить процент\nзная число', bg=color_bg,
                         font=(font_family[11], font_size[5], 'bold'))
    number = tk.Label(text='Число', bg=color_bg, font=(font_family[11], font_size[3], 'bold'))
    percent_num = tk.Label(text='Процентное число', bg=color_bg, font=(font_family[11], font_size[3], 'bold'))
    find_res = tk.Button(text='Вычислить', bg='beige', font=(font_family[6], font_size[3], 'bold italic'),
                         command=find_res)

    number_entry = tk.Entry()
    percent_entry = tk.Entry()
    number_entry.insert(0, '0')
    percent_entry.insert(0, '0')
    show_res = tk.Entry()

    clear_btn = tk.Button(text='Очистить поля ввода', bg='beige', font=(font_family[6], font_size[3], 'bold italic'),
                          command=clear)
    back_btn = tk.Button(text='Назад в меню', bg='beige', font=(font_family[6], font_size[3], 'bold italic'),
                         command=back)
    close_btn = tk.Button(text='Закрыть программу', bg='beige', font=(font_family[6], font_size[3], 'bold italic'),
                          command=close)

    # Расположение элементов
    prog_name.grid(row=0, column=0, padx=width * 0.20)

    number.grid(row=1, column=0, pady=(15, 0))
    number_entry.grid(row=2, column=0)
    percent_num.grid(row=3, column=0, pady=(15, 0))
    percent_entry.grid(row=4, column=0)

    find_res.grid(row=5, column=0, pady=(15, 0))
    show_res.grid(row=6, column=0, pady=(5, 0))

    clear_btn.grid(row=7, column=0, pady=(15, 0))
    back_btn.grid(row=8, column=0, pady=(15, 0))
    close_btn.grid(row=9, column=0)

    win_1.mainloop()


def choose_prog():
    # Главное окно
    global win_chs
    win_chs = tk.Tk()
    win_chs.title('Выберете программу')

    width = 300
    height = 100
    position_x = 700
    position_y = 500
    color_bg = 'burlywood'

    win_chs['bg'] = color_bg
    win_chs.geometry(f'{width}x{height}+{position_x}+{position_y}')

    win_chs.maxsize(width, height)
    win_chs.minsize(width, height)

    img = tk.PhotoImage(file='img/play.png')
    win_chs.iconphoto(False, img)

    # Ф-ции
    def get_prog():
        name = combobox.get()
        if name == 'Вычислить число, зная процент':
            win_chs.destroy()
            prog1()
        elif name == 'Вычислить процент, зная число':
            win_chs.destroy()
            prog2()

    def close():
        win_chs.destroy()

    # Инициализация переменных
    prog_name = ('Вычислить число, зная процент',
                 'Вычислить процент, зная число')

    combobox = ttk.Combobox(win_chs, state="readonly", width=30, values=prog_name)
    combobox.current(0)
    choose_btn = tk.Button(win_chs, text='Выбрать', bg='beige', font=(font_family[6], font_size[3], 'bold italic'),
                           command=get_prog)
    close_btn = tk.Button(text='Закрыть программу', bg='beige', font=(font_family[6], font_size[3], 'bold italic'),
                          command=close)

    # Расположение элементов
    combobox.pack()
    choose_btn.pack(pady=(5, 0))
    close_btn.pack()

    win_chs.mainloop()


if __name__ == '__main__':
    choose_prog()
