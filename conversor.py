pesos = input("Ingrese el valor en pesos colombianos COP: ")
pesos = float(pesos) #Convertir el texto en número decimal

Valor_dolar = 4085 #Valor de 1 dolar en pesos colombianos 

cant_dolares = pesos / Valor_dolar
cant_dolares = round(cant_dolares, 2) #Redondear con solo dos decimales
cant_dolares = str(cant_dolares)  #Pasar el valor a texto

print('Es equivalente a $' + cant_dolares + ' dolares')


