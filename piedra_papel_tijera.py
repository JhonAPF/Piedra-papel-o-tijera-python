import random

def juego():
    opciones = {1: 'piedra', 2: 'papel', 3: 'tijera'}
    victorias_usuario = 0
    victorias_pc = 0

    while (victorias_usuario < 3) and (victorias_pc < 3):
        pc = opciones[random.randint(1, 3)]
        usuario = int(input("Elige: \n"
                            "1. Piedra\n"
                            "2. Papel\n"
                            "3. Tijera\n"))

        if usuario not in opciones:
            print("Error de entrada. Por favor, elige 1, 2 o 3.")
            continue

        print(f"Elección del usuario: {opciones[usuario]}")
        print(f"Elección de la PC: {pc}")

        if opciones[usuario] == pc:
            print("¡Empate!\n")
        elif (opciones[usuario] == "piedra" and pc == "tijera") or (opciones[usuario] == "papel" and pc == "piedra") or (opciones[usuario] == "tijera" and pc == "papel"):
            print("¡Ganaste!\n")
            victorias_usuario += 1
        else:
            print("¡Perdiste!\n")
            victorias_pc += 1

        print(f"Marcador: Usuario {victorias_usuario}/3 - PC {victorias_pc}/3")

    if victorias_usuario == 3:
        return "¡Felicidades! Ganaste."
    else:
        return "Lo siento, perdiste."

print(juego())
