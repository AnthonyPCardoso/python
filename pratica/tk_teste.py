from tkinter import *

def double(event):                           

    print("Double Click, so let's stop") 

widget = Button(None, text='Mouse Clicks')

widget.pack()

widget.bind('<Double-1>', double) 

widget.mainloop()