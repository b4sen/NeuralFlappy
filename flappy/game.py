import pygame as pg
import sys
from bird import Bird
from pipe import Pipe

class Game:

    def __init__(self, w, h):
        self.width = w
        self.height = h
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.paused = False
        self.bird = Bird(self.screen)
        self.pipes = [Pipe(self.screen, self.screen_w),
                      Pipe(self.screen, self.screen_w + 300),
                      Pipe(self.screen, self.screen_w + 600)]

    @property
    def screen_w(self):
        return self.screen.get_width()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.bird.draw()
        for pipe in self.pipes:
            pipe.draw()
        if pg.key.get_pressed()[pg.K_SPACE]:
            self.bird.jump()
        self.bird.update()
        for pipe in self.pipes:
            pipe.move()
            if self.bird.is_collided(pipe):
                self.paused = True

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            if not self.paused:
                self.draw()
                pg.display.flip()
            self.clock.tick(60)

