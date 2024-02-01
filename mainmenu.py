import pygame, sys, game
from settingsmenu import SettingsMenu
from widget import Widget
from button import Button
from menu import Menu
from initialization import window
from shopmenu import ShopMenu

def playButton():
    '''
    Callback function for the play button.

    Returns
    -------
    None.
    '''
    MainMenu.exitMainMenu()
    if MainMenu.gameOver:
        MainMenu.gameOver = False
        ShopMenu.currency = 0
        ShopMenu.lightTowerCount = 0
        ShopMenu.fireballTowerCount = 0
        ShopMenu.lightningTowerCount = 0
        ShopMenu.poisonTowerCount = 0
        ShopMenu.lightBulletLevel = 1
        ShopMenu.fireballBulletLevel = 0
        ShopMenu.lightningBulletLevel = 0
        ShopMenu.poisonBulletLevel = 0
        ShopMenu.holyStrikeBulletLevel = 0
        ShopMenu.lightTowerLevel = 1
        ShopMenu.fireballTowerLevel = 1
        ShopMenu.lightningTowerLevel = 1
        ShopMenu.poisonTowerLevel = 1
        Menu.paused = False
        game.mainGame(window)
    Menu.paused = False

def activateSettingsMenu():
    '''
    Callback function to activate the settings menu.

    Returns
    -------
    None.
    '''
    Menu.objects[1].activateMenu()

def activateCreditsMenu():
    '''
    Callback function to activate the credits menu.

    Returns
    -------
    None.
    '''
    Menu.objects[2].activateMenu()

def confirmQuit():
    '''
    Callback function to activate the quit confirmation menu.

    Returns
    -------
    None.
    '''
    Menu.objects[5].activateMenu()

class MainMenu(Menu):
    '''
    Main menu class.

    Attributes
    ----------
    mainMenuActive : bool
        Flag indicating if the main menu is active.
    gameOver : bool
        Flag indicating if the game is over.

    Methods
    -------
    returnToMainMenu()
        Returns to the main menu.
    exitMainMenu()
        Exits the main menu.
    enterMainMenu()
        Enters the main menu.
    '''
    mainMenuActive = True
    gameOver = False

    @staticmethod
    def returnToMainMenu():
        '''
        Simple return to main menu function.

        Returns
        -------
        None.
        '''
        main_menu_image = pygame.transform.scale(pygame.image.load("Assets/UI/zz_background.png"), (900, 500))
        game_logo = pygame.transform.scale(pygame.image.load("Assets/UI/zz_logo.png"), (150, 150))
        Menu.objects[0].visible = True
        Menu.objects[1].visible = False
        Menu.objects[3].visible = False
        Menu.objects[4].visible = False
        Menu.objects[5].visible = False
        MainMenu.mainMenuActive = True
        while MainMenu.mainMenuActive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                SettingsMenu.bind(event, window)
            window.blit(main_menu_image, (0, 0))
            window.blit(game_logo, (750, 0))
            for menu in Menu.objects:
                if menu.visible:
                    menu.update()
            pygame.display.update()
        MainMenu.mainMenuActive = False
        Menu.objects[0].visible = False

    @staticmethod
    def exitMainMenu():
        '''
        Exits the main menu.

        Returns
        -------
        None.
        '''
        MainMenu.mainMenuActive = False
        Menu.objects[0].visible = False

    @staticmethod
    def enterMainMenu():
        '''
        Enters the main menu.

        Returns
        -------
        None.
        '''
        MainMenu.mainMenuActive = True
        Menu.objects[0].visible = True

    def __init__(self, _visible, _parentUI):
        '''
        Initializes the MainMenu object.

        Parameters
        ----------
        _visible : bool
            Determines if the main menu is initially visible.
        _parentUI : pygame.Surface
            The parent user interface surface.
        '''
        super().__init__(_visible, _parentUI)
        self.menuBackground = Widget("Assets/UI/zz_menubackground.png", self.parent, 100 * 15/32, -50 * 25/54, 15/32, 25/54)
        self.play = Button(playButton, "Assets/UI/zz_playbutton2.png",self.parent, 230 * 15/32, 160 * 25/54)
        self.settings = Button(activateSettingsMenu, "Assets/UI/zz_settingsbutton2.png", self.parent, 230 * 15/32, 260 * 25/54)
        self.credits = Button(activateCreditsMenu, "Assets/UI/zz_creditsbutton2.png", self.parent, 230 * 15/32, 360 * 25/54)
        self.quit = Button(confirmQuit, "Assets/UI/zz_quitbutton2.png",self.parent, 230 * 15/32, 460 * 25/54)
        self.uiElements.append(self.menuBackground)
        self.uiElements.append(self.play)
        self.uiElements.append(self.settings)
        self.uiElements.append(self.credits)
        self.uiElements.append(self.quit)
        Menu.objects.append(self)