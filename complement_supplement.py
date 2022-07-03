from tkinter import *
from tkinter import messagebox as mb
import random as rd
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb  
class complement_supplement:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.configure(bg=rgb_hack((255, 0, 122)))
        mathstution_label = Label(self.root,text='Complement', font=('Arial',14,'bold'), justify='center')
        mathstution_label.grid(row=0,column=0,columnspan=3,padx=2,pady=2)
        mathstution_label = Label(self.root,text='Supplement', font=('Arial',14,'bold'), justify='center')
        mathstution_label.grid(row=0,column=3,columnspan=3,padx=2,pady=2)

        for i in range(1,11):
            e = Entry(self.root, width=5, fg='blue', justify='center',
                           font=('Arial', 12, 'bold'))
            e.grid(row=i,column=0,padx=2,pady=2)
            
            e = Entry(self.root, width=5, fg='blue', justify='center',
                           font=('Arial', 12, 'bold'))
            e.grid(row=i,column=1,padx=2,pady=2)
            e = Entry(self.root, width=5, fg='blue', justify='center',
                           font=('Arial', 12, 'bold'))
            e.grid(row=i,column=2,padx=8,pady=2)
            e = Entry(self.root, width=5, fg='blue', justify='center',
                           font=('Arial', 12, 'bold'))
            e.grid(row=i,column=3,padx=2,pady=2)
            e = Entry(self.root, width=5, fg='blue', justify='center',
                           font=('Arial', 12, 'bold'))
            e.grid(row=i,column=4,padx=2,pady=2)
            e = Entry(self.root, width=5, fg='blue', justify='center',
                           font=('Arial', 12, 'bold'))
            e.grid(row=i,column=5,padx=8,pady=2)
        self.root.mainloop()

complement_supplement()
