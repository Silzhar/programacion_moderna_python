from tkinter import *
from tkinter import ttk


class mainApp(Tk):
    entrada = None #   opcional : entrada = ""
    tipoUnidad = None

   
    def __init__(self):
        Tk.__init__(self)
        self.title("Termometro")
        self.geometry("210x150")
        self.configure(bg="thistle3")   # self.configure(bg="#DED7B9")
        self.resizable(0,0) # no redimensiona la pantalla, la bloquea 
                       
        self.temperatura = StringVar(value="")
        self.tipoUnidad = StringVar(value="C")
                       
        self.createLayout()
        
    def createLayout(self):
            self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)
            
            self.lblUnidad = ttk.Label(self, text="Grados:").place(x=10, y=45)
            self.rb1 = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad,value="F").place(x=20,y=70)
            self.rb2 = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad,value="c").place(x=20, y=100)
            # rb1 radio button 1

    def start(self):
        self.mainloop()
        
        
if __name__ == '__main__':
    app = mainApp()
    app.start()
    