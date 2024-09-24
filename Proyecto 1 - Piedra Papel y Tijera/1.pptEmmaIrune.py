import random

opciones = ["piedra", "papel", "tijera"]
marcador = {"humano":0, "cpu":0}

# ------------------------- FUNCIÓN QUE LANZA EL MENÚ EN BUCLE HASTA QUE SELECCIONE EL 4 -------------------------------

def menu():
    opcionH = 0
    while True:
        try:
            opcionH = int(input("""
                        Elige tu opción:
                        [1] Piedra
                        [2] Papel
                        [3] Tijera
                        [4] **** SALIR ****
                    """))

            if opcionH in [1, 2, 3, 4]:
                if opcionH == 4:
                    print("Gracias por jugar!")
                    break
                if marcador["cpu"]==3:
                    print("OOOOOOOOOHHHHHH, Ha ganado la máquina...  :( ")
                    break
                if marcador["humano"]==3:
                    print("Yay! Has ganado!")
                    break
                else:
                    juego(opcionH)
                    opcionH = 0
        except:
            print("Por favor, introduce un número del 1-4")


# ---------------------- FUNCIÓN QUE INFORMA AL USUARIO DE LAS ELECCIONES Y MUESTRA MARCADOR ---------------------------

def juego(opcionH):
        opcionPC = random.randint(1, 3)

        print("--- Has elegido: ",opciones[opcionH-1]," ---")
        print("--- El ordenador ha elegido: ", opciones[opcionPC-1]," ---")

        comprobarResul(opcionH, opcionPC)
        print("[HUMANO ",marcador["humano"]," | ", marcador["cpu"],"CPU]")


# ---------------------- FUNCIÓN QUE COMPRUEBA LOS RESULTADOS Y ACTUALIZA EL MARCADOR ----------------------------------

def comprobarResul(opcionH, opcionPC):
    print("\n")

    if (opcionPC == opcionH):
        print("EMPATE")
        return

    if (opcionPC == 1):
        if (opcionH == 2):
            print("Enhorabuena, has ganado 1pto")
            marcador["humano"] += 1
            return
        else:
            print("Vaya, has perdido")
            marcador["cpu"] += 1
            return

    if (opcionPC == 2):
        if (opcionH == 1):
            print("Vaya, has perdido")
            marcador["cpu"] += 1
            return
        else:
            print("Enhorabuena, has ganado 1pto")
            marcador["humano"] += 1
            return

    if (opcionPC == 3):
        if (opcionH == 1):
            print("Enhorabuena, has ganado 1pto")
            marcador["humano"] += 1
            return
        else:
            print("Vaya, has perdido")
            marcador["cpu"] += 1
            return


# ------------------------------------------------ LANZAMOS EL MENÚ ----------------------------------------------------

if __name__ == '__main__':
   menu()





