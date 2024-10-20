import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class DialogoFile(tk.Frame):
    
    def __init__(self,master = None):
        super().__init__(master)
        self.master.title("Scelta del file")
        self.master.geometry("350x200")
        self.grid()
        self.crea_widgets()
        
    def crea_widgets(self):
        # nome del file
        self.lblNome = tk.Label(self,text = "File")
        self.lblNome.grid(row = 1, column = 0, sticky=tk.W)
        self.vNome = tk.StringVar()
        self.txtNome = tk.Entry(self,width=30,textvariable=self.vNome)
        self.txtNome.grid(row = 1, column = 1)
        
        # pulsante per apertura del file
        self.btnApri = tk.Button(self,text = "Apri", command=self.apri_file)
        self.btnApri.grid(row = 1, column = 2)
        
    def apri_file(self):
        nomefile = filedialog.askopenfilename(filetypes=(("File di testo","*.txt"),("Tutti i files","*.*")))
        self.vNome.set(nomefile)
        
        try:
            fin = open(nomefile,"r")
            content = fin.read()
            nr = content.count("\n")
            messagebox.showinfo("Conteggio","Numero di righe: " + str(nr))
        except IOError:
            messagebox.showwarning("Apertura del file","Impossibile aprire il file")
        finally:
            fin.close()
            
def main():
    f = DialogoFile()
    f.mainloop()
    
main()