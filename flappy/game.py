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
        self.hit = False
        self.bird = Bird(self.screen)
        self.pipe_offset = [-200, 100, 400]
        self.pipes = [Pipe(self.screen, self.screen_w + i) for i in self.pipe_offset]

    @property
    def screen_w(self):
        return self.screen.get_width()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.bird.draw()
        for pipe in self.pipes:
            pipe.draw()
        if pg.key.get_pressed()[pg.K_SPACE]:
            #self.bird.jump()
            pass
        self.bird.update(self.pipes)
        for pipe in self.pipes:
            pipe.move()
            if self.bird.is_collided(pipe):
                self.hit = True

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            if not self.hit:
                self.draw()
            else:
                # TODO: don't reinit, but continue with a new generation
                # maybe just reset the pipes?
                for i in range(len(self.pipes)):
                    self.pipes[i].__init__(self.screen, self.screen_w + self.pipe_offset[i])
                # self.__init__(self.width, self.height)
                self.hit = False
            pg.display.flip()
            self.clock.tick(60)

