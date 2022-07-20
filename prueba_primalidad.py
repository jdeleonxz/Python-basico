def es_primo(x):
    contador = 0

    for i in range(1, x+1):
        if i == 1 or i == x:
            continue
        if x % i == 0:
            contador += 1
    if contador == 0:
        return True
    else: 
        return False


def run():
    numero = int(input('Escriba un número: '))
    if es_primo(numero):
        print('Es un número primo')
    else:
        print('No es un número primo')


if __name__ == '__main__':
    run()