import pygame

import constants
# Set speed vector of player


class EmptyCoinblock(pygame.sprite.Sprite):
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
        self.image = pygame.image.load("block2.png")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.size = [800, 600]
        self.screen = pygame.display.set_mode(self.size)

    def update(self):
        """ Move the coin. """
        # Gravity
        # self.calc_grav()

    def die(self):
        self.kill()

    def calc_grav(self):
        """ Calculate effect of gravity. """
        print("we got into coin update")
        for i in range(60):
            self.rect.y += 10
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

# # clock = pygame.time.Clock()
#         # print("I am in this class")
#         # self.screen.blit(self.image, (50, 300))
#         # #while True:
#         # pygame.display.flip()
#         #
#         #
#         # clock.tick(60)
