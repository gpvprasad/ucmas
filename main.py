from ctypes import alignment
from tkinter import *
import random as rd
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SECOND_MS = 1000

# Python program to create a table

from tkinter import *


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
        print('insert table called init')

    def ucmactest(self):
        self.lst = [0,0,0]
        self.lst[0] = rd.randint(0,9)
        self.lst[1] = rd.randint(-self.lst[0],9-self.lst[0])
        self.lst[2] = rd.randint(-sum(self.lst),9-sum(self.lst))

    def insert_table(self,starting = False):
        if self.timer != None:
            self.root.after_cancel(self.timer)
        # code for creating table
        self.ucmactest()
        total_rows = len(self.lst)
        for i in range(total_rows):
            self.e = Entry(self.root, width=5, fg='blue', bg=YELLOW, justify='center',
                           font=('Arial', 16, 'bold'))

            self.e.grid(row=i+self.row, column=self.column)
            if not starting:
                self.e.insert(END, self.lst[i])
            self.e.configure(state=DISABLED)
        self.ans = Entry(self.root, width=5, fg='blue',bg=YELLOW,justify='center',
                         font=('Arial', 16, 'bold'))
        self.ans.grid(row=total_rows + self.row+1, column=self.column)
        if not starting:
            self.problems += 1
        self.ans.insert(END,'')


    def key_handler(self,event):
        print(event.char, event.keysym, event.keycode)
        self.ans.insert(END,event.char)
        if sum(self.lst) == int(event.char):
            self.score +=1
        print('insert table called key handler')
        self.timer = self.root.after(SECOND_MS//5, self.insert_table)

    def show_score(self):
        canvas.itemconfig(timer_text, text=f'{self.score}/{self.problems}')

    def __del__(self):
        self.root.after_cancel(self.timer)
        print("Object deleted")

states = {
    '8_1':{'Nextstates': 'ShowResult','values': 8*60}
}

timer = None
t = None

def func_reset_count(count=-1,state='Nokey'):

    #print(f'{count} {state}')
    global timer
    global t
    if state != 'Nokey' and timer == None:
        canvas.itemconfig(timer_text, text=f'00:00')
    elif(count>0):
        count_sec = count%60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        elif count_sec == 10:
            check_marks.config(text='')
        canvas.itemconfig(timer_text, text=f'{count//60}:{count_sec}')
        timer = window.after(SECOND_MS, func_reset_count, count - 1,state)
    elif count == -1 and timer == None:
        if t == None:
            t = Table(window, row=4, column=1)
        print('insert table called first time')
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
    print(t)
    window.unbind("<Key>")
    del t
    t= None
    mathstution_label.config(text='mathstution')
    check_marks.config(text='')


window = Tk()
window.title('mathstution')
window.config(padx=100,pady=50,bg=YELLOW)
mathstution_label = Label(text='mathstution',fg = GREEN, font=(FONT_NAME,50,'bold'),bg=YELLOW)
mathstution_label.grid(row = 0,column=1)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')

canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text='00:00',fill = 'white',font=(FONT_NAME,35,'bold'))
canvas.grid(row = 1,column=1)

start_button = Button(text='Start',command=func_reset_count)
start_button.grid(column=0,row=2)

check_marks = Label(text='',bg=YELLOW,fg=GREEN, font=(FONT_NAME,50,'bold'))
check_marks.grid(column=1,row=3)

t = Table(window, row=4, column=1)

window.mainloop()