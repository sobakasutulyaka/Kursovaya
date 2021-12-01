import numpy
import psycopg2
from tkinter import *
from tkinter import messagebox
from  tkinter import ttk

bd=psycopg2.connect(
    database="AvtoRemontBase",
    user="postgres",
    password="1223",
)

def dobavrab2(fio, dolz, login, pas, phone, addr, birth):
    if len(fio) != 0:
        if len(dolz) != 0:
            if len(login) != 0:
                if len(pas) != 0:
                    if len(birth) != 0:
                        if 2021-int(birth[:4])>=18:
                            cur = bd.cursor()
                            cur.execute("SELECT login FROM rabotniki")
                            provlog=cur.fetchall()
                            if login in provlog == False:

                                strok=(fio, dolz, login, pas, phone, addr, birth)
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
        ws.geometry('940x500')

        otchet_frame = Frame(ws)
        otchet_frame.pack()

        my_otchet = ttk.Treeview(otchet_frame)

        my_otchet['columns'] = ('model', 'gosnomer', 'prichina', 'detali', 'time', 'daterem', 'fiomehan','zaverch')

        my_otchet.column("#0", width=0, stretch=NO)
        my_otchet.column("model", anchor=CENTER, width=90)
        my_otchet.column("gosnomer", anchor=CENTER, width=80)
        my_otchet.column("prichina", anchor=CENTER, width=180)
        my_otchet.column("detali", anchor=CENTER, width=180)
        my_otchet.column("time", anchor=CENTER, width=90)
        my_otchet.column("daterem", anchor=CENTER, width=120)
        my_otchet.column("fiomehan", anchor=CENTER, width=120)
        my_otchet.column("zaverch", anchor=CENTER, width=80)

        my_otchet.heading("#0", text="", anchor=CENTER)
        my_otchet.heading("model", text="Модель", anchor=CENTER)
        my_otchet.heading("gosnomer", text="Гос номер", anchor=CENTER)
        my_otchet.heading("prichina", text="Причина", anchor=CENTER)
        my_otchet.heading("detali", text="Необходимые детали", anchor=CENTER)
        my_otchet.heading("time", text="Время обслуж", anchor=CENTER)
        my_otchet.heading("daterem", text="Дата обслуживания", anchor=CENTER)
        my_otchet.heading("fiomehan", text="ФИО мастера", anchor=CENTER)
        my_otchet.heading("zaverch", text="завершено?", anchor=CENTER)

        for i in range(vis):
            my_otchet.insert(parent='', index='end', text='',
                            values=(rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6], rows[i][7]))

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
    winfil.geometry('500x300')
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
    print("имя директора: ", fio)
    windir = Tk()
    windir.geometry('500x300')
    title = 'Добро пожаловать, '+fio
    windir.title(title)
    otchpers = Button(windir,text="Информация о сотрудниках",command=lambda: otchrab())
    otchpers.grid(row=1,column=1)
    dobpers = Button(windir, text="Добавить сотрудника", command=lambda: dobavrab())
    dobpers.grid(row=3, column=1)
    otchhis = Button(windir, text="История работ", command=lambda: filhis())
    otchhis.grid(row=5, column=1)
def mehokno(fio):
    print("имя механика: ", fio)
    winmeh = Tk()
    winmeh.geometry('500x300')
    title = 'Добро пожаловать, ' + fio
    winmeh.title(title)
    otchhis = Button(winmeh, text="История работ", command=lambda: filhis())
    otchhis.grid(row=1, column=1)
def sklokno(fio):
    print("имя заведующего складом: ", fio)

def menedokno(fio):
    print("имя менеджера автопарка: ", fio)

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
    out = []
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
    prov = Button(winvhod,text="Войти", command=lambda: out.append(avt(log.get(),pas.get()))) #кнопка входа, вызывает функцию проверки лог/пароль
    prov.grid(column=1, row=4)
    knopkazakr = Button(winvhod, text="закрыть", command=lambda: winvhod.destroy()) #кнопка закрыть
    knopkazakr.grid(column=2, row=4)
    winvhod.mainloop()
cur = bd.cursor()

cur.execute("SELECT * from rabotniki")
rows = cur.fetchall()
dobavrab()
vhod()


cur.close()
bd.close()

