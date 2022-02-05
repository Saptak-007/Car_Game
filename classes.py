import pygame
import random
from game_utils import collide


class Road:
    def __init__(self, img, speed=1, x=0, y=0):
        self.x = x
        self.y = y
        self.image = img
        self.speed = speed

    # Displays the road to the screen
    def display(self, surface, screen_height=None):
        surface.blit(self.image, (self.x, self.y))
        surface.blit(self.image, (self.x, self.y-screen_height))

        if self.y < screen_height:
            self.y += self.speed
        else:
            self.y = 0


class Player:
    def __init__(self, img, x_lanes=0, y=0):
        self.x_lanes = x_lanes
        self.x = random.choice(self.x_lanes)
        self.y = y
        self.image = img
        self.image_rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)

    # Displays the player to the screen
    def blit(self, surface):
        surface.blit(self.image, self.image_rect)

    # Moves the player when the left or the right key is pressed
    def move(self, direction):
        if direction.lower() == 'left':
            for lane_no, lane in enumerate(self.x_lanes):
                if self.image_rect.x == lane and self.image_rect.x != self.x_lanes[0]:
                    self.image_rect.x = self.x_lanes[lane_no-1]
                    self.x = self.x_lanes[lane_no-1]
                    break

        elif direction.lower() == 'right':
            for lane_no, lane in enumerate(self.x_lanes):
                if self.image_rect.x == lane and self.image_rect.x != self.x_lanes[-1]:
                    self.image_rect.x = self.x_lanes[lane_no+1]
                    self.x = self.x_lanes[lane_no+1]
                    break
                
    # Returns height of the image of the player
    def get_height(self):
        return self.image.get_height()

    # Checks if collision has occured
    def collision(self, obj):
        return collide(obj, self)


class Enemy:
    def __init__(self, img, speed=1, x=0, y=0):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = img
        self.image_rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
 
    # Displays the enemy to the screen
    def blit(self, surface):
        surface.blit(self.image, self.image_rect)

    # Moves the enemy
    def move(self):
        self.image_rect.y += self.speed
        self.y += self.speed

    # Checks if the enemy car is off the screen 
    def off_screen(self, screen_height):
        return self.y > screen_height