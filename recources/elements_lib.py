class predefinedArgument:
    def __init__(self,detectedName,label):
        self.detectedName = detectedName
        self.label = label

class element:
    def __init__(self,compilingMethod,tag,label,args,placeArgs):
        self.compilingMethod = compilingMethod
        self.tag = tag
        self.label = label
        self.args = args
        self.placeArgs = placeArgs

TKINTER = 0
INCLUDEFILE = 1
elements = [
    element(TKINTER,"input","Entry",[],[predefinedArgument("x","x"),predefinedArgument("y","y"),predefinedArgument("width","width"),predefinedArgument("height","height")]),
    element(TKINTER,"canvas","Canvas",[],[predefinedArgument("x","x"),predefinedArgument("y","y"),predefinedArgument("width","width"),predefinedArgument("height","height")]),
    element(TKINTER,"button","Button",[predefinedArgument("onclick","command"),predefinedArgument("inner","text")],[predefinedArgument("x","x"),predefinedArgument("y","y"),predefinedArgument("width","width"),predefinedArgument("height","height")]),
    element(INCLUDEFILE,"script","",[],[])
]
