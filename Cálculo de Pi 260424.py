import math


def CALCULAR():

    def RAIZ(valor):
        return math.sqrt(valor)

    EXCESO = 1 << 32
    CONTADOR = 0

    R = 100663296
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

    TOTAL = ((SUMA + CONTADOR * EXCESO) * 4 / R2 + RAIZ(3) / 2) * 3
    return TOTAL


print(CALCULAR())
