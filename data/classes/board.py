from data.classes.square import Square
from data.classes.piece import Piece
import pygame

class Board:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.tileWidth = width // 8
        self.tileHeight = height // 8
        self.screen = screen
        self.state = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                      ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                      ['', '', '', '', '', '', '', ''],
                      ['', '', '', '', '', '', '', ''],
                      ['', '', '', '', '', '', '', ''],
                      ['', '', '', '', '', '', '', ''],
                      ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                      ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        self.tileArr = [[Square(tileAssign(i, j), "", i, j, (width // 8)) for i in range(8)] for j in range(8)]
        for i in range(8):
             for j in range(8):
                if (self.state[i][j] != ""):
                    self.tileArr[i][j].setNewPiece(self.state[i][j])
        self.selectedTile = None
        self.selectedX = None
        self.selectedY = None

    def blitBoard(self, screen):
         for i in self.tileArr:
              for j in i:
                   j.blitTile(screen)
    
    def selectTile(self, x, y):
         self.selectedTile = self.tileArr[y][x]
         self.selectedX = x
         self.selectedY = y

    def handleClick(self, x, y):
         #see if selectedTile has been clicked again
         if self.selectedTile == self.tileArr[y][x]:
              print("same tile")
              return
         #see if a tile has been selected
         if self.selectedTile == None:
              temp = self.tileArr[y][x].piece
              #check if selected tile has a piece, if not select tile
              if temp != None:
                   print(f"selected tile {x} {y}")
                   self.selectTile(x, y)
                   self.highlightMoves()
                   pygame.display.flip()
         if (self.isValidMove(self.selectedTile.piece.getPieceString, x, y)):
              print("moved to new tile")
              #move selectedTile to new clicked tile and replace the old piece in selectedTile
              self.tileArr[y][x].piece = self.selectedTile.piece
              self.selectedTile.piece = None
              self.blitBoard(self.screen)
              self.selectedTile = None
              pygame.display.flip()
         else:
              print("invalid move")
    
    def highlightMoves(self):
         for y in self.tileArr:
              for x in y:
                   if (self.isValidMove(self.selectedTile.piece.getPieceString(), self.selectedX, self.selectedY)):
                        self.tileArr[y][x].highlight()
                   
    def isValidMove(self, piece, x, y):
         if (self.tileArr[y][x].piece != None):
              return False
         if self.selectedTile.getPiece().getPieceString()[1] == "K":
              return (abs(self.selectedX - x) == 1) and (abs(self.selectedY - y) == 1)
         return True
         

def tileAssign(i, j):
        return 'whiteTile.png' if (i + j) % 2 == 0 else 'greenTile.png'