'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT, K_SPACE, K_f)

import random

from elements.jorge import Player

from elements.bug import Enemy

from elements.wing import Wing

from elements.extra_life import Extra_life

import scenes.game_over as Fin


def gameLoop():
    ''' iniciamos los modulos de pygame'''

    pygame.init()

    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600

    ''' 2.1- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("VJ-2-Honors/assets/konoha1fin.png").convert()

    '''2.2 creamos cursor para el mouse'''
    mira_imagen = pygame.image.load("VJ-2-Honors/assets/crosshair.png")
    mira_imagen = pygame.transform.scale(mira_imagen, (32, 32))
    pygame.mouse.set_visible(False)

    ''' Preparamos el gameloop '''
    ''' 1.- creamos el reloj del juego'''

    clock = pygame.time.Clock()
    ''' 2.- generador de enemigos'''

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    #creamos evento donde añadimos los power up
    ADDPOWERUP = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDPOWERUP, 7500)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    ''' hora de hacer el gameloop '''
    # variable booleana para manejar el loop
    running = True

    # loop principal del juego

    while running:

        screen.blit(background_image, [0, 0])
        
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        # POR HACER (2.5): Pintar proyectiles en pantalla
        for projectile in player.projectiles:
            screen.blit(projectile.surf, projectile.rect)

        
        # POR HACER (2.5): Eliminar bug si colisiona con proyectil
        pygame.sprite.groupcollide(enemies, player.projectiles, True,True)
        
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        
        
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False
            Fin.gameLoop()

        mx, my = pygame.mouse.get_pos()
        screen.blit(mira_imagen, mira_imagen.get_rect(center=(mx, my)))

        pygame.display.flip()
        
        # iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            # se presiono una tecla?
            if event.type == KEYDOWN:
                # era la tecla de escape? -> entonces terminamos
                if event.key == K_ESCAPE:
                    running = False

                
                #super disparo
                if event.key == K_SPACE:
                    player.super_shoot()                

                #teletransporte
                if event.key == K_f:
                    mouse_pos = pygame.mouse.get_pos()
                    player.teleport(mouse_pos)            
                

                # fue un click al cierre de la ventana? -> entonces terminamos
            elif event.type == QUIT:
                running = False
            
            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            
            # POR HACER (2.4): Agregar evento disparo proyectil
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot(pygame.mouse.get_pos())

            #powerup
            #elif event.type==ADDPOWERUP:
                #wing = Wing(SCREEN_WIDTH, SCREEN_HEIGHT)                
                #extra_life = Extra_life(SCREEN_WIDTH, SCREEN_HEIGHT)
            #elegir entre los dos power ups
                #power_up=None
                #n_power=random.randint(0,1)
                #if n_power == 0:
                    #power_up=wing
                #else:
                    #power_up=extra_life
                    #powerups.add(power_up)
                    #all_sprites.add(power_up)

        



        clock.tick(60)
        