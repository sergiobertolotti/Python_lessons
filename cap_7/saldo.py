import locale
import tkinter as tk
from tkinter.font import Font

class Contabile(tk.Frame):
    # costruttore
    def __init__(self, master = None):
        super().__init__(master, bg = "lightcyan")
        self.master.title("Saldo contabile")
        self.master.geometry("300x200")
        self.master.config(bg = "lightcyan")
        self.grid()
        self.crea_widgets()
        
    # inseirmento dei widget 
    def crea_widgets(self):
        # imposta il font
        font14 = Font(family="Calibri", size = 14)
        
        # input entrate
        self.lblE = tk.Label(self, text = "Entrate", font = font14, bg = "lightcyan")
        self.lblE.grid(row = 0, column = 0, sticky=tk.W)
        self.vE = tk.StringVar()
        self.txtE = tk.Entry(self, font = font14, justify = tk.RIGHT, bg = "white", textvariable=self.vE)
        self.txtE.grid(row = 0, column = 1, sticky=tk.W)
        
        # input uscite
        self.lblU = tk.Label(self, text = "Uscite", font = font14, bg = "lightcyan")
        self.lblU.grid(row = 1, column = 0, sticky=tk.W)
        self.vU = tk.StringVar()
        self.txtU = tk.Entry(self, font = font14, justify= tk.RIGHT,bg = "white", textvariable=self.vU)
        self.txtU.grid(row = 1, column = 1, sticky=tk.W)
        
        # pulsante per il calcolo
        self.btnCalcolo = tk.Button(self, text = "Calcolo saldo", font = font14, command=self.calcolo_saldo)
        self.btnCalcolo.grid(row = 2, column = 0, columnspan= 2)
        
        # pulsante di annulla
        self.btnAnnulla = tk.Button(self, text = "Anulla", font = font14, command=self.svuota_caselle)
        self.btnAnnulla.grid(row = 2, column = 1, columnspan= 2, sticky=tk.E)
        
        # saldo
        self.lblS = tk.Label(self,text = "Saldo", font = font14, bg = "lightcyan")
        self.lblS.grid(row = 3, column = 0, sticky=tk.W)
        self.vS = tk.StringVar()
        self.txtS = tk.Entry(self, font = font14, justify=tk.RIGHT, bg = "lightyellow", textvariable=self.vS)
        self.txtS.grid(row = 3, column = 1)
        
        # pulsante di uscita
        self.btnEsci = tk.Button(self, text = "Esci", font = font14, command = self.master.destroy)
        self.btnEsci.grid(row = 4, column = 1, columnspan= 2)
        
    # calcolo del saldo 
    def calcolo_saldo(self):
        e = locale.atof(self.vE.get())
        self.vE.set(locale.currency(e))
        u = locale.atof(self.vU.get())
        self.vU.set(locale.currency(u))
        s = e - u
        if s < 0:
            self.txtS.config(fg = "red")
        self.vS.set(locale.currency(s))
    
    # svuota le caselle di testo
    def svuota_caselle(self):
        self.txtE.delete(0,tk.END)
        self.txtU.delete(0,tk.END)
        self.txtS.delete(0,tk.END)
        # ripristina colore normale per il saldo
        self.txtS.config(fg = "black")
         
def main():
    locale.setlocale(locale.LC_ALL,'')
    f = Contabile()
    f.mainloop()
    
main()