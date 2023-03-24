import pygame as pg
from resources import images, win
from numpy import random
from math import hypot, sin, cos, atan2


class Actor(pg.sprite.Sprite):
    def __init__(self, group, name, starting_pos=(0,0), screen_size=(800,800)):
        super().__init__(group)
        self.screen_size = screen_size
        self.screen_mid = (screen_size[0]//2, screen_size[1]//2)
        self.name = name
        self.img = images[name]
        self.img = pg.transform.scale_by(self.img, .5)
        self.img.set_colorkey((255,0,255))
        self.social = 32
        self.collision = 16
        self.speed = 50
        self.pos = pg.math.Vector2(starting_pos)
        self.dir = pg.math.Vector2( random.random()-.5, random.random()-.5 )
        self.change_dir = 1000 + 1000 * random.random()
        self.change_last = 0 

    def update(self, screen, dt, arena_radius):
        self.move(dt)
        if abs(hypot( self.pos.x - self.screen_mid[0], self.pos.y - self.screen_mid[1] )) > arena_radius:
            angle = atan2(self.screen_mid[1]-self.pos.y,  self.screen_mid[0]-self.pos.x)
            dx = cos(angle)
            dy = sin(angle)
            self.dir.xy = (dx, dy)

        elif pg.time.get_ticks() > self.change_last + self.change_dir:
            self.dir = pg.math.Vector2( random.random()-.5, random.random()-.5 ) 
            self.change_last = pg.time.get_ticks()
            self.change_dir = 1000 + 1000 * random.random()


        screen.blit(self.img, self.pos - (self.img.get_width()//2, self.img.get_height()//2))
        # pg.draw.circle(screen, (0,255,0), self.pos, self.social, 1)
        # pg.draw.circle(screen, (255,0,0), self.pos, self.collision, 1)

    def move(self, dt):
        if self.dir.magnitude() > 0:
            self.pos += self.dir.normalize() * self.speed * dt

    def fight(self, actor_2):
        if self.name in win[actor_2.name]:
            self.transform(actor_2.name)
    
    def transform(self, name):
        self.name = name
        self.img = images[name]
        self.img = pg.transform.scale_by(self.img, .5)
        self.img.set_colorkey((255,0,255))




                