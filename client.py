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
        self.vel = 3


    # draw method -> represents our character on window
    def draw(self, win):
        """
        This method have to draw the rect (pygame.draw.rect)
        on our screen
        """
        pygame.draw.rect(win, self.color, self.rect)


    def move(self):
        """
        this method checks which button was clicked
        (right or left)
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        #when we move our rect we have to updating our (x, y, width, height)
        self.rect = (self.x, self.y, self.width, self.height)


def red_raw_window(win, player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()


# def for checking events
def main():
    run = True
    # create an objects of class Player
    p = Player(50,50,100,100,(0,255,0))

    # clock -> for speed rect (here we can install speed)
    clock = pygame.time.Clock()
    while run:
        clock.tick(60) # 60 FPS speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        red_raw_window(win, p)


main()