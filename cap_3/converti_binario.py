def binario(x):
    if x != 0:
        binario(x // 2)
        print(x % 2, end = ' ')

def main():
    n = 0
    while n <= 0:
        n = int(input("Numero da convertire in binario: "))
    binario(n)

main()