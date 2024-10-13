cognome = input("Cognome: ")
nome = input("Nome: ")
data_nascita = input("Data di nascita (gg/mm/aaaa): ")
# Costruisco il nome utente
uname = cognome[:3] + nome[:3] + data_nascita[-2:]
uname = uname.lower()
print("Il tuo username è:", uname)
tasto = input()