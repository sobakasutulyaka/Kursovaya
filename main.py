import psycopg2
from tkinter import *
from tkinter import messagebox


bd=psycopg2.connect(
    database="AvtoRemontBase",
    user="postgres",
    password="1223",
)
def avt(log,pas): #проверка лог/пароля
    fio=0
    dolz=0
    cur = bd.cursor()
    provlog = "SELECT * from rabotniki where login = %s" #поиск строки с данным логином
    cur.execute(provlog,(log,))
    rows = cur.fetchall()
    if rows[0][3]==pas: #проверка пароля
        dolz=rows[0][1] #вывод ФИО и должности
        fio=rows[0][0]
    print(dolz)
    print(fio)
def vhod(): #интерфейс меню входа
    out=[]
    winvhod=Tk()
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
    prov=Button(winvhod,text="Войти", command=lambda: out.append(avt(log.get(),pas.get()))) #кнопка входа, вызывает функцию проверки лог/пароль
    prov.grid(column=1, row=4)
    knopkazakr = Button(winvhod, text="закрыть", command=winvhod.quit) #кнопка закрыть
    knopkazakr.grid(column=2, row=4)
    winvhod.mainloop()
cur=bd.cursor()

cur.execute("SELECT * from rabotniki")
rows=cur.fetchall()
vhod()



bd.close()

