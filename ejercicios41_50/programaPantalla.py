style = {'plane': 0,'bold': 1,'weak': 2}

def clear():
    print("\033[2J")

def locate(line, column):    
    print("\033[{};{}H".format(line, column),end=" ")
    
def clearLine(line=None, column=None):
    if line is not None and column is not None:
        locate(line, column)
    elif line is not None: # si el primero no está informado borra en la posicion actual
        locate(line, 1)
        
    print("\033[K",end="")

def pocessParama(params):
    if 'line' in params:
        line = params['line']
        column = 1
        if 'column' in params:
            column = params['column']
            
def Print(cadena, line, column, delEnd=False):
    locate(line, column)
    if delEnd:
        clearLine()
    print(cadena,end="")
    
def Input(msg,line, column, delEnd=True):
    locate(line, column)
    if delEnd:
        clearLine()
    return input(msg)

def Format(style, colorText, colorBack):
    print("\033[{};{};{}m".format(style, colorText,colorBack),end="")
    
def Reset():
    Format(0, 37, 40)
