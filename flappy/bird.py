import pygame as pg
from net import FlappyNet
import torch

class Bird:

    def __init__(self, surf):
        self.surf = surf
        self.h = self.surf.get_height() / 2
        self.w = self.surf.get_width() / 4
        self.speed = 10
        self.gravity = 0.9
        self.net = FlappyNet()

    def draw(self):
        # store the bounding rectangle to detect collision later
        self.bound_rect = pg.draw.circle(self.surf, (255, 255, 255), (self.w, self.h), 20)

    @property
    def screen_info(self):
        return (self.surf.get_width(), self.surf.get_height())

    def update(self, pipes):
        distance = 10e3
        pipe = None

        surf_w, surf_h = self.screen_info
        self.h += self.speed * self.gravity
        if self.h > surf_h:
            self.h = surf_h

        # determine closest pipe
        for i in range(len(pipes)):
            d = pipes[i].left - self.bound_rect.right
            if d < distance and d > 0:
                pipe = pipes[i]
                distance = d

        # create input tensor from bird position and narest pipe position
        # TODO: implement learning
        inp = torch.tensor([self.h, pipe.top_rect.left, pipe.top_rect.bottom, pipe.bot_rect.top]).float()
        if self.net(inp) > 0.5:
            self.jump()

    def mutate(self):
        self.net.input.weight = torch.nn.parameter.Parameter(self.net.input.weight * 0.1)
        self.net.hidden.weight = torch.nn.parameter.Parameter(self.net.input.weight * 0.1)

    def jump(self):
        self.h -= self.speed * 2
        if self.h < 0:
            self.h = 0

    def is_collided(self, pipe):
        return bool(self.bound_rect.colliderect(pipe.top_rect)) or bool(self.bound_rect.colliderect(pipe.bot_rect))
