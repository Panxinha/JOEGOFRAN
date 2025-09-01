"""
Hola este es modulo Bug,
este modulo manejara la creacion y acciones de los Bugs
"""

if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
import random
from pygame.locals import (RLEACCEL)
#AKATSUKI:10
pain_img   = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Pain.png'),(64, 64))
itachi_img = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Itachi.png'),(64, 64))
konan_img  = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Konan.png'),(64, 64))
zetsu_img  = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Zetsu.png'),(64, 64))
deidara_img= pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Deidara.png'),(64, 64))
sasori_img = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Sasori.png'),(64, 64))
hidan_img  = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Hidan.png'),(64, 64))
kakuzu_img = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Kakuzu.png'),(64, 64))
tobi_img   = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Tobi.png'),(64, 64))
kisame_img = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Kisame.png'),(64, 64))
class Enemy(pygame.sprite.Sprite):
    def __init__(self,img, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Enemy, self).__init__()
        self.surf = img
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH + 100,
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(2, 4)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
    
def enemyalea(SCREEN_WIDTH, SCREEN_HEIGHT):
    img = random.choice([pain_img, itachi_img, konan_img, zetsu_img, deidara_img,sasori_img, hidan_img, kakuzu_img, tobi_img, kisame_img])
    return Enemy(img, SCREEN_WIDTH, SCREEN_HEIGHT)

