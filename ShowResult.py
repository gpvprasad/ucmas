from tkinter import *
import tkinter.ttk as ttk
import csv
class disp_csv:
    def __init__(self):
        self.root = Tk()
        self.root.title("Python - Import CSV File To Tkinter Table")
        width = 600
        height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)


        TableMargin = Frame(self.root, width=600)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("problem", "correct answer", "answer","status"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('problem', text="Problem", anchor=W)
        tree.heading('correct answer', text="Correct Answer", anchor=W)
        tree.heading('answer', text="Submitted Answer", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0,width=0)
        tree.column('#1', stretch=NO, minwidth=0)
        tree.column('#2', stretch=NO, minwidth=0)
        tree.column('#3', stretch=NO, minwidth=0)
        tree.tag_configure('✓',background='green')
        tree.tag_configure('X',background='yellow')
        tree.pack()

        with open('test.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                tree.insert("", 0, values=tuple([row[r] for r in row.keys()]),tags=(row[list(row.keys())[-1]],))


