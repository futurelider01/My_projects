import tkinter as tk

root = tk.Tk()

font = ('Arial',18)

root.geometry('500x500')
root.title('My first GUI')

label = tk.Label(root,text='Hello world',font=font)
label.pack(padx=20,pady=20)

textbox = tk.Text(root,height=3,font=('Arial',16))
textbox.pack(padx=10,pady=10)

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0,weight=1)
buttonFrame.columnconfigure(1,weight=1)
buttonFrame.columnconfigure(2,weight=1)

btn1 = tk.Button(buttonFrame,text='1', font = font)
btn1.grid(column=0,row=0,sticky=tk.W+tk.E)

btn2 = tk.Button(buttonFrame,text='2', font = font)
btn2.grid(column=1,row=0,sticky=tk.W+tk.E)

btn3 = tk.Button(buttonFrame,text='3', font = font)
btn3.grid(column=2,row=0,sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame,text='4', font = font)
btn4.grid(column=0,row=1,sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame,text='5', font = font)
btn5.grid(column=1,row=1,sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame,text='6', font = font)
btn6.grid(column=2,row=1,sticky=tk.W+tk.E)

buttonFrame.pack(fill='x')

root.mainloop()