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


# +
#Helper functions
# -

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

def validateFunctionMultiplication(a,b,e):
    if (a*b == e):
        return ('✓','✓')
    else:
        return ('X','X')


# +
# selection panel

# +
root = Tk()
root.geometry("900x450")
  
w = LabelFrame(root, text ='Choose Activities', font = "50",padx=20, pady=20) 
w.pack(pady=20, padx=20)
  
CS = IntVar()  
T1T2 = IntVar()  
TablesMul = IntVar()
TestAddSub = IntVar()
MultiplicationTest = IntVar()
sumOfNNumbers = IntVar()

Button1 = Checkbutton(w, text = "Complement & Supplement", 
                      variable = CS,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,width =150,anchor="w")
Button1.pack()  

Button2 = Checkbutton(w, text = "Test 1 (0 = 5-5) & Test 2 (0 = 10-5-5) ",
                      variable = T1T2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,width =150,anchor="w")
Button2.pack()

Button3 = Checkbutton(w, text = "Tables 1 to 10",
                      variable = TablesMul,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,width =150,anchor="w")  
Button3.pack()
c0 = Frame(w,highlightbackground="green",highlightthickness=2)
Button4 = Checkbutton(c0, text = "Sum of N Numbers",
                      variable = sumOfNNumbers,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,anchor="w")  
Button4.grid(row=0,column = 0,rowspan = 2)
Label(c0,text = "N").grid(row =0,column =1)
e0 = IntVar(value =10 )
ex = Entry(c0, width=5, fg='blue', justify='center',textvariable=e0)
ex.grid(row=1, column=1)
c0.pack(anchor=W)

#addition substraction configuration
c0 = Frame(w,highlightbackground="green",highlightthickness=2,width=800)
Button5 = Checkbutton(c0, text = "Addition substraction test",
                      variable = TestAddSub,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,anchor="w")  
Button5.grid(row=0,column = 0,rowspan = 2)
Label(c0,text = "maths grade").grid(row =0,column =1)

e1 = IntVar(value =1 )
ex = Entry(c0, width=5, fg='blue', justify='center',textvariable=e1)
ex.grid(row=1, column=1)

e3 = IntVar(value = 100)
Label(c0,text="Target").grid(row=0,column=2)
ex = Entry(c0,width=5, fg='blue',  justify='center',textvariable=e3)
ex.grid(row=1, column=2)
Label(c0,text='max sum').grid(row = 0,column=3)

e2 = IntVar(value=9)
ex = Entry(c0, width=5, fg='blue', justify='center',textvariable=e2)
ex.grid(row=1, column=3)
c0.pack(anchor="w")

Label(c0,text="Duration in mins").grid(row=0,column=4)
e4 = IntVar(value = 10)
ex = Entry(c0, width=5, fg='blue', bg=YELLOW, justify='center',textvariable=e4)
ex.grid(row=1, column=4)

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python
def ShowChoice():
    print(v.get())
o1 = Canvas(c0)
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

o1.grid(row=0, column=5,rowspan=2)
#multiplication configuration
c1 = Frame(w,highlightbackground="green",highlightthickness=2,width=800)
Button6 = Checkbutton(c1, text = "Multiplication test",
                      variable = MultiplicationTest,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,anchor="w")  
# Create the entry box
entry_var = StringVar()
entry_box = Entry(c1, textvariable=entry_var)
maxnumber = Label(c1,
                      text = "enter max multiplication number",highlightbackground="blue",highlightthickness=2)
Button6.grid(row = 0,column=0)
maxnumber.grid(row = 0,column=1)
entry_box.grid(row = 0,column=2)
c1.pack(anchor="w")
b1 = Button(w,text='Start',command=root.destroy,anchor="w")
b1.pack()
mainloop() 

# +
# complement supplement
# -

if CS.get() == 1:
    complementsummassion = cs.complement_supplement('Complement',validateFunction,'Supplement',10)
    group1=[(i,5-i) for i in range(0,5)]*2
    rd.shuffle(group1)
    group2 = [(i,10-i) for i in range(0,10)]
    rd.shuffle(group2)
    complementsummassion.filldata(group1=group1,group2=group2)
    complementsummassion.startdisplay()

if T1T2.get() ==1:
    group1 = [(i,10-i) for i in range(1,11)]
    T1test = cs.complement_supplement('Test 1 (0 = 5-5)',validateFunction,noofRows = len(group1),noofColumns=4)
    T1test.filldata(group1=group1,group2=5)
    group1 = [(i,10-i) for i in range(1,11)]
    T2test = cs.complement_supplement('Test2 (0 = 10-5-5)',validateFunction,noofRows = len(group1),noofColumns=5)
    T2test.filldata(group1=group1,group2=10,group3=-5)
    T1test.startdisplay()
    T2test.startdisplay()

# +
#Tables 1 to 10
# -

if TablesMul.get() ==1:
    for j in range(1,11):
        group1 = [(i,10-i) for i in range(1,10)]
        complementsummassion = cs.complement_supplement('Multiplication '+str(j),validateFunctionMultiplication,noofRows = len(group1),noofColumns=4)
        complementsummassion.filldata(group1=group1,group2=j)
        complementsummassion.startdisplay()

sumN = 0
posN =0
def valSumNnumbers(a,b,c=5,d=5,e=None,f=None):
    global sumNTest,posN,sumN
    #print(a,b,c,d,e)
    
    if e == b+a and posN == e0.get():
        return ('✓')
    elif e == b+a:
        sumN +=posN
        group1 = [(sumN,1)]
        posN+=1
        sumNTest.refershdata(group1=group1,group2=posN)
        return ('-')
    else:
        return ('X')
if sumOfNNumbers.get() ==1:
    sumNTest = cs.complement_supplement('Sum of ' +str(e0.get())+' numbers',valSumNnumbers,noofRows=1,noofColumns=4)
    group1 = [(sumN,1)]
    posN+=1
    sumNTest.filldata(group1=group1,group2=posN)
    sumNTest.startdisplay()


# Python program to create a table for ucmas test

class Table:

    def __init__(self, root,row,column):
        self.root = root
        self.c0 = Frame(self.root,highlightbackground="green",highlightthickness=2)
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

        if not starting:
            for slave in self.e:
                slave.grid_forget()
            self.e = []
        #print(f"Number of items {total_rows} itesms{self.lst} it's sum is {sum(self.lst)}")
        for i in range(total_rows):
            self.e.append( Entry(self.c0, width=5, fg='blue', bg=YELLOW, justify='center',
                        font=('Arial', 16, 'bold')))

            self.e[i].grid(row=i, column=self.column)
            if not starting:
                self.e[i].insert(END, self.lst[i])
            self.e[i].configure(state=DISABLED)
        if starting:
            self.ans = Entry(self.c0, width=5, fg='blue',bg=YELLOW,justify='center',
                         font=('Arial', 16, 'bold'))
            self.ans.grid(row=total_rows +1, column=self.column)
            
        if not starting:
            self.ans.grid(row=total_rows + 1, column=self.column)
            self.ans.option_clear()
            self.problems += 1
            self.maths_answersheet.addData(problem = tuple(self.lst),correct_answer = sum(self.lst),answer='',status = 'X')
            self.ans.delete(0, END)
        self.c0.grid(row= self.row,column = self.column)

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
            t = Table(window, row=3, column=0)
        #print('insert table called first time')
        t.insert_table()
        state = '8_1'
        count = int(e4.get()) *60
        canvas.itemconfig(timer_text, text=f'{count//60}:00')
        window.bind("<Key>", t.key_handler)

        timer = window.after(SECOND_MS, func_reset_count, count - 1,state)
    elif count == 0:
        func_stop()


if TestAddSub.get()==1:
    window = Tk()
    if int(e2.get())>9:
        print('opening quiz')
        openQuizUi(window,e1,e2,e3,e4,v.get())
    else:
        window.title('mathstution')
        window.config(padx=100,pady=50,bg=YELLOW)
        mathstution_label = Label(text='mathstution',fg = GREEN, font=(FONT_NAME,50,'bold'),bg=YELLOW)
        mathstution_label.grid(row = 0,column=0)

        canvas = Canvas(width=200,height=230,bg=YELLOW,highlightthickness=0)
        tomato_img = PhotoImage(file='tomato.png')

        canvas.create_image(100,112,image=tomato_img)
        timer_text = canvas.create_text(103,130,text='00:00',fill = 'white',font=(FONT_NAME,35,'bold'))
        canvas.grid(row = 1,column=0,columnspan=2)

        start_button = Button(text='Start',command=func_reset_count)
        start_button.grid(row=2,column=0)

        t = Table(window, row=3, column=0)

    window.mainloop()

# +
# Multiplication of random numbers
# -

if MultiplicationTest.get() ==1:
    if len(entry_var.get()) == 0:
        group1 = [(rd.randint(1, 9),10-i) for i in range(1,10)]
        complementsummassion = cs.complement_supplement('Multiplication Test',validateFunctionMultiplication,noofRows = len(group1),noofColumns=4)
        complementsummassion.filldata(group1=group1,group2=[rd.randint(1, 10) for i in range(1,10)])
    else:
        group1 = [(rd.randint(1, int(entry_var.get())),10-i) for i in range(1,10)]
        complementsummassion = cs.complement_supplement('Multiplication Test',validateFunctionMultiplication,noofRows = len(group1),noofColumns=4)
        complementsummassion.filldata(group1=group1,group2=[rd.randint(1, int(entry_var.get())) for i in range(1,10)])
    complementsummassion.startdisplay()
