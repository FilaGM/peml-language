import sys
from recources.compiler_lib import *
from recources.compile_elements_lib import testForElements
import tkinter as tk
import os

file = open(sys.argv[1],"r")
print("Started compiling file: "+sys.argv[1])
file = file.read()

compiledFile = compileToElement(file)

command = compileToCommand(compiledFile)
print("Number of steps: "+ str(len(command)))

compiled = open(sys.argv[2],"w")
compiled.write("import tkinter as tk\n")
for arg in compiledFile["args"]:
    if(getArgumentFromString(arg)["name"] == "name"):
        compiled.write("#formspace "+getArgumentFromString(arg)["content"] + "\n")

formTags = []
steps = 1
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
        if(argumentExists("height",args)):
            height = getArgument("height", args)["content"]
        compiled.write(getArgument("name", args)["content"] + " = tk.Frame("+i.parrent["tag"]+" ,width="+width+", height="+height+")\n")
        if(argumentExists("x", args) and argumentExists("y", args)):
            compiled.write(getArgument("name", args)["content"] + ".place(x=\"" + getArgument("x", args)["content"] + "\",y=\"" + getArgument("y", args)["content"] + "\")\n\n")
        else:
            compiled.write(getArgument("name", args)["content"] + ".pack()\n\n")
        i.element["tag"] = getArgument("name", args)["content"]
    elif(found == False):
        compiled.write(testForElements(i))

    elif(found == True and i.element["tag"] == "form"):
        i.element["tag"] = getArgument("name",args)["content"]
        compiled.write("#==form init " + i.element["tag"] + "==\n")
        compiled.write(i.element["tag"] + " = tk.Tk()\n")
        if(argumentExists("dimensions",args)):
            compiled.write(i.element["tag"] + ".geometry(\"" + deleteFromStringAll(getArgument("dimensions",args)["content"],"\"") + "\")\n")
            compiled.write("mainFormCanvas_" + i.element["tag"] + " = tk.Canvas("+i.element["tag"]+",width="+deleteFromStringAll(getArgument("dimensions", args)["content"][getArgument("dimensions", args)["content"].find("x")+1:],"\"")+",height="+deleteFromStringAll(getArgument("dimensions", args)["content"][:getArgument("dimensions", args)["content"].find("x")],"\"")+")\n")
        else:
            compiled.write("mainFormCanvas_" + i.element["tag"] + " = tk.Canvas("+i.element["tag"]+",width=100,height=100)\n")
        if(argumentExists("backgroundColor",args)):
            backgroundColor = getArgument("backgroundColor", args)["content"]
        if(argumentExists("title",args)):
            compiled.write(i.element["tag"] + ".title(\""+getArgument("title",args)["content"]+"\")\n")
        else:
            compiled.write(i.element["tag"] + ".title(\""+i.element["tag"]+"\")\n")
        compiled.write("mainFormCanvas_" + i.element["tag"] + ".place(x=0,y=0)\n")
        formTags.append(i.element["tag"])
        compiled.write("#==form init " + i.element["tag"] + "==\n\n")

    print(str(int((100 / len(command)) * steps)) + "%")
    steps += 1

print("done")
compiled.write("#<looping forms>\n")
for i in formTags:
    compiled.write(i + ".mainloop()\n")

compiled.write("#formspace end")
