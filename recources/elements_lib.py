class predefinedArgument:
    def __init__(self,detectedName,label):
        self.detectedName = detectedName
        self.label = label

class element:
    def __init__(self,prefabed,tag,label,args,placeArgs):
        self.prefabed = prefabed
        self.tag = tag
        self.label = label
        self.args = args
        self.placeArgs = placeArgs

elements = [
    element(True,"input","Entry",[],[predefinedArgument("x","x"),predefinedArgument("y","y"),predefinedArgument("width","width"),predefinedArgument("height","height")]),
    element(True,"canvas","Canvas",[],[predefinedArgument("x","x"),predefinedArgument("y","y"),predefinedArgument("width","width"),predefinedArgument("height","height")]),
    element(False,"script","",[predefinedArgument("path","")],[])
]
