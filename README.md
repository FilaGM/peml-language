# PythonStructuralLanguage
Language for making python desktop apps.

## Introduction

The PSL language is in base similar to html but there are some differences.

PSL basic structure looks like this:
```html
<formspace, name="project">
  <form, name="window1",dimensions="500x500">
    <label, name="sometext">Some text</label>
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
## Syntax

### Add attribute to element

In order to make a valid attribute for a element like `name` you need to follow those rules:

Lets say that you need to add a `name` attribute to this label
```html
<label>Hello World!</label>
```
First you make `,` after the last attribute or tag like this
```html
<label,>Hello World!</label>
```
Then you add attribute name for us it is `name` whit `=`:
```html
<label, name=>Hello World!</label>
```
Now you only add the attribute value and you are done:
```html
<label, name="sometext">Hello World!</label>
```
The `,` is very important because of the way the compiler compiles the argument you can find more about the compiling process in the [compiling](#compiling) section.

It doesn\`t matter if there is the space after the `,` because the compiler deletes it in the process of compiling

### Name attribute

This attribute has to be in every element or you are going to run in problems.
You can read more about naming in [naming](#naming problems).

You have to add `name` attribute for every element like ```name="example"```
because if the names mach for two or more elements you are not going to be able identifi them in scripts.

## Compiling
### naming problems

## License
[MIT](https://choosealicense.com/licenses/mit/)
