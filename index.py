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

#==form init window2==
window2 = tk.Tk()
window2.geometry("500x500")
window2.title("window2")
#==form init window2==

frame3 = tk.Frame(window2,width="100",height="100")
frame3.pack()

frame4 = tk.Frame(frame1,width="100",height="100")
frame4.pack()

hello1 = tk.Label(frame4,text="Hello")
hello1.pack()

hello2 = tk.Label(frame4,text="Hell")
hello2.pack()

#<looping forms>
window1.mainloop()
window2.mainloop()
#formspace end