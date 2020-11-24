class CommandElement:
    def __init__(self,parrent,element):
        self.parrent = parrent
        self.element = element

def deleteFromStringAll(string,toDelete):
    string = string.split(toDelete)
    string2 = ""
    for i in string:
        string2 += i
    return string2

def compileToElement(string):
    str = deleteFromStringAll(string," ")
    str = deleteFromStringAll(str,"\n")
    str = str[str.find("<"):]
    args = []
    content = ""
    for i in range(0,100):
        args.append("")
    argIndex = 0
    for char in str:
        if(char == ","):
            argIndex += 1
        if(char == ">"):
            break
        args[argIndex] += char

    a = 0
    for arg in args:
        arg = deleteFromStringAll(arg,",")
        arg = deleteFromStringAll(arg,"<")
        args[a] = arg
        a += 1
    while '' in args:
        args.remove('')

    str = deleteFromStringAll(string," ")
    str = str[str.find(">") + 1:]
    try:
        str = str[:str.find("</" + args[0] + ">")]
    except:
        return "null"
    content = str
    content = deleteFromStringAll(content,"\n")
    str = deleteFromStringAll(string," ")
    str = deleteFromStringAll(string,"\n")
    argString = ""
    i = 0
    for arg in args:
        if(i != 0):
            argString += "," + arg
        else:
            argString += arg
        i += 1
    object = {
        "tag":args[0],
        "args":args[1:],
        "content":compileContent(content),
        "selfString":deleteFromStringAll(str[str.find("<"+argString+">"):str.find("</"+args[0]+">") + len("</"+args[0]+">")]," ")
    }
    return object

def compileContent(content):
    subElementsString = deleteFromStringAll(content," ")
    subElementsString = deleteFromStringAll(subElementsString,"\n")
    subElements = []
    lastElementStringIndex = 0
    while True:
        if(compileToElement(subElementsString) == "null"):
            break
        if not "</" in subElementsString:
            break
        subElements.append(compileToElement(subElementsString))
        subElementsString = subElementsString.replace(subElements[lastElementStringIndex]["selfString"],"")
        lastElementStringIndex += 1
    return subElements

def compileToCommand(object):
    compiledArray = []
    def compile(object):
        if(object["content"] != []):
            for a in object["content"]:
                compiledArray.append(CommandElement(object,a))
                compile(a)
    compile(object)
    return compiledArray

def getArgumentFromString(str):
    str = deleteFromStringAll(str," ")
    argName = str[:str.find("=")]
    argContent = str[str.find("=") + 1:]
    argContent = deleteFromStringAll(argContent, "\"")
    object = {
        "name":argName,
        "content":argContent
    }
    return object
def getArgument(argument,args):
    found = False
    ret = {
        "name":"null",
        "content":"null"
    }
    for a in args:
        arg = getArgumentFromString(a)
        if(arg["name"] == argument):
            ret = arg
    return ret

def argumentExists(argument,args):
    if(getArgument(argument,args)["name"] == "null"):
        return False
    else:
        return True

def argumentsToString(args):
    string = ""
    for arg in args:
        string += "," + arg["name"] + "=" + "\"" + arg["content"] + "\""
    return string

def getInnerText(element):
    elementString = element["selfString"]
    elementString = elementString[elementString.find(">") + 1:elementString.find("<") - (len(element["tag"]) + 3)]
    return elementString
