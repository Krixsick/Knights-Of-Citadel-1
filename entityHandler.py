import pygame
entities = pygame.sprite.Group()

class Entity(pygame.sprite.Sprite):
    def __init__(self, entity_image, max_health, castle=False):
        '''
        Initializes an Entity object.

        Parameters
        ----------
        entity_image : pygame.Surface
            The image representing the entity.
        max_health : int
            The maximum health of the entity.
        castle : bool, optional
            Determines if the entity is a castle, by default False.
        '''
        super().__init__()
        self.image = entity_image
        self.rect = self.image.get_rect()
        self.castle = castle
        entities.add(self)
        self.hitbox = self.rect
        self.max_health = max_health
        self.current_health = max_health

    def update_hitbox(self):
        '''
        Updates the hitbox to match the current entity's position and size.
        '''
        self.hitbox = self.rect

    def get_hitbox(self):
        '''
        Returns the hitbox rectangle of the entity.

        Returns
        -------
        pygame.Rect
            The hitbox rectangle of the entity.
        '''
        return self.hitbox

    def take_damage(self, damage):
        '''
        Reduces the entity's health by the specified damage amount.

        Parameters
        ----------
        damage : int
            The amount of damage to be taken.
        '''
        self.current_health -= damage
        if self.current_health <= 0:
            self.kill()  # If health drops below or equal to 0, kill the entity

    def heal(self, amount):
        '''
        Increases the entity's health by the specified amount.

        Parameters
        ----------
        amount : int
            The amount of health to be added.
        '''
        self.current_health += amount
        if self.current_health > self.max_health:
            # Limit the current health to the maximum health
            self.current_health = self.max_health

    def is_alive(self):
        '''
        Checks if the entity is still alive (has positive health).

        Returns
        -------
        bool
            True if the entity is alive, False otherwise.
        '''
        return self.current_health > 0

    def kill(self):
        '''
        Kills the entity by removing it from the sprite group it belongs to.
        '''
        super().kill()
        # Kill the entity by removing it from the sprite group it belongs to
