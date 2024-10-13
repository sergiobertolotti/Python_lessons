class Anagrafica(object):
    # attributi pubblici
    codice = 0
    cognome = ""
    nome = ""
    
    # attributi privati
    __registrato = False
    
    # metodi pubblici
    def registra(self):
        self.__registrato = True
        
    def mostra(self):
        if self.__registrato:
            print(self.codice)
            print(self.cognome)
            print(self.nome)
        else:
            print("non registrato")
            
# funzione principale
def main():
    persona = Anagrafica()
    persona.codice = int(input("Codice: "))
    persona.cognome = input("Cognome: ")
    persona.nome = input("Nome: ")
    #persona.registra()
    persona.__registrato = True
    persona.mostra()
    
# istruzione di avvio del programma
main()
