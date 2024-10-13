# creazione della coda a due ingressi
lavoro = [] 

# menu delle scelte
def presenta_menu():
    print("---------------------------------")
    print("1. Accodamento nuova lavorazione")
    print("2. Esecuzione di una lavorazione")
    print("3. Visualizza coda lavorazioni")
    print("4. Fine lavoro")
    print("---------------------------------")


# scelta da menu
def scelta_operazione():
    operazione = int(input("Inserisci la tua scelta: "))
    while operazione not in [1,2,3,4]:
        print("Valore scelto non ammesso")
        operazione = int(input("Inserisci la tua scelta: "))
    return operazione

# inserisce una lavorazione nella coda
# priorità: 1 alta, 2 bassa
# codlav: stringa con il codice della lavorazione
def accoda():
    priorita = int(input("priorità (1,2): ")) 
    codlav = input("Codice lavorazione: ")
    if priorita == 1:
        lavoro.insert(0,codlav)
    else:
        lavoro.append(codlav)


# esecuzione di una lavorazione
def esegui():
    if len(lavoro) == 0:
        print("Coda lavorazioni vuota")
    else:
        codlav = lavoro.pop(0)
        print("Avvio lavorazione:", codlav)


# visualizzazione delle lavorazioni
def visualizza():
    print("Coda delle lavorazioni")
    for pos in range(len(lavoro)):
        codlav = lavoro[pos]
        print("Codice:",codlav)

# funzione principale
def main():
    proseguo = True
    while proseguo:
        presenta_menu()
        scelta = scelta_operazione()
        if scelta == 1:
            accoda()
        elif scelta == 2:
            esegui()
        elif scelta == 3:
            visualizza()
        else:
            print("Fine lavoro")
            proseguo = False

# esecuzione del programma
main()
