class Calcolatrice(object):
    # metodi
    def addizione(self):
        return self.a + self.b
    
    def sottrazione(self):
        return self.a - self.b
    
    def moltiplicazione(self):
        return self.a * self.b
    
    def divisione(self):
        if self.b == 0:
            print("Divisione per zero non si può fare")
            risultato = None
        else:
            risultato = self.a / self.b
        return risultato
    
    # costruttore
    def __init__(self):
        self.a = 0.0
        self.b = 0.0