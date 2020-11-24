import tkinter as tk
#formspace project
#==form init window1==
window1 = tk.Tk()
window1.geometry("500x500")
window1.title("window1")
#==form init window1==

frame1 = tk.Frame(window1,width="100",height="100")
frame1.pack()

frame2 = tk.Frame(frame1,width="100",height="100")
frame2.pack()

hello = tk.Label(frame2,text="Hello")
hello.pack()

hello = tk.Label(frame2,text="Hell")
hello.pack()

#<looping forms>
window1.mainloop()
#formspace end