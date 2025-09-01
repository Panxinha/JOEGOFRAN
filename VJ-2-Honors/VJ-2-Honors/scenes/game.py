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
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT, K_SPACE, K_t)
from elements.jorge import Player
from elements.Enemigos import enemyalea
from elements.wing import Wing
from elements.extra_life import Extra_life
from elements.Jefe1 import Boss1
from elements.Nube_enemiga import Nube
import scenes.game_over as Fin

def gameLoop():
    pygame.init()
    pygame.mixer.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
    SCORE_FOR_BOSS = 1000
    INVULN_MS = 500

    # Cargas de imagenes:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("VJ-2-Honors/assets/konoha1fin.png").convert()

    mira_imagen = pygame.image.load("VJ-2-Honors/assets/crosshair.png")
    mira_imagen = pygame.transform.scale(mira_imagen, (32, 32))

    corazon = pygame.image.load("VJ-2-Honors/assets/vidas.png")
    corazon = pygame.transform.scale(corazon, (40, 40))

    # Música / sonidos:
    pygame.mixer.music.load("VJ-2-Honors/assets/Narutomusic.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    disparo = pygame.mixer.Sound("VJ-2-Honors/assets/Disparo.mp3")
    bomba = pygame.mixer.Sound("VJ-2-Honors/assets/Bomba.mp3")

    # Extra
    def mostrar_vidas(surface, vidas):
        for i in range(vidas):
            surface.blit(corazon, (10 + i * 40, 10))

    font1 = pygame.font.SysFont("Times New Roman", 30)
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()

    # SPRITES 
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)
    nube = pygame.sprite.Group()

    boss_spawned = False
    boss_dead = False
    boss = None

    player.invulnerable_until = 0

    # === EVENTOS ===
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 1000)

    ADDPOWERUP = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDPOWERUP, 7500)

    ADDNUBE = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDNUBE, 5000)
    # === GAME LOOP ===
    running = True
    while running:
        # DIBUJO BASE
        screen.blit(background_image, (0, 0))
        mostrar_vidas(screen, player.vidas)
        texto_puntos = font1.render(f'Puntuación: {player.puntos}', True, (0, 0, 0))
        screen.blit(texto_puntos, (800, 10))

        # ACTUALIZACIONES
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        nube.update()

        if boss_spawned and boss and not boss_dead:
            # Seguir y actualizar jefe sólo si existe
            boss.update(player.rect.center)

        # COLISIONES: balas del jugador vs enemigos normales
        if pygame.sprite.groupcollide(enemies, player.projectiles, True, True):
            player.puntos += 100

        # COLISIONES: jugador vs enemigos normales (quitar 1 vida, NO cerrar juego)
        now = pygame.time.get_ticks()
        if now > player.invulnerable_until:
            hit_list = pygame.sprite.spritecollide(player, enemies, dokill=True)
            if hit_list:  # si chocó con al menos uno
                player.vidas -= 1
                player.invulnerable_until = now + INVULN_MS
                if player.vidas <= 0:
                    player.kill()
                    pygame.mixer.music.stop()
                    running = False
                    Fin.gameLoop()
                    return "Perdió"

        # COLISIONES: proyectiles del jefe vs jugador
        if boss_spawned and boss and not boss_dead:
            if pygame.sprite.spritecollide(player, boss.projectiles, dokill=True):
                if now > player.invulnerable_until:
                    player.vidas -= 1
                    player.invulnerable_until = now + INVULN_MS
                    if player.vidas <= 0:
                        player.kill()
                        pygame.mixer.music.stop()
                        running = False
                        Fin.gameLoop()
                        return "Perdió"

        # SPAWN DEL JEFE (sólo al alcanzar el umbral)
        if (not boss_spawned) and player.puntos >= SCORE_FOR_BOSS:
            boss = Boss1(SCREEN_WIDTH, SCREEN_HEIGHT)
            boss.aparece = True
            boss_spawned = True
            all_sprites.add(boss)

        # DAÑO AL JEFE
        if boss_spawned and boss and not boss_dead:
            if pygame.sprite.spritecollide(boss, player.projectiles, dokill=True):
                boss.vida -= 5
                print("vida jefe", boss.vida)
                if boss.vida <= 0:
                    boss.kill()
                    boss_dead = True
                    player.puntos += 500
                    running = True
                    return "Ganó"
                
        if pygame.sprite.groupcollide(nube, player.projectiles, True, True):
            player.puntos += 50


        # DIBUJAR SPRITES
        for n in nube:
            screen.blit(n.surf, n.rect)

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        for e in enemies:
            screen.blit(e.surf, e.rect)

        for projectile in player.projectiles:
            screen.blit(projectile.surf, projectile.rect)

        if boss_spawned and boss and not boss_dead:
            for projectile in boss.projectiles:
                screen.blit(projectile.surf, projectile.rect)
            boss.barra_vida(screen)

        # DIBUJAR MIRA
        mx, my = pygame.mouse.get_pos()
        screen.blit(mira_imagen, mira_imagen.get_rect(center=(mx, my)))
        pygame.display.flip()

        # EVENTOS
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE:
                    player.super_shoot()
                    disparo.play()
                    bomba.play()
                elif event.key == K_t:
                    player.teleport(pygame.mouse.get_pos())

            elif event.type == QUIT:
                running = False

            elif event.type == ADDENEMY and not boss_dead:
                enemies.add(enemyalea(SCREEN_WIDTH, SCREEN_HEIGHT))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot(pygame.mouse.get_pos())
                disparo.play()

            elif event.type == ADDNUBE:
                nube.add(Nube(SCREEN_WIDTH, SCREEN_HEIGHT, player.rect.center))

            #powerup
            #elif event.type==ADDPOWERUP: 
            #wing = Wing(SCREEN_WIDTH, SCREEN_HEIGHT)
            #extra_life = Extra_life(SCREEN_WIDTH, SCREEN_HEIGHT)
            #elegir entre los dos power ups
            #power_up=None #n_power=random.randint(0,1)
            #if n_power == 0:
            #power_up=wing
            #else:
            #power_up=extra_life
            #powerups.add(power_up)
            #all_sprites.add(power_up)
        clock.tick(60)
