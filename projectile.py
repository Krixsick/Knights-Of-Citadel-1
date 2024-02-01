import pygame
import math
from entityHandler import entities, Entity


class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, vel, size, damage, sprite_image, sprite_frames=[], mouseAngle=None):
        '''
        Initializes the Projectile object.

        Parameters
        ----------
        pos : tuple
            The initial position of the projectile.
        vel : tuple
            The velocity of the projectile.
        size : int
            The size of the projectile.
        damage : int
            The damage inflicted by the projectile.
        sprite_image : pygame.Surface
            The sprite image of the projectile.
        sprite_frames : list, optional
            The list of sprite frames for animation, by default [].
        mouseAngle : float, optional
            The angle in radians between the projectile and the mouse pointer, by default None.
        '''
        super().__init__()
        self.sprite = sprite_image
        self.pos = pos
        self.vel = vel
        self.size = size
        self.angle = 0 if self.size == 15 else math.degrees(
            math.atan2(self.vel[1], self.vel[0]))
        self.image = pygame.transform.rotate(self.sprite, -self.angle)
        self.displayRect = self.image.get_rect(center=pos)
        self.rect = self.image.get_rect(center=pos)
        self.damage = damage
        self.sprite_frames = [
            sprite_image] if sprite_frames == [] else sprite_frames
        self.frame = 0
        self.animation_speed = 5
        self.frame_counter = 0
        self.mouseAngle = mouseAngle
        entities.add(self)

        # Lightning bolt hitbox fix
        self.hitboxes = []
        if self.size == 3:
            min_x = self.pos[0] - self.image.get_width() // 2
            min_y = self.pos[1] - self.image.get_height() // 2
            rotated_hitbox = pygame.Rect(
                min_x, min_y, self.image.get_width(), self.image.get_height())
            self.hitboxes = self.split_hitbox(
                rotated_hitbox, 30, self.mouseAngle)
            self.rect = self.hitboxes

    def update(self):
        '''
        Updates the position, angle, and animation frame of the projectile.

        Returns
        -------
        None.
        '''
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.angle = math.degrees(math.atan2(self.vel[1], self.vel[0]))

        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.frame = (self.frame + 1) % len(self.sprite_frames)
            self.sprite = self.sprite_frames[self.frame]
            if self.size != 15:
                self.image = pygame.transform.rotate(self.sprite, -self.angle)
            self.rect = self.image.get_rect(center=self.pos)
            self.displayRect = self.rect

    def split_hitbox(self, hitbox, segment_count, angle):
        '''
        Splits the hitbox into segments based on the angle of the projectile.

        Parameters
        ----------
        hitbox : pygame.Rect
            The hitbox rectangle of the projectile.
        segment_count : int
            The number of segments to split the hitbox into.
        angle : float
            The angle in radians between the projectile and the mouse pointer.

        Returns
        -------
        list
            A list of segmented hitboxes.
        '''
        segment_width = hitbox.width // segment_count
        segment_height = 20

        hitboxes = []
        if (angle >= 0 and angle < math.radians(90)) or (angle >= math.radians(-180) and angle < math.radians(-90)):
            directionMultiplier = 1
            start_y = hitbox.y
        else:
            directionMultiplier = -1
            start_y = hitbox.y + hitbox.height

        angle_rad = math.radians(angle)
        vertical_displacement = hitbox.height * math.sin(angle_rad)
        segment_displacement = vertical_displacement / segment_count

        for i in range(segment_count):
            try:
                segment_x = hitbox.x + i * segment_width
                segment_y = start_y + i * \
                    (segment_displacement / math.sin(angle_rad)) * \
                    directionMultiplier
            except ZeroDivisionError:
                continue

            segment_hitbox = pygame.Rect(
                segment_x, segment_y, segment_width, segment_height)
            hitboxes.append(segment_hitbox)

        return hitboxes

    def draw(self, surface):
        '''
        Draws the projectile and hitboxes on the given surface.

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw on.

        Returns
        -------
        None.
        '''
        surface.blit(self.image, self.displayRect)


    def kill(self):
        '''
        Kills the projectile by removing it from the sprite group it belongs to.

        Returns
        -------
        None.
        '''
        super().kill()