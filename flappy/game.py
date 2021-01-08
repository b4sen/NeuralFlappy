import pygame as pg
import sys
from copy import deepcopy
import random

from bird import Bird
from pipe import Pipe


class Game:

    def __init__(self, w, h, num_agents=100):
        self.width = w
        self.height = h
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.num_agents = num_agents
        self.birds = [Bird(self.screen) for i in range(self.num_agents)]
        self.dead_birds = []
        # self.bird = Bird(self.screen)
        self.pipe_offset = [-200, 100, 400]
        self.pipes = [Pipe(self.screen, self.screen_w + i) for i in self.pipe_offset]

    @property
    def screen_w(self):
        return self.screen.get_width()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for pipe in self.pipes:
            pipe.draw()
        if pg.key.get_pressed()[pg.K_SPACE]:
            torch.save(self.birds[0].net.state_dict(), 'models/trained_agent.pth')
        for bird in self.birds:
            bird.draw()
            bird.update(self.pipes)
        # self.bird.update(self.pipes)
        for pipe in self.pipes:
            pipe.move()
            for bird in self.birds:
                # check for collision
                if bird.is_collided(pipe):
                   self.dead_birds.append(bird)
                   self.birds.remove(bird)

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            self.draw()
            if len(self.birds) == 0:
                # TODO: don't reinit, but continue with a new generation
                # maybe just reset the pipes?
                for i in range(len(self.pipes)):
                    self.pipes[i].__init__(self.screen, self.screen_w + self.pipe_offset[i])
                # self.__init__(self.width, self.height)
                # spawn new generation, simply init again for now
                # self.birds = [Bird(self.screen) for i in range(self.num_agents)]
                self.init_generation()
            pg.display.flip()
            self.clock.tick(60)

    def init_generation(self):
        total_fitness = sum([bird.score for bird in self.dead_birds])
        print(total_fitness)
        # set fitness of dead birds
        for bird in self.dead_birds:
            bird.fitness += bird.score / total_fitness

        # create populatein
        self.birds = [self.pick_one() for i in range(self.num_agents)]

        # clear out the dead birds
        self.dead_birds = []

    # using Dan Shiffman's algorithm
    def pick_one(self):
        idx = 0
        r = random.random()
        while r > 0:
            r = r - self.dead_birds[idx].fitness
            idx += 1
        idx -= 1
        bird = self.dead_birds[idx]
        child = Bird(self.screen)
        child.net = deepcopy(bird.net)
        child.mutate(0.1)
        return child

