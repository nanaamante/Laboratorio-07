#Escribir una función que determine la longitud de la
#subcadena más larga que contiene solo dígitos.
def lontitud_digitos(cadena):
    digitos = 0

    for i in cadena:
        if i.isdigit():
            digitos += 1
        else:
            pass 
    return digitos

texto = input("Digite texto: ")
resultado = lontitud_digitos(texto)

print("La longitud de digitos es: ",resultado )