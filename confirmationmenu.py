import pygame
from sys import exit
from widget import Widget
from button import Button
from menu import Menu
from mainmenu import MainMenu

def confirmQuitButton():
    '''
    Function to quit the game and exit the program when the quit button is clicked.
    '''
    pygame.quit()
    exit()

def deactivateConfirmationMenu():
    '''
    Function to deactivate the confirmation menu and resume the game when the cancel button is clicked.
    '''
    Menu.paused = False
    Menu.objects[5].visible = False
    Menu.objects[4].visible = False

class ConfirmationMenu(Menu):
    '''
    A class representing a confirmation menu in the game.

    Methods
    -------
    __init__(_visible, _parentUI)
        Initializes a confirmation menu object.
    '''

    def __init__(self, _visible, _parentUI):
        '''
        Initializes a confirmation menu object.

        Parameters
        ----------
        _visible : bool
            Determines if the confirmation menu is initially visible or hidden.
        _parentUI : pygame.Surface
            The parent user interface surface to blit the confirmation menu onto.
        '''
        super().__init__(_visible, _parentUI)
        self.menubackground = Widget("Assets/UI/zz_menu.png", self.parent, 750 * 15/32 + 300, 400 * 25/54, 0.7, 0.7)
        self.cancel = Button(deactivateConfirmationMenu, "Assets/UI/zz_cancelbutton.png", self.parent, 890 * 15/32 + 300, 610 * 25/54)
        self.confirm = Button(confirmQuitButton, "Assets/UI/zz_quitbutton2.png", self.parent, 890 * 15/32 + 300, 710 * 25/54)
        self.uiElements.append(self.menubackground)
        self.uiElements.append(self.cancel)
        self.uiElements.append(self.confirm)
        Menu.objects.append(self)
