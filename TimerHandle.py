#Import the library
from tkinter import *
SECOND_MS = 1000
class timerhandle:
   def __init__(self,gui,countins,callback=None) -> None:
      self.timer = None
      self.root = gui
      self.count = countins
      self.callback = callback
      self.t = Label(self.root, text='', 
            font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
      self.t.place(x=70,y=50)
      self.run_timer()

   def run_timer(self):
      if self.timer != None:
         self.count -= 1
         self.root.after_cancel(self.timer)
      
      if self.count>0:
         count_sec = self.count%60
         if count_sec < 10:
            count_sec = f"0{count_sec}"
         self.t.configure( text=f'{self.count//60}:{count_sec}')
         
         self.timer = self.root.after(SECOND_MS, self.run_timer)
      else:
         self.callback()
   
   def finished(self):
      self.root.after_cancel(self.timer)