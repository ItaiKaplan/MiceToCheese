import pygame, sys, random, math
import pygame, sys, random
from pygame.math import *

class Brain:
    size = 4000
    speed = 4

    def __init__(self):
        self.directions = []
        self.step = 0
        self.randomize()

    def randomize(self):
        for i in range(self.size):
            t = (random.randint(-1,1) * self.speed, random.randint(-1,1) * self.speed)
            self.directions.append(t)
        # for i in range(self.size):
        #     angle = random.uniform(0, 2 * math.pi)
        #     self.directions.append(angle)
            # vector = pygame.math.Vector2(random.uniform(0, 1) , random.uniform(-1, 1) )
            # vector.normalize()
            t = (random.randint(-1,1) * self.speed, random.randint(-1,1) * self.speed)
            self.directions.append(t)

    def clone(self):
        clone = Brain()
        for i in range(self.size):
            clone.directions[i] = self.directions[i]

        return clone

    def mutate(self):
        chance_to_mutate = 0.01
        for i in range(self.size):
            rand = random.random()
            if rand < chance_to_mutate:
                t = (random.randint(-1, 1), random.randint(-1, 1))
                self.directions[i] = t