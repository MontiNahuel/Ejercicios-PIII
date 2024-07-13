def permutaciones(palabras, palabrasCopy, frasesFormadas, fraseActual):
    if len(fraseActual) == len(palabras):
        frasesFormadas.append(fraseActual)
    else:
        for i in range (len(palabrasCopy)):
            palabra = palabrasCopy[i]
            fraseActual = fraseActual + palabra
            palabrasCopy.remove(palabra)
            print(fraseActual)
            permutaciones(palabras, palabrasCopy, frasesFormadas, fraseActual)
            

def permutacionesV2(palabras, palabrasCopy, frasesFormadas, fraseActual):
    if len(fraseActual) == len(palabras):
        frasesFormadas.append(fraseActual)
    else:
        for i in range(len(palabrasCopy)):
            palabra = palabrasCopy[i]
            nuevaFrase = fraseActual + palabra
            nuevasPalabrasCopy = palabrasCopy[:i] + palabrasCopy[i+1:]
            permutacionesV2(palabras, nuevasPalabrasCopy, frasesFormadas, nuevaFrase)
            

def permutacionesV3(palabras, profundidad, frasesFormadas, fraseActual):
    if profundidad == len(palabras):
        frasesFormadas.append(fraseActual)
    else:
        for i in range(len(palabras)):
            palabra = palabras[i]
            nuevaFrase = fraseActual + palabra
            permutacionesV3(palabras, profundidad + 1, frasesFormadas, nuevaFrase)

def permutacionesV4(palabras, palabrasNuevas, profundidad, frasesFormadas, fraseActual):
    if (profundidad == len(palabras)):
        frasesFormadas.append(fraseActual)
    else:
        for i in range(len(palabrasNuevas)):
            palabra = palabrasNuevas[i]
            nuevaFrase = fraseActual + palabra
            palabrasNuevas2 = palabrasNuevas.copy()
            palabrasNuevas2.remove(palabra)
            permutacionesV4(palabras, palabrasNuevas2, profundidad + 1, frasesFormadas, nuevaFrase)

palabras = ['A', 'B', 'C', 'D']
frasesFormadas = []
#permutacionesV2(palabras, palabras.copy(), frasesFormadas, "")
#permutacionesV3(palabras, 0, frasesFormadas, "")
permutacionesV4(palabras, palabras.copy(), 0, frasesFormadas, "")
print(frasesFormadas)
