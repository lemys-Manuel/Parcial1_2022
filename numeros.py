'''.Construir un programa que permita ingresar N (cantidad digitada por
el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3
fueron ingresados (+1)'''





contador=0
contador1=0


nombreusuario=str(input('Ingrese su nombre Por Favor:'))
print(f'Hola {nombreusuario} Ingrese la cantidad de numeros enteros que desea digitar:')

numero=int(input('digite la cantidad de numeros:'))
for i in range (numero):

    pedido=int(input('digite un numero:'))

    if(pedido %2 ==0):
        contador=contador +1
        print(f'{pedido} es multiplo de 2')

    elif (pedido %3 ==0):
        contador1=contador1 +1
        print(f'{pedido} es multiplo de 3')
    
print(f'multiplos de 2 -> tenemos {contador} Numeros y multiplos de 3 -> Tenemos {contador1} Numeros')     