import pygame
from data.classes.board import Board

#helper for mouse detection
def in_range(x, low, high):
    return ((x >= low) & (x <= high))

# define a main function
def main():
    OSKI_X = 750
    OSKI_Y = 500
    X_OFFSET = 20
    Y_OFFSET = 30
    WINDOW_SIZE = (800, 800)
    # initialize the pygame module
    pygame.init()
    pygame.font.init()
    print("maybe \n")
    # OSKI IS 750x500
    pic = pygame.image.load("data/imgs/bK.png")
    pygame.display.set_caption("minimal program")
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode(WINDOW_SIZE)
    board  = Board(800, 800, screen)
    board.blitBoard(screen)
    pygame.display.flip()
    # define a variable to control the main loop
    running = True
    clicked = False
    # main loop
    while running:
        # event handling, gets all event from the event queue
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        x_tile = x // 100
        y_tile = y // 100
        image = pygame.image.load("data/imgs/point.png")
        screen.blit(image, (10, 10))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Called handle") 
                board.handleClick(x_tile, y_tile)
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

#helper func for checking mouse pos