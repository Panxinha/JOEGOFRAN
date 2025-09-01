if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
from pygame.locals import (RLEACCEL)
kunai = pygame.image.load('VJ-2-Honors/assets/pngkunai.png')
kunai_scaled = pygame.transform.scale(kunai, (50, 50))
class Projectile(pygame.sprite.Sprite):
    
    def __init__(self, pos, direction, SCREEN_WIDTH, SCREEN_HEIGHT): 
        super(Projectile, self).__init__()
        self.surf = kunai_scaled
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=pos)
        self.speed=10
        self.direction=direction
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
    
        

    def update(self): 
        self.rect.move_ip(self.direction[0] * self.speed,self.direction[1] * self.speed)
        if(self.rect.left < 0 
           or self.rect.right > self.screen_width
           or self.rect.top < 0
           or self.rect.bottom > self.screen_height):
            self.kill()
    
