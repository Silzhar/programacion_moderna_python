'''  import tkinter  crea interfaces gráficas multiplataforma
widget : controles visuales    
ttk.Button , ttkRadioButton  tipo de boton, ttk.Entry tipo de entrada       '''

from tkinter import *
from tkinter import ttk

 # importamos Tk para heredar el objeto y crear pantalla propia 
 # ventana o gestor de controles visuales. Tk: objeto con todos los metodos
class mainApp(Tk):
    size = "1024x768"    # // ventana principal
        
    def __init__(self): # detalla los metodos de la clase
        Tk.__init__(self)
      
        self.geometry(self.size) #define ventana 
        self.title("Ventana de comienzo")
        self.configure(bg = "purple")
        
    def start(self):
        self.mainloop()  # o root.mainloop()  arranque de ventana
    
if __name__== '__main__':
    app = mainApp()
    app.start()
