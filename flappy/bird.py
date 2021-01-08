import pygame as pg

class Bird:

    def __init__(self, surf):
        self.surf = surf
        self.h = self.surf.get_height() / 2
        self.w = self.surf.get_width() / 4
        self.speed = 10
        self.gravity = 0.9

    def draw(self):
        # store the bounding rectangle to detect collision later
        self.bound_rect = pg.draw.circle(self.surf, (255, 255, 255), (self.w, self.h), 20)

    @property
    def screen_info(self):
        return (self.surf.get_width(), self.surf.get_height())

    def update(self):
        surf_w, surf_h = self.screen_info
        self.h += self.speed * self.gravity
        if self.h > surf_h:
            self.h = surf_h
        if self.h < 0:
            self.h = 0

    def jump(self):
        self.h -= self.speed * 2

    def is_collided(self, pipe):
        return bool(self.bound_rect.colliderect(pipe.top_rect)) or bool(self.bound_rect.colliderect(pipe.bot_rect))
