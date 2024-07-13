def combinationSumHeuristica(candidatos : list, target : int, suma : int, combinacion : list, combinaciones : list) -> None:
    if (suma == target):
        if (not existeCombinacion(combinaciones, combinacion.copy())):
            combinaciones.append(combinacion.copy())
        return None
    elif suma > target:
        return None
    else:
        for f in range(len(candidatos)):
            candidato = candidatos[f]
            combinacion.append(candidato)
            sumaActual = suma + candidato
            nuevosCandidatos = candidatos.copy()
            nuevosCandidatos.remove(candidato)
            combinationSumHeuristica(nuevosCandidatos, target, sumaActual, combinacion, combinaciones)
            combinacion.pop()

def existeCombinacion(combinacionesCorrectas : list, combinacion : list) -> bool:
    for f in range(len(combinacionesCorrectas)):
        for i in range(len(combinacionesCorrectas[f])):
            if combinacionesCorrectas[f][i] in combinacion:
                combinacion.remove(combinacionesCorrectas[f][i])
                
    return len(combinacion) == 0
    
           
listaNumeros : list = [2, 3, 5, 7, 8]
target : int = 10
combinaciones : list = []
combinationSumHeuristica(listaNumeros, target, 0, [], combinaciones)
print(combinaciones)

# Prueba existeCombinacion
#combinacion : list = [2, 3, 4]
#listaCombinaciones = [[2, 3, 5], [2, 3, 7], [2, 5, 7], [3, 5, 7]]
#print(existeCombinacion(listaCombinaciones, combinacion)) # True