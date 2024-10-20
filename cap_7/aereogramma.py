import tkinter as tk

class GraficoTorta(tk.Frame):
    # costruttore
    def __init__(self,master = None):
        super().__init__(master)
        self.master.title("Aereogramma")
        self.master.geometry("500x600")
        self.option_add("*Font","helvetica 12")
        self.grid()
        self.crea_widgets()
        
    # inserimento dei widgets    
    def crea_widgets(self):
        # etichette e caselle dei dati
        self.lblA = tk.Label(self,text="A")
        self.lblA.grid(row = 0, column = 0)
        self.vA = tk.DoubleVar()
        self.txtA = tk.Entry(self, justify = tk.RIGHT,textvariable=self.vA)
        self.txtA.grid(row = 0, column = 1)
        
        self.lblB = tk.Label(self,text="B")
        self.lblB.grid(row = 1, column = 0)
        self.vB = tk.DoubleVar()
        self.txtB = tk.Entry(self, justify = tk.RIGHT,textvariable=self.vB)
        self.txtB.grid(row = 1, column = 1)
        
        self.lblC = tk.Label(self,text="C")
        self.lblC.grid(row = 2, column = 0)
        self.vC = tk.DoubleVar()
        self.txtC= tk.Entry(self, justify = tk.RIGHT,textvariable=self.vC)
        self.txtC.grid(row = 2, column = 1)
        
        # pulsante per tracciare il grafico
        self.btn1 = tk.Button(self, text="Grafico", command=self.traccia_grafico)
        self.btn1.grid(row= 3, column = 0, columnspan= 2)
        
        # Canvas
        self.c1 = tk.Canvas(self,width = 400, height=400, bg="white")
        self.c1.grid(row = 4, column = 1)

        # pulsante di uscita
        self.btnEsci = tk.Button(self,text="Esci",command=self.master.destroy)
        self.btnEsci.grid(row = 5, column = 0, columnspan=2)
        
    # traccia il grafico a torta
    def traccia_grafico(self):
        a = self.vA.get()
        b = self.vB.get()
        c = self.vC.get()
        s = a + b + c
        #angoli
        arcA = a * 360 / s
        arcB = b * 360 / s
        arcC = c * 360 / s
        
        # settori
        self.c1.create_arc(10,10,390,390,start = 0,extent = arcA, fill="red")
        self.c1.create_arc(10,10,390,390,start = arcA, extent = arcB, fill="green")
        self.c1.create_arc(10,10,390,390,start = arcA + arcB, extent=arcC, fill="blue")
        
        
def main():
    f = GraficoTorta()
    f.mainloop()
    
    
main()