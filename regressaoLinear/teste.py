def main():
    entrada = input()
    numeros = str(entrada).split()

    a = int(numeros[0])
    b = int(numeros[1])
    c = int(numeros[2])

    if a + b > c and a + c > b and c + b > a:
        print("Sim")
    else:
        print("Não")


main()