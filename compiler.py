import sys
from compiler_lib import *
import tkinter as tk
import os
file = open(sys.argv[1],"r")

file = file.read()

compiledFile = compileToElement(file)

command = compileToCommand(compiledFile)

compiled = open(sys.argv[2],"w")
compiled.write("import tkinter as tk\n")
for arg in compiledFile["args"]:
    if(getArgumentFromString(arg)["name"] == "name"):
        compiled.write("#formspace "+getArgumentFromString(arg)["content"] + "\n")

formTags = []
for i in command:
    found = False
    args = i.element["args"]
    for a in command:
        if(i.element["tag"] == a.parrent["tag"]):
            found = True

    print(i.parrent["tag"]," -> ",i.element["tag"],"|",found)
    if(found == True and i.element["tag"] != "form"):
        width = "100"
        height = "100"
        if(argumentExists("width",args)):
            width = getArgument("width", args)["content"]
        if(argumentExists("height",args)):
            width = getArgument("height", args)["content"]
        compiled.write(getArgument("name", args)["content"] + " = tk.Frame("+i.parrent["tag"]+",width=\""+width+"\",height=\""+height+"\")\n")
        if(argumentExists("x", args) and argumentExists("y", args)):
            compiled.write(getArgument("name", args)["content"] + ".place(x=\"" + getArgument("x", args)["content"] + "\",y=\"" + getArgument("y", args)["content"] + "\")\n\n")
        else:
            compiled.write(getArgument("name", args)["content"] + ".pack()\n\n")
    elif(found == False):
        #script
        if(i.element["tag"] == "script"):
            if(argumentExists("path", args)):
                if not (os.path.exists(getArgument("path", args)["content"])):
                    compiled.write("#Failed to load the script. File dirrectory is not valid.\n")
                else:
                    compiled.write("#~script " + getArgument("name", args)["content"] + "~ START\n")
                    compiled.write(open(getArgument("path", args)["content"],"r").read())
                    compiled.write("#~script " + getArgument("name", args)["content"] + "~ END\n\n")
            else:
                compiled.write("#~script " + getArgument("name", args)["content"] + "~ START\n")
                compiled.write(getInnerText(i.element) + "\n")
                compiled.write("#~script " + getArgument("name", args)["content"] + "~ END\n\n")
        #input
        elif(i.element["tag"] == "input"):
            compiled.write(getArgument("name", args)["content"] + " = tk.Entry(" + i.parrent["tag"] + ")\n")
            if(argumentExists("x", args) and argumentExists("y", args)):
                compiled.write(getArgument("name", args)["content"] + ".place(x=\"" + getArgument("x", args)["content"] + "\",y=\"" + getArgument("y", args)["content"] + "\")\n\n")
            else:
                compiled.write(getArgument("name", args)["content"] + ".pack()\n\n")
        #label
        else:
            compiled.write(getArgument("name", args)["content"] + " = tk.Label(" + getArgument("name", i.parrent["args"])["content"] + ",text=\"" + getInnerText(i.element) + "\")\n")
            if(argumentExists("x", args) and argumentExists("y", args)):
                compiled.write(getArgument("name", args)["content"] + ".place(x=\"" + getArgument("x", args)["content"] + "\",y=\"" + getArgument("y", args)["content"] + "\")\n\n")
            else:
                compiled.write(getArgument("name", args)["content"] + ".pack()\n\n")

    elif(found == True and i.element["tag"] == "form"):
        i.element["tag"] = getArgument("name",args)["content"]
        compiled.write("#==form init " + i.element["tag"] + "==\n")
        compiled.write(i.element["tag"] + " = tk.Tk()\n")
        if(argumentExists("dimensions",args)):
            compiled.write(i.element["tag"] + ".geometry(\"" + getArgument("dimensions",args)["content"] + "\")\n")
        if(argumentExists("title",args)):
            compiled.write(i.element["tag"] + ".title(\""+getArgument("title",args)["content"]+"\")\n")
        else:
            compiled.write(i.element["tag"] + ".title(\""+i.element["tag"]+"\")\n")
        formTags.append(i.element["tag"])
        compiled.write("#==form init " + i.element["tag"] + "==\n\n")

compiled.write("#<looping forms>\n")
for i in formTags:
    compiled.write(i + ".mainloop()\n")

compiled.write("#formspace end")
