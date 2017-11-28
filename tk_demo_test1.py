import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar()
var2 = tk.StringVar()
l1 = tk.Label(window)
l1["textvariable"]=var1
l1["bg"]='green'
l1["font"] = ('Arial', 12)
l1["width"] = 15
l1["height"] = 2
#l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
l1.pack()
l2 = tk.Label(window, textvariable=var2, bg='red', font=('Arial', 12), width=15,
             height=2)
#l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
l2.pack()

on_hit1 = True
on_hit2 = False

def init_text():
    global on_hit2
    global on_hit1
    
    if on_hit1 == True:
        var1.set('you hit1 me')             
    else:
        var1.set('')
   
    if on_hit2 == True:    
        var2.set('you hit2 me')             
    else:      
        var2.set('')        
        
def hit1_me():
    global on_hit1
    
    if on_hit1 == False:
        on_hit1 = True
        var1.set('you hit1 me')             
    else:
        on_hit1 = False
        var1.set('')
        
    print(var1.get(),var2.get())

def hit2_me():
    global on_hit2
    
    if on_hit2 == False:
        on_hit2 = True        
        var2.set('you hit2 me')             
    else:
        on_hit2 = False        
        var2.set('')
        
    print(var1.get(),var2.get())
    
b1 = tk.Button(window, text='hit me', width=15,
              height=2, command=hit1_me)
b1.pack()
b2 = tk.Button(window, text='hit me', width=15,
              height=2, command=hit2_me)
b2.pack()

init_text()
window.mainloop()