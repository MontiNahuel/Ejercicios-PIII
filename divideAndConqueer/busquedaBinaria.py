def busquedaBinaria(data : list, target : all) -> bool:
    inicio = 0
    fin = len(data) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if data[medio] == target:
            return True
        elif data[medio] < target:
            inicio = medio + 1
        else:
            fin = medio - 1
    return False


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 9
    print(busquedaBinaria(data, target))

# Prueba busquedaBinaria
if __name__ == "__main__":
    main()
    