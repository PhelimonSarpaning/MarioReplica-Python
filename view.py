import pygame

import constants
import bricks
import coinblock
import coins
import emptyCoinblock

class View():

    platform_list = None
    enemy_list = None

    # Background image
    background = None

    num = 1

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update
    def update(self):
        """ Update everything."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw Screen """

        # Draw the background
        screen.fill(constants.WHITE)
        screen.blit(self.background, (self.world_shift // 3, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


# Create view
class Level_01(View):

    def __init__(self, player):

        # Call the parent constructor
        View.__init__(self, player)

        self.background = pygame.image.load("mario10.jpg")
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        level = [[bricks.BRICK_LEFT, 500, 500],
                 [bricks.BRICK_MIDDLE, 570, 500],
                 [bricks.BRICK_RIGHT, 640, 500],
                 [bricks.BRICK_LEFT, 1190, 500],
                 [bricks.BRICK_MIDDLE, 1200, 500],
                 [bricks.BRICK_RIGHT, 1240, 500],
                 [coinblock.BRICK_LEFT, 700, 700],
                 [coinblock.BRICK_MIDDLE, 770, 700],
                 [coinblock.BRICK_RIGHT, 840, 700]

                 ]

        # Go through the array above and add bricks
        for platform in level:
            block = bricks.Platform()
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a coinblock
        if self.num == 1:
            block = coinblock.MovingPlatform()
        elif self.num == 2:
            block = emptyCoinblock.EmptyCoinblock()
        block.rect.x = 980
        block.rect.y = 380
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

    def newblock(self):
        #self.world_shift = 10
        block = emptyCoinblock.EmptyCoinblock()
        block.rect.x = 980 + self.world_shift
        block.rect.y = 380
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)



