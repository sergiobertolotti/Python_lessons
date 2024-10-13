# Funzione per l'incremento di 1
def aggiungi1(x,z):
    x += 1
    for i in range(len(z)):
        z[i] += 1

# Funzione per l'incremento di 10
def aggiungi10(y):
    y += 10
    return y


# Funzione per la stampa
def stampa(x,y,z):
    print(x)
    print(y)
    print(z)


# Funzione principale
def main():
    a = 10
    b = 20
    lista = [5,6,7]
    print("Prima: ")
    stampa(a,b,lista)
    aggiungi1(a,lista)
    b = aggiungi10(b)
    print("Dopo: ")
    stampa(a,b,lista)

#Istruzione di avivo del programma
main()