#!/usr/bin/env python
import sys, os
import pygame
from pygame.locals import *
import esper

FPS = 30
SCREEN_SIZE = 256, 240
CLEAR_COLOR = 255, 255, 255

class Renderable:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

class RenderProcessor(esper.Processor):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def process(self):
        self.screen.fill(CLEAR_COLOR)
        for ent, ren in self.world.get_component(Renderable):
            self.screen.blit(ren.image, (ren.x, ren.y))
        pygame.display.flip()

def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Dirt II')
    clock = pygame.time.Clock()

    pygame.mixer.music.load(
      os.path.join('data', 'music', 'meadow_thoughts.ogg'))
    pygame.mixer.music.play(loops=-1)

    world = esper.World()

    render_processor = RenderProcessor(screen=screen)
    world.add_processor(render_processor)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        world.process()
        clock.tick(FPS)

if __name__ == '__main__':
    run()
