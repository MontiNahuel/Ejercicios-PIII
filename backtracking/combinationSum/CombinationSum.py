from random import randint as r

def combinationSum(numeros, target, suma, combinacion, combinaciones):
    if suma == target:
        combinaciones.append(combinacion.copy())
        return
    if suma > target:
        return
    else:
        for f in range(len(numeros)):
            nuevaCombinacion = combinacion.copy()
            nuevaCombinacion.append(numeros[f])
            nuevaSuma = suma + numeros[f]
            combinationSum(numeros, target, nuevaSuma, nuevaCombinacion, combinaciones)
            
def combinationSumV2(numeros, target, suma, combinacion, combinaciones):
    if suma == target:
        combinaciones.append(combinacion.copy())
        return
    if suma > target:
        return
    else:
        for f in range(len(numeros)):
            combinacion.append(numeros[f])
            nuevaSuma = suma + numeros[f]
            combinationSum(numeros, target, nuevaSuma, combinacion, combinaciones)
            combinacion.pop()

#numeros : list = [r(1, 10) for _ in range(10)]
numeros : list = [2, 3, 6, 7]
print("Numeros cantidatos: ", numeros)
combinaciones : list = []
combinationSum(numeros, 10, 0, [], combinaciones)
print(combinaciones)