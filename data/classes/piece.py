import pygame

class Piece:
    def __init__(self, pieceString):
        self.pieceString = pieceString
        self.pic = pygame.image.load(f"data/imgs/{self.pieceString}.png")
        self.pic = pygame.transform.scale(self.pic, (80, 80))
        self.pic.set_colorkey((34, 34, 34))

    def blitPiece(self, screen, x, y):
        screen.blit(self.pic, (x + 10, y + 10))

    def getPieceString(self):
        return self.pieceString
