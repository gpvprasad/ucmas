from tkinter import *
from tkinter import messagebox as mb
import random as rd
from turtle import title
from genericfunctions import *
class complement_supplement:
    def __init__(self,text1,validationfunction,text2=None,noofRows=10,noofColumns=6) -> None:
        if noofColumns == 4 or noofColumns == 5 :
            self.columnspan = int(noofColumns)
        elif noofColumns %3 !=0:
            raise NameError("two operads with one operator possible, last column to show result")
        elif noofColumns %3 ==0:
            if text2 == None:
                noofColumns = 3
                self.columnspan = int(noofColumns)
            else:
                self.columnspan = int(noofColumns/2)
        self.root = Tk()
        self.validationfunction = validationfunction

        self.root.config(padx=1,pady=2)
        self.root.configure(bg=rgb_hack((0xff, 0x00, 0x7f)))
        

        mathstution_label = Label(self.root,text=text1, font=('Arial',14,'bold'), justify='center')
        mathstution_label.grid(row=0,column=0,columnspan=self.columnspan,padx=2,pady=2)
        if text2 != None:
            mathstution_label = Label(self.root,text=text2, font=('Arial',14,'bold'), justify='center')
            mathstution_label.grid(row=0,column=3,columnspan=self.columnspan,padx=2,pady=2)

        self.ent = {}
        for i in range(1,noofRows+1):
            self.ent[i] = []
            for j in range(0,noofColumns):
                self.ent[i].append(Entry(self.root, width=5, fg='blue', justify='center',
                            font=('Arial', 12, 'bold')))
                if j != self.columnspan-1 and j!=(self.columnspan*2-1):
                    self.ent[i][-1].grid(row=i,column=j,padx=2,pady=2)
                else:
                    self.ent[i][-1].grid(row=i,column=j,padx=8,pady=2)
        self.validate_button = Button(self.root,text='Validate',command=self.CorrectAnswers)
        self.validate_button.grid(column=noofColumns-1,row=i+1)
    
    def startdisplay(self):
        self.root.mainloop()
    
    def CorrectAnswers(self):
        for key,value in self.ent.items():
            if len(value) ==6:
                x = self.validationfunction(int(value[0].get()),int(value[1].get()),int(value[3].get()),int(value[4].get()))
                value[2].configure(state=NORMAL)
                value[2].delete(0, END)
                value[2].insert(END,x[0])
                value[2].configure(state=DISABLED)
                value[5].configure(state=NORMAL)
                value[5].delete(0, END)
                value[5].insert(END,x[1])
                value[5].configure(state=DISABLED)
            elif len(value) == 4:
                x = self.validationfunction(int(value[0].get()),int(value[1].get()),e = int(value[2].get()))
                value[3].configure(state=NORMAL)
                value[3].delete(0, END)
                value[3].insert(END,x[0])
                value[3].configure(state=DISABLED)
            elif len(value) == 5:
                x = self.validationfunction(int(value[0].get()),int(value[1].get()),e = int(value[2].get())+int(value[3].get()))
                value[4].configure(state=NORMAL)
                value[4].delete(0, END)
                value[4].insert(END,x[0])
                value[4].configure(state=DISABLED)
            else:
                x = self.validationfunction(int(value[0].get()),int(value[1].get()))
                value[2].configure(state=NORMAL)
                value[2].delete(0, END)
                value[2].insert(END,x[0])
                value[2].configure(state=DISABLED)
        if x[0] == '✓' or x[0] == 'X':
            self.validate_button.configure(state=DISABLED)
    
    def filldata(self,group1:list,group2=None,group3=None):
        if self.columnspan%3 ==0 :
            for i in range(0,len(group1)):
                if type(group1[i])!=tuple:
                    raise NameError("Only two operands needed")
                if len(group1) != len(self.ent):
                    raise NameError("Mismatch in size")
                todisp = rd.choice(range(0,len(group1[i])))
                self.ent[i+1][todisp].insert(END,group1[i][todisp]) 
                self.ent[i+1][todisp].configure(state=DISABLED)
                self.ent[i+1][self.columnspan-1].configure(state=DISABLED)

            if group2 != None:
                for i in range(0,len(group2)):
                    if type(group2[i])!=tuple:
                        raise NameError("Only two operands needed")
                    if len(group2) != len(self.ent):
                        raise NameError("Mismatch in size")
                    todisp = rd.choice(range(0,len(group2[i])))
                    self.ent[i+1][todisp+self.columnspan].insert(END,group2[i][todisp]) 
                    self.ent[i+1][todisp+self.columnspan].configure(state=DISABLED)
                    self.ent[i+1][self.columnspan+self.columnspan-1].configure(state=DISABLED)
        elif self.columnspan == 4 or self.columnspan == 5:
            for i in range(0,len(group1)):
                if type(group1[i])!=tuple:
                    raise NameError("Only two operands needed")
                if len(group1) != len(self.ent):
                    raise NameError("Mismatch in size")
                self.ent[i+1][0].insert(END,group1[i][0]) 
                self.ent[i+1][0].configure(state=DISABLED)
                if isinstance(group2, list):
                    self.ent[i+1][1].insert(END,group2[i]) 
                else:
                    self.ent[i+1][1].insert(END,group2) 
                self.ent[i+1][1].configure(state=DISABLED)
                if group3 != None:
                    self.ent[i+1][2].insert(END,group3) 
                    self.ent[i+1][2].configure(state=DISABLED)
                self.ent[i+1][self.columnspan-1].configure(state=DISABLED)
    def refershdata(self,group1:list,group2=None,group3=None):
        if self.columnspan == 4:
            for i in range(0,len(group1)):
                if type(group1[i])!=tuple:
                    raise NameError("Only two operands needed")
                if len(group1) != len(self.ent):
                    raise NameError("Mismatch in size")
                self.ent[i+1][0].configure(state="normal")
                self.ent[i+1][0].delete(0, END)
                self.ent[i+1][0].insert(END,group1[i][0]) 
                self.ent[i+1][0].configure(state=DISABLED)
                self.ent[i+1][1].configure(state="normal")
                self.ent[i+1][1].delete(0, END)
                if isinstance(group2, list):
                    self.ent[i+1][1].insert(END,group2[i]) 
                else:
                    self.ent[i+1][1].insert(END,group2) 
                self.ent[i+1][1].configure(state=DISABLED)



