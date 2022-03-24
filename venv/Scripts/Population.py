import pygame, math, random
from pygame.math import *
from Mouse import Mouse
from Brain import Brain


class Population:
    mouses = []
    fitness_sum = 0
    generation = 1
    best_mouse_index = -1
    steps = 0
    min_step = Brain.size  # minimum steps that the best mouse have taken

    def __init__(self, size):
        for i in range(size):
            mouse = Mouse()
            self.mouses.insert(i, mouse)

    def show(self, display):
        for mouse in self.mouses:
            if not mouse.is_best:
                mouse.show(display)

        self.mouses[0].show(display)
        self.steps += 1

    def update(self):
        for mouse in self.mouses:
            if mouse.brain.step > self.min_step:
                mouse.alive = False
            else:
                mouse.update()

    def calculate_individual_fitness(self):
        for mouse in self.mouses:
            mouse.calculate_fitness()

    def calculate_fitness_sum(self):
        self.fitness_sum = 0
        for mouse in self.mouses:
            self.fitness_sum += mouse.fitness

    def all_mouses_dead(self):
        for mouse in self.mouses:
            if mouse.alive and not mouse.reached_goal:
                return False
        return True

    def next_mouse_generation(self):
        self.steps = 0
        new_mouses = []
        self.find_best_mouse()
        self.calculate_fitness_sum()
        new_mouses.insert(0, self.mouses[self.best_mouse_index].make_baby())
        new_mouses[0].is_best = True
        new_mouses[0].image = pygame.image.load('images/KingMouseResized.png')
        for i in range(len(self.mouses) - 1):
            parent = self.select_parent()
            new_mouses.insert(i + 1, parent.make_baby())

        self.mouses = new_mouses.copy()
        self.generation += 1

    def find_best_mouse(self):
        max_fitness_found = 0
        best_found_index = 0
        for i in range(len(self.mouses)):
            if self.mouses[i].fitness > max_fitness_found:
                max_fitness_found = self.mouses[i].fitness
                best_found_index = i

        self.best_mouse_index = best_found_index

        if (self.mouses[self.best_mouse_index].reached_goal):
            self.min_step = self.mouses[self.best_mouse_index].brain.step

    def select_parent(self):
        rand = random.uniform(0, self.fitness_sum)
        running_sum = 0

        for i in range(len(self.mouses)):
            running_sum += self.mouses[i].fitness
            if running_sum > rand:
                return self.mouses[i]

        print("im not supposed to be here!")
        return self.mouses[0]

    def mutate_babies(self):
        for mouse in self.mouses:
            mouse.brain.mutate()