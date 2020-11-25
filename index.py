import tkinter as tk
#formspace project
#==form init window1==
window1 = tk.Tk()
window1.geometry("500x500")
mainFormCanvas_window1 = tk.Canvas(window1,width=500,height=500)
window1.title("window1")
mainFormCanvas_window1.place(x=0,y=0)
#==form init window1==

sometext0 = tk.Label(window1,text="Sometext")
sometext0.pack()

hello = tk.Entry(window1)
hello.place(x=200,y=100,width=290,height=100)
#<looping forms>
window1.mainloop()
#formspace end