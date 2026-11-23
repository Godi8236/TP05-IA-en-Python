# Prompt utilizado:
# "Genera un conjunto de 5 frutas diferentes para utilizar
# en un ejercicio de Python sobre conjuntos."
# IA utilizada: ChatGPT
frutasIA = {"manzana", "banana", "pera", "naranja", "mango"}
frutas = set()
def analizar_conjuntos(fruta):
    while fruta != "fin":
        frutas.add(fruta)
        fruta = input("Ingrese frutas: (fin para terminar): ")
frutaUsuario = input("Ingrese fruta: (fin para terminar): ")
analizar_conjuntos(frutaUsuario)

# Elementos que están en ambos conjuntos
interseccion = frutas & frutasIA
# Elementos que están solamente en el conjunto del usuario
soloFrutas = frutas - frutasIA
# Elementos que están solamente en el conjunto de la IA
soloIA = frutasIA - frutas

print("\nRESULTADOS")
print("Elementos que están en ambos conjuntos:", interseccion)
print("Elementos que están solo en el conjunto del usuario:", soloFrutas)
print("Elementos que están solo en el conjunto de la IA:", soloIA)

if frutas == frutasIA:
    print("Los conjuntos son idénticos.")
else:
    print("Los conjuntos son diferentes.")