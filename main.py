import pygame
import random
pygame.init()

class DrawInformation:
    # General variables, used throughout
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        # Sets width and height of window, sets title, calls set_list
        self.width = width
        self.height = height
        
        # instantiates window
        self.window = pygame.display.set_mode((width, height))

        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    def set_list(self, lst):
        # Sets the height and width of the bars, accounting for top and side padding
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        
        self.pixel_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR) # Fills display with preset BACKGROUND_COLOR variable
    pygame.display.update()


def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def main():
    # starts game, while loop for pygame
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)

    while run:
        clock.tick(60) #Framerate

        draw(draw_info)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Checks for x button
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()