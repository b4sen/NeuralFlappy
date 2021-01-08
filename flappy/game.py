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
        self.pipe = Pipe(self.screen)

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            if not self.paused:
                self.screen.fill((0, 0, 0))
                self.bird.draw()
                self.pipe.draw()
                if pg.key.get_pressed()[pg.K_SPACE]:
                    self.bird.jump()
                self.bird.update()
                self.pipe.move()
                if self.bird.is_collided(self.pipe):
                    self.paused = True
                pg.display.flip()
            self.clock.tick(60)

