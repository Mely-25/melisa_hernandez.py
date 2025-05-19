import random

def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def pedir_letra():
    while True:
        letra = input("Ingresa una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("esa no es una letra valida. intentá otra vez.")

def jugar():
    palabras = ["amable", "extravagante", "prejuicio", "cazadores", "princesa"]
    palabra_secreta = random.choice(palabras)
    vidas = 6
    letras_adivinadas = []
    letras_incorrectas = []

    print("\n🎮 Bienvenido/a al juego del ahorcado 🎮")
    
    while vidas > 0:
        print("\nPalabra:", mostrar_palabra(palabra_secreta, letras_adivinadas))
        print("Vidas restantes:", vidas)
        print("Letras incorrectas:", ", ".join(letras_incorrectas))

        letra = pedir_letra()

        if letra in letras_adivinadas or letra in letras_incorrectas:
            print("⚠️  Ya probaste con esa ingresá otra letra.")
            continue

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("✅ ¡Sii! la letra está en la palabra.")
        else:
            letras_incorrectas.append(letra)
            vidas -= 1
            print("❌ mmm... no es correcto seguí intentando.")

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("\n🎉 ¡Felicidades! Ganaste:", palabra_secreta)
            break
    else:
        print("\n💀 Perdiste, te quedaste sin vidas. La palabra era:", palabra_secreta)

while True:
    jugar()
    respuesta = input("\n¿Querés jugar de nuevo? (s/n): ").lower()
    if respuesta != 's':
        print("👋 ¡Gracias por jugar! nos vemos.")
        break