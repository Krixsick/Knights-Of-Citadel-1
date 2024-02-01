#Importing modules and assets to the game
import pygame
import os
import random

#Setting the dimensions for the window
win_width = 900
win_height = 500
# Instance of Enemy Class
enemies = []

#Sprites for the enemy spawning from the left side
left_enemy = [pygame.image.load(os.path.join("Assets/Enemy", "L1E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L2E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L3E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L4E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L5E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L6E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L7E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L8E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L9P.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L10P.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L11P.png"))
              ]
#Sprites for the enemy spawning from the right side
right_enemy = [pygame.image.load(os.path.join("Assets/Enemy", "R1E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R2E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R3E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R4E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R5E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R6E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R7E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R8E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R9P.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R10P.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R11P.png"))
               ]


class Enemy:
  '''
  A class allows us to access the attributes and values associated with the enemy entity. Such as its health, damage, pathing, health bar, its movement and combining the sprites together

  Methods
  -------
  calculate_path() -> Str
    Provides a list of coordinates assiocated with the x and y positions on the screen for the enemies to follow. This set of path comprised of paths for the enemy to follow from the left, right, and bottom right side.
  move() -> Str
    Modifies the speed/pace at which the enemy will move at
  step() -> Str
    Used to control the animation at which the enemies' sprites function
  draw() -> str
    Used to render the drawings of the enemies' sprites and will constantly update the health bar of the boss
  off_screen -> str
    If the enemies travels offscreen from our game, it will just delete itsself
  kill() -> str
    When called, it will just delete the boss
  is_collision() -> list
    Creates a circular collision hitbox of the enemies and uses the projectile parameter to make the tower attacks do damage 
    
'''
  def __init__(self, x, y, direction, health = 100):
      self.x = x
      self.y = y
      self.direction = direction
      self.stepIndex = 0
      self.health = health
      self.maxHealth = health
      self.damage = 10  # Add the damage attribute with a default value of 10
      self.width = 55  # Adjust the width of the enemy
      self.height = 55  # Adjust the height of the enemy
      # Create the rect object
      self.path = []  # List to store the path coordinates
      self.calculatePath()  # Calculate the path for the enemy
      self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

  def step(self):
    '''
        Used to control the animation at which the enemies' sprites function
        
        Attributes
        -------
        None
        
        Returns
        -------
        None
    '''
    if self.stepIndex >= 55:
        self.stepIndex = 0

  def calculatePath(self):
    '''
        Determines a set path for the enemies to follow to attack the tower. It follows a direction from the list of coordinates provding the x and y positions of the path. It has 3 lists for coordinates as each of these lists provide the necessary coordinates for enemies to follow when spawning from the three locations.
        
        Attributes
        -------
        None
        
        Returns
        -------
        None
  '''
   # Calculate the path for the enemy to follow
    target_x = win_width // 2  # X-coordinate of the target position
    target_y = win_height // 2  # Y-coordinate of the target position
    # Calculate a simple linear path from the enemy's current position to the target position
    if self.direction == 'left':
      path_points = [
          (self.x, self.y),       # Starting position
          (879, 147), 
          (854, 130),  
          (814, 112),  
          (779, 109),  
          (670, 109),  
          (612, 119),
          (585, 132),
          (580, 160), (560, 202), (540, 260), (410, 250)
      ]

      self.path = path_points
    elif self.direction == 'right':
      self.path = [(self.x, self.y), (9, 73), (30, 79), (35, 138), (69, 179), (90, 194),
                   (127, 195), (234, 195), (269, 199), (300, 222), (320, 237), (380, 230)]

    elif self.direction == 'left2':
      self.path = [(self.x, self.y), (769, 486), (747, 433), (718, 418), (676, 400),
                   (628, 395), (580, 390), (557, 393), (504, 374), (486, 331), (380, 230)]

  def move(self):
    '''
        Changes the movement of the boss to make it walk faster or slower towards the tower. It uses the x and y values of the boss and adjusts them to follow the pathway at a certain speed
        
        Attributes
        ----------
        None
        
        Returns
        -------
        None
  '''
    # Move the enemy along the calculated path
    if self.path:
        target_x, target_y = self.path[0]
        if self.x < target_x:
            self.x += 0.5
        elif self.x > target_x:
            self.x -= 0.5
        if self.y < target_y:
            self.y += 0.5
        elif self.y > target_y:
            self.y -= 0.5
        self.rect.x = self.x
        self.rect.y = self.y
        if self.x == target_x and self.y == target_y:
            self.path.pop(0)  # Remove the current target from the path

  def draw(self, win):
    '''
          Used to constantly update the boss' sprites and health bar. It keeps track whether an interaction has occured and will update to the event accordingly. 
          
          Attributes
          ----------
          win -> int
            The height and width of the screen so it can draw all the images according to that resolution. 
          
          Returns
          -------
          None
'''
    self.step()
    self.move()
    # Left is when enemies are moving towards the left side
    if self.direction == 'left':
        win.blit(left_enemy[self.stepIndex // 10], (self.x, self.y))
    # Right is when enemies are moving towards the right side
    if self.direction == 'right':
        win.blit(right_enemy[self.stepIndex // 10], (self.x, self.y))
        self.stepIndex = (self.stepIndex + 1) % (len(left_enemy) * 10)
    if self.direction == 'left2':
        win.blit(left_enemy[self.stepIndex // 10], (self.x, self.y))

# Health bar variables
    health_bar_width = 50
    health_bar_height = 5
    health_bar_x = self.x + (self.width - health_bar_width) // 2
    health_bar_y = self.y - health_bar_height - 2
    health_bar_fill = (self.health/ self.maxHealth) * health_bar_width

    # Draw health bar
    health_bar_outline = pygame.Rect(
        health_bar_x, health_bar_y, health_bar_width, health_bar_height)
    health_bar_fill_rect = pygame.Rect(
        health_bar_x, health_bar_y, health_bar_fill, health_bar_height)

    pygame.draw.rect(win, (255, 0, 0), health_bar_outline)
    pygame.draw.rect(win, (0, 255, 0), health_bar_fill_rect)

  def off_screen(self):
    '''
          Used to keep track whether the boss has exited out the game's display screen. 
          
          Attributes
          ----------
          None 
          
          Returns
          -------
          Whether the enemy has been found of screen or not
'''
    return not(self.x >= -55 and self.x <= win_width)

  def is_collision(self, projectile):
    '''
          Used to keep track when the projectile has come into contact with the hitboxes of the enemies
          
          Attributes
          ----------
          projectiles -> list
            Uses a projectile from our tower and tracks if the distance between the object is projectile is true or not
          
          Returns
          -------
          if the distance is less than the sum of the radii of the enemy and projectile
'''
    
    # Calculate the distance between the center of the enemy and the center of the projectile
    distance = ((self.x + self.radius) - (projectile.pos[0] + projectile.width / 2)) ** 2 + \
               ((self.y + self.radius) -
                (projectile.pos[1] + projectile.height / 2)) ** 2
    # Check if the distance is less than the sum of the radii of the enemy and the projectile
    return distance < (self.radius + max(projectile.width, projectile.height)) ** 2

  def kill(self):
    '''
          When called, it will instantly remove the boss 
          
          Attributes
          ----------
          None
          
          Returns
          -------
          None
'''
    # Implement the kill method for the enemy
    self.health = -1000  # Set health to 0 to indicate that the enemy is dead
