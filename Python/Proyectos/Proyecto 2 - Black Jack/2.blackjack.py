import random
import time

# Función para generar una carta al azar 
def generar_carta():
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10 para J, Q, K y 11 para As
    return random.choice(cartas)

# Función para ajustar el valor del As si el jugador se pasa de 21
def ajustar_as(mano):
    while sum(mano) > 21 and 11 in mano:
        # Convierte el As de 11 a 1 si se ha pasao de 21
        mano[mano.index(11)] = 1
    return mano

def jugar_blackjack():
    print("Juego de BlackJack!")
    jugadores = []
    
    # Elegir el número de jugadores
    while True:
        try:
            num_jugadores = int(input("Elige número de jugadores (1, 2 o 3): "))
            if num_jugadores in [1, 2, 3]:
                break
            else:
                print("Elige entre 1, 2 o 3 jugadores")
        except ValueError:
            print("Error. Tiene que ser un número.")
    
    # Ingresar los nombres de los jugadores
    for i in range(num_jugadores):
        nombre = input(f"Inroduce el nombre del jugador {i + 1}: ")
        jugadores.append({'nombre': nombre, 'mano': [], 'activo': True})
    
    # Ronda de turnos para cada jugador
    for jugador in jugadores:
        print(f"\nTurno de {jugador['nombre']}")
        jugador['mano'].append(generar_carta())
        jugador['mano'].append(generar_carta())
        
        while True:
            print(f"Cartas de {jugador['nombre']}: {jugador['mano']} (Total: {sum(jugador['mano'])})")
            
            # Revisar si el jugador se pasa de 21
            jugador['mano'] = ajustar_as(jugador['mano'])
            if sum(jugador['mano']) > 21:
                print(f"{jugador['nombre']} se ha pasado de 21 y queda eliminado.")
                jugador['activo'] = False
                break
            elif sum(jugador['mano']) == 21:
                print("¡BlackJack!")
                break
            
            # Sigue o se planta
            decision = input("Quieres otra carta? (s/n): ").strip().lower()
            if decision == 's':
                carta = generar_carta()
                print(f"{jugador['nombre']} has sacado un {carta}")
                jugador['mano'].append(carta)
                time.sleep(1)  # Pausa que si no se me cierra
            else:
                print(f"{jugador['nombre']} se planta.")
                break

    # Ganador
    ganador = None
    max_puntuacion = 0
    for jugador in jugadores:
        if jugador['activo']:
            puntuacion = sum(jugador['mano'])
            if 21 >= puntuacion > max_puntuacion:
                max_puntuacion = puntuacion
                ganador = jugador['nombre']
    
    # Mostrar el resultado
    if ganador:
        print(f"\n{ganador} ha ganado!")
    else:
        print("\nTodos los jugadores se han pasado de 21. Todos pierden.")

# Iniciar el juego
jugar_blackjack()
