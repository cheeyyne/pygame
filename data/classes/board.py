from data.classes.square import Square

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tileWidth = width // 8
        self.tileHeight = height // 8
        self.state = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                      ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                      ['', '', '', '', '', '', '', ''],
                      ['', '', '', '', '', '', '', ''],
                      ['', '', '', '', '', '', '', ''],
                      ['', '', '', '', '', '', '', ''],
                      ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                      ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        self.tileArr = [[Square(tileAssign(i, j), i, j, (width // 8)) for i in range(8)] for j in range(8)]

    def blitBoard(self, screen):
         for i in self.tileArr:
              for j in i:
                   j.blitTile(screen)
    
def tileAssign(i, j):
        return 'whiteTile.png' if (i + j) % 2 == 0 else 'greenTile.png'