import pygame, math
from pygame.math import *
from Brain import Brain


class Mouse:
    GOAL_LOCATION = (250, 50)
    goal_image = pygame.image.load('images/good_cheese_image.png')
    goal_rect = pygame.Rect(GOAL_LOCATION[0], GOAL_LOCATION[1], goal_image.get_width(), goal_image.get_height())
    obstacle_rect1 = pygame.Rect(0, 400, 350, 10)
    obstacle_rect2 = pygame.Rect(300, 200, 150, 10)

    def __init__(self):
        self.brain = Brain()
        self.fitness = 0
        self.alive = True
        self.reached_goal = False
        self.is_best = False
        self.image = pygame.image.load('images/GoodMouseResized.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = pygame.Rect(300, 550, self.image.get_width(), self.image.get_height())

    def move(self):
        if self.brain.step < self.brain.size:
            self.rect.x += self.brain.directions[self.brain.step][0]
            self.rect.y += self.brain.directions[self.brain.step][1]
            self.brain.step += 1
        else:
            self.die()

    def show(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    # def get_image(self):
    #     if self.alive():
    #         speed = self.brain.speed
    #         if self.brain.directions[self.brain.step][0] == 1 * speed and self.brain.directions[self.brain.step][1] == 1* speed:
    #             self.image = soute-east
    #         if self.brain.directions[self.brain.step][0] == 1* speed and self.brain.directions[self.brain.step][1] == 0:
    #             self.image = east
    #         if self.brain.directions[self.brain.step][0] == 1* speed and self.brain.directions[self.brain.step][1] == -1* speed:
    #             self.image = north-east
    #         if self.brain.directions[self.brain.step][0] == 0 and self.brain.directions[self.brain.step][1] == 1* speed:
    #             self.image = south
    #         if self.brain.directions[self.brain.step][0] == 0 and self.brain.directions[self.brain.step][1] == -1* speed:
    #             self.image = north
    #         if self.brain.directions[self.brain.step][0] == -1* speed and self.brain.directions[self.brain.step][1] == 1* speed:
    #             self.image = south_west
    #         if self.brain.directions[self.brain.step][0] == -1* speed and self.brain.directions[self.brain.step][1] == 0:
    #             self.image = west
    #         if self.brain.directions[self.brain.step][0] == -1* speed and self.brain.directions[self.brain.step][1] == -1 * speed:
    #             self.image = northwest

    def update(self):
        if self.alive and not self.reached_goal:
            # self.get_image()
            self.move()
            if self.rect.x <= 0 or self.rect.x >= 600 or self.rect.y <= 0 or self.rect.y >= 600 or \
                    self.rect.colliderect(self.obstacle_rect1) or self.rect.colliderect(self.obstacle_rect2):
                self.die()
            elif self.rect.colliderect(self.goal_rect):
                self.reached_goal = True

    def calculate_fitness(self):
        if (self.reached_goal):
            self.fitness = 1 / 16 + 100000 / (self.brain.step ** 2)
        else:
            distance_to_goal = math.sqrt((self.goal_rect.x - self.rect.x) ** 2 + (self.goal_rect.y - self.rect.y) ** 2)
            self.fitness = 1 / (distance_to_goal ** 2)

    def make_baby(self):
        baby = Mouse()
        baby.brain = self.brain.clone()
        return baby

    def die(self):
        self.alive = False
        if not self.is_best:
            self.image = pygame.image.load('images/DeadMouseResized.png')
        else:
            self.image = pygame.image.load('images/DeadKingMouseResized.png')

