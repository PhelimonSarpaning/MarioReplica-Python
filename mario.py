
import pygame

import constants

from coins import Coin

from coinblock import MovingPlatform


class Mario(pygame.sprite.Sprite):

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the mario
    walking_frames_l = []
    walking_frames_r = []

    # What direction is mario facing?
    direction = "R"

    # List of sprites we can bump against
    level = None

    show_coin = False

    jump_count = 0



    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        # # Load all the right facing mario images into a list

        image = pygame.image.load("mario1.png")
        self.walking_frames_r.append(image)
        image = pygame.image.load("mario2.png")
        self.walking_frames_r.append(image)
        image = pygame.image.load("mario3.png")
        self.walking_frames_r.append(image)
        image = pygame.image.load("mario4.png")
        self.walking_frames_r.append(image)
        image = pygame.image.load("mario5.png")
        self.walking_frames_r.append(image)

        # Load all the right facing mario images, then flip them to face left.
        image = pygame.image.load("mario1.png")
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("mario2.png")
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("mario3.png")
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("mario4.png")
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.image.load("mario5.png")
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):

        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # check if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            print(block)
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0
            print(isinstance(block, MovingPlatform))

            if isinstance(block, MovingPlatform):
                self.jump_count += 1
                coin = Coin()
                self.show_coin = True
            if self.jump_count >= 6:
                self.show_coin = False

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ when user presses jump button """

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def left(self):
        """ when user presses left. """
        self.change_x = -6
        self.direction = "L"

    def right(self):
        """ when user presses right. " """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
