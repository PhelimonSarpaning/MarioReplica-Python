

import pygame

import constants
import view

from mario import Mario
from coins import Coin
from coinblock import Coinblock
from emptyCoinblock import EmptyCoinblock
from view import View


def main():
    """ Main"""
    pygame.init()

    # Set the height and width of the screen
    size = [800, 600]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Turtle Attack!")

    # let mario appear
    mario = Mario()
    coin = Coin()
    coinblock = Coinblock()
    empty = EmptyCoinblock()
    act_view = View(mario)

    i = 0

    # initialize views
    view_list = []
    view_list.append(view.Level_01(mario))

    # Set the current level
    current_view_no = 0
    current_view = view_list[current_view_no]

    active_sprite_list = pygame.sprite.Group()
    mario.level = current_view

    mario.rect.x = 340
    mario.rect.y = constants.SCREEN_HEIGHT - mario.rect.height
    active_sprite_list.add(mario)

    # Loop until the user clicks the close button.
    done = False

    # how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # checks events
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # boolean that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mario.left()
                if event.key == pygame.K_RIGHT:
                    mario.right()
                if event.key == pygame.K_SPACE:
                    mario.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and mario.change_x < 0:
                    mario.stop()
                if event.key == pygame.K_RIGHT and mario.change_x > 0:
                    mario.stop()

        print("this is main class for coin ", mario.show_coin)
        if mario.show_coin:
            i += 1
            coin.rect.x = mario.rect.x
            coin.rect.y = mario.rect.y
            active_sprite_list.add(coin)
            print("num ", i)
            print()
        if i == 5:
            print("damn it is 5 oooooh")
            mario.show_coin = False
            i = 0

        print("okay ", mario.show_coin)

        print("my jump count is ", mario.jump_count)
        if mario.jump_count == 5:
            coinblock.image = pygame.image.load("block2.png")
            print("image file is ", coinblock.image)
            print(" the number in view is ", act_view.num)
            act_view.num = 2

        if act_view.num == 2:
            current_view.newblock()
            act_view.num = 1


            coinblock.kill()


        # Update items in the level
        current_view.update()

        # Update mario.
        active_sprite_list.update()

        block_hit_list = pygame.sprite.spritecollide(mario, mario.level.platform_list, False)
        for block in block_hit_list:
            print("this is from main game class " + block)

        # If mario gets near the right side, shift the world left (-x)
        if mario.rect.x >= 500:
            diff = mario.rect.x - 500
            mario.rect.x = 500
            current_view.shift_world(-diff)

        # If mario gets near the left side, shift the world right (+x)
        if mario.rect.x <= 120:
            diff = 120 - mario.rect.x
            mario.rect.x = 120
            current_view.shift_world(diff)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_view.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        coin.kill()
        # Limit to 60 frames per second
        clock.tick(60)

        # update the screen with what we've drawn.
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()
