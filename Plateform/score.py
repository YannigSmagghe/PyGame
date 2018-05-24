"""
Module for managing platforms.
"""
import constants
import pygame


class Score():

    def __init__(self):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.score = 0

    # Update everythign on this level
    def update(self, screen, player,current_level_no):
        self.score += player.change_x
        int(self.score)
        font = pygame.font.Font(None, 36)
        text_score = font.render("Score: " + str(self.score), 1, (constants.WHITE))
        text_speed = font.render("Speed: " + str(player.speed), 1, (constants.WHITE))
        text_lvl = font.render("Level: " + str(current_level_no), 1, (constants.WHITE))
        textpos_score = text_score.get_rect(centerx=screen.get_width() - 600)
        textpos_speed = text_speed.get_rect(centerx=screen.get_width() - 150)
        textpos_lvl = text_lvl.get_rect(centerx=screen.get_width() / 2)
        screen.blit(text_score, textpos_score)
        screen.blit(text_speed, textpos_speed)
        screen.blit(text_lvl, textpos_lvl)
