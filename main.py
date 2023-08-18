from tkinter import *
from tkinter.ttk import Combobox
from forex_python.converter import CurrencyRates

c = CurrencyRates()


def convert(*args):
    F1 = combo1.get()
    F2 = combo2.get()

    one_argument = task[F1]
    two_argument = task[F2]
    num = number.get()
    amount = c.convert(f"{one_argument}", f"{two_argument}", int(num))
    answer.delete(0, END)
    answer.insert(END, amount)


window = Tk()

window.title('Конверт валют')
window.configure(bg='grey', bd=0)
window.geometry('380x340')

task = {
    "Российский рубль": "RUB",
    "Доллар США": "USD",
    "Евро": "EUR",
    "Японская иена": "JPY",
    "Британский фунт стерлингов": "GBP",
    "Австралийский доллар": "AUD",
    "Канадский доллар": "CAD",
    "Швейцарский франк": "CHF",
    "Китайский юань": "CNY",
    "Индийская рупия": "INR",
    "Сингапурский доллар": "SGD",
    "Новозеландский доллар": "NZD",
    "Гонконгский доллар": "HKD",
    "Шведская крона": "SEK",
    "Южнокорейская вона": "KRW",
    "Южноафриканский рэнд": "ZAR"}

Label(window, text='Введите число и выберите как конвертировать', font=('Times New Roman', 11, 'bold'), bg='#151719',
      fg='white').place(x=20, y=40)
Label(window, text='Конвертировать', font=('Times New Roman', 10, 'bold'), bg='#151719', fg='white', width=16).place(
    x=20, y=80)
Label(window, text='Конвертировать из', font=('Times New Roman', 10, 'bold'), bg='#151719', fg='white', width=16).place(
    x=20, y=120)
Label(window, text='Конвертировать в ', font=('Times New Roman', 10, 'bold'), bg='#151719', fg='white', width=16).place(
    x=20, y=160)
Label(window, text='Результат', font=('Times New Roman', 10, 'bold'), bg='#151719', fg='white', width=16).place(x=20,
                                                                                                                y=200)

number = Entry(window, width=27, bd=0, font=('Times New Roman', 12, 'bold'))
number.place(x=145, y=79)

combo1 = Combobox(master=window, width=33)
combo1['values'] = list(task.keys())
combo1.place(x=145, y=119)

combo2 = Combobox(master=window, width=33)
combo2['values'] = list(task.keys())
combo2.place(x=145, y=159)

answer = Entry(window, width=27, bg='#98FB98', fg='black', font=('Times New Roman', 12, 'bold'))
answer.place(x=145, y=199)

Button(window, text='Конвертировать', font=('Times New Roman', 11, 'bold'), bd=0, bg='green', fg='black', width=15,
       height=3, command=convert).place(x=120, y=250)

window.mainloop()
