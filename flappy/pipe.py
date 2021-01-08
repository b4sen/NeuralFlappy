import pygame as pg
import random

class Pipe:

    def __init__(self, surf):
        self.surf = surf
        self.w = 50
        self.gap = 200
        self.left = self.surf_w
        self.speed = 4
        self.top_y = self.pick_top()
        self.bot_y = self.top_y + self.gap
        self.bot_h = self.surf_h - self.bot_y

    @property
    def surf_h(self):
        return self.surf.get_height()

    @property
    def surf_w(self):
        return self.surf.get_width()

    def draw(self):
        self.top_rect = pg.draw.rect(self.surf, (255, 255, 255),
                                     (self.left, 0, self.w, self.top_y))
        self.bot_rect = pg.draw.rect(self.surf, (255, 255, 255),
                                     (self.left, self.bot_y, self.w, self.bot_h))

    def move(self):
        self.left -= self.speed
        if self.left < -self.w:
            self.__init__(self.surf)

    def pick_top(self):
        return random.randint(20, self.surf_h - self.gap - 20)

