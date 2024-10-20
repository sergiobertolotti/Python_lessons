import tkinter as tk
from tkinter.colorchooser import askcolor

class DialogoColore(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master.title("Scelta del colore")
        self.master.geometry("400x300")
        self.grid()
        self.crea_widgets()
        
    def crea_widgets(self):
        self.vTesto = tk.StringVar()
        self.txtTesto = tk.Entry(self, width = 30, textvariable=self.vTesto)
        self.txtTesto.grid(row = 1, column = 1)
        
        self.btnColore = tk.Button(self,text = "Colore", width = 10, command=self.imposta_colore)
        self.btnColore.grid(row = 1, column = 2)
        
        self.btnSfondo = tk.Button(self, text = "Sfondo", width = 10, command=self.imposta_sfondo)
        self.btnSfondo.grid(row = 2, column = 2)
    def imposta_colore(self):
        c1 = askcolor()[1]
        self.txtTesto.config(fg = c1)
        
    def imposta_sfondo(self):
        c2 = askcolor()[1]
        self.txtTesto.config(bg = c2)
        
def main():
    f = DialogoColore()
    f.mainloop()
    
main()