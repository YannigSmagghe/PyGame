import pygame

import constants
import platforms


class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = [platforms.SPIKE]

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
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


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [
            [platforms.GRASS_LEFT, 0, 550],
            [platforms.GRASS_MIDDLE, 70, 550],
            [platforms.GRASS_MIDDLE, 140, 550],
            [platforms.GRASS_MIDDLE, 210, 550],
            [platforms.GRASS_MIDDLE, 280, 550],
            [platforms.GRASS_MIDDLE, 320, 550],
            [platforms.GRASS_MIDDLE, 370, 550],
            [platforms.GRASS_RIGHT, 440, 550],
            [platforms.GRASS_LEFT, 500, 500],
            [platforms.GRASS_MIDDLE, 570, 500],
            [platforms.GRASS_RIGHT, 640, 500],
            [platforms.GRASS_LEFT, 800, 400],
            [platforms.GRASS_MIDDLE, 870, 400],
            [platforms.GRASS_RIGHT, 940, 400],
            [platforms.GRASS_LEFT, 1000, 500],
            [platforms.GRASS_MIDDLE, 1070, 500],
            [platforms.GRASS_RIGHT, 1140, 500],
            [platforms.STONE_PLATFORM_LEFT, 1120, 280],
            [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
            [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
            [platforms.GRASS_LEFT, 2400, 500],
            [platforms.GRASS_MIDDLE, 2470, 500],
            [platforms.GRASS_RIGHT, 2540, 500],
            [platforms.GRASS_LEFT, 2700, 450],
            [platforms.GRASS_MIDDLE, 2770, 450],
            [platforms.GRASS_RIGHT, 2840, 450],
            [platforms.GRASS_LEFT, 3000, 400],
            [platforms.GRASS_MIDDLE, 3070, 400],
            [platforms.GRASS_RIGHT, 3140, 400],
            [platforms.GRASS_LEFT, 3300, 350],
            [platforms.GRASS_MIDDLE, 3370, 350],
            [platforms.GRASS_RIGHT, 3440, 350],
        ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        movingPlateform = [
            [platforms.STONE_PLATFORM_MIDDLE, 1350, 280, 1350, 1600],
            [platforms.STONE_PLATFORM_MIDDLE, 1600, 280, 1600, 2400],
        ]
        # Add a custom moving platform

        for platform in movingPlateform:
            block = platforms.MovingPlatform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.boundary_left = platform[3]
            block.boundary_right = platform[4]
            block.change_x = 1
            block.player = self.player
            block.level = self
            self.platform_list.add(block)

        enemyList = [
            [platforms.SPIKE, 0, 500,0,350],
        ]
        # Add a custom moving platform

        for enemy in enemyList:
            block = platforms.MovingPlatform(enemy[0])
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.boundary_left = enemy[3]
            block.boundary_right = enemy[4]
            block.change_x = 1
            block.player = self.player
            block.level = self
            self.enemy_list.add(block)



# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [
            [platforms.GRASS_LEFT, 300, 550],
            [platforms.GRASS_MIDDLE, 370, 550],
            [platforms.GRASS_RIGHT, 440, 550],
            [platforms.STONE_PLATFORM_LEFT, 500, 550],
            [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
            [platforms.STONE_PLATFORM_RIGHT, 640, 550],
            [platforms.GRASS_LEFT, 800, 400],
            [platforms.GRASS_MIDDLE, 870, 400],
            [platforms.GRASS_RIGHT, 940, 400],
            [platforms.GRASS_LEFT, 1000, 500],
            [platforms.GRASS_MIDDLE, 1070, 500],
            [platforms.GRASS_RIGHT, 1140, 500],
            [platforms.STONE_PLATFORM_LEFT, 1120, 280],
            [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
            [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
            [platforms.STONE_PLATFORM_LEFT, 1120, 280],
            [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
            [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
            [platforms.GRASS_LEFT, 2400, 500],
            [platforms.GRASS_MIDDLE, 2470, 500],
            [platforms.GRASS_RIGHT, 2540, 500],
            [platforms.GRASS_LEFT, 2700, 450],
            [platforms.GRASS_MIDDLE, 2770, 450],
            [platforms.GRASS_RIGHT, 2840, 450],
            [platforms.GRASS_LEFT, 3000, 400],
            [platforms.GRASS_MIDDLE, 3070, 400],
            [platforms.GRASS_RIGHT, 3140, 400],
            [platforms.GRASS_LEFT, 3300, 350],
            [platforms.GRASS_MIDDLE, 3370, 350],
            [platforms.GRASS_RIGHT, 3440, 350],
        ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        movingPlateform = [
            [platforms.STONE_PLATFORM_MIDDLE, 1350, 280, 1350, 1600],
            [platforms.STONE_PLATFORM_MIDDLE, 1600, 280, 1600, 2400],
        ]
        # Add a custom moving platform

        for platform in movingPlateform:
            block = platforms.MovingPlatform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.boundary_left = platform[3]
            block.boundary_right = platform[4]
            block.change_x = 1
            block.player = self.player
            block.level = self
            self.platform_list.add(block)

class Level_Dead(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Game_Over.jpg").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000

class Level_Win(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Game_Win.jpg").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000
