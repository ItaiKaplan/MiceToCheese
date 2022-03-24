import pygame, sys, random, time
from pygame.math import *
from pygame.locals import *
from Population import Population
from Brain import Brain
from Mouse import Mouse


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


pygame.init()
# GOAL_LOCATION = (300, 30)
WINDOW_SIZE = (600, 600)
clock = pygame.time.Clock();
display = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption("Mice go to the Cheese!")
font =  pygame.font.Font('freesansbold.ttf', 16)


# goal_image = pygame.image.load('images/good_cheese_image.png')
#goal_rect = pygame.Rect(500, 500, goal_image.get_width(),goal_image.get_height())
population = Population(100)

# text = 'Generation = {0}'.format(pop.generation)
# text = font.render(text, True, (255,255,255))
# textRect = text.get_rect()
# textRect.center = (50, 50)




if __name__ == "__main__":
    while True:
        display.fill((239, 231, 219))

        blit_text(display, "Generation = {0}\nSteps taken = {1}\{2}\nMinimum steps to goal = {3}".format(
                                                                                                    population.generation,
                                                                                                    population.steps,
                                                                                                    Brain.size,
                                                                                                    population.min_step),
                                                                                                    (10,10), font)

        display.blit(Mouse.goal_image, Mouse.GOAL_LOCATION)
        pygame.draw.rect(display, (100, 70, 30), Mouse.obstacle_rect1)
        pygame.draw.rect(display, (100, 70, 30), Mouse.obstacle_rect2)


        if population.all_mouses_dead():
            population.calculate_individual_fitness()
            population.next_mouse_generation()
            population.mutate_babies()
        else:
            population.show(display)
            population.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)