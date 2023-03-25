import pygame as pg
from resources import images
from numpy import random

class Explosion(pg.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        self.name = 'explosion'
        self.pos = pg.math.Vector2(pos)
        self.img = images['explosion']
        self.img = pg.transform.scale_by(self.img, 2)
        self.img.set_colorkey((255,0,255))
        self.collision = self.img.get_width()//2
        self.timer = pg.time.get_ticks() +  800
        

    def update(self, screen, dt, arena_radius):
        if pg.time.get_ticks() > self.timer:
            self.kill()
        screen.blit(self.img, self.pos - (self.img.get_width()//2, self.img.get_height()//2) )
        # pg.draw.circle(screen, (0,255,0), self.pos, self.collision, 1 )
    
    def fight(self, actor):
        if random.random() > 0.01:
            actor.kill()