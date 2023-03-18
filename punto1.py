from os import remove

opcion = 1 
ciclistas = []

print()
while opcion != 0:
    print()
    print()
    print("*********** LISTA DE SUPERMERCADO ***********")
    print()
    print("Opcion 1 = Ingresar una ciclista")
    print("Opcion 2 = Mostrar todos los ciclistas")
    print("Opcion 3 = Buscar un ciclista por codigo")
    print("Opcion 4 = Editar un ciclista por codigo")
    print("Opcion 5 = Eliminar un codigo")
    print("Opcion O = Salir ")
    print()
    opcion = int(input("SELECCIONE UNA OPCIÓN = "))
    print()
    if(opcion == 1):
        ciclista = {}
        print("----------INGRESAR ciclista-----------")
        ciclista['codigo']  = len(ciclistas)+1
        ciclista['nombre']  = input("Digite el nombre del ciclista = ")
        ciclista['edad']    = int(input("Digite el edad del ciclista = "))
        ciclista['pais']    = input("Digite el pais del ciclista = ")
        ciclista['equipo']  = input("Digite el equipo del ciclista = ")
        ciclista['tiempo']  = int(input("Digite el tiempo del ciclista = "))
        ciclistas.append(ciclista)
        print()
        print("ciclista registrado con exito")
        print()
    elif(opcion == 2):
        if(len(ciclistas) > 0):
            print("----------LISTADO DE ciclistas-----------")
            print(f"listado de ciclistas registrados => {ciclistas}")
        else:
            print("la lista no tiene elementos!")
    elif(opcion == 3):
        print()
        print("----------BUSCAR ciclista-----------")
        buscado = int(input("Ingrese el codigo del ciclista a buscar = "))
        for ciclista in ciclistas:
            if(buscado == ciclista['codigo']):
                print(f"ciclista encontrado => {ciclista}")
                print()
            else:
                print("ciclista no encontrado =/ ")
    elif(opcion == 4):
        print("----------EDITAR ciclista-----------")
        print()
        buscado = int(input("Ingrese el codigo del ciclista a editar = "))
        for ciclista in ciclistas:
            if(buscado == ciclista['codigo']):
                print (f"ciclista a editar {buscado}")
                ciclista['timepo'] = int(input("Ingrese el  NUEVO tiempo del ciclista = "))
                print("tiempo editado con exito!")
            else:
                print("ciclista no encontrado =/ ")
    elif(opcion == 5):
        print("----------ELIMINAR ciclista-----------")
        print()
        buscado = int(input("Ingrese el codigo del ciclista a eliminar = "))
        for ciclista in ciclistas:
            if(buscado == ciclista['codigo']):

                print(f"ciclista eliminar => {ciclista}")
                ciclistas.remove(ciclista)
                print("ciclista eliminado con exito! ")
                break
            else:
                print("ciclista no encontrado =/ ")
    else:
        print("Opcion invalida")
        print()