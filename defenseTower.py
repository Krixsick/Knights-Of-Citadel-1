import pygame
import math

class AutomatedDefenseTower:
    def __init__(self, x, y, projectileType, sprite, interval):
        '''
        Initializes an AutomatedDefenseTower object.

        Parameters
        ----------
        x : int
            The x-coordinate position of the defense tower.
        y : int
            The y-coordinate position of the defense tower.
        projectileType : str
            The type of projectile used by the defense tower.
        sprite : pygame.Surface
            The sprite image of the defense tower.
        interval : int
            The interval between spawning projectiles.
        '''
        self.x = x
        self.y = y
        self.image = sprite
        self.clock = pygame.time.Clock()
        self.projectileType = projectileType
        self.spawn_interval = interval
        self.last_spawn_time = pygame.time.get_ticks()
        self.rect = self.image.get_rect(center=[self.x, self.y])

    def draw(self, window):
        '''
        Draws the defense tower on the given window.

        Parameters
        ----------
        window : pygame.Surface
            The window surface to draw the defense tower onto.
        '''
        window.blit(self.image, (self.x, self.y))

    def find_nearest_enemy(self, enemies):
        '''
        Finds the nearest enemy to the defense tower from the given list of enemies.

        Parameters
        ----------
        enemies : list
            A list of enemy objects.

        Returns
        -------
        list or None
            The position of the nearest enemy as a list [x, y] or None if no enemies are present.
        '''
        min_distance = float('inf')  # Initialize the minimum distance as infinity
        nearest_enemy = None  # Initialize the nearest enemy as None

        tower_pos = (self.x, self.y)  # Position of the defense tower

        for enemy in enemies:
            # Calculate the distance between the defense tower and each enemy
            distance = math.sqrt(
                (enemy.x - tower_pos[0]) ** 2 + (enemy.y - tower_pos[1]) ** 2)

            if distance < min_distance:
                # If the calculated distance is less than the current minimum distance,
                # update the minimum distance and nearest enemy accordingly
                min_distance = distance
                nearest_enemy = [enemy.x, enemy.y]

        return nearest_enemy  # Return the position of the nearest enemy
