
import pygame
from data.classes.piece import Piece
class Square:
    def __init__(self, tileString, pieceString, x, y, offset):
        if pieceString != "":
            self.piece = Piece(pieceString)
        else:
            self.piece = None
        self.tilepic = pygame.image.load(f"data/imgs/{tileString}")
        self.highlighpic = pygame.image.load("data/imgs/point.png")
        self.offset = offset
        self.x = x
        self.y = y
        self.isHighlighted = False

    def getPieceString(self):
        return self.piece
    def setNewPiece(self, pieceString):
        self.piece = Piece(pieceString)

    def highlight(self):
        self.isHighlighted = True
    
    def blitTile(self, screen):
        screen.blit(self.tilepic, (self.x * self.offset, self.y * self.offset))
        if (self.piece == None) and self.isHighlighted:
            screen.blit(self.highlight, ((self.x * self.offset), (self.y * self.offset)))
        if self.piece != None:
            self.piece.blitPiece(screen, self.x * self.offset, self.y * self.offset)
        