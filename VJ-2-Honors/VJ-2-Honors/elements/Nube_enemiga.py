import pygame
Nube = pygame.image.load('VJ-2-Honors/assets/nube.png')
Nube_scaled = pygame.transform.scale(Nube, (70, 70))

class Nube(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, player_pos):
        super(Nube, self).__init__()
        self.surf = Nube_scaled
        self.screen_height=SCREEN_HEIGHT
        self.screen_width=SCREEN_WIDTH  
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(midright=(1000, player_pos[0]))
        self.speed=6
  

    def update(self):
        self.rect.x-=self.speed
        if self.rect.left==0:
            self.kill()