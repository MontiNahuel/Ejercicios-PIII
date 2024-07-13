def permutacionesUnicas(palabras : list, profundidad : int, frasesFormadas : list, fraseActual : str, longitudTotal : int) -> None:
    if (profundidad == longitudTotal):
        frasesFormadas.append(fraseActual)
    else:
        for f in range(len(palabras)):
            palabra = palabras[f]
            fraseActualNueva = fraseActual + palabra
            palabrasNuevas = palabras.copy()
            palabrasNuevas.remove(palabra)
            permutacionesUnicas(palabrasNuevas, profundidad + 1, frasesFormadas, fraseActualNueva, longitudTotal)
            fraseActualNueva = fraseActualNueva[:-1]

palabras = ['A', 'B', 'C', 'D']
frasesFormadas = []
permutacionesUnicas(palabras, 0, frasesFormadas, "", len(palabras))
print(frasesFormadas)