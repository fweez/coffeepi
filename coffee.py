#!/usr/bin/env python

import pygame

SCREENSIZE = (96,64)

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
clock = pygame.time.Clock()

if pygame.font:
    font = pygame.font.Font(None, 40)
    text = font.render("ready", 1, (255,255,255))
    textpos = text.get_rect()
    screen.blit(text, textpos)
    pygame.display.flip()


while 1:
    clock.tick(60)
    

