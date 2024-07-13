def combinationSumUnique(numeros, target, suma, combinacionActual, combinaciones):
    if suma == target:
        combinaciones.append(combinacionActual.copy())
        return
    if suma > target:
        return
    else:
        for f in range(len(numeros)):
            sumaActual = suma + numeros[f]
            combinacionActual.append(numeros[f])
            numerosNuevos = numeros[:f] + numeros[f+1:]
            combinationSumUnique(numerosNuevos, target, sumaActual, combinacionActual, combinaciones)
            combinacionActual.pop()

def combinationSumUniqueV2(numeros, target, suma, combinacionActual, combinaciones):
    if suma == target:
        combinaciones.append(combinacionActual.copy())
        return
    if suma > target:
        return
    else:
        for f in range(len(numeros)):
            sumaActual = suma + numeros[f]
            combinacionActual.append(numeros[f])
            numerosNuevos = numeros[:f] + numeros[f+1:]
            combinationSumUniqueV2(numerosNuevos, target, sumaActual, combinacionActual, combinaciones)
            combinacionActual.pop()



numeros : list = [2, 3, 5, 7]
print("Numeros cantidatos: ", numeros)
combinaciones : list = []
combinationSumUniqueV2(numeros, 10, 0, [], combinaciones)
print(combinaciones)