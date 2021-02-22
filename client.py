import pygame

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

client_number = 0

# class for our ckarachkter


class Player():
    # construct of class (initialisation of elements)
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)


    # draw method -> represents our character on window
    def draw(self):
        """
        This method have to draw the rect (pygame.draw.rect)
        on our screen
        :return: None
        """
    def move(self):
        """
        this method checks which button was clicked
        (right or left)
        :return: None
        """




def red_raw_window():
    win.fill((255, 255, 255))
    pygame.display.update()


# def for checking events
def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        red_raw_window()

