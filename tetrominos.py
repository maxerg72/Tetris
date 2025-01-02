import pygame

class Tetromino:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def move_left(self):
        self.x -= 1