import math

def fatt(x):
    if x == 0:
        f = 1
    else:
        f = x * fatt(x - 1)
    return f


def main():
    n = int(input("Numero naturale: "))
    try:
        print("Fattoriale del numero", n, "=", math.factorial(n))
    except ValueError:
        print("Il numero immesso deve essere un numero intero e positivo")
main()