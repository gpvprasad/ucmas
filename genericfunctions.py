import random as rd
from tkinter import *
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb  

def ucmactest(self,starting,e1,e2,e3,e4,ucmacs_typ=0,nextLevel=False):
    finalmaxsum = 9 
    self.target = int(e3.get())
    if not starting:
        if(nextLevel == False):
            self.lst = [0]*(int(e1.get())+2)
        else:
            self.lst = [0]*(rd.choice([int(e1.get()),int(e1.get())+1])+2)
        finalmaxsum = int(e2.get())
        
        if ucmacs_typ == 0:
            finalmaxsum = 9
    else:
        self.lst = [0]*3
    if finalmaxsum >0:
        self.lst[0] = rd.randint(0,finalmaxsum)
    else:
        self.lst[0] = rd.randint(finalmaxsum,-finalmaxsum)
    if ucmacs_typ == 0:
        finalmaxsum = 9
    for i in range(1,len(self.lst)):
        nextnumber  = 0
        while nextnumber == 0:
            if finalmaxsum >0:
                nextnumber = rd.randint(-sum(self.lst),finalmaxsum-sum(self.lst))
            else:
                nextnumber = rd.randint(finalmaxsum,-finalmaxsum)
                if sum(self.lst) +nextnumber < finalmaxsum or sum(self.lst) +nextnumber > -finalmaxsum or nextnumber < finalmaxsum or nextnumber > -finalmaxsum:
                    nextnumber = 0
        self.lst[i] = nextnumber
    return self.lst
