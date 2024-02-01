# https://www.w3schools.com/python/python_lambda.asp
import pygame
from widget import Widget
from button import Button
from mainmenu import MainMenu
from settingsmenu import SettingsMenu
from menu import Menu
from initialization import window

def backToMainMenu():
  '''
    Returns to the main menu and also saved config (such as highscore)

    Returns         
    -------
    None.
    '''
  SettingsMenu.saveConfig()
  MainMenu.returnToMainMenu()

def activateSettingsMenu():
    '''
    Activates the settings menu by activating the corresponding menu object.

    Returns
    -------
    None.
    '''
    Menu.objects[1].activateMenu()
    Menu.objects[4].deactivateMenu()

def continueButtonOnClick():
    '''
    Callback function for the continue button click event.
    Resumes the game by setting the menu's paused state to False and deactivating the menu.

    Returns
    -------
    None.
    '''
    Menu.paused = False
    Menu.objects[4].deactivateMenu()

def confirmQuit():
    '''
    Callback function for the quit button click event.
    Activates the confirmation menu.

    Returns
    -------
    None.
    '''
    Menu.objects[5].activateMenu()


class PauseMenu(Menu):
    def __init__(self, _visible, _parentUI):
        '''
        Initializes the PauseMenu object.

        Parameters
        ----------
        _visible : bool
            Determines if the pause menu is initially visible.
        _parentUI : pygame.Surface
            The parent user interface surface.
        '''
        super().__init__(_visible, _parentUI)
        self.font = pygame.font.SysFont('Times New Roman', 30)
        self.pausemenuBackground = Widget("Assets/UI/zz_pausemenubackground.png", self.parent, 250, 10)
        self.continueButton = Button(continueButtonOnClick, "Assets/UI/zz_continuebutton.png", self.parent, 300, 75)
        self.settingsButton = Button(activateSettingsMenu, "Assets/UI/zz_bigsettingsbutton.png", self.parent, 300, 150)
        self.mainMenuButton = Button(backToMainMenu, "Assets/UI/zz_mainmenubutton.png", self.parent, 300, 225)
        self.exitGameButton = Button(confirmQuit, "Assets/UI/zz_exitgamebutton.png", self.parent, 300, 300)
        self.defeatScreen = Widget("Assets/UI/defeatscreen.png", self.parent, 0, 0)
        self.mainMenuButton2 = Button(backToMainMenu, "Assets/UI/zz_mainmenubutton.png", self.parent, 300, 400)
        self.uiElements.append(self.pausemenuBackground)
        self.uiElements.append(self.continueButton)
        self.uiElements.append(self.settingsButton)
        self.uiElements.append(self.mainMenuButton)
        self.uiElements.append(self.exitGameButton)
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
        if MainMenu.gameOver:
            self.defeatScreen.update()
            self.mainMenuButton2.update()
            window.blit(self.font.render(f"High Score: {SettingsMenu.highScore}", 1, (255, 200, 0)), (350, 350))