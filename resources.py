import pygame as pg
import os

name_list = [
    "rock",
    "gun",
    "lightning",
    "devil",
    "dragon",
    "water",
    "air",
    "paper",
    "sponge",
    "wolf",
    "tree",
    "human",
    "snake",
    "scissors",
    "fire",
]

images = {
    "rock": pg.image.load(os.path.join('assets/img/rock.png')).convert(),
    "gun": pg.image.load(os.path.join('assets/img/gun.png')).convert(),
    "lightning": pg.image.load(os.path.join('assets/img/lightning.png')).convert(),
    "devil": pg.image.load(os.path.join('assets/img/devil.png')).convert(),
    "dragon": pg.image.load(os.path.join('assets/img/dragon.png')).convert(),
    "water": pg.image.load(os.path.join('assets/img/water.png')).convert(),
    "air": pg.image.load(os.path.join('assets/img/air.png')).convert(),
    "paper": pg.image.load(os.path.join('assets/img/paper.png')).convert(),
    "sponge": pg.image.load(os.path.join('assets/img/sponge.png')).convert(),
    "wolf": pg.image.load(os.path.join('assets/img/wolf.png')).convert(),
    "tree": pg.image.load(os.path.join('assets/img/tree.png')).convert(),
    "human": pg.image.load(os.path.join('assets/img/human.png')).convert(),
    "snake": pg.image.load(os.path.join('assets/img/snake.png')).convert(),
    "scissors": pg.image.load(os.path.join('assets/img/scissors.png')).convert(),
    "fire": pg.image.load(os.path.join('assets/img/fire.png')).convert(),
}


half_list = len(name_list)//2
win = dict()
for i, name in enumerate(name_list):
    if i < half_list:
        win[name] = [name_list[j-1] for j in range(i, i-half_list, -1)]
    else:
        win[name] = name_list[name_list.index(name)-half_list:name_list.index(name)]