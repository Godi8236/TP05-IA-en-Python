def frutas_verduras(dato):
    frutas = ["banana","manzana","pera"]
    verduras = ["lechuga","zanahoria","cebolla"]
    cantFrutas = 0
    cantVerduras = 0
    while dato != "fin":
        if dato in frutas:
            cantFrutas += 1
        elif dato in verduras:
            cantVerduras += 1
        dato = input("Ingrese otra fruta/verdura (o 'fin' para salir): ")
    if cantFrutas > cantVerduras:
        respuesta = "Se ingresaron mas frutas que verduras"
    elif cantVerduras > cantFrutas:
        respuesta = "Se ingresaron mas verduras que frutas"
    else:
        respuesta = "Se ingresaron cantidades iguales"
    return respuesta,cantFrutas,cantVerduras
datoUsuario = input("Ingrese una fruta: ")
respuesta,cantFrutas,cantVerduras = frutas_verduras(datoUsuario)
print("\n--- Resultado ---" )
print("La cantidad de frutas ingresadas es: ",cantFrutas)
print("La cantidad de verduras ingresadas es: ",cantVerduras)
print(respuesta)