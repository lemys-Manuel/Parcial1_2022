'''
Menu de Opciones
1.Digitar 1 para recibir{codigo,nombre,precio} de un producto {+0.4}
2.digitar 2 pára mostrar todos los p+roductos registrados{+0.4}
3.digitar 3 pára permitir buscar por codigo un producto y editar el precio de este{+0.4}
4.digitar 4 para buscar por codigo un producto y eliminar el producto{+0.4}
5.digitar 0 para salir'''


print('Menu de Opciones Supermercado')
print('***')
print('1.para agregar producto')
print('2.para mostrar producto')
print('3. para editar producto')
print('4.para eliminar producto')
print('5. digita 0 para salir producto')

opcion=1
productos=[]
while opcion!=0:
    opcion=int(input('Digite una de las opciones del Menu:\n'))
    if(opcion==1):
        producto={}
        
        producto['codigo']=str(input('digita el codigo del producto:\n'))
        producto['nombre']=str(input('digita el Nombre del producto:\n'))
        producto['precio']=int(input('digita el precio del producto:\n'))
      
        productos.append(producto)
        
    elif opcion==2:
        print(productos)
    elif opcion==3:
        buscarcodigo=input('Digita un codigo a buscar:\n')
        for producto in productos:
            if producto['codigo']==buscarcodigo:
              print('producto encontrado exitosamente')
              break
            else:
                print('el Producto no se encuentra en La lista producto') 
                break
    elif opcion==4:
        eliminarcodigo=input('Digita el codigo a eliminar:\n')
        for producto in productos:
            if producto['codigo']==eliminarcodigo:
                eliminarcodigo.remove(producto)
                del producto['codigo']
                eliminarcodigo.clear()
else: print('haz presionado 0 Saliendo del programa')             
            