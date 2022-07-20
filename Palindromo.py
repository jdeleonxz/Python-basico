def palindromo(palabra):
    palabra = palabra.replace(' ', '') #Quitamos espacios en blanco
    palabra = palabra.lower()          #Ponemos todas las letras en miniscula
    palabra_invertida = palabra[::-1]  #Invertimos la palabra
    if palabra == palabra_invertida:
        return True
    else:
        return False


# IMPORTANTE: crear una función que sea la encargada de correr el programa
def run():
    palabra = input('Escriba una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es un palindromo')
    else: 
        print('No es un palindromo')


# Punto de entrada del programa en el cual python correra todo lo que esta debajo
if __name__ == '__main__':
    run()

