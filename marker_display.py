import pygame
from pygame.locals import *
from time import time

WIDTH = 1920
HEIGHT = 1080

def set_x(x):
        return(x*WIDTH - 84)

def set_y(y):
        return(HEIGHT - (y*HEIGHT + 84))

def start():
        pygame.init()
        windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        windowSurface.fill((200,200,200))
        pygame.display.toggle_fullscreen()
        img = pygame.image.load("marker.png")
        #img = pygame.transform.scale(img, (150,150))
        end = False
        pygame.mouse.set_visible(False)

        x = 10000
        y = 10000
        windowSurface.blit(img, (set_x(x), set_y(y)))
        sites = [(0.1, .70), (.25, .70),  (.5, .70), (.75, .70), (0.9,.70),
                (0.1,.5), (.25, .5),(.5,.5), (.75,.5),(.9,.5),
                (0.1,.35), (.25, .35),(.5,.35), (.75,.35),(.9,.35),
                (0.1,.25), (.25, .25), (.5, .25), (.75, .25), (.9, .25),
                (0.2,0.15), (.8,0.15)]
        set_time = -100
        while True:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        end = True
                t = time()

                if t > set_time + 2.5 and sites:
                        loc = sites.pop(0)
                        x = loc[0]
                        y = loc[1]
                        set_time = t
                elif t > set_time + 2.5:
                        pygame.quit()
                        end = True

                if end:
                        break
                windowSurface.fill((200,200,200))
                windowSurface.blit(img, (set_x(x), set_y(y))) #Replace (0, 0) with desired coordinates
                pygame.display.flip()

        return
