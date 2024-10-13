# giorni della settimana
settimana = ["Lun", "Mar", "Mer", "Gio", "Ven" , "Sab", "Dom"]

# ricevo gli incassi per ogni giorno della sttimana
def leggi_incassi():
    incassi = []
    for giorno in settimana: 
        valore = float(input("Incasso di " + giorno + ": "))
        incassi.append(valore)
    return incassi

# calcolo incasso settmanale
def calcola_totale(dati):
    totale = 0
    for j in range(len(dati)):
        totale += dati[j]
    print(30 * '-')
    print("Incasso settimanale: ", totale)
    print(30 * '-')


# funzione principale
def main():
    incassi = leggi_incassi()
    calcola_totale(incassi)


# eseguo il programma
main()