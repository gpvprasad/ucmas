# from tkinter import *
# class Checkbar(Frame):
#    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
#       Frame.__init__(self, parent)
#       self.vars = []
#       for pick in picks:
#          var = IntVar()
#          chk = Checkbutton(self, text=pick, variable=var)
#          chk.pack(side=side, anchor=anchor, expand=YES)
#          self.vars.append(var)
#    def state(self):
#       return map((lambda var: var.get()), self.vars)
# if __name__ == '__main__':
#    root = Tk()
#    lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
#    tgl = Checkbar(root, ['English','German'])
#    lng.pack(side=TOP,  fill=X)
#    tgl.pack(side=LEFT)
#    lng.config(relief=GROOVE, bd=2)

#    def allstates(): 
#       print(list(lng.state()), list(tgl.state()))
#    Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
#    Button(root, text='Peek', command=allstates).pack(side=RIGHT)
#    root.mainloop()

import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python
o1 = tk.Canvas()

languages = [("Python"),
   	     ("Perl"),
    	     ("Java"),
             ("C++"),
             ("C")]

def ShowChoice():
    languages.reverse()
    for language in languages:
        tk.Radiobutton(o1, 
                    text=language,
                    padx = 20, 
                    variable=v, 
                    command=ShowChoice,
                    value=i).pack(anchor=tk.W)

tk.Label(o1, 
         text="""Choose your favourite 
programming language:""",
         justify = tk.LEFT,
         padx = 20).pack()
i =0 
for language in languages:
    tk.Radiobutton(o1, 
                   text=language,
                   padx = 20, 
                   variable=v, 
                   command=ShowChoice,
                   value=i).pack(anchor=tk.W)
    i +=1
o1.grid(row = 0,column=1)

root.mainloop()