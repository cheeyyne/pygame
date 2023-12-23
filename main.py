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
    # initialize the pygame module
    pygame.init()
    print("maybe \n")
    # OSKI IS 750x500
    logo = pygame.image.load("oski.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800,800))
    board  = Board(800, 800)
    board.blitBoard(screen)
    pygame.display.flip()
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if (in_range(x, X_OFFSET, X_OFFSET + OSKI_X) & in_range(y, Y_OFFSET, Y_OFFSET + OSKI_Y)):
            screen.blit(logo, (X_OFFSET + 100, Y_OFFSET + 100))
        else: 
            screen.blit(logo, (X_OFFSET, Y_OFFSET))
        pygame.display.flip()
        for event in pygame.event.get():
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