def run():
    numero = int(input('Ingrese el número que quiere potenciar hasta 1000: '))
    conteo = 0
    potencia = numero**conteo
    while potencia <= 1000:
        print(str(numero) + ' elevado a la ' + str(conteo) + ' es igual a ' + str(potencia))
        conteo = conteo + 1
        potencia = numero**conteo
    print('El numero de veces que se elevó el numero fueron: ' + str(conteo))


if __name__ == '__main__':
    run()
