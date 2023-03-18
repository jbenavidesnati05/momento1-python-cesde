print()
print("***************** INICO DEL PROGRAMA *********************")
print()
cantidad = 20

contador = 0
multi2   = 0
multi3   = 0
multi23   = 0
multiX   = 0
print()
while contador < cantidad:
    valor = int(input(f"Ingrese el número {contador+1} a verificar =>  "))
    contador += 1
    if  valor%2 == 0:
        multi2 +=1
    elif valor%3 == 0:
        multi3 +=1
    elif valor%3 == 0 and valor%2:
        multi23 +=1
    else:
        multiX +=1

print()
print("***************** RESULTADOS *********************")
print()
print(f"1) Son multiplos de 2 = {multi2}")
print(f"2) Son multiplos de 3 = {multi3}")
print(f"2) Son multiplos de 2 y de 3 = {multi23}")
print(f"3) No son  multiplos ni de 2 ni de 3  = {multiX}")
print(f"4) Cantidad de valores verificados = {cantidad}")