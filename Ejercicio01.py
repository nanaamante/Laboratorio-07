#Escribir una función que determine si una cadena es un
#palíndromo (se lee igual en ambos sentidos) o no:
def es_palindromo(cadena):
    cadena = cadena.lower() #Cambiamos todas las mayúculas a minúsculas
    cadena = cadena.replace(" ","") #Quitamos todos los espacios
    cadena = cadena.replace("á", "a") #Remmplazamos las palabras con tilde con una palabra normal.
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")

    posicion_izquierda = 0
    posicion_derecha = len(cadena)-1

    while posicion_derecha >= posicion_izquierda:
        if not cadena[posicion_izquierda]== cadena[posicion_derecha]:
           return False
        posicion_izquierda += 1
        posicion_derecha -= 1
    return True

cadena = input("Ingrese una palabra o frase: ")

if es_palindromo(cadena):
    print("Es una palabra o frase Palindromo")
else:
    print("No una palabra o frase Palindromo")