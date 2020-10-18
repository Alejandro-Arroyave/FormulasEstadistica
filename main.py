import math

# Project: Intevalos de Confianza Estadística
# Author: Alejandro Arroyave Bedoya
# Institution: Universidad EAFIT
# Date: 2020, Noviembre


def IntervalosDeConfianzaParaMiu():
    respuesta = input("¿Es distribución normal? (Si/No): ")
    if respuesta.lower() == "si":
        return IntConfDistNormalParaMiu()
    elif respuesta.lower() == "no":
        return IntConfDistNoNormalParaMiu()


def IntConfDistNormalParaMiu():
    respuesta = input(
        "¿La variación poblacional (\u03C3) es conocida? (Si/No): ")
    if respuesta == "si":
        x = float(input("Ingresa la media muestral (X): "))
        z = float(input("Ingresa el quantil (Z\u03B1/2): "))
        sigma = float(input("Ingresa la variación poblacional (\u03C3): "))
        n = int(input("Ingresa el tamaño muestral (n): "))
        return (x - (z * (sigma / math.sqrt(n))),
                x + (z * (sigma / math.sqrt(n))))
    elif respuesta == "no":
        x = float(input("Ingresa la media muestral (X): "))
        t = float(input("Ingresa el valor de tabla (t\u03B1/2,n-1): "))
        s = float(input("Ingresa la desviación estándar muestral (S): "))
        n = int(input("Ingresa el tamaño muestral (n): "))
        return (x - (t * (s / math.sqrt(n))), x + (t * (s / math.sqrt(n))))


def IntConfDistNoNormalParaMiu():
    n = int(input("Ingresa el tamaño muestral (n): "))
    if n >= 30:
        respuesta = input(
            "¿La variación poblacional (\u03C3) es conocida? (Si/No): ")
        if respuesta.lower() == "si":
            x = float(input("Ingresa la media muestral (X): "))
            z = float(input("Ingresa el quantil (Z\u03B1/2): "))
            sigma = float(input("Ingresa la desviación estándar (\u03C3): "))
            return (x - (z * (sigma / math.sqrt(n))),
                    x + (z * (sigma / math.sqrt(n))))
        elif respuesta.lower() == "no":
            x = float(input("Ingresa la media muestral (X): "))
            z = float(input("Ingresa el quantil (Z\u03B1/2): "))
            s = float(input("Ingresa la desviación estándar muestral (S): "))
            return (x - (z * (s / math.sqrt(n))), x + (z * (s / math.sqrt(n))))
    else:
        return "Distribución exacta"


def IntervalosDeConfianzaParaMiuUnoMenosDos():
    respuesta = input("¿X1 y X2 tienen distribución normal? (Si/No): ")
    if respuesta.lower() == "si":
        return IntConfDistNormalParaMiuUnoMenosDos()
    elif respuesta.lower() == "no":
        return IntConfDistNoNormalParaMiuUnoMenosDos()


def SP(s1, s2, n1, n2):
    return math.sqrt((((n1 - 1) * s1**2) + ((n2 - 1) * s2**2)) / (n1 + n2 - 2))


def IntConfDistNormalParaMiuUnoMenosDos():
    respuesta = input("¿\u03C31 y \u03C32 son conocidas? ")
    if respuesta.lower() == "si":
        x1 = float(input("Ingresa la media muestral variable 1 (X1): "))
        x2 = float(input("Ingresa la media muestral variable 2 (X2): "))
        z = float(input("Ingresa el quantil (Z\u03B1/2): "))
        sigma1 = float(
            input("Ingresa la desviación estándar variable 1 (\u03C31): "))
        sigma2 = float(
            input("Ingresa la desviación estándar variable 2 (\u03C32): "))
        n1 = int(input("Ingresa el tamaño muestral 1 (n1): "))
        n2 = int(input("Ingresa el tamaño muestral 2 (n2): "))
        raiz = math.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
        return ((x1 - x2) - (z * raiz), (x1 - x2) + (z * raiz))
    else:
        respuesta = input("¿\u03C31 y \u03C32 son iguales? ")
        if respuesta.lower() == "si":
            x1 = float(input("Ingresa la media muestral variable 1 (X1): "))
            x2 = float(input("Ingresa la media muestral variable 2 (X2): "))
            t = float(
                input("Ingresa el valor de tabla (t\u03B1/2,(n1+n2)-2): "))
            s1 = float(
                input("Ingresa la desviación estándar muestral 1 (S1): "))
            s2 = float(
                input("Ingresa la desviación estándar muestral 2 (S2): "))
            n1 = int(input("Ingresa el tamaño muestral 1 (n1): "))
            n2 = int(input("Ingresa el tamaño muestral 2 (n2): "))
            sp = SP(s1, s2, n1, n2)
            return ((x1 - x2) - (t * sp * math.sqrt((1 / n1) + (1 / n2))),
                    (x1 - x2) + (t * sp * math.sqrt((1 / n1) + (1 / n2))))
        else:
            x1 = float(input("Ingresa la media muestral variable 1 (X1): "))
            x2 = float(input("Ingresa la media muestral variable 2 (X2): "))
            t = float(input("Ingresa el valor de tabla (t\u03B1/2,v): "))
            s1 = float(
                input("Ingresa la desviación estándar muestral 1 (S1): "))
            s2 = float(
                input("Ingresa la desviación estándar muestral 2 (S2): "))
            n1 = int(input("Ingresa el tamaño muestral 1 (n1): "))
            n2 = int(input("Ingresa el tamaño muestral 2 (n2): "))
            return ((x1 - x2) - (t * math.sqrt((s1**2 / n1) + (s2**2 / n2))),
                    (x1 - x2) + (t * math.sqrt((s1**2 / n1) + (s2**2 / n2))))


def IntConfDistNoNormalParaMiuUnoMenosDos():
    n1 = int(input("Ingresa el tamaño muestral 1 (n1): "))
    n2 = int(input("Ingresa el tamaño muestral 2 (n2): "))
    if n1 >= 30 and n2 >= 30:
        respuesta = input("¿\u03C31 y \u03C32 son conocidas? ")
        if respuesta == "si":
            x1 = float(input("Ingresa la media muestral variable 1 (X1): "))
            x2 = float(input("Ingresa la media muestral variable 2 (X2): "))
            z = float(input("Ingresa el quantil (Z\u03B1/2): "))
            sigma1 = float(
                input("Ingresa la desviación estándar variable 1 (\u03C31): "))
            sigma2 = float(
                input("Ingresa la desviación estándar variable 2 (\u03C32): "))
            raiz = math.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
            return ((x1 - x2) - (z * raiz), (x1 - x2) + (z * raiz))
        elif respuesta == "no":
            x1 = float(input("Ingresa la media muestral variable 1 (X1): "))
            x2 = float(input("Ingresa la media muestral variable 2 (X2): "))
            z = float(input("Ingresa el quantil (Z\u03B1/2): "))
            s1 = float(
                input("Ingresa la desviación estándar muestral 1 (S1): "))
            s2 = float(
                input("Ingresa la desviación estándar muestral 2 (S2): "))
            return ((x1 - x2) - (z * math.sqrt((s1**2 / n1) + (s2**2 / n2))),
                    (x1 - x2) + (z * math.sqrt((s1**2 / n1) + (s2**2 / n2))))
    else:
        print("Distribución Exacta")


def IntervalosConfianzaP():
    p = float(
        input(
            "Ingresa la proporción (P). Si no ingresas un dato, se asumirá en 0.5: "
        ))
    z = float(input("Ingresa el quantil (Z\u03B1/2): "))
    n = int(input("Ingresa el tamaño muestral (n): "))
    return (p - (z * math.sqrt(p * (1 - p) / n)),
            p + (z * math.sqrt(p * (1 - p) / n)))


def init():
    respuesta = int(
        input(
            "Calcular Intervalos de confianza para \u03BC (1). \n Calcular Intervalos de confianza para \u03BC1 - \u03BC2 (2)\nOpción: "
        ))
    if respuesta == 1:
        print(IntervalosDeConfianzaParaMiu())
    elif respuesta == 2:
        print(IntervalosDeConfianzaParaMiuUnoMenosDos())
    elif respuesta == 3:
        print(IntervalosConfianzaP())
    print("Te amo mucho, tú puedes mi cielito :3")


init()
