import pygame as pg
from net import FlappyNet
import torch

class Bird:

    def __init__(self, surf):
        self.surf = surf
        self.h = self.surf.get_height() / 2
        self.w = self.surf.get_width() / 4
        self.speed = 0
        self.lift = -10
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
        self.speed += self.gravity
        self.h += self.speed
        if self.h > surf_h:
            self.h = surf_h
            self.speed = 0

        # determine closest pipe
        for i in range(len(pipes)):
            d = (pipes[i].left + pipes[i].w) - self.bound_rect.right
            if d < distance and d > 0:
                pipe = pipes[i]
                distance = d

        # create input tensor from bird position and narest pipe position
        # TODO: implement learning
        inp = torch.tensor([self.h, self.speed, pipe.top_rect.left, pipe.top_rect.bottom, pipe.bot_rect.top]).float()
        if self.net(inp) > 0.5:
            self.jump()

    def mutate(self):
        # TODO: implement mutation
        # change a random weight by a random value? maybe sample from a distribution?
        if random.random() < 0.1:
            self.net.mutate()

    def jump(self):
        self.speed = self.lift
        if self.h < 0:
            self.h = 0
            self.speed = 0

    def is_collided(self, pipe):
        hit = bool(self.bound_rect.colliderect(pipe.top_rect)) or bool(self.bound_rect.colliderect(pipe.bot_rect))
        return hit
