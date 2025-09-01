import pygame
import math
import time
bossPNG = pygame.image.load('VJ-2-Honors/assets/Kaguya.png')
bossPNG_scaled = pygame.transform.scale(bossPNG, (200, 200))
from elements.Jefe_projectile import jefe_projectile

class Boss(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Boss, self).__init__()
        self.aparece=False
        self.surf = bossPNG_scaled
        self.screen_height=SCREEN_HEIGHT
        self.screen_width=SCREEN_WIDTH  
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(midright=(SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2))
        self.vida=100
        self.speed=2
        self.tiempo_disparo=0

        self.projectiles=pygame.sprite.Group()


    def disparo(self, player_pos):
        direction=(player_pos[0]-self.rect.centerx,player_pos[1]-self.rect.centery)
        length=math.hypot(direction[0],direction[1])
        direction=(direction[0]/length,direction[1]/length)
        projectile=jefe_projectile(self.rect.center,direction,self.screen_width,self.screen_height)
        self.projectiles.add(projectile)

    def update(self, player_pos):
        self.rect.y+=self.speed
        if self.rect.top < 50 or self.rect.bottom >=650 :
            self.speed*=-1
        if time.time()-self.tiempo_disparo>1:
            self.disparo(player_pos)
            self.tiempo_disparo = time.time()
        
        self.projectiles.update()

    def barra_vida(self, surface):

        bar_width = 80
        bar_height = 10
        bar_x = self.rect.centerx - bar_width // 2
        bar_y = self.rect.top - 20 

        pygame.draw.rect(surface, (150, 150, 150), (bar_x, bar_y, bar_width, bar_height))
        
        health_width = (self.vida / 100) * bar_width
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, health_width, bar_height))
