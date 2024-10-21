# serpiente_game.py

import pygame
import random

pygame.init()

# Configurar la ventana
WIDTH = 600
HEIGHT = 600
ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Serpiente")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Fuente para mostrar la puntuación
fuente = pygame.font.SysFont('calibri', 30)

clock = pygame.time.Clock()

def pintar_text(text, color, size, x, y):
    fuente = pygame.font.SysFont('calibri', size)
    texto_surface = fuente.render(text, True, color)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = (x, y)
    ventana.blit(texto_surface, texto_rect)

class Serpiente:
    def __init__(self):
        self.posicion = [(200, 200), (220, 200), (240, 200)]
        self.direccion = 'RIGHT'
        self.tamanio = 3

    def mover(self):
        cabeza = self.posicion[0]
        nueva_cabeza = cabeza
        
        if self.direccion == 'UP':
            nueva_cabeza = (cabeza[0], cabeza[1] - 20)
        elif self.direccion == 'DOWN':
            nueva_cabeza = (cabeza[0], cabeza[1] + 20)
        elif self.direccion == 'LEFT':
            nueva_cabeza = (cabeza[0] - 20, cabeza[1])
        elif self.direccion == 'RIGHT':
            nueva_cabeza = (cabeza[0] + 20, cabeza[1])

        self.posicion.insert(0, nueva_cabeza)
        self.posicion.pop()

    def pintar(self):
        for pos in self.posicion:
            pygame.draw.rect(ventana, VERDE, (pos[0], pos[1], 20, 20))

    def crecer(self):
        self.tamanio += 1

    def se_ha_pegao(self):
        return len(self.posicion) > len(set(self.posicion))

class Comida:
    def __init__(self):
        self.posicion = (random.randint(0, WIDTH - 20) // 20 * 20,
                          random.randint(0, HEIGHT - 20) // 20 * 20)

    def pintar(self):
        pygame.draw.rect(ventana, ROJO, (self.posicion[0], self.posicion[1], 20, 20))

def main():
    serpiente = Serpiente()
    comida = Comida()
    puntos = 0
    game_over = False
    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and serpiente.direccion != 'DOWN':
                    serpiente.direccion = 'UP'
                elif evento.key == pygame.K_DOWN and serpiente.direccion != 'UP':
                    serpiente.direccion = 'DOWN'
                elif evento.key == pygame.K_LEFT and serpiente.direccion != 'RIGHT':
                    serpiente.direccion = 'LEFT'
                elif evento.key == pygame.K_RIGHT and serpiente.direccion != 'LEFT':
                    serpiente.direccion = 'RIGHT'

        serpiente.mover()

        if serpiente.se_ha_pegao():
            game_over = True

        if serpiente.posicion[0] == comida.posicion:
            serpiente.crecer()
            puntos += 1
            comida.posicion = (random.randint(0, WIDTH - 20) // 20 * 20,
                              random.randint(0, HEIGHT - 20) // 20 * 20)

        ventana.fill(NEGRO)
        serpiente.pintar()
        comida.pintar()
        
        pintar_text(f'Puntuación: {puntos}', BLANCO, 30, 10, 10)

        pygame.display.update()
        clock.tick(10)

    if (game_over):
        pygame.quit()

if __name__ == "__main__":
    main()
