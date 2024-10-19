import tkinter as tk
from tkinter import messagebox

class Anagrafe(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master.title("Dati anagrafici")
        self.master.geometry("300x200")
        self.grid()
        self.crea_widgets()
        
    def crea_widgets(self):
        
        # cognome
        self.lblCognome = tk.Label(self,text = "Cognome")
        self.lblCognome.grid(row = 0, column = 0, sticky = tk.W)
        self.vCognome = tk.StringVar()
        self.txtCognome = tk.Entry(self,textvariable=self.vCognome)
        self.txtCognome.grid(row = 0, column = 1)
        
        # nome
        self.lblNome = tk.Label(self, text="Nome")
        self.lblNome.grid(row = 1, column = 0, sticky=tk.W)
        self.vNome = tk.StringVar()
        self.txtNome = tk.Entry(self,textvariable=self.vNome)
        self.txtNome.grid(row = 1, column = 1)
        
        # pulsante di invio
        self.btnInvio = tk.Button(self,text="Invio",command=self.invio_dati)
        self.btnInvio.grid(row = 2, column = 0, columnspan= 2)
    
        # pulsante di annulla
        self.btnAnnulla = tk.Button(self,text="Annulla", command=self.svuota_caselle)
        self.btnAnnulla.grid(row = 2, column = 1, columnspan= 2, sticky=tk.E)
        
    def invio_dati(self):
        c = self.vCognome.get()
        n = self.vNome.get()
        if c == "" or n =="":
            messagebox.showwarning("Attenzione", "I dati sono obbligatori")
        else:
            messagebox.showinfo("Conferma","Dati inseriti:  \n" + c + " " + n)
    
    def svuota_caselle(self):
        self.txtCognome.delete(0,tk.END)
        self.txtNome.delete(0,tk.END)
        

def main():
    f = Anagrafe()
    f.mainloop()
    
    
main()
        
        