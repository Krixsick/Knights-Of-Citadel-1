#Importing all the modules and libraries 
import pygame
from pygame.locals import *
import os
from settingsmenu import SettingsMenu

#Castle Image
castle_image = pygame.transform.scale(
    pygame.image.load('Assets/Tower/tower.png'), (85, 130))
   
def draw_tower(window, tower_health):
  '''
          Draws the tower's health bar and updates it accrodingly to how much health is left after each collision with an enemy or boss.
          
          Attributes
          ----------
          window -> int
            The display resolution of the game so it can draw a health bar that is placed accordingly to the tower's location
          tower_health -> int
            The amount of health the tower has stored
          
          Returns
          -------
          None
'''
  window.blit(castle_image, (385, 168))
  bar_width = 70
  bar_height = 10
  bar_x = 390
  bar_y = 160

  # Calculate the width of the health bar based on the tower's current health
  health_percentage = tower_health / 100.0
  current_width = int(bar_width * health_percentage)

  # Draw the background of the health bar
  pygame.draw.rect(window, (255, 0, 0),
                   (bar_x, bar_y, bar_width, bar_height))

  # Draw the current health of the tower as a green bar
  pygame.draw.rect(window, (0, 255, 0),
                   (bar_x, bar_y, current_width, bar_height))


def collides_with_enemy(enemy, tower_position, tower_health):
  '''
          Updates the health of the tower everytime a collision occurs. 
          
          Attributes
          ----------
          enemy -> int
            Uses the enemy value as a method to see if the tower hitbox connects with the enemy and uses it's attack power to decrease the health of the tower
          tower_position -> int
            The location of the tower
          tower_health -> int
            The amount of health the tower has stored
          
          Returns
          -------
          tower_health -> int
            Returns the updated version of the health for the tower
'''
  tower_rect = pygame.Rect(
      tower_position[0] - 20, tower_position[1], 35, 130)
  if tower_rect.colliderect(enemy.rect):
      tower_health -= enemy.damage  # Subtract the enemy's damage from the tower's health
      tower_hit_sound = pygame.mixer.Sound('Assets/SFX/tower_impact.wav')
      tower_hit_sound.set_volume(SettingsMenu.towerhitsoundvolume)
      pygame.mixer.Sound.play(tower_hit_sound)
      enemy.kill()  # Kill the enemy
  return tower_health
