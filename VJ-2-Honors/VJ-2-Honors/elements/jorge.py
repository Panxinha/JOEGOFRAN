"""
Hola este es modulo Jorge,
este modulo manejara la creacion y movimiento de Jorge
"""

if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
from pygame.locals import (
    K_w, K_s, K_a, K_d, RLEACCEL)
import math

from elements.projectile import Projectile


JorgePNG = pygame.image.load('VJ-2-Honors/assets/jorge_zorro.png')
JorgePNG_scaled = pygame.transform.scale(JorgePNG, (80, 80))

class Player(pygame.sprite.Sprite):
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Player, self).__init__()
        self.surf = JorgePNG_scaled
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.cooldown=200
        self.last_shot=0
        self.projectiles = pygame.sprite.Group()
        self.vidas = 3
        self.speed = 4
        self.shoot_cooldown = 0  # Tiempo restante del cooldown del disparo
        self.teleport_cooldown = 0  # Tiempo restante del cooldown del teleport


        # POR HACER (2.3): Crear lista de proyectiles
        self.projectiles=pygame.sprite.Group()


    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -4)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 4)
        if pressed_keys[K_a]:
            self.rect.move_ip(-4, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(4, 0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
        
        # POR HACER (2.3): Actualizar la posición de los proyectiles
        self.projectiles.update()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if self.teleport_cooldown > 0:
            self.teleport_cooldown -= 1

    
    def shoot(self, mouse_pos): 
        ahora=pygame.time.get_ticks()

        if ahora - self.last_shot < self.cooldown:
            return
        
        # POR HACER (2.3): Crear y calcular dirección proyectil
        #calcula direc
        direction = (mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)
        length = math.hypot(direction[0], direction[1])
         

        if length == 0:
            return  
        direction = (direction[0]/length, direction[1] / length)


        #crea proyectil
        projectile=Projectile(self.rect.center, direction, self.screen_width, self.screen_height)
        self.projectiles.add(projectile)

        self.last_shot = ahora

    #Definimos una habilidad de un ataque super cargado que lanza 8 proyectiles a su alrededor
    def super_shoot(self):
        if self.shoot_cooldown == 0:
            direction=(1,0) #definimos direccion al frente
            length = math.hypot(*direction)
            direction = (direction[0] / length, direction[1] / length)

            #calculamos direcciones laterales hacia al frente, con una diferencia de 30 grados desde el centro
            angle = math.atan2(direction[1], direction[0])
            angle1 = angle + math.radians(30)
            angle2 = angle - math.radians(30)
            direction0 = direction
            direction1 = (math.cos(angle1), math.sin(angle1))
            direction2 = (math.cos(angle2), math.sin(angle2))

            #calculmos dieccion para arriba y abajo
            angle_up = angle + math.radians(90)
            angle_down = angle - math.radians(90)
            direction3 = (math.cos(angle_up), math.sin(angle_up))
            direction4 = (math.cos(angle_down), math.sin(angle_down))

            #se aproximar a dos decimales
            direction0 = (round(direction0[0], 2), round(direction0[1], 2))
            direction1 = (round(direction1[0], 2), round(direction1[1], 2))
            direction2 = (round(direction2[0], 2), round(direction2[1], 2))
            direction3 = (round(direction3[0], 2), round(direction3[1], 2))
            direction4 = (round(direction4[0], 2), round(direction4[1], 2))

            #calculamos la direccion para atras, junto con sus disparos laterales a 30 grados
            direction_b = (-1,0)
            length = math.hypot(*direction_b)
            direction = (direction_b[0] / length, direction_b[1] / length)
            angle = math.atan2(direction_b[1], direction_b[0])
            angle1 = angle + math.radians(30)
            angle2 = angle - math.radians(30)

            direction0_b=direction_b
            direction1_b = (math.cos(angle1), math.sin(angle1))
            direction2_b = (math.cos(angle2), math.sin(angle2))


            #se aproxima a dos decimales
            direction0_b = (round(direction0_b[0], 2), round(direction0_b[1], 2))
            direction1_b = (round(direction1_b[0], 2), round(direction1_b[1], 2))
            direction2_b = (round(direction2_b[0], 2), round(direction2_b[1], 2))

            #ahora creamos los proyectiles salgan desde la posicion del jugador
            directions = [direction0, direction1, direction2, direction3, direction4, direction0_b, direction1_b, direction2_b]
            for direction in directions:
                projectile = Projectile(self.rect.center, direction, self.screen_width, self.screen_height)
                self.projectiles.add(projectile)            

            self.shoot_cooldown=150

    #definimos la habilidad de teletrasportarse
    def teleport(self, mouse_pos):
        if self.teleport_cooldown == 0:
            self.rect.center = mouse_pos
            self.teleport_cooldown = 200    

    def reset(self):
        self.rect.center = (self.screen_width//2, self.screen_height//2)
        self.vidas = 3
        self.speed = 4
        #self.speed_powerup_time = 0
        self.shoot_cooldown = 0
        self.teleport_cooldown = 0
        #self.boss_collision_cooldown = 0

