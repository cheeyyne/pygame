import pygame
class Square:
    def __init__(self, pic, x, y, offset):
        self.tilepic = pygame.image.load(f"data/imgs/{pic}")
        self.offset = offset
        self.x = x
        self.y = y

    def blitTile(self, screen):
        screen.blit(self.tilepic, (self.x * self.offset, self.y * self.offset))