#Escribir una función que determine la longitud de la
#subcadena más larga que no contiene ninguna letra
#repetida.
def longitud_subcadena(frase):# se esta definiendo la funciòn
    palabras = frase.split() # se esta unando la funciòn split para determinar la longitud  
    masLarga = palabras[0]# se define la posiciòn

    for i in range(1, len(palabras)): #se aplica la funciòn len para contar
        if len(masLarga) < len(palabras[i]):
            masLarga = palabras[i]

    print(len(masLarga))
    return masLarga

frase = input("Ingrese la frase: ")
print(longitud_subcadena(frase))