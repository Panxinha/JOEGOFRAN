import pygame
class jefe_projectile(pygame.sprite.Sprite):
    def __init__(self, pos, direction, SCREEN_WIDTH, SCREEN_HEIGHT): 
        super(jefe_projectile, self).__init__()
        self.surf=pygame.Surface((20,20))
        self.surf.fill((255,0,0))
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