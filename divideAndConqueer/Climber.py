def obtenerPico(data : list, inicio : int, fin : int, valor : int, encontrado : bool) -> int:
    medio = (inicio + fin) // 2
    if medio == 0 and data[medio] > data[medio + 1]:
        encontrado = True
        return data[medio]
    elif medio == len(data) - 1 and data[medio] > data[medio - 1]:
        encontrado = True
        return data[medio]
    elif data[medio] > data[medio - 1] and data[medio] > data[medio + 1]:
        encontrado = True
        return data[medio]
    if inicio + 1 == fin:
        return -1
    if inicio == fin:
        return -1
    else:
        if data[medio] > data[medio - 1] and data[medio] > data[medio + 1]:
            return data[medio]
        nuevoValor = obtenerPico(data, medio + 1, fin, valor, encontrado)
        if not encontrado and nuevoValor != -1:
            valor = nuevoValor
        valor = obtenerPico(data, inicio, medio - 1, valor, encontrado)
        if not encontrado and nuevoValor != -1:
            valor = nuevoValor
        return valor

def main():
    data = [1, 1, 3, 6, 5, 6, 6, 7, 8]
    print(obtenerPico(data, 0, len(data) - 1, -1, False))


if __name__ == "__main__":
    main()