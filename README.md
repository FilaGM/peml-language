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
You can see that we have two main parts the `<formspace>` and the `<form>`

The `<formspace>` is place where all the forms. That means that we can initialized how many forms we want.

The `<form>` is how we initialize a form (window), there always has to be at least one element in the form. You can find why in the [compiling](#compiling) section.

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

### Attributes

In order to make a valid attribute for a element like `name` you need to follow those rules:

Lets say that you need to add a `name` attribute to this label
```html
<label>Hello World!</label>
```
First you make `,` after the last attribute or tag like this
```html
<label,>Hello World!</label>
```
Then you add attribute name for us it is `name` and we add `=`:
```html
<label, name=>Hello World!</label>
```
Now you only add the attribute value and you are done:
```html
<label, name="sometext">Hello World!</label>
```
The `,` is very important because of the way the compiler compiles the argument you can find more about the compiling process in the [compiling](#compiling) section.

It doesn\`t matter if there is the space after the `,` because the compiler deletes it in the process of compiling
You can read more about naming in [Spacing problems](#spacing-problems).

#### Every element can have currently this attributes:

`name="string"` every element should have this attribute

`x="number"` number representing a integer or float

`y="number"` number representing a integer or float

`width="number"` number representing a integer or float

`height="number"` number representing a integer or float

#### Attribute -> `Name`

This attribute has to be in every element or you are going to run in problems.

You have to add `name` attribute value for every element different like:

 ```name="example1"``` and ```name="example2"```

Because if the names match for two or more elements you are not going to be able identifi them in scripts. You can read more about naming in [Naming problems](#naming-problems).

### Elements
#### Frames
There is no such thing as `div` or other frames like in HTML

Because every element that has other elements in it is considered frame (Not counting the `<formspace>` that is special case).
```html
<div, name="frame1">
  <label, name="sometext1">Hello World!</label>
</div>
<dwa, name="frame2">
  <label, name="sometext2">Hello World!</label>
</dwa>
<whatever, name="frame3">
  <label, name="sometext3">Hello World!</label>
</whatever>
```
So all of these are going to work the same way.

They are going to be compiled like this:
```python
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
```



## Compiling
### Naming problems
### Spacing problems

## License
[MIT](https://choosealicense.com/licenses/mit/)
