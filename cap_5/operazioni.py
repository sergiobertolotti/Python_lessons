from calcolatrice import *

Calc = Calcolatrice()
a = float(input("Primo dato: "))
b = float(input("Secondo dato: "))

Calc.a = a
Calc.b = b

c = input("""
    Scegliere l'operazione:
    [ + ] Addizione
    [ - ] Sottrazione
    [ * ] Moltiplicazione
    [ / ] Divisione
    
==> """)

if c == "+":
    risultato = Calc.addizione()
elif c == "-":
    risultato = Calc.sottrazione()
elif c == "*":
    risultato = Calc.moltiplicazione()
elif c == "/":
    risultato = Calc.divisione()
else:
    risultato = "Operazione sconosciuta"
    
print(risultato)