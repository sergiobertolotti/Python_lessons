# Calcolo il costo finale data la quantità, il prezzo unitarioe l'aliquota IVA
art_descr = input("Imetti la descrizione dell'articolo: ")
art_qta = int(input("Immetti la quantità: "))
art_prz = float(input("Immetti il prezzo unitario: "))
art_IVA = float(input("Immetti l'aliquota IVA: "))

imponibile = art_qta * art_prz
IVA = imponibile * art_IVA / 100
lordo = imponibile + IVA
print("L'articolo ", art_descr , "Costa in totale: ", lordo)