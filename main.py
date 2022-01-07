import pprint

def calcularNumerosPrimos(n):
    numerosPrimos = []
    for numero in range(1, n+1):
        for number in range(2, numero):
            if (numero % number) == 0:
                break
        else:
            numerosPrimos.append(numero)

    pprint.pprint(numerosPrimos)


calcularNumerosPrimos(5000)