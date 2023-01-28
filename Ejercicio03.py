#Escribir una función que divida una cadena dada en una
#lista de subcadenas cada vez que aparezca un carácter
#específico.
def separacion_caracter(cadena, caracter):# se define la funciòn
    cadena_separada = cadena.split(caracter)# se aplica el metodo split para dividir dividir 
    return cadena_separada

print(separacion_caracter("hola soy del VRAEM mi nombre es margoth: ", "a"))