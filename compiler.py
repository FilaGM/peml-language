import sys
from compiler_lib import *
import tkinter as tk
file = open(sys.argv[1],"r")

file = file.read()

compiledFile = compileToElement(file)

command = compileToCommand(compiledFile)

compiled = open("index.py","w")
compiled.write("import tkinter as tk\n")
for arg in compiledFile["args"]:
    if(getArgumentFromString(arg)["name"] == "name"):
        compiled.write("#namespace "+getArgumentFromString(arg)["content"] + "\n")

formTags = []
for i in command:
    found = False
    args = i.element["args"]
    for a in command:
        if(i.element["tag"] == a.parrent["tag"]):
            found = True
    if(found == True and i.element["tag"] != "form"):
        width = "100"
        height = "100"
        if(argumentExists("width",args)):
            width = getArgument("width", args)["content"]
        compiled.write(i.element["tag"] + " = tk.Frame("+i.parrent["tag"]+",width=\""+width+"\",height=\""+height+"\")\n")

    if(found == True and i.element["tag"] == "form"):
        i.element["tag"] = getArgument("name",args)["content"]
        compiled.write("#==formspace " + i.element["tag"] + "==\n")
        compiled.write(i.element["tag"] + " = tk.Tk()\n")
        compiled.write(i.element["tag"] + ".geometry(\"" + getArgument("dimensions",args)["content"] + "\")\n")
        if(argumentExists("title",args)):
            compiled.write(i.element["tag"] + ".title(\""+getArgument("title",args)["content"]+"\")")
        else:
            compiled.write(i.element["tag"] + ".title(\""+i.element["tag"]+"\")")
        formTags.append(i.element["tag"])

compiled.write("#<looping form>\n")
for i in formTags:
    compiled.write(i + ".mainloop()\n")

compiled.write("#namespace end")
