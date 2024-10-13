def calcolo(base, esponente = 2):
    potenza = base ** esponente
    return potenza

numero = int(input("Immetti un numero: "))
espo = int(input("Immetti l'esponente: "))
print("La potenza di ", espo," del numero ",numero, " è: ",calcolo(numero,espo))