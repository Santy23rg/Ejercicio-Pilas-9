def menu(pila):
    while True:
        print("\nQue desea realizar con la pila?\n")
        resp = int(input("1. Ordenar de manera descendente \n2. Eliminar un dato \n3. Salir del programa\n"))
        if resp == 1:
            pila.sort(reverse=True)
            print("La pila ordenada es\n",pila)
        elif resp == 2:
            num = int(input("Ingrese el numero que desea Eliminar: \n"))
            respo = delete(pila, num)
            if respo:
                print("Se elimino correctamente el dato, La pila resultante es:\n", pila)
            else:
                print("El dato buscado no se encuentra en la pila\n")
        elif resp == 3:
            break
        else:
            print("Opcion no valida intente nuevamente")

def delete(pila, num):
    aux = []
    while len(pila) != 0:
        deleted = pila.pop()
        if deleted != num:
            aux.append(deleted)
        else:
            if len(aux)>0:
                while len(aux) != 0:
                    delet = aux.pop()
                    pila.append(delet)
                return pila
            else:
                return pila
    while len(aux) != 0:
        delet = aux.pop()
        pila.append(delet)
    
    print(pila)
    return False

def factorial(num):
    auxNum = 1  
    for i in range(1, num+1):
        auxNum *= i
        
    return auxNum
    
pila = []

while True:
    num = int(input("Ingrese el numero factorial que desea agregar a la pila: "))
    fact = factorial(num)
    pila.append(fact)
    resp = int(input("Desea ingresar otro numero?\n1) Si\n2) No\n"))
    if resp == 1:
        continue
    else:
        print("La pila registrada es: \n", pila)
        break
    
menu(pila)
