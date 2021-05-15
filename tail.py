import pygame
from math import pi
from copy import deepcopy

import queue

class Tail:
    SEGMENTS = 5
    SIZE = 50

    def __init__(self, pos, size = 20, segment = 0):
        self.pos = pos
        self.oldPos = deepcopy(pos)
        self.size = size
        self.buffer = queue.Queue(self.SIZE)
        self.updateFactor = 0
        self.color = (255, 0, 255)

        self.segment = segment
        if segment < self.SEGMENTS:
            self.tail = Tail(deepcopy(self.oldPos), segment=segment + 1)

    def updatePos(self, pos):


        if self.updateFactor >= self.SIZE:
            # self.updateFactor = 0
            self.oldPos = self.buffer.get() 
        
        self.updateFactor = self.updateFactor + 1
        self.buffer.put(deepcopy(pos))
        self.pos = deepcopy(pos)
        if self.segment < self.SEGMENTS:
            self.tail.updatePos(deepcopy(self.oldPos))

    def draw(self, screen):

        pygame.draw.line(screen, self.color, self.pos, self.oldPos, width = (self.SEGMENTS - self.segment) * self.SEGMENTS)
        if self.segment < 5:
            self.tail.draw(screen)
