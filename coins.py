import pygame


class Coin(pygame.sprite.Sprite):
    coin_num = 0
    display_width = 800
    display_height = 600
    coin_show = False
    change_x = 0
    change_y = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        print("in coin class it is ", self.coin_show)
        print("we are here")
        self.image = pygame.image.load("bitcoin.png")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.size = [800, 600]
        self.screen = pygame.display.set_mode(self.size)

    def update(self):
        """ Move the coin. """
        # Gravity
        #self.calc_grav()

    def die(self):
        self.kill()



