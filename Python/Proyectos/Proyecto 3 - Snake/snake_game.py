import pygame
import random

# Inicializar pygame
pygame.init()

# Constantes para colores y tamaño de ventana
WIDTH, HEIGHT = 600, 600
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Iniciar ventana y reloj
ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de la Serpiente")
clock = pygame.time.Clock()

# Diccionario con las dificultades y las velocidades
dificultad = {'facil': 5, 'normal': 10, 'dificil': 15}

# ------------------------------- Serpiente -------------------------------
class Serpiente:
    def __init__(self):
        self.posicion = [(100, 100)]
        self.direccion = 'RIGHT'
        self.creciendo = False

    def mover(self):
        # Actualizar la posicion dependiendo de lo que se ha pulsado
        x, y = self.posicion[0]
        if self.direccion == 'UP':
            y -= 20
        elif self.direccion == 'DOWN':
            y += 20
        elif self.direccion == 'LEFT':
            x -= 20
        elif self.direccion == 'RIGHT':
            x += 20

        new_head = (x, y)
        if not self.creciendo:
            self.posicion.pop()
        else:
            self.creciendo = False

        self.posicion.insert(0, new_head)

    def crecer(self):
        # Cambia creciendo a true
        self.creciendo = True

    def colisionar(self):
        # Mira se se ha pegado con las paredes o consigo misma
        x, y = self.posicion[0]
        return (
            x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or
            self.posicion[0] in self.posicion[1:]
        )

    def dibujar(self):
        # Pinta la serpiente posicion a posicion
        for parte in self.posicion:
            pygame.draw.rect(ventana, BLANCO, (*parte, 20, 20))

# ------------------------------- Comida -------------------------------
class Comida:
    def __init__(self):
        self.posicion = self.nueva_posicion()

    def nueva_posicion(self):
        # Posicion random nueva, con las constantes del tamaó de la ventana
        return (random.randint(0, (WIDTH - 20) // 20) * 20,
                random.randint(0, (HEIGHT - 20) // 20) * 20)

    def dibujar(self):
        # Pintar la comida
        pygame.draw.rect(ventana, (255, 0, 0), (*self.posicion, 20, 20))

# Si no pongo esto no se me centra el texto
def pintar_texto(texto, color, tamano, x, y, center=False):
    fuente = pygame.font.Font(None, tamano)
    texto_surface = fuente.render(texto, True, color)
    texto_rect = texto_surface.get_rect()
    if center:
        texto_rect.center = (x, y)
    else:
        texto_rect.topleft = (x, y)
    ventana.blit(texto_surface, texto_rect)

# Para seleccionar la dificultad
def seleccionar_dificultad():
    ventana.fill(NEGRO)
    pintar_texto("Selecciona la dificultad: 1. Fácil 2. Normal 3. Difícil", BLANCO, 36, WIDTH // 2, HEIGHT // 2, center=True)
    pygame.display.update()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return dificultad['facil']
                elif evento.key == pygame.K_2:
                    return dificultad['normal']
                elif evento.key == pygame.K_3:
                    return dificultad['dificil']

# ------------------------------- Main -------------------------------
def main():
    serpiente = Serpiente()
    comida = Comida()
    puntos = 0
    game_over = False

    # Seleccionar la dificultad
    velocidad = seleccionar_dificultad()
    
    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            elif evento.type == pygame.KEYDOWN:
                # para moverse, pero controlando no pulsar tecla contraria
                if evento.key == pygame.K_UP and serpiente.direccion != 'DOWN':
                    serpiente.direccion = 'UP'
                elif evento.key == pygame.K_DOWN and serpiente.direccion != 'UP':
                    serpiente.direccion = 'DOWN'
                elif evento.key == pygame.K_LEFT and serpiente.direccion != 'RIGHT':
                    serpiente.direccion = 'LEFT'
                elif evento.key == pygame.K_RIGHT and serpiente.direccion != 'LEFT':
                    serpiente.direccion = 'RIGHT'

        serpiente.mover()

        # Mirar si se ha chocado
        if serpiente.colisionar():
            game_over = True

        # Mirar si ha comido
        if serpiente.posicion[0] == comida.posicion:
            serpiente.crecer()
            puntos += 1
            comida.posicion = comida.nueva_posicion()

        # Actualizar
        ventana.fill(NEGRO)
        serpiente.dibujar()
        comida.dibujar()
        
        # Actualizar puntuación
        pintar_texto(f'Puntuación: {puntos}', BLANCO, 30, 10, 10)

        pygame.display.update()
        clock.tick(velocidad)

    # Game over
    ventana.fill(NEGRO)
    pintar_texto("Game Over", BLANCO, 72, WIDTH // 2, HEIGHT // 2 - 50, center=True)
    pintar_texto(f'Puntuación final: {puntos}', BLANCO, 36, WIDTH // 2, HEIGHT // 2 + 10, center=True)
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()

# Empezar juego
main()
