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
pain_img   = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Pain.png'),(70, 70))
itachi_img = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Itachi.png'),(70, 70))
konan_img  = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Konan.png'),(70, 70))
zetsu_img  = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Zetsu.png'),(70, 70))
deidara_img= pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Deidara.png'),(70, 70))
sasori_img = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Sasori.png'),(70, 70))
hidan_img  = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Hidan.png'),(70, 70))
kakuzu_img = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Kakuzu.png'),(70, 70))
tobi_img   = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Tobi.png'),(70, 70))
kisame_img = pygame.transform.scale(pygame.image.load('VJ-2-Honors/assets/Kisame.png'),(70, 70))
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

