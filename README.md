# PythonStructuralLanguage
Language for making python desktop apps.

## Syntax

The PSL language is in base similar to html but there are some differences.

When you are using HTML u would do this to make basic structure for your web page:
```html
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <label>Some text</label>
  </body>
</html>
```
##But in PSL it look like this:
```html
<formspace,name="project">
  <form,name="window1",dimensions="500x500">
    <label,name="sometext">Some text</label>
  </form>
</formspace>
```
The compiler compiles it to this script that is executable via python:
```python
import tkinter as tk
#formspace project
#==form init window1==
window1 = tk.Tk()
window1.geometry("500x500")
window1.title("window1")
#==form init window1==

sometext = tk.Label(window1,text="Sometext")
sometext.pack()

#<looping forms>
window1.mainloop()
#formspace end
```
