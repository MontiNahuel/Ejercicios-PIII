def mostrar_tablero():
    for i in range(0, 9, 3):
        print(tablero[i], "|", tablero[i + 1], "|", tablero[i + 2])
        if i < 6:
            print("---------")


def jugar(tablero : list, ficha : str, posicion : int) -> bool:
    if (posicion < 0 or posicion > 8):
        return False
    else:
        tablero[posicion] = ficha
        return True

def ganador(tablero : list, ficha : str) -> bool:
    for i in range(0, 9, 3):
        if tablero[i] == ficha and tablero[i + 1] == ficha and tablero[i + 2] == ficha:
            return True
    for i in range(3):
        if tablero[i] == ficha and tablero[i + 3] == ficha and tablero[i + 6] == ficha:
            return True
    if tablero[0] == ficha and tablero[4] == ficha and tablero[8] == ficha:
        return True
    if tablero[2] == ficha and tablero[4] == ficha and tablero[6] == ficha:
        return True
    return False

def tablero_lleno(tablero : list) -> bool:
    return " " not in tablero

def jugarIa(tablero : list, ficha : str) -> bool:
    pass
    

tablero = [" " for _ in range(9)]