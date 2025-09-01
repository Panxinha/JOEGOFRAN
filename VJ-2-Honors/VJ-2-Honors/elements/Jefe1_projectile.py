import pygame
fuego = pygame.image.load('VJ-2-Honors/assets/fuego.png')
fuego_scaled = pygame.transform.scale(fuego, (50, 50))

class jefe1_projectile(pygame.sprite.Sprite):
    def __init__(self, pos, direction, SCREEN_WIDTH, SCREEN_HEIGHT): 
        super(jefe1_projectile, self).__init__()
        self.surf=fuego_scaled
        self.surf.set_colorkey((0,0,0))
        self.rect=self.surf.get_rect(center=pos)
        self.speed=6
        self.direction=direction
        self.screen_width=SCREEN_WIDTH
        self.screen_heigth=SCREEN_HEIGHT

    def update(self): 
        self.rect.move_ip(self.direction[0]*self.speed,self.direction[1]*self.speed)
        if (self.rect.left<0
            or self.rect.right>self.screen_width
            or self.rect.top<0
            or self.rect.bottom>self.screen_heigth):
            self.kill()