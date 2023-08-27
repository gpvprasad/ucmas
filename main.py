# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import math
from ctypes import alignment
from tkinter import *
from tkinter import messagebox as mb
import random as rd
import csv
from ShowResult import disp_csv
from quiz import quizformat,openQuizUi
import json
import recordandsave as rs
import complement_supplement as cs
from genericfunctions import *
from TimerHandle import timerhandle as th
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SECOND_MS = 1000

# Python program to create a table

from tkinter import *

def validateFunction(a,b,c=5,d=5,e=None,f=None):
    if None == e:
        if (a+b == 5) and (c+d==10):
            return ('✓','✓')
        elif (a+b == 5) and (c+d!=10):
            return ('✓','X')
        elif (a+b != 5) and (c+d==10):
            return ('X','✓')
        else:
            return ('X','X')
    else:
        if a == b+e:
            return ('✓')
        else:
            return ('X')

complementsummassion = cs.complement_supplement('Complement',validateFunction,'Supplement',10)
group1=[(i,5-i) for i in range(0,5)]*2
rd.shuffle(group1)
group2 = [(i,10-i) for i in range(0,10)]
rd.shuffle(group2)
complementsummassion.filldata(group1=group1,group2=group2)
complementsummassion.startdisplay()

group1 = [(i,10-i) for i in range(1,10)]
complementsummassion = cs.complement_supplement('Test1',validateFunction,noofRows = len(group1),noofColumns=4)
complementsummassion.filldata(group1=group1,group2=5)
complementsummassion.startdisplay()

group1 = [(i,10-i) for i in range(1,10)]
complementsummassion = cs.complement_supplement('Test2',validateFunction,noofRows = len(group1),noofColumns=5)
complementsummassion.filldata(group1=group1,group2=10,group3=-5)
complementsummassion.startdisplay()


def validateFunctionMultiplication(a,b,e):
    if (a*b == e):
        return ('✓','✓')
    else:
        return ('X','X')


for j in range(1,11):
    group1 = [(i,10-i) for i in range(1,10)]
    complementsummassion = cs.complement_supplement('Multiplication '+str(j),validateFunctionMultiplication,noofRows = len(group1),noofColumns=4)
    complementsummassion.filldata(group1=group1,group2=j)
    complementsummassion.startdisplay()


class Table:

    def __init__(self, root,row,column):
        self.root = root
        self.row = row
        self.column = column
        self.timer = None
        self.e = []
        self.ans = None
        self.lst = []
        self.problems = 0
        self.score = 0
        self.insert_table(True)
        self.target = int(e3.get())
        self.maths_answersheet = rs.recordandsave(['problem','correct_answer','answer','status'])
        #print('insert table called init')

    

    def insert_table(self,starting = False):
        if self.timer != None:
            self.root.after_cancel(self.timer)
        # code for creating table
        ucmactest(self,starting,e1,e2,e3,e4,v.get(),True)
        total_rows = len(self.lst)
        #print(total_rows)
        if not starting:
            for rowno, row in reversed(list(enumerate(self.e))):
                    self.e[rowno].destroy()
            self.e = []

        for i in range(total_rows):
            self.e.append( Entry(self.root, width=5, fg='blue', bg=YELLOW, justify='center',
                        font=('Arial', 16, 'bold')))
            print(i,i+self.row,self.column)

            self.e[i].grid(row=i+self.row, column=self.column)
            if not starting:
                self.e[i].insert(END, self.lst[i])
            self.e[i].configure(state=DISABLED)
        if starting:
            self.ans = Entry(self.root, width=5, fg='blue',bg=YELLOW,justify='center',
                         font=('Arial', 16, 'bold'))
            self.ans.grid(row=total_rows + self.row+1, column=self.column)
            
        if not starting:
            self.ans.grid(row=total_rows + self.row+1, column=self.column)
            self.ans.option_clear()
            self.problems += 1
            self.maths_answersheet.addData(problem = tuple(self.lst),correct_answer = sum(self.lst),answer='',status = 'X')
            self.ans.delete(0, END)


    def key_handler(self,event):
        #print(event.char, event.keysym, event.keycode)
        self.ans.insert(0,event.char)
        self.maths_answersheet.modifyLatest(answer=int(event.char))
        if sum(self.lst) == int(event.char):
            self.score +=1
            self.maths_answersheet.modifyLatest(status = '✓')
        self.timer = self.root.after(SECOND_MS//5, self.insert_table)

    def show_score(self):
        mb.showinfo("Result",f"score={self.score}\nattempted={self.problems}\nTarget={self.target}")
        e1.configure(state=NORMAL)
        e2.configure(state=NORMAL)
        e3.configure(state=NORMAL)
        e4.configure(state=NORMAL)
        self.maths_answersheet.saveData()
        k = disp_csv()

    def __del__(self):
        #self.root.after_cancel(self.timer)
        #print("Object deleted")
        pass

states = {
    '8_1':{'Nextstates': 'ShowResult'}
}

timer = None
t = None
def openQuiz():
    openQuizUi(window,e1,e2,e3,e4,v.get())
def func_reset_count(count=-1,state='Nokey'):

    #print(f'{count} {state}')
    global timer
    global t
    start_button["state"] = "disabled"
    button["state"] = "disabled"
    if int(e2.get())>9:
        switchtoquiz = mb.askokcancel("askokcancel", "Total greater than 9, not possible in this window Want to continue to quiz format?")
        if switchtoquiz == 1:
            openQuiz()

    if state != 'Nokey' and timer == None:
        canvas.itemconfig(timer_text, text=f'00:00')
    elif(count>0):
        count_sec = count%60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(timer_text, text=f'{count//60}:{count_sec}')
        timer = window.after(SECOND_MS, func_reset_count, count - 1,state)
    elif count == -1 and timer == None:
        if t == None:
            t = Table(window, row=3, column=1)
        #print('insert table called first time')
        t.insert_table()
        state = '8_1'
        count = int(e4.get()) *60
        canvas.itemconfig(timer_text, text=f'{count//60}:00')
        window.bind("<Key>", t.key_handler)

        timer = window.after(SECOND_MS, func_reset_count, count - 1,state)
    elif count == 0:
        func_stop()


def func_stop():
    global timer
    global t
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'00:00')
    timer = None
    t.show_score()
    #print(t)
    window.unbind("<Key>")
    del t
    t= None
    mathstution_label.config(text='mathstution')
    start_button["state"] = "normal"
    button["state"] = "normal"

window = Tk()
window.title('mathstution')
window.config(padx=100,pady=50,bg=YELLOW)
mathstution_label = Label(text='mathstution',fg = GREEN, font=(FONT_NAME,50,'bold'),bg=YELLOW)
mathstution_label.grid(row = 0,column=1)

canvas2 = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
mathstution_label = Label(canvas2,text='mathsgrade',fg = GREEN, font=(FONT_NAME,20,'bold'),bg=YELLOW)
mathstution_label.place(relx = 0.0,
                 rely = 1.0,anchor='sw')
canvas2.grid(row = 1,column=0)

canvas = Canvas(width=200,height=230,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')


canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text='00:00',fill = 'white',font=(FONT_NAME,35,'bold'))
canvas.grid(row = 1,column=1,columnspan=2)

canvas2 = Canvas(width=275,height=224,bg=YELLOW,highlightthickness=0)
mathstution_label = Label(canvas2,text='max total\n(1-9)\n >9 \nchoose quizformat',fg = GREEN, font=(FONT_NAME,20,'bold'),bg=YELLOW)
mathstution_label.place(relx = 0.0,
                 rely = 1.0,anchor='sw')
canvas2.grid(row = 0,column=3)

e1 = Entry(window, width=5, fg='blue', bg=YELLOW, justify='center',
                           font=('Arial', 16, 'bold'))
e1.grid(row=2, column=0)
e1.insert(END,'1')


e2 = Entry(window, width=5, fg='blue', bg=YELLOW, justify='center',
                           font=('Arial', 16, 'bold'))
e2.grid(row=1, column=3)
e2.insert(END,'9')

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python
def ShowChoice():
    print(v.get())
o1 = Canvas()
o1.create_text(300, 50, text="Summing model", fill="black", font=('Helvetica 15 bold'))

Radiobutton(o1, 
            text="9+9-9...",
            padx = 20, 
            variable=v, 
            command=ShowChoice,
            value=0).pack(anchor=W)
Radiobutton(o1, 
            text="maxno+9-9...",
            padx = 20, 
            variable=v, 
            command=ShowChoice,
            value=1).pack(anchor=W)

Radiobutton(o1, 
            text="maxno+maxno-maxno...",
            padx = 20, 
            variable=v, 
            command=ShowChoice,
            value=2).pack(anchor=W)


o1.grid(row=2, column=3)
Label(window, 
         text="Duration in mins").grid(row=3,column=3)
e4 = Entry(window, width=5, fg='blue', bg=YELLOW, justify='center',
                           font=('Arial', 16, 'bold'))
e4.grid(row=4, column=3)
e4.insert(END,'10')

start_button = Button(text='Start',command=func_reset_count)
start_button.grid(column=1,row=2)

Label(window, 
         text="Target").grid(row=3,column=0)
e3 = Entry(window,width=5, fg='blue', bg=YELLOW, justify='center',
                           font=('Arial', 16, 'bold'))
e3.grid(row=4, column=0)
e3.insert(END,'100')                           
button = Button(text='quiz',command=openQuiz)
button.grid(column=0,row=5)

t = Table(window, row=3, column=1)

#quizformat(window)
window.mainloop()


