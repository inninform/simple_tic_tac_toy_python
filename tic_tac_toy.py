import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
program = Tk()
program.title("player 1")
def winner_player1():
    t1 = btn1.cget("text")
    print(t1)
    t2 = btn2.cget("text")
    print(t2)
    t3 = btn3.cget("text")
    print(t3)
    t4 = btn4.cget("text")
    print(t4)
    t5 = btn5.cget("text")
    print(t5)
    t6 = btn6.cget("text")
    print(t6)
    t7 = btn7.cget("text")
    print(t7)
    t8 = btn8.cget("text")
    print(t8)
    t9 = btn9.cget("text")
    print(t9)
    if t1+t2+t3=="XXX":
        tkinter.messagebox.showinfo("the player 1 is winnner")
    elif t4+t5+t6=="XXX":
        tkinter.messagebox.showinfo("the player 1 is winnner")
    elif t7+t8+t9=="XXX":
        tkinter.messagebox.showinfo("the player 1 is winnner")
    elif t1+t4+t7=="XXX":
        tkinter.messagebox.showinfo("the player 1 is winnner")
    elif t2+t5+t8=="XXX":
        tkinter.messagebox.showinfo("the player 1 is winnner")
    elif t3+t6+t9=="XXX":
        tkinter.messagebox.showinfo("the player 1 is winnner")
    elif t1+t5+t9=="XXX":
        tkinter.messagebox.showinfo("the player 1 is winnner")
    elif t3+t5+t7=="XXX":
        tkinter.messagebox.showinfo("the player 1 is winnner")
def winner_player2():
    O_text = "OOO"
    t1 = btn1.cget("text")
    print(t1)
    t2 = btn2.cget("text")
    print(t2)
    t3 = btn3.cget("text")
    print(t3)
    t4 = btn4.cget("text")
    print(t4)
    t5 = btn5.cget("text")
    print(t5)
    t6 = btn6.cget("text")
    print(t6)
    t7 = btn7.cget("text")
    print(t7)
    t8 = btn8.cget("text")
    print(t8)
    t9 = btn9.cget("text")
    print(t9)
    if t1+t2+t3==O_text:
        tkinter.messagebox.showinfo("the player 2 is winnner")
    elif t4+t5+t6==O_text:
        tkinter.messagebox.showinfo("the player 2 is winnner")
    elif t7+t8+t9==O_text:
        tkinter.messagebox.showinfo("the player 2 is winnner")
    elif t1+t4+t7==O_text:
        tkinter.messagebox.showinfo("the player 2 is winnner")
    elif t2+t5+t8==O_text:
        tkinter.messagebox.showinfo("the player 2 is winnner")
    elif t3+t6+t9==O_text:
        tkinter.messagebox.showinfo("the player 2 is winnner")
    elif t1+t5+t9==O_text:
        tkinter.messagebox.showinfo("the player 2 is winnner")
    elif t3+t5+t7==O_text:
        tkinter.messagebox.showinfo("the player 2 is winnner")
def func1():
    if know() == 1:
        btn1.config(text="X",font=20,fg="red")
        var.set(0)
        program.title("player 2")
        winner_player1()
        btn1['state'] = DISABLED
    elif know() == 0:
        btn1.config(text="Y",font=20,fg="blue")
        var.set(1)
        program.title("player 1")
        winner_player2()
    btn1.config(state=DISABLED)
def func2():
    if know() == 1:
        btn2.config(text="X",font=20,fg="red")
        var.set(0)
        program.title("player 2")
        winner_player1()
    elif know() == 0:
        btn2.config(text="O",font=20,fg="blue")
        var.set(1)
        program.title("player 1")
        winner_player2()
    btn2.config(state=DISABLED)
def func3():
    if know() == 1:
        btn3.config(text="X",font=20,fg="red")
        var.set(0)
        program.title("player 2")
        winner_player1()
    elif know() == 0:
        btn3.config(text="O",font=20,fg="blue")
        var.set(1)
        program.title("player 1")
        winner_player2()
    btn3.config(state=DISABLED)
def func4():
    if know() == 1:
        btn4.config(text="X",font=20,fg="red")
        var.set(0)
        program.title("player 2")
        winner_player1()
    elif know() == 0:
        btn4.config(text="O",font=20,fg="blue")
        var.set(1)
        program.title("player 1")
        winner_player2()
    btn4.config(state=DISABLED)
def func5():
    if know() == 1:
        btn5.config(text="X",font=20,fg="red")
        var.set(0)
        program.title("player 2")
        winner_player1()
    elif know() == 0:
        btn5.config(text="O",font=20,fg="blue")
        var.set(1)
        program.title("player 1")
        winner_player2()
    btn5.config(state=DISABLED)
def func6():
    if know() == 1:
        btn6.config(text="X",font=20,fg="red")
        var.set(0)
        program.title("player 2")
        winner_player1()
    elif know() == 0:
        btn6.config(text="O",font=20,fg="blue")
        var.set(1)
        program.title("player 1")
        winner_player2()
    btn6.config(state=DISABLED)
def func7():
    if know() == 1:
        btn7.config(text="X",font=20,fg="red")
        var.set(0)
        program.title("player 2")
        winner_player1()
    elif know() == 0:
        btn7.config(text="O",font=20,fg="blue")
        var.set(1)
        program.title("player 1")
        winner_player2()
    btn7.config(state=DISABLED)
def func8():
    if know() == 1:
        btn8.config(text="X",font=20,fg="red")
        var.set(0)
        program.title("player 2")
        winner_player1()
    elif know() == 0:
        btn8.config(text="O",font=20,fg="blue")
        var.set(1)
        program.title("player 1")
        winner_player2()
    btn8.config(state=DISABLED)
def func9():
    if know() == 1:
        btn9.config(text="X",font=20,fg="red")
        var.set(0)
        program.title("player 2")
        winner_player1()
    elif know() == 0:
        btn9.config(text="O",font=20,fg="blue")
        var.set(1)
        program.title("player 1")
        winner_player2()
    btn9.config(state=DISABLED)
def know():
    print(var.get())
    return var.get()
var = IntVar()
checkbox_Know = ttk.Checkbutton(program,variable=var,onvalue=True,offvalue=False)
checkbox_Know.grid(row=3,column=1,sticky='snew')
checkbox_Know.config(state=ACTIVE,command=know)
var.set(1)
var.get()
print(var.get())
btn1 = Button(program,text='')
btn1.grid(row=0,column=0,ipadx=40,ipady=40,sticky='snew')
btn1.config(command=func1)
btn2 = Button(program,text='')
btn2.grid(row=0,column=1,ipadx=40,ipady=40,sticky='snew')
btn2.config(command=func2)
btn3 = Button(program,text='')
btn3.grid(row=0,column=2,ipadx=40,ipady=40,sticky='snew')
btn3.config(command=func3)
btn4 = Button(program,text='')
btn4.grid(row=1,column=0,ipadx=40,ipady=40,sticky='snew')
btn4.config(command=func4)
btn5 = Button(program,text='')
btn5.grid(row=1,column=1,ipadx=40,ipady=40,sticky='snew')
btn5.config(command=func5)
btn6 = Button(program,text='')
btn6.grid(row=1,column=2,ipadx=40,ipady=40,sticky='snew')
btn6.config(command=func6)
btn7 = Button(program,text='')
btn7.grid(row=2,column=0,ipadx=40,ipady=40,sticky='snew')
btn7.config(command=func7)
btn8 = Button(program,text='')
btn8.grid(row=2,column=1,ipadx=40,ipady=40,sticky='snew')
btn8.config(command=func8)
btn9 = Button(program,text='')
btn9.grid(row=2,column=2,ipadx=40,ipady=40,sticky='snew')
btn9.config(command=func9)
lab_player1 = Label(program,text="player 1 : X")
lab_player1.grid(row=4,column=0)
lab_player1.config()
lab_player2 = Label(program,text="player 2 : O")
lab_player2.grid(row=4,column=2)
lab_player2.config()
program.mainloop()