import pygame as pg
from math import hypot

WIDTH, HEIGHT = 600,600
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

from actor import Actor
from resources import name_list
from numpy import random


all_sprites = pg.sprite.Group()

actor_n = 200



arena_radius = WIDTH//2
arena_shrink = 10

def generate_actors(n, screen_size):
    global name_list
    group = pg.sprite.Group()
    for i in range(n):
        if i < len(name_list):
            Actor(group, name_list[i], (WIDTH * random.random(), HEIGHT * random.random()), screen_size)
        else:
            Actor(group, name_list[int(len(name_list)*random.random())], (WIDTH * random.random(), HEIGHT * random.random()), screen_size)
    return group

def dist(a, b):
    return hypot(a.pos.x - b.pos.x, a.pos.y - b.pos.y)

while True:
    dt = clock.tick() / 1000
    pg.display.set_caption(str(round(clock.get_fps(), 3)))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_j:
                arena_radius = WIDTH//2
                all_sprites = generate_actors(actor_n, (WIDTH, HEIGHT))
            elif event.key == pg.K_SPACE:
                arena_shrink = 50
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                arena_shrink = 10

    screen.fill((51, 163, 81))
    for sprite in all_sprites.sprites():
        for sprite_2 in all_sprites.sprites():
            if sprite.name == sprite_2.name:
                continue
            elif dist(sprite, sprite_2) < sprite.collision:
                sprite.fight(sprite_2)
                
        

        sprite.update(screen, dt, arena_radius)
    arena_radius -= arena_shrink * dt
    pg.draw.circle(screen, (88, 51, 163), (WIDTH//2, HEIGHT//2), arena_radius, 3)
    pg.display.flip()
