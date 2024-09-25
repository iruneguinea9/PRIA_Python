import random

# ------------------------- FUNCIÓN QUE LANZA EL MENÚ EN BUCLE HASTA QUE SELECCIONE EL NÚMERO DE JUGADORES -------------------------------
jugadores = {}
palos =  ["corazones","picas","diamantes","tréboles"]
cartas = ["as",2,3,4,5,6,7,8,9,10,"joker","reina","rey"]
baraja = [(palo,carta) for palo in palos] 
def menu():
    while True:
        try:
            nJugadores = int(input("""
            ################# BLACK JACK #################

            Introduce el número de jugadores (máximo 3):                        
                                   """))
            if nJugadores in [1, 2, 3]:
                for i in range(nJugadores):
                    print("Turno del juegador nº",i+1)
                    nombre = input("Por favor, introduce tu nombre")
                    jugadores[nombre] = 0
                    seguir= True
                    while (seguir):
                        print("El crupier te reparte una carta... ")

 
        except:
            print("Por favor, introduce un número del 1-3")


def valorCarta(carta):
    if(carta)


# ------------------------------------------------ LANZAMOS EL MENÚ ----------------------------------------------------

if __name__ == '__main__':
   menu()



