def conversor(var1, var2, var3):
    if var3 == 1:
        if var2 == 1:
            valor_euro = var1 / 4300
            valor_euro = round(valor_euro, 2)
            resultado = ('El equivalente en Euros de ' +
                         str(var1) + ' COP es ' + str(valor_euro))
            return resultado
        elif var2 == 2:
            valor_usdolar = var1 / 4086
            valor_usdolar = round(valor_usdolar, 2)
            resultado = ('El equivalente en US DOLAR de ' +
                         str(var1) + ' COP es ' + str(valor_usdolar))
            return resultado
        elif var2 == 3:
            valor_yen = var1 / 31.39
            valor_yen = round(valor_yen, 2)
            resultado = ('El equivalente en YENES de ' +
                         str(var1) + ' COP es ' + str(valor_yen))
            return resultado
        elif var2 == 4:
            valor_reales = var1 / 793.23
            valor_reales = round(valor_reales, 2)
            resultados = ('El equivalente en REALES de ' +
                          str(var1) + ' COP es ' + str(valor_reales))
            return resultado
        elif var2 == 5:
            valor_candolar = var1 / 3134
            valor_candolar = round(valor_candolar, 2)
            resultados = ('El equivalente en CAN DOLAR de ' +
                          str(var1) + ' COP es ' + str(valor_candolar))
            return resultado
        elif var2 == 6:
            valor_ausdolar = var1 / 2826
            valor_ausdolar = round(valor_ausdolar, 2)
            resultados = ('El equivalente en AUS DOLAR de ' +
                          str(var1) + ' COP es ' + str(valor_ausdolar))
            return resultado
        elif var2 == 7:
            valor_mexpeso = var1 / 200.19
            valor_mexpeso = round(valor_mexpeso, 2)
            resultado = ('El equivalente en PESOS MEXICANOS de ' +
                         str(var1) + ' COP es ' + str(valor_mexpeso))
            return resultado
        elif var2 == 8:
            valor_arg = var1 / 34.93
            valor_arg = round(valor_arg, 2)
            resultado = ('El equivalente en PESOS ARGENTINOS de ' +
                         str(var1) + ' COP es ' + str(valor_arg))
            return resultado
        elif var2 == 9:
            valor_suecia = var1 / 406.28
            valor_suecia = round(valor_suecia, 2)
            resultado = ('El equivalente en CORONAS SUECAS de ' +
                         str(var1) + ' COP es ' + str(valor_suecia))
            return resultado
        elif var2 == 10:
            valor_soles = var1 / 1071
            valor_soles = round(valor_soles, 2)
            resultado = ('El equivalente en SOLES de ' +
                         str(var1) + ' COP es ' + str(valor_soles))
            return resultado
        else:
            resultado = ('Introduzca un número valido de idioma')
            return resultado

    elif var3 == 2:
        if var2 == 1:
            valor_euro = var1 * 4300
            valor_euro = round(valor_euro, 2)
            resultado = ('El equivalente en COP de ' +
                         str(var1) + ' EUROS es ' + str(valor_euro))
            return resultado
        elif var2 == 2:
            valor_usdolar = var1 * 4086
            valor_usdolar = round(valor_usdolar, 2)
            resultado = ('El equivalente en COP de ' + str(var1) +
                         ' US DOLAR es ' + str(valor_usdolar))
            return resultado
        elif var2 == 3:
            valor_yen = var1 * 31.39
            valor_yen = round(valor_yen, 2)
            resultado = ('El equivalente en COP de ' +
                         str(var1) + ' YENES es ' + str(valor_yen))
            return resultado
        elif var2 == 4:
            valor_reales = var1 * 793.23
            valor_reales = round(valor_reales, 2)
            resultado = ('El equivalente en COP de ' +
                         str(var1) + ' REALES es ' + str(valor_reales))
            return resultado
        elif var2 == 5:
            valor_candolar = var1 * 3134
            valor_candolar = round(valor_candolar, 2)
            resultado = ('El equivalente en COP de ' + str(var1) +
                         ' CAN DOLAR es ' + str(valor_candolar))
            return resultado
        elif var2 == 6:
            valor_ausdolar = var1 * 2826
            valor_ausdolar = round(valor_ausdolar, 2)
            resultado = ('El equivalente en COP de ' + str(var1) +
                         ' AUS DOLAR es ' + str(valor_ausdolar))
            return resultado
        elif var2 == 7:
            valor_mexpeso = var1 * 200.19
            valor_mexpeso = round(valor_mexpeso, 2)
            resultado = ('El equivalente en COP de ' + str(var1) +
                         ' PESOS MEXICANOS es ' + str(valor_mexpeso))
            return resultado
        elif var2 == 8:
            valor_arg = var1 * 34.93
            valor_arg = round(valor_arg, 2)
            resultado = ('El equivalente en COP de ' + str(var1) +
                         ' PESOS ARGENTINOS es ' + str(valor_arg))
            return resultado
        elif var2 == 9:
            valor_suecia = var1 * 406.28
            valor_suecia = round(valor_suecia, 2)
            resultado = ('El equivalente en COP de ' + str(var1) +
                         ' CORONAS SUECAS es ' + str(valor_suecia))
            return resultado
        elif var2 == 10:
            valor_soles = var1 * 1071
            valor_soles = round(valor_soles, 2)
            resultado = ('El equivalente en COP de ' +
                         str(var1) + ' SOLES es ' + str(valor_soles))
            return resultado
        else:
            resultado = ('Introduzca un número valido de idioma')
            return resultado
    else:
        resultado = ('Introduzca un número valido de operación')
        return resultado


# CONVERSOR DE MONEDAS A VALOR MAYO 2022
# operaciones_realizables = ['1: Convertir COP a otra moneda', '2: Convertir otra moneda a COP']

menu_operaciones = """
Bienvenido al conversor de monedas. 
A continuación encuentra las operaciones que realizamos:

1: Convertir COP a otra moneda
2: Convertir otra moneda a COP
"""

# listado_monedas = ['1: EURO', '2: US DOLAR', '3: YEN', '4: REALES (BRAZIL)', '5: CANADIAN DOLAR',
# '6: AUSTRALIAN DOLAR', '7: PESO MEXICANO', '8: PESO ARGENTINO', '9: CORONA SUECA',
# '10: SOLES (PERÚ)']

menu_monedas = """
A continuación encuentra el listado de monedas que manejamos:
1: EURO
2: US DOLAR
3: YEN
4: REALES (BRAZIL)
5: DOLAR CANADIENSE
6: DOLAR AUSTRALIANO
7: PESO MEXICANO
8: PESO ARGENTINO
9: CORONA SUECA
10: SOLES (PERÚ)
"""

Open = 0

while Open == 0:

    # print('Bienvenido al conversor. A continuación tenemos las operaciones a realizar: ')
    # print('\n'.join(map(str, operaciones_realizables)))
    print(menu_operaciones)

    dirección = int(
        input('Por favor indique el número de la operación a relizar: '))

    # print('A continuación tenemos las monedas sobre las cuales trabajamos:')
    # print('\n'.join(map(str, listado_monedas)))
    print(menu_monedas)

    Monedas = int(input(
        'Por favor indique el número correspondiente a la moneda sobre la cual quiere trabajar: '))

    VALOR = float(input('Indique la cantidad que posee de la moneda base: '))

    op = conversor(VALOR, Monedas, dirección)
    print(op)

    Open = int(
        input('Presione 1 para cerrar el programa o 0 para realizar otra operación: '))
