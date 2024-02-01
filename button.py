# Credits to...
#https://www.thepythoncode.com/article/make-a-button-using-pygame-in-python
#https://favtutor.com/blogs/static-variable-python
#---https://www.pygame.org/docs/ref/mouse.html---
#https://www.geeksforgeeks.org/how-to-change-screen-background-color-in-pygame/
#https://www.geeksforgeeks.org/pygame-surface-blit-function/

import pygame

class Button:
    '''
    A class representing a button in a user interface.

    Methods
    -------
    update() -> None
        Updates the button's state and appearance based on user interactions.
    '''

    def __init__(self, _onClick, _sprite, _parentUI, _posX=0, _posY=0, _customWidthMultiplier=1, _customHeightMultiplier=1):
        '''
        Initializes a button object.

        Parameters
        ----------
        _onClick : function
            The function to call when the button is clicked.
        _sprite : str
            The path to the sprite image file for the button.
        _parentUI : pygame.Surface
            The parent user interface surface to blit the button onto.
        _posX : int, optional
            The x-coordinate position of the button on the parent surface, by default 0.
        _posY : int, optional
            The y-coordinate position of the button on the parent surface, by default 0.
        _customWidthMultiplier : int, optional
            The custom width multiplier to scale the button sprite, by default 1.
        _customHeightMultiplier : int, optional
            The custom height multiplier to scale the button sprite, by default 1.
        '''
        self.parent = _parentUI
        self.sprite = pygame.image.load(_sprite)
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width() * _customWidthMultiplier, self.sprite.get_height() * _customHeightMultiplier))
        self.buttonRect = self.sprite.get_rect()
        self.buttonRect.topleft = (_posX, _posY)
        self.buttonSurface = pygame.Surface((self.sprite.get_width(), self.sprite.get_height()))
        self.onClick = _onClick
        self.pressed = False

    def update(self):
        '''
        Updates the button's state and appearance based on user interactions.
        '''
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.set_alpha(255)
        self.buttonSurface.blit(self.sprite, (0, 0))
        
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.set_alpha(200)
            
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.set_alpha(160)
                if not self.pressed:
                    self.onClick()
                    self.pressed = True
            else:
                self.pressed = False

        self.parent.blit(self.buttonSurface, (self.buttonRect.x, self.buttonRect.y))
