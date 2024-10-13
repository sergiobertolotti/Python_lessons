# classe base
class Anagrafica(object):
    # attributi pubblici
    codice = 0
    cognome = ""
    nome = ""
    
    # attributi privati
    __registrato = False
    
    # metodi (pubblici)
    def registra(self):
        self.__registrato = True
        
    def mostra(self):
        if self.__registrato:
            print(self.codice)
            print(self.cognome)
            print(self.nome)
        else:
            print("non registrato")
            
# classe derivata
class Studente(Anagrafica):
    
    # metodi ed attributi (privati)
    def __init__(self):
        self.__promosso = False
        
    # metodi (pubblici)
    def promuovi(self):
        self.__promosso = True
        
    def controlla(self):
        if self.__promosso:
            print("Studente promosso")
        else:
            print("Studente non promosso")
            
# funzione principale
def main():
    stud1 = Studente()
    # inserimento dei dati
    stud1.codice = int(input("Codice: "))
    stud1.cognome = input("Cognome: ")
    stud1.nome = input("Nome: ")
    
    # operazioni sull'oggetto
    stud1.registra()
    stud1.controlla()
    risp = input("Promosso (s/n): ")
    if (risp == "s"):
        stud1.promuovi()
    stud1.mostra()
    stud1.controlla()
    

# istruzione di avvio del programma
main()