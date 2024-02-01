import pygame
from widget import Widget
from button import Button
from menu import Menu

def returnButton():
    '''
    Function to handle the action when the return button is clicked in the Credits menu.
    '''
    Menu.objects[1].deactivateMenu()
    Menu.objects[2].deactivateMenu()
    Menu.objects[0].activateMenu()

class CreditsMenu(Menu):
    '''
    A class representing the Credits menu in the game.

    Methods
    -------
    __init__(_visible, _parentUI)
        Initializes a CreditsMenu object.
    '''

    def __init__(self, _visible, _parentUI):
        '''
        Initializes a CreditsMenu object.

        Parameters
        ----------
        _visible : bool
            Determines if the Credits menu is initially visible or hidden.
        _parentUI : pygame.Surface
            The parent user interface surface to blit the Credits menu onto.
        '''
        super().__init__(_visible, _parentUI)
        self.font = pygame.font.SysFont('Times New Roman', 20)
        self.titleFont = pygame.font.SysFont('Times New Roman', 40)
        self.creditsBackground = Widget("Assets/UI/creditsmenu.png", self.parent, 0, 0)
        self.returnButton = Button(returnButton, "Assets/UI/zz_mainmenubutton.png", self.parent, 315, 445)
        self.uiElements.append(self.creditsBackground)
        self.uiElements.append(self.returnButton)
        Menu.objects.append(self)

    def update(self):
        '''
        Updates the menu by updating each UI element.

        Returns
        -------
        None.
        '''
        for uiElement in self.uiElements:
            uiElement.update()
        #window.blit(self.titleFont.render("Credits", (255,255,255)), (0,0))