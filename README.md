# PythonHyperTextFormMarkupLanguage
Language for making python desktop apps.

## Introduction

The PHTFML language is in base similar to html but there are some differences.

PHTFML basic structure looks like this:
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
You can read more about naming in [Spacing problems](#spacing).

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

Because if the names match for two or more elements you are not going to be able identifi them in scripts and even in other forms they would cause problems. You can read more about naming in [Naming problems](#naming-problems).

### Elements
#### Global tags
Global tags are set of tags creating different elements like for example `input` or `script`

Global tags have to be always in lower case or they will not work!
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

`NEVER PLACE TWO SAME TAGED FRAMES IN EACH OTHER`
It will result in crashing the compiler or getting stuck in middle of compiling.

Do not do this:
```html
<frame, name="frame1">
  <frame, name="frame2">
  </frame>
</frame>
```
do not do this either:
```html
<frame1, name="frame1">
  <frame2, name="frame2">
    <frame1, name="frame3">
    </frame1>
  <frame2>
</frame1>
```
You can do this:
```html
<frame1, name="frame1">
  <frame2, name="frame2">
  <frame2>
</frame1>
```
You can find why in the [compiling](#compiling) section.

#### Labels
Every element that doesn\`t have any other element inside it or doesn\`t correspond to any global tag is considered label
```
<label, name="hello">Hello World</label>
<text, name="HELLO">Hello World</text>
```
These two elements are going to be the same in the form.
#### Inputs
To create input you have to use global tag `input` for example like this:
```html
<input, name="input1"></input>
```
No else tag will create text input.
## Compiling
### Compile your script
In order to run the PSL script you need to use run this command in command prompt:
```bash
run %You script name%
```
To run the test file you can use this:
```bash
run test.phtfml
```
But you can run this only in the compiler directory.

If you want to compile scrits from other directory you need to run this still in the compiler folder:

```bash
py compiler.py %You script name or full path% %Output script name or full path%
```
So for the test file it is:
``` bash
py compiler.py test.phtfml index.py
```
or:
```html
py compiler.py %PATH%/test.phtfml %PATH%/index.py
```
### How does the compiler work?
It takes three steps to create the compiled file first we take original file:
```html
<formspace, name="project">
  <form, name="window1",dimensions="500x500">
    <label, name="sometext">Some text</label>
  </form>
</formspace>
```
And compile it to JSON style format:
```
'tag', 'formspace'
'args', ['name="project"']
'content', []
```
The content should have all the elements of formspace in it but it wont fit into here so im not going to place it there.

After this finishes the compiler takes it and converts it to `ParrentChild` that means something like this:
```
formspace -> window1
window1 -> frame1
frame1 -> text
```
From that we can finally make the fully compiled code:
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

hello = tk.Label(frame1,text="HelloWorld!")
hello.pack()

#<looping forms>
window1.mainloop()
#formspace end
```
### Naming problems
### Spacing
Spacing doesn`t cause any trouble because it is deleted by compiler first that means
from this:
```html
<input     ,name =   "name"></input>
```
the compiler makes this:
```html
<input,name="name"></input>
```
And after that it gets compiled.
So there cann\`t be used spaces in labels or names.
## License
[MIT](https://choosealicense.com/licenses/mit/)
