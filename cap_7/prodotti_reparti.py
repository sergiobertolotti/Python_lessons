# variabili globali
listaprodotti = []
    
# definizione della classe
class Prodotto(object):
    # attributi privati
    __descrizione = ""
    __prezzo = 0.0
    
    # attributi pubblici
    numrep = 0
    
    # metodi pubblici
    def registra(self,descrizione, prezzo, numrep):
        self.__descrizione = descrizione
        self.__prezzo = prezzo
        self.numrep = numrep
    # variabili globali
    listaprodotti = []    
    def visualizza(self):
        print("{0:25} {1:10.2f}".format(self.__descrizione,self.__prezzo))
        
# funzioni del programma
def inserisci_prodotti():
    finito = "n"        
    while finito.lower() == "n":
        desc = input("Descrizione prodotto: ")
        prz = float(input("Prezzo prodotto: "))
        np = int(input("Numero reparto: "))
        prod = Prodotto()
        prod.registra(desc,prz,np)
        listaprodotti.append(prod)
        finito = input("finito (s/n)? ")
            
def elenca_prodotti():
    print("-" * 20)
    print("Lista dei prodotti")
    print("-" * 20)
    for k in range(len(listaprodotti)):
        print("Prodotto {:d}".format(k+1), end = ' ')
        listaprodotti[k].visualizza()
             
def elenca_per_reparto(reparto, listaprodotti):
    for p in listaprodotti:
        if p.numrep == reparto:
            p.visualizza()

    
    
# funzione principale
def main():
    print("-" * 20)
    inserisci_prodotti()
    elenca_prodotti()
    print("-" * 20)
        
    i = int(input("Inserisci il numero di reparto: "))
    elenca_per_reparto(i, listaprodotti)
        
# istruzione di avvio del programma
main()