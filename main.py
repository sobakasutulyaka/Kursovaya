import numpy
import psycopg2
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

bd = psycopg2.connect(
    database="AvtoRemontBase",
    user="postgres",
    password="1223",
)

def hiszapr(filtr,vvod):
    cur = bd.cursor()
    if filtr == "название детали":
        provfiltr = "SELECT * from historyzaprosi where name = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "совместимостимое авто":
        provfiltr = "SELECT * from historyzaprosi where sovmest = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "дата":
        provfiltr = "SELECT * from historyzaprosi where data = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "нет":
        cur.execute("SELECT * from historyzaprosi")

    rows = cur.fetchall()
    if rows == []:
        messagebox.showinfo("ошибка", "Записей с этим фильтром не обнаружено")

    else:
        vis, dl = numpy.shape(rows)
        ws = Tk()
        ws.title('История запросов')
        ws.geometry('1000x500')

        otchet_frame = Frame(ws)
        otchet_frame.pack()

        my_otchet = ttk.Treeview(otchet_frame)

        my_otchet['columns'] = (
            'id', 'name', 'price', 'kolvo', 'sovmest', 'data', 'vipoln', 'detid', 'remontid')

        my_otchet.column("#0", width=0, stretch=NO)
        my_otchet.column("id", anchor=CENTER, width=50)
        my_otchet.column("name", anchor=CENTER, width=180)
        my_otchet.column("price", anchor=CENTER, width=120)
        my_otchet.column("kolvo", anchor=CENTER, width=50)
        my_otchet.column("sovmest", anchor=CENTER, width=180)
        my_otchet.column("data", anchor=CENTER, width=180)
        my_otchet.column("vipoln", anchor=CENTER, width=80)
        my_otchet.column("detid", anchor=CENTER, width=70)
        my_otchet.column("remontid", anchor=CENTER, width=70)

        my_otchet.heading("#0", text="", anchor=CENTER)
        my_otchet.heading("id", text="id", anchor=CENTER)
        my_otchet.heading("name", text="Название", anchor=CENTER)
        my_otchet.heading("price", text="Цена", anchor=CENTER)
        my_otchet.heading("kolvo", text="Кол-во", anchor=CENTER)
        my_otchet.heading("sovmest", text="Совместимость", anchor=CENTER)
        my_otchet.heading("data", text="Дата запроса", anchor=CENTER)
        my_otchet.heading("vipoln", text="Выполнение", anchor=CENTER)
        my_otchet.heading("detid", text="id детали", anchor=CENTER)
        my_otchet.heading("remontid", text="id ремонта", anchor=CENTER)

        for i in range(vis):
            print(i)
            print(rows[0][0], rows[0][1], rows[0][2])
            my_otchet.insert(parent='', index='end', text='', values=(
                rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6], rows[i][7],
                rows[i][8]))

        my_otchet.pack()

        Button(ws, text="Закрыть", width=15, height=1, command=lambda: ws.destroy()).pack()

        ws.mainloop()


def filtrzapr():
    windob=Tk()
    windob.geometry('500x300')
    windob.title("Выберите фильтр")
    Label(windob, text="Уточните фильтр").grid(column=2, row=2)
    vvodfiltr = StringVar()
    Entry(windob, relief=RAISED, width=25, borderwidth=2, textvariable=vvodfiltr).grid(column=2, row=3)

    vib = ['название детали', 'дата', 'совместимое авто','нет']
    filtr = ttk.Combobox(windob, values=vib)
    filtr.set("фильтр")
    filtr.grid(row=1, column=2)

    otchhiskn = Button(windob, text="Открыть историю запросов",
                       command=lambda: hiszapr(filtr.get(), vvodfiltr.get()))
    otchhiskn.grid(row=5, column=2)
    Button(windob, text="Закрыть", command=lambda: windob.destroy()).grid(column=2,row=7)
    windob.mainloop()

def invent(filtr, vvod):
    cur = bd.cursor()
    if filtr == "название":
        provfiltr = "SELECT * from sklad where name = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "совместимость":
        provfiltr = "SELECT * from sklad where sovmest = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "производитель":
        provfiltr = "SELECT * from sklad where proizv = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "наличие":
        cur.execute("SELECT * from sklad where kolvo > 0")

    elif filtr == "нет":
        cur.execute("SELECT * from sklad")

    rows = cur.fetchall()
    if rows == []:
        messagebox.showinfo("ошибка", "Записей с этим фильтром не обнаружено")

    else:

        vis, dl = numpy.shape(rows)
        ws = Tk()
        ws.title('Инвентаризация')
        ws.geometry('1170x500')

        otchet_frame = Frame(ws)
        otchet_frame.pack()

        my_otchet = ttk.Treeview(otchet_frame)

        my_otchet['columns'] = (
            'id', 'name', 'proizv', 'kolvo', 'price', 'sovmest', 'dtime', 'vazn')

        my_otchet.column("#0", width=0, stretch=NO)
        my_otchet.column("id", anchor=CENTER, width=50)
        my_otchet.column("name", anchor=CENTER, width=180)
        my_otchet.column("proizv", anchor=CENTER, width=180)
        my_otchet.column("kolvo", anchor=CENTER, width=50)
        my_otchet.column("price", anchor=CENTER, width=120)
        my_otchet.column("sovmest", anchor=CENTER, width=180)
        my_otchet.column("dtime", anchor=CENTER, width=80)
        my_otchet.column("vazn", anchor=CENTER, width=70)

        my_otchet.heading("#0", text="", anchor=CENTER)
        my_otchet.heading("id", text="id", anchor=CENTER)
        my_otchet.heading("name", text="Название", anchor=CENTER)
        my_otchet.heading("proizv", text="производитель", anchor=CENTER)
        my_otchet.heading("kolvo", text="Кол-во", anchor=CENTER)
        my_otchet.heading("price", text="Цена", anchor=CENTER)
        my_otchet.heading("sovmest", text="Совместимость", anchor=CENTER)
        my_otchet.heading("dtime", text="Время доставки", anchor=CENTER)
        my_otchet.heading("vazn", text="Важность", anchor=CENTER)


        for i in range(vis):
            my_otchet.insert(parent='', index='end', text='', values=(
                rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6], rows[i][7]))

        my_otchet.pack()
        Button(ws, text="Закрыть", width=15, height=1, command=lambda: ws.destroy()).pack()

        my_otchet.pack()

        ws.mainloop()

def filtrinvent():
    winfil = Tk()
    winfil.geometry('300x200')
    winfil.title("Инвентаризация")
    fil = ["название", "совместимость", "наличие", "производитель", "нет"]
    filtr = ttk.Combobox(winfil, values=fil)
    filtr.set("Выберите фильтр")
    filtr.grid(row=1, column=1)
    vvodverh = Label(winfil, text="Введите значение фильтра")
    vvodverh.grid(row=2, column=1)
    vvodfiltr = Entry(winfil)
    vvodfiltr.grid(row=3, column=1)
    otchhiskn = Button(winfil, text="Открыть отчёт об инвентаризации", command=lambda: invent(filtr.get(), vvodfiltr.get()))
    otchhiskn.grid(row=5, column=1)
    Button(winfil, text="Закрыть", command=lambda: winfil.destroy())
    winfil.mainloop()

def dobskl2(nazv,proizv,sovm,price,dtime,vazn):
    if len(nazv) != 0:
        if len(proizv) != 0:
            if len(sovm) != 0:

                        if price.isdigit() == True:
                            if dtime.isdigit() == True:
                                if len(vazn) != 0:

                                    strok = (nazv, proizv, sovm, price, dtime, vazn)
                                    cur.execute(f"INSERT INTO sklad (name,proizv,sovmest, price,dtime,vazn) VALUES {strok}")
                                    bd.commit()
                                    messagebox.showinfo("Успех", "Запись успешно добавлена!")

                                else:
                                    messagebox.showinfo("Ошибка", "Поле 'важность' должно быть заполнено")

                            else:
                                messagebox.showinfo("ошибка", "Поле 'дата доставки' заполнено некорректно")
                        else:
                            messagebox.showinfo("ошибка", "Поле 'цена' заполнено некорректно")

            else:
                messagebox.showinfo("ошибка", "Поле 'совместимость' должно быть заполнено")
        else:
            messagebox.showinfo("ошибка", "Поле 'производитель' должно быть заполнено")
    else:
        messagebox.showinfo("ошибка", "Поле 'название' должно быть заполнено")

def dobskl():
    windob = Tk()
    windob.geometry('620x450')
    windob.title("Добавление новой позиции на склад")

    Label(windob, text="Введите название").grid(column=1, row=1)
    nazv = StringVar()
    Entry(windob, relief=RAISED, width=25, borderwidth=2, textvariable=nazv).grid(column=1, row=2)

    Label(windob, text="Введите производителя").grid(row=4, column=1)
    proizv = StringVar()
    Entry(windob, relief=RAISED, width=25, borderwidth=2, textvariable=proizv).grid(column=1, row=5)

    Label(windob, text="Выберите совместимое авто").grid(column=3, row=1)
    cur = bd.cursor()
    cur.execute("SELECT model from autopark")
    vib = cur.fetchall()
    sovm = ttk.Combobox(windob, values=vib)
    sovm.set("модель")
    sovm.grid(row=2, column=3)

    Label(windob, text="Цена").grid(row=4, column=3)
    price = StringVar()
    Entry(windob, relief=RAISED, width=25, borderwidth=2, textvariable=price).grid(column=3, row=5)

    Label(windob, text="время доставки").grid(row=1, column=5)
    dtime = StringVar()
    Entry(windob, relief=RAISED, width=25, borderwidth=2, textvariable=dtime).grid(column=5, row=2)

    Label(windob, text="Важность позиции (да/нет)").grid(column=5, row=4)

    vib2 = ['да','нет']
    vazn = ttk.Combobox(windob, values=vib2)
    vazn.set("нет")
    vazn.grid(row=5, column=5)

    dobav = Button(windob, text="Добавить",
                   command=lambda: dobskl2(nazv.get(), proizv.get(), sovm.get(), price.get(), dtime.get(),
                                             vazn.get()))
    dobav.grid(column=3, row=7)

    zakr = Button(windob, text="Закрыть", command=lambda: windob.destroy())
    zakr.grid(column=5, row=7)

    windob.mainloop()


def hiszak(filtr,vvod):
    cur = bd.cursor()
    if filtr == "название детали":
        provfiltr = "SELECT * from historyzakupok where namedet = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "совместимость":
        provfiltr = "SELECT * from historyzakupok where sovmest = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "статус":
        provfiltr = "SELECT * from historyzakupok where zipoln = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "дата":
        provfiltr = "SELECT * from historyzakupok where zakdata = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "нет":
        cur.execute("SELECT * from historyzakupok")

    rows = cur.fetchall()
    if rows == []:
        messagebox.showinfo("ошибка", "Записей с этим фильтром не обнаружено")

    else:

        vis, dl = numpy.shape(rows)
        ws = Tk()
        ws.title('История закупок')
        ws.geometry('1170x500')

        otchet_frame = Frame(ws)
        otchet_frame.pack()

        my_otchet = ttk.Treeview(otchet_frame)

        my_otchet['columns'] = (
            'id', 'name', 'kolvo', 'price', 'sovmest', 'data', 'vipoln', 'detid')

        my_otchet.column("#0", width=0, stretch=NO)
        my_otchet.column("id", anchor=CENTER, width=50)
        my_otchet.column("name", anchor=CENTER, width=180)
        my_otchet.column("kolvo", anchor=CENTER, width=50)
        my_otchet.column("price", anchor=CENTER, width=120)
        my_otchet.column("sovmest", anchor=CENTER, width=180)
        my_otchet.column("data", anchor=CENTER, width=180)
        my_otchet.column("vipoln", anchor=CENTER, width=80)
        my_otchet.column("detid", anchor=CENTER, width=70)

        my_otchet.heading("#0", text="", anchor=CENTER)
        my_otchet.heading("id", text="id", anchor=CENTER)
        my_otchet.heading("name", text="Название", anchor=CENTER)
        my_otchet.heading("kolvo", text="Кол-во", anchor=CENTER)
        my_otchet.heading("price", text="Цена", anchor=CENTER)
        my_otchet.heading("sovmest", text="Совместимость", anchor=CENTER)
        my_otchet.heading("data", text="Дата запроса", anchor=CENTER)
        my_otchet.heading("vipoln", text="Выполнение", anchor=CENTER)
        my_otchet.heading("detid", text="id детали", anchor=CENTER)

        for i in range(vis):
            my_otchet.insert(parent='', index='end', text='', values=(
                rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6], rows[i][7]))

        my_otchet.pack()
        Button(ws, text="Закрыть", width=15, height=1, command=lambda: ws.destroy()).pack()

        my_otchet.pack()

        ws.mainloop()

def filhiszak():
    winfil = Tk()
    winfil.geometry('300x200')
    winfil.title("Отчёт о истории закупок")
    fil = ["название детали", "совместимость", "статус", "дата", "нет"]
    filtr = ttk.Combobox(winfil, values=fil)
    filtr.set("Выберите фильтр")
    filtr.grid(row=1, column=1)
    vvodverh = Label(winfil, text="Введите значение фильтра")
    vvodverh.grid(row=2, column=1)
    vvodfiltr = Entry(winfil)
    vvodfiltr.grid(row=3, column=1)
    otchhiskn = Button(winfil, text="Открыть историю", command=lambda: hiszak(filtr.get(), vvodfiltr.get()))
    otchhiskn.grid(row=5, column=1)
    winfil.mainloop()

def prinskl2(prov,spisid):

    if prov == 0:
        cur = bd.cursor()
        provlog2 = "UPDATE historyzakupok SET vipoln = 'выполнено' where zakupid = %s"
        cur.execute(provlog2, (spisid,))
        bd.commit()
        messagebox.showinfo("Успешно", "Груз успешно принят!")
    else:
        cur = bd.cursor()
        cur.execute("UPDATE historyzakupok SET vipoln = 'выполнено' where vipoln = 'готово к приёму'")
        bd.commit()
        messagebox.showinfo("Успешно", "Партия груза успешно принята!")

def prinskl():
    winzakr = Tk()
    winzakr.geometry('700x300')
    winzakr.title("Приём поставки")
    Label(winzakr, text="Выберите id детали, которую хотите принять").grid(column=1, row=1)
    Label(winzakr, text="либо нажмите 'принять всё' чтобы принять всю поставку").grid(column=3, row=1)

    cur = bd.cursor()
    cur.execute("SELECT historyzakupok.zakupid from historyzakupok where vipoln = 'готово к приёму'")
    rows = cur.fetchall()
    rabots = ttk.Combobox(winzakr, values=rows)
    rabots.set("id")
    rabots.grid(row=3, column=1)

    Button(winzakr, text="Принять", command=lambda: prinskl2(0, rabots.get())).grid(column=1, row=4)
    Button(winzakr, text="Принять всё", command=lambda: prinskl2(1, 0)).grid(column=3, row=3)
    Button(winzakr, text="Закрыть", command=lambda: winzakr.destroy()).grid(column=3, row=4)
def zavoz():
    cur=bd.cursor()
    cur.execute("UPDATE historyzakupok set vipoln='готово к приёму' where vipoln = 'заказано'")
    bd.commit()
    messagebox.showinfo("Успешно!", "Доставка принята и может быть обработана в меню 'закупки'")

def zakup():
    cur = bd.cursor()
    cur.execute("SELECT * from historyzakupok where vipoln <> 'выполнено'")
    rows = cur.fetchall()
    if rows == []:
        messagebox.showinfo("ошибка", "Активных закупок не обнаружено")

    else:
        print(rows)
        vis, dl = numpy.shape(rows)
        ws = Tk()
        ws.title('Активные закупки')
        ws.geometry('1000x500')

        otchet_frame = Frame(ws)
        otchet_frame.pack()

        my_otchet = ttk.Treeview(otchet_frame)

        my_otchet['columns'] = (
            'id', 'name', 'kolvo', 'price', 'sovmest', 'data', 'vipoln', 'detid')

        my_otchet.column("#0", width=0, stretch=NO)
        my_otchet.column("id", anchor=CENTER, width=50)
        my_otchet.column("name", anchor=CENTER, width=180)
        my_otchet.column("kolvo", anchor=CENTER, width=50)
        my_otchet.column("price", anchor=CENTER, width=120)
        my_otchet.column("sovmest", anchor=CENTER, width=180)
        my_otchet.column("data", anchor=CENTER, width=180)
        my_otchet.column("vipoln", anchor=CENTER, width=80)
        my_otchet.column("detid", anchor=CENTER, width=70)


        my_otchet.heading("#0", text="", anchor=CENTER)
        my_otchet.heading("id", text="id", anchor=CENTER)
        my_otchet.heading("name", text="Название", anchor=CENTER)
        my_otchet.heading("kolvo", text="Кол-во", anchor=CENTER)
        my_otchet.heading("price", text="Цена", anchor=CENTER)
        my_otchet.heading("sovmest", text="Совместимость", anchor=CENTER)
        my_otchet.heading("data", text="Дата запроса", anchor=CENTER)
        my_otchet.heading("vipoln", text="Выполнение", anchor=CENTER)
        my_otchet.heading("detid", text="id детали", anchor=CENTER)


        for i in range(vis):
            my_otchet.insert(parent='', index='end', text='', values=(
                rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6], rows[i][7]))

        my_otchet.pack()
        Button(ws, text="Принять доставку", width=15, height=1, command=lambda: prinskl()).pack()
        Button(ws, text="Закрыть", width=15, height=1, command=lambda: ws.destroy()).pack()

        ws.mainloop()
def vipzapr():
    cur = bd.cursor()
    cur.execute("SELECT * from historyzaprosi where vipoln = 'нет'")
    rows = cur.fetchall()
    if rows == []:
        messagebox.showinfo("ошибка", "Активных запросов не обнаружено")

    else:

        vis, dl = numpy.shape(rows)
        ws = Tk()
        ws.title('Активные запросы')
        ws.geometry('1000x500')

        otchet_frame = Frame(ws)
        otchet_frame.pack()

        my_otchet = ttk.Treeview(otchet_frame)

        my_otchet['columns'] = (
            'id', 'name', 'price', 'kolvo', 'sovmest', 'data', 'vipoln', 'detid', 'remontid')

        my_otchet.column("#0", width=0, stretch=NO)
        my_otchet.column("id", anchor=CENTER, width=50)
        my_otchet.column("name", anchor=CENTER, width=180)
        my_otchet.column("price", anchor=CENTER, width=120)
        my_otchet.column("kolvo", anchor=CENTER, width=50)
        my_otchet.column("sovmest", anchor=CENTER, width=180)
        my_otchet.column("data", anchor=CENTER, width=180)
        my_otchet.column("vipoln", anchor=CENTER, width=80)
        my_otchet.column("detid", anchor=CENTER, width=70)
        my_otchet.column("remontid", anchor=CENTER, width=70)

        my_otchet.heading("#0", text="", anchor=CENTER)
        my_otchet.heading("id", text="id", anchor=CENTER)
        my_otchet.heading("name", text="Название", anchor=CENTER)
        my_otchet.heading("price", text="Цена", anchor=CENTER)
        my_otchet.heading("kolvo", text="Кол-во", anchor=CENTER)
        my_otchet.heading("sovmest", text="Совместимость", anchor=CENTER)
        my_otchet.heading("data", text="Дата запроса", anchor=CENTER)
        my_otchet.heading("vipoln", text="Выполнение", anchor=CENTER)
        my_otchet.heading("detid", text="id детали", anchor=CENTER)
        my_otchet.heading("remontid", text="id ремонта", anchor=CENTER)

        for i in range(vis):
            print(i)
            print(rows[0][0], rows[0][1], rows[0][2])
            my_otchet.insert(parent='', index='end', text='', values=(
            rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6], rows[i][7], rows[i][8]))

        my_otchet.pack()

        Button(ws, text="Закрыть", width=15, height=1, command=lambda: ws.destroy()).pack()

        ws.mainloop()


def provzak():
    cur = bd.cursor()
    cur.execute("SELECT * from historyzaprosi where vipoln = 'нет'")
    rows = cur.fetchall()
    if rows == []:
        messagebox.showinfo("ошибка", "Активных запросов не обнаружено")

    else:
        print(rows)
        vis, dl = numpy.shape(rows)
        ws = Tk()
        ws.title('Активные запросы')
        ws.geometry('1000x500')

        otchet_frame = Frame(ws)
        otchet_frame.pack()

        my_otchet = ttk.Treeview(otchet_frame)

        my_otchet['columns'] = (
            'id', 'name', 'price', 'kolvo', 'sovmest', 'data', 'vipoln', 'detid', 'remontid')

        my_otchet.column("#0", width=0, stretch=NO)
        my_otchet.column("id", anchor=CENTER, width=50)
        my_otchet.column("name", anchor=CENTER, width=180)
        my_otchet.column("price", anchor=CENTER, width=120)
        my_otchet.column("kolvo", anchor=CENTER, width=50)
        my_otchet.column("sovmest", anchor=CENTER, width=180)
        my_otchet.column("data", anchor=CENTER, width=180)
        my_otchet.column("vipoln", anchor=CENTER, width=80)
        my_otchet.column("detid", anchor=CENTER, width=70)
        my_otchet.column("remontid", anchor=CENTER, width=70)

        my_otchet.heading("#0", text="", anchor=CENTER)
        my_otchet.heading("id", text="id", anchor=CENTER)
        my_otchet.heading("name", text="Название", anchor=CENTER)
        my_otchet.heading("price", text="Цена", anchor=CENTER)
        my_otchet.heading("kolvo", text="Кол-во", anchor=CENTER)
        my_otchet.heading("sovmest", text="Совместимость", anchor=CENTER)
        my_otchet.heading("data", text="Дата запроса", anchor=CENTER)
        my_otchet.heading("vipoln", text="Выполнение", anchor=CENTER)
        my_otchet.heading("detid", text="id детали", anchor=CENTER)
        my_otchet.heading("remontid", text="id ремонта", anchor=CENTER)

        for i in range(vis):
            print(i)
            print(rows[0][0],rows[0][1],rows[0][2])
            my_otchet.insert(parent='', index='end', text='', values=(rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6], rows[i][7],rows[i][8]))

        my_otchet.pack()
        Button(ws, text="Закрыть", width=15, height=1, command=lambda: ws.destroy()).pack()

        ws.mainloop()

def zaverrab2(prov,spisid):

    if prov == 0:
        cur = bd.cursor()
        provlog2 = "UPDATE historyrem SET zaverch = 'да' where remontid = %s"
        cur.execute(provlog2, (spisid,))
        bd.commit()
        messagebox.showinfo("Успешно", "Работа успешно завершена!")
    else:
        cur = bd.cursor()
        cur.execute("UPDATE historyrem SET zaverch = 'да' where zaverch = 'нет'")
        bd.commit()
        messagebox.showinfo("Успешно", "Все работы успешно завершены!")

def zaverrab():
    winzakr = Tk()
    winzakr.geometry('700x300')
    winzakr.title("Закрытие работы")
    Label(winzakr,text="Выберите id работ, которые хотите закрыть").grid(column=1, row=1)
    Label(winzakr,text="либо нажмите 'закрыть все' чтобы закрыть все работы").grid(column=3, row=1)

    cur = bd.cursor()
    cur.execute("SELECT historyrem.remontid from historyrem where zaverch = 'нет'")
    rows = cur.fetchall()
    rabots = ttk.Combobox(winzakr, values=rows)
    rabots.set("id")
    rabots.grid(row=3, column=1)

    Button(winzakr, text="Завершить", command=lambda: zaverrab2(0, rabots.get())).grid(column=1, row=4)
    Button(winzakr, text="Завершить все", command=lambda: zaverrab2(1, 0)).grid(column=3, row=3)
    Button(winzakr, text="Закрыть", command=lambda: winzakr.destroy()).grid(column=3, row=4)
def provtekrab():

    cur = bd.cursor()
    cur.execute("SELECT * from historyrem where zaverch = 'нет'")
    rows = cur.fetchall()

    if rows == []:
        messagebox.showinfo("ошибка", "Активных работ не обнаружено")

    else:

        vis, dl = numpy.shape(rows)
        ws = Tk()
        ws.title('Активные работы')
        ws.geometry('1170x500')

        otchet_frame = Frame(ws)
        otchet_frame.pack()

        my_otchet = ttk.Treeview(otchet_frame)

        my_otchet['columns'] = (
        'id', 'model', 'gosnomer', 'prichina', 'utochrem', 'detali', 'time', 'daterem', 'fiomehan', 'zaverch')

        my_otchet.column("#0", width=0, stretch=NO)
        my_otchet.column("id", anchor=CENTER, width=50)
        my_otchet.column("model", anchor=CENTER, width=90)
        my_otchet.column("gosnomer", anchor=CENTER, width=80)
        my_otchet.column("prichina", anchor=CENTER, width=180)
        my_otchet.column("utochrem", anchor=CENTER, width=180)
        my_otchet.column("detali", anchor=CENTER, width=180)
        my_otchet.column("time", anchor=CENTER, width=90)
        my_otchet.column("daterem", anchor=CENTER, width=120)
        my_otchet.column("fiomehan", anchor=CENTER, width=120)
        my_otchet.column("zaverch", anchor=CENTER, width=80)

        my_otchet.heading("#0", text="", anchor=CENTER)
        my_otchet.heading("id", text="id", anchor=CENTER)
        my_otchet.heading("model", text="Модель", anchor=CENTER)
        my_otchet.heading("gosnomer", text="Гос номер", anchor=CENTER)
        my_otchet.heading("prichina", text="Причина", anchor=CENTER)
        my_otchet.heading("utochrem", text="Уточнение причины", anchor=CENTER)
        my_otchet.heading("detali", text="Необходимые детали", anchor=CENTER)
        my_otchet.heading("time", text="Время обслуж", anchor=CENTER)
        my_otchet.heading("daterem", text="Дата обслуживания", anchor=CENTER)
        my_otchet.heading("fiomehan", text="ФИО мастера", anchor=CENTER)
        my_otchet.heading("zaverch", text="завершено?", anchor=CENTER)

        for i in range(vis):
            my_otchet.insert(parent='', index='end', text='',
                             values=(rows[i][9], rows[i][0], rows[i][1], rows[i][2], rows[i][8], rows[i][3], rows[i][4],
                                     rows[i][5], rows[i][6], rows[i][7]))

        my_otchet.pack()
        Button(ws,text="Завершить работу",width=15, height=1, command=lambda: zaverrab()).pack()
        Button(ws, text="Закрыть", width=15, height=1, command=lambda: ws.destroy()).pack()

        ws.mainloop()

def dobrabot2(gosnomer,rabots,utochprich,detal,vrem,remdat,fio):
    if len(gosnomer) != 0:
        if len(rabots) != 0:
            if len(utochprich) != 0:

                        if len(vrem) != 0:
                            if len(remdat) != 0:
                                if int(remdat[:4]) <=2021:
                                    cur = bd.cursor()
                                    cur.execute("SELECT gosnumber FROM autopark")
                                    provlog = cur.fetchall()
                                    a = False
                                    for i in range(len(provlog)):
                                        if gosnomer in str(provlog[i]):
                                            a = True

                                    if a == True:
                                        strok = (gosnomer, rabots, utochprich, detal, vrem, remdat, fio)
                                        cur.execute(f"INSERT INTO historyrem (gosnomer,prichina,detrem, detali,time,daterem, fiomehan) VALUES {strok}")
                                        provlog2 = "update autopark set rabotaet='нет' where gosnumber =%s"
                                        cur.execute(provlog2, (gosnomer,))
                                        bd.commit()
                                        messagebox.showinfo("Успех", "Запись успешно добавлена!")

                                    else:
                                        messagebox.showinfo("Ошибка", "автомобиль не найден")
                                else:
                                    messagebox.showinfo("Ошибка", "Вы из будущего?")
                            else:
                                messagebox.showinfo("ошибка", "Поле 'дата обслуживания' должно быть заполнено")
                        else:
                            messagebox.showinfo("ошибка", "Поле 'время обслуживания' должно быть заполнено")

            else:
                messagebox.showinfo("ошибка", "Поле 'уточнение причины' должно быть заполнено")
        else:
            messagebox.showinfo("ошибка", "Поле 'причина работы' должно быть заполнено")
    else:
        messagebox.showinfo("ошибка", "Поле 'гос номер' должно быть заполнено")


def dobrabot(fio):
    windob=Tk()
    windob.geometry('620x450')
    windob.title("Добавление новой работы")

    Label(windob,text="Введите гос номер").grid(column=1,row=1)
    gosnomer=StringVar()
    Entry(windob,relief=RAISED, width=25, borderwidth=2, textvariable=gosnomer).grid(column=1,row=2)
    Label(windob, text="Выберите причину обслуживания").grid(column=3, row=1)

    vib = ["плановое обсуживание", "ремонт"]
    rabots = ttk.Combobox(windob, values=vib)
    rabots.set("причина")
    rabots.grid(row=2, column=3)

    Label(windob, text="Уточните причину обслуживания").grid(row=4,column=3)
    utochprich=StringVar()
    Entry(windob,relief=RAISED, width=25, borderwidth=2, textvariable=utochprich).grid(column=3,row=5)

    Label(windob,text="Уточните необходимую запчасть").grid(row=1,column=5)
    detal=StringVar()
    Entry(windob,relief=RAISED, width=25, borderwidth=2, textvariable=detal).grid(column=5,row=2)

    Label(windob, text="Введите время ремонта (ч)").grid(row=4,column=1)
    vrem=StringVar()
    Entry(windob,relief=RAISED, width=25, borderwidth=2, textvariable=vrem).grid(column=1,row=5)

    Label(windob, text="Введите дату ремонта (год-месяц-день)").grid(row=7,column=1)
    remdat=StringVar()
    Entry(windob,relief=RAISED, width=25, borderwidth=2, textvariable=remdat).grid(column=1,row=8)

    dobav = Button(windob, text="Добавить",
                   command=lambda: dobrabot2(gosnomer.get(),rabots.get(),utochprich.get(),detal.get(),vrem.get(),remdat.get(),fio))
    dobav.grid(column=3, row=10)

    zakr = Button(windob, text="Закрыть", command=lambda: windob.destroy())
    zakr.grid(column=5, row=10)

    windob.mainloop()

def delavto2(vvod):
    cur = bd.cursor()
    cur.execute("SELECT gosnumber FROM autopark")
    provlog = cur.fetchall()
    a = False
    for i in range(len(provlog)):
        if vvod in str(provlog[i]):
            a = True

    if a == True:
        provlog2 = "DELETE from autopark where gosnumber = %s"  # удаление строки с данным логином
        cur.execute(provlog2, (vvod,))
        bd.commit()
        messagebox.showinfo("Успех", "Автомобиль успешно удалён!")
    else:
        messagebox.showinfo("Ошибка", "Автомобиль с данным гос номером не найден")


def delavto():
    windel = Tk()
    windel.geometry('300x150')
    windel.title("Удаление автомобиля")
    text = Label(windel, text="Введите гос номер автомобиля:")
    text.grid(column=1, row=1)
    log = StringVar()
    log.set("гос номер")
    vvod = Entry(windel, relief=RAISED, width=25, borderwidth=2, textvariable=log)
    vvod.grid(column=1, row=3)
    udal = Button(windel,text="Удалить", command=lambda: delavto2(vvod.get()))
    udal.grid(column=1,row=5)
    zakr = Button(windel, text="Закрыть", command=lambda: windel.destroy())
    zakr.grid(column=2,row=5)

    windel.mainloop()


def dobavto2(gosnomer, model, birth, rabots):
    if len(gosnomer) != 0:
        if len(model) != 0:
            if len(rabots) != 0:
                    if len(birth) != 0:
                        if birth.isdigit() == True:
                            if int(birth)<=2021:
                                cur = bd.cursor()
                                cur.execute("SELECT gosnumber FROM autopark")
                                provlog=cur.fetchall()
                                a=False
                                for i in range(len(provlog)):
                                    if gosnomer in str (provlog[i]):
                                        a=True

                                if a == False:

                                    strok=(gosnomer, model, birth, rabots)
                                    cur.execute(f"INSERT INTO autopark (gosnumber,model,birthyear,rabotaet) VALUES {strok}")
                                    bd.commit()
                                    messagebox.showinfo("Успех", "Запись успешно добавлена!")

                                else:
                                    messagebox.showinfo("Ошибка", "Данный логин занят")
                            else:
                                messagebox.showinfo("ошибка", "Вы пытаетесь добавить автомобиль из будущего")
                        else:
                            messagebox.showinfo("ошибка", "Введите год числом")
                    else:
                        messagebox.showinfo("ошибка", "Поле 'год производства' должно быть заполнено")
            else:
                messagebox.showinfo("ошибка", "Поле 'работоспособность' должно быть заполнено")
        else:
            messagebox.showinfo("ошибка", "Поле 'модель' должно быть заполнено")
    else:
        messagebox.showinfo("ошибка", "Поле 'гос номер' должно быть заполнено")



def dobavavto():
    dobavtowin = Tk()
    dobavtowin.geometry('400x200')
    dobavtowin.title("Добавление нового ТС")
    Label(dobavtowin, text="Введите гос номер:").grid(column=1, row=1)
    gosnomer = StringVar()
    Entry(dobavtowin, relief=RAISED, width=25, borderwidth=2, textvariable=gosnomer).grid(column=1, row=2)  # ввод госномера

    Label(dobavtowin, text="Введите модель:").grid(column=3, row=1)
    model = StringVar()
    Entry(dobavtowin, relief=RAISED, width=15, borderwidth=2, textvariable=model).grid(column=3, row=2)  # ввод модели

    Label(dobavtowin, text="Введите год производства:").grid(column=1, row=3)
    birth = StringVar()
    Entry(dobavtowin, relief=RAISED, width=15, borderwidth=2, textvariable=birth).grid(column=1, row=4)  # ввод года производства

    Label(dobavtowin, text="Работоспособность").grid(column=3, row=3)
    vib = ["да", "нет"]
    rabots=ttk.Combobox(dobavtowin, values=vib)
    rabots.set("работоспособность")
    rabots.grid(row=4, column=3)

    dobav=Button(dobavtowin, text="Добавить", command=lambda: dobavto2(gosnomer.get(), model.get(), birth.get(), rabots.get()))
    dobav.grid(column=1, row=5)

    zakr=Button(dobavtowin, text="Закрыть", command=lambda: dobavtowin.destroy())
    zakr.grid(column=3,row=5)
    dobavtowin.mainloop()

def otchavto(filtr,vvod):
    rows=[]
    a = 0
    cur = bd.cursor()
    if filtr == "госномер тс":
        provfiltr = "SELECT * from autopark where gosnumber = %s"
        cur.execute(provfiltr, (vvod,))
        rows = cur.fetchall()
        a = 1

    elif filtr == "модель":
        provfiltr = "SELECT * from autopark where model = %s"
        cur.execute(provfiltr, (vvod,))
        rows = cur.fetchall()
        a = 1

    elif filtr == "количество работ более":
        if vvod.isdigit() == True:
            provfiltr = "SELECT * from autopark where kolvorem > %s"
            cur.execute(provfiltr, (vvod,))
            rows = cur.fetchall()
            a = 1
        else:
            messagebox.showinfo("ошибка", "Введите число")

    elif filtr == "количество работ менее":
        if vvod.isdigit() == True:
            provfiltr = "SELECT * from autopark where kolvorem < %s"
            cur.execute(provfiltr, (vvod,))
            rows = cur.fetchall()
            a = 1
        else:
            messagebox.showinfo("ошибка", "Введите число")

    elif filtr == "стоимость работ более":
        if vvod.isdigit() == True:
            provfiltr = "SELECT * from autopark where stoimrem > %s"
            cur.execute(provfiltr, (vvod,))
            rows = cur.fetchall()
            a = 1
        else:
            messagebox.showinfo("ошибка", "Введите число")

    elif filtr == "стоимость работ менее":
        if vvod.isdigit() == True:
            provfiltr = "SELECT * from autopark where stoimrem < %s"
            cur.execute(provfiltr, (vvod,))
            rows = cur.fetchall()
            a = 1
        else:
            messagebox.showinfo("ошибка", "Введите число")

    elif filtr == "общее время простоя более":
        if vvod.isdigit() == True:
            provfiltr = "SELECT * from autopark where downtime > %s"
            cur.execute(provfiltr, (vvod,))
            rows = cur.fetchall()
            a = 1
        else:
            messagebox.showinfo("ошибка", "Введите число")

    elif filtr == "общее время простоя менее":
        if vvod.isdigit() == True:
            provfiltr = "SELECT * from autopark where downtime < %s"
            cur.execute(provfiltr, (vvod,))
            rows = cur.fetchall()
            a = 1
        else:
            messagebox.showinfo("ошибка", "Введите число")

    elif filtr == "год изготовления с":
        if vvod.isdigit() == True:
            provfiltr = "SELECT * from autopark where birthyear >= %s"
            cur.execute(provfiltr, (vvod,))
            rows = cur.fetchall()
            a = 1
        else:
            messagebox.showinfo("ошибка", "Введите число")

    elif filtr == "год изготовления по":
        if vvod.isdigit() == True:
            provfiltr = "SELECT * from autopark where birthyear <= %s"
            cur.execute(provfiltr, (vvod,))
            rows = cur.fetchall()
            a = 1
        else:
            messagebox.showinfo("ошибка", "Введите число")

    elif filtr == "работоспособность":
        if vvod == 'да' or vvod == 'нет':
            provfiltr = "SELECT * from autopark where rabotaet = %s"
            cur.execute(provfiltr, (vvod,))
            rows = cur.fetchall()
            a = 1
        else:
            messagebox.showinfo("ошибка", "Введите да или нет")

    elif filtr == "нет":
        cur.execute("SELECT * from autopark")
        rows = cur.fetchall()
        a = 1


    if rows == [] and a==1:
        messagebox.showinfo("ошибка", "Записей с этим фильтром не обнаружено")

    elif rows == [] and a==0:
        deystv=0

    else:

        vis, dl = numpy.shape(rows)
        ws = Tk()
        ws.title('История обслуживаний ТС')
        ws.geometry('940x500')

        otchet_frame = Frame(ws)
        otchet_frame.pack()

        my_otchet = ttk.Treeview(otchet_frame)

        my_otchet['columns'] = ('model', 'gosnomer', 'birth', 'kolvorem', 'stoimrem', 'downtime', 'rab')

        my_otchet.column("#0", width=0, stretch=NO)
        my_otchet.column("model", anchor=CENTER, width=90)
        my_otchet.column("gosnomer", anchor=CENTER, width=80)
        my_otchet.column("birth", anchor=CENTER, width=180)
        my_otchet.column("kolvorem", anchor=CENTER, width=180)
        my_otchet.column("stoimrem", anchor=CENTER, width=90)
        my_otchet.column("downtime", anchor=CENTER, width=120)
        my_otchet.column("rab", anchor=CENTER, width=120)

        my_otchet.heading("#0", text="", anchor=CENTER)
        my_otchet.heading("model", text="Модель", anchor=CENTER)
        my_otchet.heading("gosnomer", text="Гос номер", anchor=CENTER)
        my_otchet.heading("birth", text="Год изготовления", anchor=CENTER)
        my_otchet.heading("kolvorem", text="Кол-во работ", anchor=CENTER)
        my_otchet.heading("stoimrem", text="Стоимость работ", anchor=CENTER)
        my_otchet.heading("downtime", text="Время простоя", anchor=CENTER)
        my_otchet.heading("rab", text="Работоспособность", anchor=CENTER)

        for i in range(vis):
            my_otchet.insert(parent='', index='end', text='',
                             values=(rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6]))

        my_otchet.pack()

        ws.mainloop()


def filavto():
    winfil = Tk()
    winfil.geometry('300x200')
    winfil.title("Отчёт об автопарке")
    fil = ["госномер тс", "модель", "год изготовления с", "год изготовления по","количество работ более", "количество работ менее", "стоимость работ более", "стоимость работ менее", "общее время простоя более", "общее время простоя менее", "работоспособность", "нет"]
    filtr = ttk.Combobox(winfil, width=30, values=fil)
    filtr.set("Выберите фильтр")
    filtr.grid(row=1, column=2)
    vvodverh = Label(winfil, text="Введите значение фильтра")
    vvodverh.grid(row=2, column=2)
    vvodfiltr = Entry(winfil)
    vvodfiltr.grid(row=3, column=2)
    otchhiskn = Button(winfil, text="Открыть отчёт", command=lambda: otchavto(filtr.get(), vvodfiltr.get()))
    otchhiskn.grid(row=5, column=2)

    winfil.mainloop()

def delrab2(vvod):
    cur = bd.cursor()
    cur.execute("SELECT login FROM rabotniki")
    provlog = cur.fetchall()
    a = False
    for i in range(len(provlog)):
        if vvod in str(provlog[i]):
            a = True

    if a == True:
        provlog2 = "DELETE from rabotniki where login = %s"  # удаление строки с данным логином
        cur.execute(provlog2, (vvod,))
        bd.commit()
        messagebox.showinfo("Успех", "Сотрудник успешно удалён!")
    else:
        messagebox.showinfo("Ошибка", "Сотрудник с данным логином не найден")


def delrab():
    windel = Tk()
    windel.geometry('300x150')
    windel.title("Удаление сотрудика")
    text = Label(windel, text="Введите логин сотрудника:")
    text.grid(column=1, row=1)
    log = StringVar()
    log.set("логин")
    vvod = Entry(windel, relief=RAISED, width=25, borderwidth=2, textvariable=log)
    vvod.grid(column=1, row=3)
    udal = Button(windel,text="Удалить", command=lambda: delrab2(vvod.get()))
    udal.grid(column=1,row=5)
    zakr = Button(windel, text="Закрыть", command=lambda: windel.destroy())
    zakr.grid(column=2,row=5)

    windel.mainloop()

def dobavrab2(fio, dolz, logiin, pas, phone, addr, birth):
    if len(fio) != 0:
        if len(dolz) != 0:
            if len(logiin) != 0:
                if len(pas) != 0:
                    if len(birth) != 0:
                        if 2021-int(birth[:4])>=18:
                            cur = bd.cursor()
                            cur.execute("SELECT login FROM rabotniki")
                            provlog=cur.fetchall()
                            a=False
                            for i in range(len(provlog)):
                                if logiin in str (provlog[i]):
                                    a=True

                            if a == False:

                                strok=(fio, dolz, logiin, pas, phone, addr, birth)
                                cur.execute(f"INSERT INTO rabotniki (fio,post,login,pass,phone,address,birthdate) VALUES {strok}")
                                bd.commit()
                                messagebox.showinfo("Успех", "Запись успешно добавлена!")

                            else:
                                messagebox.showinfo("Ошибка", "Данный логин занят")
                        else:
                            messagebox.showinfo("ошибка", "Вы пытаетесь добавить несовершеннолетнего пользователя")
                    else:
                        messagebox.showinfo("ошибка", "Поле 'дата рождения' должно быть заполнено")
                else:
                    messagebox.showinfo("ошибка", "Поле 'пароль' должно быть заполнено")
            else:
                messagebox.showinfo("ошибка", "Поле 'логин' должно быть заполнено")
        else:
            messagebox.showinfo("ошибка", "Поле 'должность' должно быть заполнено")
    else:
        messagebox.showinfo("ошибка", "Поле 'ФИО' должно быть заполнено")


def dobavrab():
    dobrabwin=Tk()
    dobrabwin.geometry('660x200')
    dobrabwin.title("Добавление нового работника")
    text11 = Label(dobrabwin, text="Введите ФИО:")
    text11.grid(column=1, row=1)
    fio = StringVar()
    vvod11 = Entry(dobrabwin, relief=RAISED, width=25, borderwidth=2, textvariable=fio)  # ввод ФИО
    vvod11.grid(column=1, row=2)

    text12 = Label(dobrabwin, text="Введите должность:")
    text12.grid(column=3, row=1)
    vib = ["директор", "механик", "заведующий складом", "менеджер автопарка"]
    dolz = ttk.Combobox(dobrabwin, values=vib)
    dolz.set("должность")
    dolz.grid(row=2, column=3)

    text13 = Label(dobrabwin, text="Введите дату рождения (год-месяц-день):")
    text13.grid(column=5, row=1)
    birth = StringVar()
    vvod13 = Entry(dobrabwin, relief=RAISED, width=15, borderwidth=2, textvariable=birth)  # ввод ФИО
    vvod13.grid(column=5, row=2)

    text21 = Label(dobrabwin, text="Введите логин:")
    text21.grid(column=1, row=4)
    login = StringVar()
    vvod21 = Entry(dobrabwin, relief=RAISED, width=15, borderwidth=2, textvariable=login)  # ввод ФИО
    vvod21.grid(column=1, row=5)

    text22 = Label(dobrabwin, text="Введите телефон:")
    text22.grid(column=3, row=4)
    phone = StringVar()
    vvod22 = Entry(dobrabwin, relief=RAISED, width=15, borderwidth=2, textvariable=phone)  # ввод ФИО
    vvod22.grid(column=3, row=5)

    text31 = Label(dobrabwin, text="Введите пароль:")
    text31.grid(column=1, row=7)
    pas = StringVar()
    vvod31 = Entry(dobrabwin, relief=RAISED, width=15, borderwidth=2, textvariable=pas)  # ввод ФИО
    vvod31.grid(column=1, row=8)

    text32 = Label(dobrabwin, text="Введите адрес:")
    text32.grid(column=3, row=7)
    add = StringVar()
    vvod32 = Entry(dobrabwin, relief=RAISED, width=15, borderwidth=2, textvariable=add)  # ввод ФИО
    vvod32.grid(column=3, row=8)

    dobav=Button(dobrabwin, text="Добавить", command=lambda: dobavrab2(fio.get(), dolz.get(), login.get(), pas.get(), phone.get(), add.get(), birth.get()))
    dobav.grid(column=2, row=10)

    zakr=Button(dobrabwin, text="Закрыть", command=lambda: dobrabwin.destroy())
    zakr.grid(column=4,row=10)

    dobrabwin.mainloop()

def otchhis(filtr,vvod):
    cur = bd.cursor()
    if filtr == "госномер тс":
        provfiltr = "SELECT * from historyrem where gosnomer = %s"
        cur.execute(provfiltr, (vvod, ))

    elif filtr == "модель":
        provfiltr = "SELECT * from historyrem where model = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "причина":
        provfiltr = "SELECT * from historyrem where prichina = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "дата":
        provfiltr = "SELECT * from historyrem where daterem = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "ФИО механика":
        provfiltr = "SELECT * from historyrem where fiomehan = %s"
        cur.execute(provfiltr, (vvod,))

    elif filtr == "нет":
        cur.execute("SELECT * from historyrem")

    rows = cur.fetchall()
    if rows == []:
        messagebox.showinfo("ошибка", "Записей с этим фильтром не обнаружено")

    else:

        vis, dl = numpy.shape(rows)
        ws = Tk()
        ws.title('История обслуживаний ТС')
        ws.geometry('1170x500')

        otchet_frame = Frame(ws)
        otchet_frame.pack()

        my_otchet = ttk.Treeview(otchet_frame)

        my_otchet['columns'] = ('id','model', 'gosnomer', 'prichina','utochrem', 'detali', 'time', 'daterem', 'fiomehan','zaverch')

        my_otchet.column("#0", width=0, stretch=NO)
        my_otchet.column("id", anchor=CENTER, width=50)
        my_otchet.column("model", anchor=CENTER, width=90)
        my_otchet.column("gosnomer", anchor=CENTER, width=80)
        my_otchet.column("prichina", anchor=CENTER, width=180)
        my_otchet.column("utochrem", anchor=CENTER, width=180)
        my_otchet.column("detali", anchor=CENTER, width=180)
        my_otchet.column("time", anchor=CENTER, width=90)
        my_otchet.column("daterem", anchor=CENTER, width=120)
        my_otchet.column("fiomehan", anchor=CENTER, width=120)
        my_otchet.column("zaverch", anchor=CENTER, width=80)

        my_otchet.heading("#0", text="", anchor=CENTER)
        my_otchet.heading("id", text="id", anchor=CENTER)
        my_otchet.heading("model", text="Модель", anchor=CENTER)
        my_otchet.heading("gosnomer", text="Гос номер", anchor=CENTER)
        my_otchet.heading("prichina", text="Причина", anchor=CENTER)
        my_otchet.heading("utochrem", text="Уточнение причины", anchor=CENTER)
        my_otchet.heading("detali", text="Необходимые детали", anchor=CENTER)
        my_otchet.heading("time", text="Время обслуж", anchor=CENTER)
        my_otchet.heading("daterem", text="Дата обслуживания", anchor=CENTER)
        my_otchet.heading("fiomehan", text="ФИО мастера", anchor=CENTER)
        my_otchet.heading("zaverch", text="завершено?", anchor=CENTER)

        for i in range(vis):
            my_otchet.insert(parent='', index='end', text='',
                            values=(rows[i][9],rows[i][0], rows[i][1], rows[i][2], rows[i][8],rows[i][3], rows[i][4], rows[i][5], rows[i][6], rows[i][7]))

        my_otchet.pack()

        ws.mainloop()

def otchrab():
    cur = bd.cursor()
    cur.execute("SELECT * from rabotniki")
    rows = cur.fetchall()
    vis, dl = numpy.shape(rows)
    ws = Tk()
    ws.title('Информация о сотрудниках')
    ws.geometry('810x500')

    otchet_frame = Frame(ws)
    otchet_frame.pack()

    my_otchet = ttk.Treeview(otchet_frame)

    my_otchet['columns'] = ('fio', 'post', 'login', 'pass', 'phone','address','birthdate')

    my_otchet.column("#0", width=0,  stretch=NO)
    my_otchet.column("fio",anchor=CENTER, width=170)
    my_otchet.column("post",anchor=CENTER,width=140)
    my_otchet.column("login",anchor=CENTER,width=80)
    my_otchet.column("pass",anchor=CENTER,width=80)
    my_otchet.column("phone",anchor=CENTER,width=100)
    my_otchet.column("address",anchor=CENTER,width=120)
    my_otchet.column("birthdate",anchor=CENTER,width=120)

    my_otchet.heading("#0",text="",anchor=CENTER)
    my_otchet.heading("fio",text="ФИО",anchor=CENTER)
    my_otchet.heading("post",text="Должность",anchor=CENTER)
    my_otchet.heading("login",text="Логин",anchor=CENTER)
    my_otchet.heading("pass",text="Пароль",anchor=CENTER)
    my_otchet.heading("phone",text="Номер телефона",anchor=CENTER)
    my_otchet.heading("address",text="Домашний адрес",anchor=CENTER)
    my_otchet.heading("birthdate",text="Дата рождения",anchor=CENTER)

    for i in range (vis):
        my_otchet.insert(parent='',index='end',text='',
        values=(rows[i][0],rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6]))

    my_otchet.pack()

    ws.mainloop()

def filhis():
    winfil = Tk()
    winfil.geometry('300x200')
    winfil.title("Отчёт о истории ремонтов")
    fil=["госномер тс","модель","причина","дата","ФИО механика","нет"]
    filtr=ttk.Combobox(winfil, values = fil)
    filtr.set("Выберите фильтр")
    filtr.grid(row=1, column=1)
    vvodverh=Label(winfil,text="Введите значение фильтра")
    vvodverh.grid(row=2,column=1)
    vvodfiltr=Entry(winfil)
    vvodfiltr.grid(row=3,column=1)
    otchhiskn = Button(winfil,text="Открыть отчёт",command=lambda: otchhis(filtr.get(),vvodfiltr.get()))
    otchhiskn.grid(row=5,column=1)

    winfil.mainloop()
def dirokno(fio):

    windir = Tk()
    windir.geometry('555x300')
    title = 'Добро пожаловать, '+fio
    windir.title(title)
    otchpers = Button(windir,text="Информация о сотрудниках", width=25, command=lambda: otchrab())
    otchpers.grid(row=1,column=1)
    dobpers = Button(windir, text="Добавить сотрудника", width=25, command=lambda: dobavrab())
    dobpers.grid(row=3, column=1)
    udalrab = Button(windir, text="Удалить сотрудника", width=25, command=lambda: delrab())
    udalrab.grid(row=5, column=1)
    otchhis = Button(windir, text="История работ", width=25, command=lambda: filhis())
    otchhis.grid(row=1, column=7)
    otchavto = Button(windir, text="Автопарк", width=25, command=lambda: filavto())
    otchavto.grid(row=1, column=5)
    dobavto = Button(windir, text="Добавить автомобиль", width=25, command=lambda: dobavavto())
    dobavto.grid(row=3, column=5)
    Button(windir, text="Удалить автомобиль", width=25, command=lambda: delavto()).grid(row=5, column=5)
    Button(windir, text="Инвентаризация", width=25, command=lambda: filtrinvent()).grid(column=7, row=3)
    Button(windir, text="Закрыть", command=lambda: windir.destroy()).grid(column=5,row=6)
    Button(windir, text="Сменить пользователя", command=lambda: vhod()).grid(column=7, row=6)
    windir.mainloop()

def mehokno(fio):

    print("имя механика: ", fio)
    winmeh = Tk()
    winmeh.geometry('500x300')
    title = 'Добро пожаловать, ' + fio
    winmeh.title(title)
    otchhis = Button(winmeh, text="История работ", width=25, command=lambda: filhis())
    otchhis.grid(row=1, column=1)
    Button(winmeh, text="Добавить работу", width=25, command=lambda: dobrabot(fio)).grid(row=3, column=1)
    Button(winmeh, text="Текущие работы", width=25, command=lambda: provtekrab()).grid(row=5, column=1)
    otchavto = Button(winmeh, text="Автопарк", width=25, command=lambda: filavto())
    otchavto.grid(row=1, column=3)
    Button(winmeh, text="Закрыть", command=lambda: winmeh.destroy()).grid(column=3, row=7)
    Button(winmeh, text="Сменить пользователя", command=lambda: vhod()).grid(column=1, row=7)
    winmeh.mainloop()

def sklokno(fio):
    print("имя заведующего складом: ", fio)
    winskl=Tk()
    winskl.geometry('600x300')
    title = 'Добро пожаловать, ' + fio
    winskl.title(title)
    Button(winskl,text="Проверить запросы", width=25, command=lambda: provzak()).grid(column=1,row=1)
    Button(winskl, text="История запросов", width=25, command=lambda: filtrzapr()).grid(column=1, row=2)
    Button(winskl, text="История закупок", width=25, command=lambda: filhiszak()).grid(column=2, row=1)
    Button(winskl, text="Закупки", width=25, command=lambda: zakup()).grid(column=2, row=2)
    Button(winskl, text="Встретить доставку", width=25, command=lambda: zavoz()).grid(column=2, row=3)
    Button(winskl, text="Добавить позицию", width=25, command=lambda: dobskl()).grid(column=3, row=1)
    Button(winskl, text="Инвентаризация", width=25, command=lambda: filtrinvent()).grid(column=3, row=2)
    Button(winskl, text="Закрыть", command=lambda: winskl.destroy()).grid(column=3, row=5)
    Button(winskl, text="Сменить пользователя", command=lambda: vhod()).grid(column=2, row=5)
    winskl.mainloop()

def menedokno(fio):
    print("имя менеджера автопарка: ", fio)
    winman=Tk()
    winman.geometry('600x300')
    title = 'Добро пожаловать, ' + fio
    winman.title(title)
    Button(winman, text="История работ", width=25, command=lambda: filhis()).grid(row=1, column=1)
    Button(winman, text="Автопарк", width=25, command=lambda: filavto()).grid(row=1, column=3)
    Button(winman, text="Инвентаризация", width=25, command=lambda: filtrinvent()).grid(column=5, row=1)
    Button(winman, text="Закрыть", command=lambda: winman.destroy()).grid(column=5, row=3)
    Button(winman, text="Сменить пользователя", command=lambda: vhod()).grid(column=3, row=3)
    winman.mainloop()

def avt(log,pas): #проверка лог/пароля
    fio = 0
    dolz = 0
    cur = bd.cursor()
    provlog = "SELECT * from rabotniki where login = %s" #поиск строки с данным логином
    cur.execute(provlog, (log, ))
    rows = cur.fetchall()
    if rows == []:
        messagebox.showinfo("ошибка", "Такого пользователя не существует, проверьте логин и пароль")
    elif rows[0][3] == pas: #проверка пароля
        dolz = rows[0][1] #вывод ФИО и должности
        fio = rows[0][0]

    else:
        messagebox.showinfo("ошибка", "Такого пользователя не существует, проверьте логин и пароль")

    if dolz == 'директор':
        dirokno(fio)
    elif dolz == 'механик':
        mehokno(fio)
    elif dolz == 'заведующий складом':
        sklokno(fio)
    elif dolz == 'менеджер автопарка':
        menedokno(fio)

def vhod(): #интерфейс меню входа

    winvhod = Tk()
    winvhod.geometry('300x150')
    winvhod.title("Авторизация")
    verhtext = Label(winvhod, text="Введите логин и пароль: ")
    verhtext.grid(column=1, row=1)
    log = StringVar()
    log.set("логин")
    vvodlog = Entry(winvhod, relief=RAISED, width=15, borderwidth=2, textvariable=log) #ввод логина
    vvodlog.grid(column=1, row=2)
    pas = StringVar()
    pas.set("пароль")
    vvodlog = Entry(winvhod, relief=RAISED, width=15, borderwidth=2, textvariable=pas) #ввод пароля
    vvodlog.grid(column=1, row=3)
    prov = Button(winvhod,text="Войти", command=lambda: avt(log.get(), pas.get())) #кнопка входа, вызывает функцию проверки лог/пароль
    prov.grid(column=1, row=4)
    knopkazakr = Button(winvhod, text="закрыть", command=lambda: winvhod.destroy()) #кнопка закрыть
    knopkazakr.grid(column=2, row=4)
    winvhod.mainloop()

cur = bd.cursor()

cur.execute("SELECT * from rabotniki")
rows = cur.fetchall()

vhod()


cur.close()
bd.close()

