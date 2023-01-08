import tkinter as tk
from tkinter import ttk, messagebox

# fonts, colors
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
    10: '10',
    11: '11',
    12: '12',
    14: '14',
    16: '16',
    18: '18'
}

color = {
    1: '#A0D2EB',
    2: '#E5EAF5',
    3: '#D0BDF4',
    4: '#8458B3',
    5: '#494D5F',
    6: '#9DF9EF'
}

bg_clr = color[4]
btn_clr = color[1]
fnt_clr_b = color[5]
fnt_clr_w = 'white'
back_clr = color[2]


def message_error():
    return messagebox.showinfo('Ошибка', 'Введите значения -_-')


def close(win_name):
    win_name.destroy()


def close_buttton(win_name):
    return tk.Button(text='Закрыть', bg=btn_clr, fg=fnt_clr_b, activebackground=back_clr,
                     font=(font_family[6], font_size[12], 'bold italic'), command=lambda: close(win_name))


def back(win_name):
    win_name.destroy()
    main_menu()


def back_to_menu_button(win_name):
    return tk.Button(text='Вернуться', bg=btn_clr, fg=fnt_clr_b, activebackground=back_clr,
                     font=(font_family[6], font_size[12], 'bold italic'), command=lambda: back(win_name))


def simple_label(label_name, fontsize, fontstyle):
    return tk.Label(text=label_name, bg=bg_clr, fg=fnt_clr_w, font=(font_family[11], fontsize, fontstyle))


def simple_entry():
    return tk.Entry(width=5)


def btn_pass():
    pass


def simple_btn(win_name, btn_text, command):
    return tk.Button(win_name, text=btn_text, bg=btn_clr, fg=fnt_clr_b, activebackground=back_clr,
                     font=(font_family[6], font_size[12], 'bold italic'), command=command)


def fuel_calc():
    # prog menu
    win_fuel = tk.Tk()
    win_fuel.title('Рассчитать топливо на гонку')
    win_fuel['bg'] = bg_clr

    width = 230
    height = 475
    position_x = 700
    position_y = 300

    win_fuel.geometry(f'{width}x{height}+{position_x}+{position_y}')
    win_fuel.maxsize(width, height)
    win_fuel.minsize(width, height)

    # Func
    def clear_entry():
        entry_names = [res_show, race_lenght, min_v, sec, msec, fuel_cons]
        for name in entry_names:
            name.delete(0, tk.END)

    def calc_fuel():
        if race_lenght.get() == '' or min_v.get() == '' or sec.get() == '' or msec.get() == '':
            message_error()
        else:
            r_v = int(race_lenght.get()) * 60
            min_value = int(min_v.get()) * 60
            sec_value = int(sec.get())
            msec_value = int(msec.get()) / 1000
            fuel_cons_value = float(fuel_cons.get())

            laps = r_v / (min_value + sec_value + msec_value)
            result = laps * fuel_cons_value
            res_show.delete(0, tk.END)
            res_show.insert(0, f'{round(result)} л')

    # Labels initialization & position
    simple_label('Длительность гонки', font_size[14], 'bold italic').grid(row=0, column=0, columnspan=2, padx=5)
    simple_label('Лучшее время круга', font_size[14], 'bold italic').grid(row=2, column=0, columnspan=2)
    simple_label('Минуты', font_size[12], 'bold').grid(row=3, column=0, columnspan=2)
    simple_label('Секунды', font_size[12], 'bold').grid(row=5, column=0, columnspan=2)
    simple_label('Милисек', font_size[12], 'bold').grid(row=7, column=0, columnspan=2)
    simple_label('Расход топлива\nЛитры.Мл', font_size[14], 'bold italic').grid(row=9, column=0, columnspan=2)

    # Entries initialization & position
    race_lenght = simple_entry()
    min_v, sec, msec, fuel_cons = simple_entry(), simple_entry(), simple_entry(), simple_entry()

    race_lenght.grid(row=1, column=0, pady=(0, 10), columnspan=2)
    min_v.grid(row=4, column=0, columnspan=2)
    sec.grid(row=6, column=0, columnspan=2)
    msec.grid(row=8, column=0, columnspan=2, pady=(0, 10))
    fuel_cons.grid(row=10, column=0, columnspan=2, pady=(0, 15))

    simple_btn(win_fuel, 'Рассчитать', calc_fuel).grid(row=11, column=0, columnspan=2)
    close_btn = close_buttton(win_fuel)
    back_btn = back_to_menu_button(win_fuel)
    res_show = simple_entry()
    res_show.grid(row=12, column=0, pady=(5, 10), columnspan=2)
    simple_btn(win_fuel, 'Очистить ввод', clear_entry).grid(row=13, column=0, columnspan=2, pady=10)
    back_btn.grid(row=14, column=0, padx=5)
    close_btn.grid(row=14, column=1)

    win_fuel.mainloop()


def psi_calc():
    # prog menu
    win_psi = tk.Tk()
    win_psi.title('Рассчитать давление')
    win_psi['bg'] = bg_clr

    width = 220
    height = 390
    position_x = 700
    position_y = 300

    win_psi.geometry(f'{width}x{height}+{position_x}+{position_y}')
    win_psi.maxsize(width, height)
    win_psi.minsize(width, height)

    # Func
    def calc_psi():
        psi, lf, rf, lr, rr = psi_entry.get(), lf_entry.get(), rf_entry.get(), lr_entry.get(), rr_entry.get()
        tyres_names = [lf, rf, lr, rr]
        tyres_names2 = [lf_show, rf_show, lr_show, rr_show]

        if psi == '' or lf == '' or rf == '' or lr == '' or rr == '':
            message_error()
        else:
            for i in range(len(tyres_names2)):
                for j in range(i, i + 1):
                    tyres_names2[i].delete(0, tk.END)
                    psi_add = round(float(psi) - float(tyres_names[j]), 1)
                    if psi_add > 0:
                        tyres_names2[i].insert(0, f'+{psi_add}')
                    else:
                        tyres_names2[i].insert(0, f'{psi_add}')

    def clear():
        tyres_names = [psi_entry, lf_entry, rf_entry, lr_entry, rr_entry, lf_show, rf_show, lr_show, rr_show, ]
        for tyre in tyres_names:
            tyre.delete(0, tk.END)

    # Labels, Entries initialization & position
    simple_label('Нужное давление', font_size[14], 'bold italic').grid(row=0, column=0, columnspan=2)
    psi_entry = simple_entry()
    psi_entry.grid(row=1, column=0, columnspan=2)

    simple_label('LF', font_size[12], 'bold').grid(row=2, column=0)
    lf_entry = simple_entry()
    lf_entry.grid(row=3, column=0)

    simple_label('RF', font_size[12], 'bold').grid(row=2, column=1)
    rf_entry = simple_entry()
    rf_entry.grid(row=3, column=1)

    simple_label('LR', font_size[12], 'bold').grid(row=4, column=0, pady=(5, 0))
    lr_entry = simple_entry()
    lr_entry.grid(row=5, column=0)

    simple_label('RR', font_size[12], 'bold').grid(row=4, column=1, pady=(5, 0))
    rr_entry = simple_entry()
    rr_entry.grid(row=5, column=1)

    # show
    simple_btn(win_psi, 'Рассчитать', calc_psi).grid(row=6, column=0, columnspan=2, pady=(15, 10))

    simple_label('LF', font_size[12], 'bold').grid(row=7, column=0)
    lf_show = simple_entry()
    lf_show.grid(row=8, column=0)

    simple_label('RF', font_size[12], 'bold').grid(row=7, column=1)
    rf_show = simple_entry()
    rf_show.grid(row=8, column=1)

    simple_label('LR', font_size[12], 'bold').grid(row=9, column=0)
    lr_show = simple_entry()
    lr_show.grid(row=10, column=0, pady=(0, 5))

    simple_label('RR', font_size[12], 'bold').grid(row=9, column=1)
    rr_show = simple_entry()
    rr_show.grid(row=10, column=1, pady=(0, 5))

    # Buttons initialization & position
    simple_btn(win_psi, 'Очистить ввод', clear).grid(row=11, column=0, columnspan=2, pady=10)

    close_btn = close_buttton(win_psi)
    back_btn = back_to_menu_button(win_psi)
    back_btn.grid(row=12, column=0, padx=5)
    close_btn.grid(row=12, column=1)


def main_menu():
    # main menu
    win_main = tk.Tk()
    win_main.title('Выберите программу')
    win_main['bg'] = bg_clr

    width = 300
    height = 100
    position_x = 700
    position_y = 500
    win_main.geometry(f'{width}x{height}+{position_x}+{position_y}')
    win_main.maxsize(width, height)
    win_main.minsize(width, height)

    icon = tk.PhotoImage(file='img/play.png')
    win_main.iconphoto(False, icon)

    # Func
    def get_prog():
        if combobox.get() == 'Рассчитать топливо':
            win_main.destroy()
            fuel_calc()
        elif combobox.get() == 'Рассчитать давление':
            win_main.destroy()
            psi_calc()

    # Variable initialization
    prog_name = ('Рассчитать топливо',
                 'Рассчитать давление')

    combobox = ttk.Combobox(win_main, state='readonly', width=30, values=prog_name)
    combobox.current(0)

    choose_btn = simple_btn(win_main, 'Выбрать', get_prog)
    close_btn = close_buttton(win_main)

    # element position
    combobox.pack()
    choose_btn.pack(pady=(5, 5))
    close_btn.pack()

    win_main.mainloop()


if __name__ == '__main__':
    main_menu()
