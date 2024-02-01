#Importing modules and initializing variables 
import pygame
import os
win_width = 900
win_height = 500

#Importing the sprites for the boss and trasnforming the images to an appropriate scale 
left_boss = [
  pygame.transform.scale(pygame.image.load(os.path.join("Assets/Boss", "Walk (1).png")), (65, 100)),
  pygame.transform.scale(pygame.image.load(os.path.join("Assets/Boss", "Walk (2).png")), (65, 100)),
  pygame.transform.scale(pygame.image.load(os.path.join("Assets/Boss", "Walk (3).png")), (65, 100)),
  pygame.transform.scale(pygame.image.load(os.path.join("Assets/Boss", "Walk (4).png")), (65, 100)),
  pygame.transform.scale(pygame.image.load(os.path.join("Assets/Boss", "Walk (5).png")), (65, 100)),
  pygame.transform.scale(pygame.image.load(os.path.join("Assets/Boss", "Walk (6).png")), (65, 100)),
  pygame.transform.scale(pygame.image.load(os.path.join("Assets/Boss", "Walk (7).png")), (65, 100)),
  pygame.transform.scale(pygame.image.load(os.path.join("Assets/Boss", "Walk (8).png")), (65, 100)),
  pygame.transform.scale(pygame.image.load(os.path.join("Assets/Boss", "Walk (9).png")), (65, 100)),
  pygame.transform.scale(pygame.image.load(os.path.join("Assets/Boss", "Walk (10).png")), (65, 100))
]

class Boss:
    '''
    A class allows us to access the attributes and values associated with the boss entity. Such as its health, damage, pathing, health bar, its movement and combining the sprites together
  
    Methods
    -------
    set_path() -> Str
      Provides a list of coordinates assiocated with the x and y positions on the screen for the boss to follow.
    move() -> Str
      Modifies the speed/pace at which the boss will move at
    step() -> Str
      Used to control the animation at which the boss' sprites function
    draw() -> str
      Used to render the drawings of the boss' sprites and will constantly update the health bar of the boss
    off_screen -> str
      If the boss travels offscreen from our game, it will just delete itsself
    kill() -> str
      When called, it will just delete the boss
      
    '''
  
    def __init__(self, x, y, direction, health = 500):
      self.x = x
      self.y = y
      self.height = 100
      self.width = 65
      self.health = health
      self.maxHealth = health
      self.damage = 95
      self.direction = direction
      self.stepIndex = 0
      self.path = []
      self.rect = pygame.Rect(x, y, 60, 100)  # Create a rect for collision detection
      self.set_path()
    
    def set_path(self):
        '''
        Determines a set path for the boss to follow to attack the tower. It follows a direction from the list of coordinates provding the x and y positions of the path. 
        
        Attributes
        -------
        None
        
        Returns
        -------
        None
        '''
        if self.direction == 'left':
            path_points = [
                (self.x, self.y),
                (879, 147),
                (854, 130),
                (814, 112),
                (779, 109),
                (670, 109),
                (612, 119),
                (585, 132),
                (580, 160),
                (560, 202),
                (540, 260),
                (410, 250)
            ]
            self.path = path_points
    
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
        if self.path:
            target_x, target_y = self.path[0]
            if self.x < target_x:
                self.x += 0.2
            elif self.x > target_x:
                self.x -= 0.2
            if self.y < target_y:
                self.y += 0.2
            elif self.y > target_y:
                self.y -= 0.2
            self.rect.x = self.x
            self.rect.y = self.y
            if self.x == target_x and self.y == target_y:
                self.path.pop(0)  # Remove the current target from the path
    
    def step(self):
        '''
          Used to control the animation at which the boss' sprites function
          
          Attributes
          ----------
          None
          
          Returns
          -------
          None
        '''
        if self.stepIndex >= 55:
            self.stepIndex = 0
    
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
            win.blit(left_boss[self.stepIndex // 10], (self.x, self.y))
      
        # Health bar variables
        health_bar_width = 50
        health_bar_height = 5
        health_bar_x = self.x + (self.width - health_bar_width) // 2
        health_bar_y = self.y - health_bar_height - 2
        health_bar_fill = (self.health/ self.maxHealth) * health_bar_width
      
        # Draw health bar
        health_bar_outline = pygame.Rect(health_bar_x, health_bar_y, health_bar_width, health_bar_height)
        health_bar_fill_rect = pygame.Rect(health_bar_x, health_bar_y, health_bar_fill, health_bar_height)
      
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
          False
            If the boss hasn't left the screen, the condition is false
        '''
        # Check if the boss is off the screen
        if self.x > win_width or self.x < 0 or self.y > win_height or self.y < 0:
            return True
        return False
    
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
        self.health = -1000