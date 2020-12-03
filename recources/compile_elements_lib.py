from recources.compiler_lib import getArgument, argumentExists, getInnerText, deleteFromStringAll
from recources.elements_lib import elements
import os

def testForElements(element):
    string = ""
    found = False
    for elm in elements:
        if(element.element["tag"] == elm.tag):
            found = True
            if(elm.compilingMethod == 0):
                string += getArgument("name", element.element["args"])["content"] + " = tk." + elm.label + "(" + getArgument("name", element.parrent["args"])["content"]
                for arg in elm.args:
                    if(arg.detectedName == "inner"):
                        string += "," + arg.label + "=" + "\"" +getInnerText(element.element) + "\""
                    elif(argumentExists(arg.detectedName,element.element["args"])):
                        string += "," + arg.label + "=" + getArgument(arg.detectedName,element.element["args"])["content"]
                string += ")\n"
                if(len(elm.placeArgs) != 0):
                    placedArgs = 0
                    string += getArgument("name", element.element["args"])["content"] + ".place("
                    for arg in elm.placeArgs:
                        if(argumentExists(arg.detectedName,element.element["args"])):
                            if(placedArgs > 0):
                                string += ","
                            string += arg.label + "=" + getArgument(arg.detectedName,element.element["args"])["content"]
                            placedArgs += 1
                    string += ")\n"
            if(elm.compilingMethod == 1):
                args = element.element["args"]
                file = open(str(getArgument("path",args)["content"]),"r")
                string += "#file " + getArgument("name",args)["content"] + " start\n"
                string += file.read()
                string += "#file "+ getArgument("name",args)["content"] + " end\n"
            else:
                pass
            break
    if(found == False):
        args = element.element["args"]
        string += getArgument("name", args)["content"] + " = tk.Label(" + getArgument("name", element.parrent["args"])["content"] + ",text=\"" + getInnerText(element.element) + "\")\n"
        if(argumentExists("x", args) and argumentExists("y", args)):
            string += getArgument("name", args)["content"] + ".place(x=\"" + getArgument("x", args)["content"] + "\",y=\"" + getArgument("y", args)["content"] + "\")\n\n"
        else:
            string += getArgument("name", args)["content"] + ".pack()\n\n"
    return string
