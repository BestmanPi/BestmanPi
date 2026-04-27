import math


def RAIZ(valor):
    return math.sqrt(valor)


def CALCULAR():

    EXCESO = 1 << 32
    CONTADOR = 0

    R = 3 << 25
    H = int(R / 2)
    BM = R * RAIZ(3) / 2
    R2 = R * R
    SUMA = 0

    for i in range(H):
        Y = i + 0.5
        SUMA += RAIZ(R2 - Y * Y) - BM
        if SUMA >= EXCESO:
            SUMA -= EXCESO
            CONTADOR += 1

    TOTAL = ((SUMA + CONTADOR * EXCESO + BM * R / 4) / R2) * 12

    return TOTAL


print("Pi= ", CALCULAR())
