import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)


def gameLoop():
    ''' iniciamos los modulos de pygame'''

    pygame.init()

    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600

    ''' 2.- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_over_image = pygame.image.load("VJ-2-Honors/assets/game_over.png").convert()
    game_over_scaled = pygame.transform.scale(game_over_image, (1000, 700))
    
    running = True

    while running:

        screen.blit(game_over_scaled, [0, 0])
        
        pygame.display.flip()
        
        # iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            # se presiono una tecla?
            if event.type == KEYDOWN:
                # era la tecla de escape? -> entonces terminamos
                if event.key == K_ESCAPE:
                    running = False

            # fue un click al cierre de la ventana? -> entonces terminamos
            elif event.type == QUIT:
                running = False
            