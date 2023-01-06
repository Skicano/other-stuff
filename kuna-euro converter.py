from tkinter import *

a = Tk()
a.title('PYTHON EXCHANGE')
a.config(bg='#1d967f')

b = Label(width=20, height=5, bg='#1d967f')
b.grid(column=0, row=0)

c = Label(width=20, height=5, bg='#1d967f')
c.grid(column=3, row=3)

d = Label(width=20, height=5, bg='#1d967f')
d.grid(column=6, row=7)


def exchange1():
    inputk = float(entryk.get())
    inputk = inputk/7.5
    kune_output.configure(text='Vrijednost kuna u eurima je {:.2f} eura'.format(inputk), font=('Calibri', 16, 'bold'))
    entryk.delete(0, END)


kune_label = Label(text='Unesite vrijednost u kunama:   ', font=('Calibri', 16, 'bold'), bg='#1d967f')
kune_output = Label(font=('Calibri', 16), bg='#1d967f')
entryk = Entry(font=('Calibri', 16), width=3)
kune_button = Button(text='Konvertiraj u eure', font=('Calibri', 16), bg='yellow', command=exchange1)
kune_label.grid(row=2, column=1)
entryk.grid(row=2, column=2)
kune_button.grid(row=2, column=5)
kune_output.grid(row=3, column=1)


def exchange2():
    inpute = float(entrye.get())
    inpute = inpute*7.5
    euri_output.configure(text='Vrijednost eura u kunama je {:.2f} kuna.'.format(inpute), font=('Calibri', 16, 'bold'))
    entrye.delete(0, END)


euri_label = Label(text='Unesite vrijednost u eurima:   ', font=('Calibri', 16, 'bold'), bg='#1d967f')
euri_output = Label(font=('Calibri', 16), bg='#1d967f')
entrye = Entry(font=('Calibri', 16), width=3)
euri_button = Button(text='Konvertiraj u kune', font=('Calibri', 16), bg='yellow', command=exchange2)
euri_label.grid(row=5, column=1)
entrye.grid(row=5, column=2)
euri_button.grid(row=5, column=5)
euri_output.grid(row=6, column=1)

mainloop()
