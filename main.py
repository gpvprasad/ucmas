from ctypes import alignment
from tkinter import *
from tkinter import messagebox as mb
import random as rd
import csv
import pandas as pd
from ShowResult import disp_csv
from quiz import quizformat
import json

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SECOND_MS = 1000

# Python program to create a table

from tkinter import *

maths_answersheet = {
    'problem':[],
    'answer':[],
    'correct answer':[],
    'status':[]
}


def openQuizUi():
    class Point:
        target: int
        lst: list([])
    var = Point()
    var.target = int(e3.get())
    var.lst = []
    options = []
    data = {
        "question": [],
        "answer": [],
        "options": []
    }
    for i in range(var.target):
        options = []
        ucmactest(var,False)
        question = str(var.lst[0])
        for i in var.lst[1:]:
            if i<0:
                question += str(i)
            else:
                question += '+'+str(i)
        data['question'].append(question)
        options.append(sum(var.lst))
        options.append(rd.choice([i for i in range(0,int(e2.get())) if i != sum(var.lst)]))
        options.append(rd.choice([i for i in range(0,int(e2.get())) if i != sum(var.lst)]))
        options.append(rd.choice([i for i in range(0,int(e2.get())) if i != sum(var.lst)]))
        rd.shuffle(options)
        data['options'].append(options )
        data['answer'].append(options.index(sum(var.lst))+1)
    with open("data.json", "w") as outfile:
        json.dump(data, outfile,indent=4)
    
    quizformat(window)

def ucmactest(self,starting):
    self.target = int(e3.get())
    if not starting:
        e1.configure(state=DISABLED)
        e2.configure(state=DISABLED)
        e3.configure(state=DISABLED)

        self.lst = [0]*(int(e1.get())+2)
        finalmaxsum = int(e2.get())
    else:
        self.lst = [0]*3
        finalmaxsum = 9
    
    self.lst[0] = rd.randint(0,finalmaxsum)
    for i in range(1,len(self.lst)):
        self.lst[i] = rd.randint(-sum(self.lst),finalmaxsum-sum(self.lst))

class Table:

    def __init__(self, root,row,column):
        self.root = root
        self.row = row
        self.column = column
        self.timer = None
        self.e = None
        self.ans = None
        self.lst = []
        self.problems = 0
        self.score = 0
        self.insert_table(True)
        self.target = int(e3.get())
        #print('insert table called init')

    

    def insert_table(self,starting = False):
        if self.timer != None:
            self.root.after_cancel(self.timer)
        # code for creating table
        ucmactest(self,starting)
        total_rows = len(self.lst)
        #print(total_rows)
        for i in range(total_rows):
            self.e = Entry(self.root, width=5, fg='blue', bg=YELLOW, justify='center',
                           font=('Arial', 16, 'bold'))

            self.e.grid(row=i+self.row, column=self.column)
            if not starting:
                self.e.insert(END, self.lst[i])
            self.e.configure(state=DISABLED)
        if starting:
            self.ans = Entry(self.root, width=5, fg='blue',bg=YELLOW,justify='center',
                         font=('Arial', 16, 'bold'))
            self.ans.grid(row=total_rows + self.row+1, column=self.column)
        if not starting:
            self.ans.option_clear()
            self.problems += 1
            maths_answersheet['problem'].append(tuple(self.lst))
            maths_answersheet['correct answer'].append(sum(self.lst))
            maths_answersheet['answer'].append('')
            maths_answersheet['status'].append('X')
        self.ans.delete(0, END)


    def key_handler(self,event):
        #print(event.char, event.keysym, event.keycode)
        self.ans.insert(0,event.char)
        maths_answersheet['answer'][-1]=int(event.char)
        if sum(self.lst) == int(event.char):
            self.score +=1
            maths_answersheet['status'][-1]='✓'
        self.timer = self.root.after(SECOND_MS//5, self.insert_table)

    def show_score(self):
        mb.showinfo("Result",f"score={self.score}\nattempted={self.problems}\nsolved={self.target}")
        e1.configure(state=NORMAL)
        e2.configure(state=NORMAL)
        df = pd.DataFrame(maths_answersheet)
        df.to_csv('test.csv', index = False)
        #print(maths_answersheet)
        k = disp_csv()

    def __del__(self):
        #self.root.after_cancel(self.timer)
        #print("Object deleted")
        pass

states = {
    '8_1':{'Nextstates': 'ShowResult','values': 8*60}
}

timer = None
t = None

def func_reset_count(count=-1,state='Nokey'):

    #print(f'{count} {state}')
    global timer
    global t
    if int(e2.get())>9:
        switchtoquiz = mb.askokcancel("askokcancel", "Total greater than 9, not possible in this window Want to continue to quiz format?")
        if switchtoquiz == 1:
            openQuizUi()

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
        count = states[state]['values']
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

window = Tk()
window.title('mathstution')
window.config(padx=100,pady=50,bg=YELLOW)
mathstution_label = Label(text='mathstution',fg = GREEN, font=(FONT_NAME,50,'bold'),bg=YELLOW)
mathstution_label.grid(row = 0,column=1)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')

mathstution_label = Label(text='mathsgrade',fg = GREEN, font=(FONT_NAME,20,'bold'),bg=YELLOW)
mathstution_label.grid(row = 1,column=0)

canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text='00:00',fill = 'white',font=(FONT_NAME,35,'bold'))
canvas.grid(row = 1,column=1,columnspan=2)

mathstution_label = Label(text='max total(1-9)',fg = GREEN, font=(FONT_NAME,20,'bold'),bg=YELLOW)
mathstution_label.grid(row = 1,column=3)

e1 = Entry(window, width=5, fg='blue', bg=YELLOW, justify='center',
                           font=('Arial', 16, 'bold'))
e1.grid(row=2, column=0)
e1.insert(END,'1')


e2 = Entry(window, width=5, fg='blue', bg=YELLOW, justify='center',
                           font=('Arial', 16, 'bold'))
e2.grid(row=2, column=3)
e2.insert(END,'9')

start_button = Button(text='Start',command=func_reset_count)
start_button.grid(column=1,row=2)

Label(window, 
         text="Target").grid(row=3,column=0)
e3 = Entry(window,width=5, fg='blue', bg=YELLOW, justify='center',
                           font=('Arial', 16, 'bold'))
e3.grid(row=4, column=0)
e3.insert(END,'100')                           
button = Button(text='quiz',command=openQuizUi)
button.grid(column=0,row=5)

t = Table(window, row=3, column=1)

#quizformat(window)
window.mainloop()
