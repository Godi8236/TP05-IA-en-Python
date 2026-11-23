def analizar_frase(frase):
    vocales = "aeiouáéíóú"
    consonantes = "bcdfghjklmnñpqrstvwxyz"
    cantEspacios = frase.count(" ")
    cantPalabras = len(frase.split())
    cantVocales = 0
    cantConsonantes = 0
    for i in frase:
        if i in vocales:
            cantVocales += 1
        elif i in consonantes:
            cantConsonantes += 1
    return cantPalabras,cantVocales,cantConsonantes,cantEspacios
fraseUsuario =(input("Ingrese una frase: "))
cantPalabras,cantVocales,cantConsonantes,cantEspacios = analizar_frase(fraseUsuario)

print("\n--- Resultado ---" )
print(f"Cantidad de vocales: ",cantVocales)
print(f"Cantidad de consonantes: ",cantConsonantes)
print(f"Cantidad de palabras: ",cantPalabras)
print(f"Cantidad de espacios: ",cantEspacios)