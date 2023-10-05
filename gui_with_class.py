import tkinter as tk
from tkinter import messagebox as msgbox

class MyGUI:
    def __init__(self) -> None:
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Close', command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Close no qs', command=exit)

        self.actionmenu = tk.Menu(self.menubar,tearoff=0)
        self.actionmenu.add_command(label='Show message', command=self.show_message)
        

        self.menubar.add_cascade(menu = self.filemenu, label='File')
        self.menubar.add_cascade(menu = self.actionmenu, label='Action')

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root,text='Your Message',font=('Arial',18))
        self.label.pack(padx=10,pady=10)

        self.textbox = tk.Text(self.root,height=5,font=('Arial',18))
        self.textbox.bind('<KeyPress>', self.shortcut)
        self.textbox.pack(padx=10,pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root,text='Show messagebox',font=('Arial',18),variable=self.check_state)
        self.check.pack(padx=10,pady=10)
        
        self.button = tk.Button(self.root, text='Show message',font=('Arial',18),command=self.show_message)
        self.button.pack(padx=10,pady=10)
        
        self.clearbtn = tk.Button(self.root, text='Clear All',font=('Arial',18),command=self.clear)
        self.clearbtn.pack(padx=10,pady=10)

        self.root.protocol('WM_DELETE_WINDOW',self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get()==0:
            print(self.textbox.get('1.0',tk.END))
        else:
            msgbox.showinfo(title='Message',message=self.textbox.get('1.0',tk.END))
    
    def shortcut(self,event):
        if event.keysym == 'Return' and event.state == 12:
            self.show_message()

    def on_closing(self):
        if msgbox.askyesno(title='Quit?',message='Do you really want to leave?'):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0',tk.END)

MyGUI()

        