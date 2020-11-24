import tkinter as tk
#formspace project
#==form init window1==
window1 = tk.Tk()
window1.geometry("500x500")
window1.title("window1")
#==form init window1==

frame1 = tk.Frame(window1,width="100",height="100")
frame1.pack()

sometext1 = tk.Label(frame1,text="HelloWorld!")
sometext1.pack()

frame2 = tk.Frame(window1,width="100",height="100")
frame2.pack()

sometext2 = tk.Label(frame2,text="HelloWorld!")
sometext2.pack()

frame3 = tk.Frame(window1,width="100",height="100")
frame3.pack()

sometext3 = tk.Label(frame3,text="HelloWorld!")
sometext3.pack()

#<looping forms>
window1.mainloop()
#formspace end