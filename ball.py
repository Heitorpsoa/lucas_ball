import pygame
from tail import Tail
from enum import Enum


class Ball:
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    ATRICT = 0.7
    
    def __init__(self, pos, size = 20, gravity = 0.001):
        self.pos = pos
        self.speed = [0, 0]
        self.acc = [0, gravity]
        
        self.size = size
        self.color = self.BLUE

        self.gravity = gravity
        self.jumping = False

        self.tail = Tail(pos, [0, 0])


    def reset(self):
        self.acc = [0, self.gravity]

    def jump(self):
        
        self.speed[1] = -0.5
        self.jumping = True


    def move(self, acc):
        self.acc[0] += acc[0]
        self.acc[1] += acc[1]

    def applySpeed(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

        self.tail.updatePos(self.pos)
    
    def applyAcc(self):
        self.speed[0] += self.acc[0]
        self.speed[1] += self.acc[1]


    def borderColision(self, screen):
        w, h = screen.get_size()

        # Borda de baixo 
        if self.pos[1] + self.size > h:
            self.speed[1] = - abs(self.speed[1]) * self.ATRICT
            self.jumping = False
        
        # Borda de cima
        if self.pos[1] + self.size < 0:
            self.speed[1] = abs(self.speed[1]) * self.ATRICT

        # Borda da esquerda
        if self.pos[0] - self.size < 0:
            self.speed[0] = abs(self.speed[0]) * self.ATRICT

        # Borda da direita
        if self.pos[0] + self.size > w:
            self.speed[0] =  - abs(self.speed[0]) * self.ATRICT
         
    def draw(self, screen):
        #checando se bateu nas bordas
        self.borderColision(screen)
        
        self.applyAcc()
        self.applySpeed()


        pygame.draw.circle(screen, self.color, radius=self.size, center=self.pos)
        self.tail.draw(screen)
