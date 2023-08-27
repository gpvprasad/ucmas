import random as rd
from tkinter import *
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb  

def ucmactest(self,starting,e1,e2,e3,e4,ucmacs_typ=0,nextLevel=False):
    finalmaxsum = 9 
    self.target = int(e3.get())
    if not starting:
        e1.configure(state=DISABLED)
        e2.configure(state=DISABLED)
        e3.configure(state=DISABLED)
        e4.configure(state=DISABLED)
        if(nextLevel == False):
            self.lst = [0]*(int(e1.get())+2)
        else:
            self.lst = [0]*(rd.choice([int(e1.get()),int(e1.get())+1])+2)
        finalmaxsum = int(e2.get())
        
        if ucmacs_typ == 0:
            finalmaxsum = 9
    else:
        self.lst = [0]*3
    self.lst[0] = rd.randint(0,finalmaxsum)
    if ucmacs_typ == 1:
        finalmaxsum = 9
    for i in range(1,len(self.lst)):
        self.lst[i] = rd.randint(-sum(self.lst),finalmaxsum-sum(self.lst))
    return self.lst
