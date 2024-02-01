import pygame
from widget import Widget
from button import Button
from menu import Menu
from initialization import window
from configparser import ConfigParser

def returnButton():
    '''
    Function to handle the return button action in the settings menu.
    '''
    Menu.objects[1].deactivateMenu()
    Menu.objects[4].deactivateMenu()
    Menu.paused = False
    SettingsMenu.saveConfig()


def bindingButton(_binding):
    '''
    Function to handle the binding button action in the settings menu.

    Parameters:
    _binding (str): The name of the key binding being set.
    '''
    SettingsMenu.isBinding = True
    SettingsMenu.binding = _binding

def increaseDifficulty():
  if SettingsMenu.gameDifficulty != 3:
    SettingsMenu.gameDifficulty += 1

def decreaseDifficulty():
  if SettingsMenu.gameDifficulty != 1:
    SettingsMenu.gameDifficulty -= 1

class SettingsMenu(Menu):
    '''
    Class representing the settings menu in the game.
    '''

    # Key bindings
    firebulletkeybind = pygame.K_SPACE
    switchprojectilekeybind = pygame.K_r
    placetowerkeybind = pygame.K_t
    selectlighttowerkeybind = pygame.K_1
    selectfireballtowerkeybind = pygame.K_2
    selectlightningtowerkeybind = pygame.K_3
    selectpoisontowerkeybind = pygame.K_4
    pausegamekeybind = pygame.K_ESCAPE
    selectlightprojectilekeybind = pygame.K_x
    selectfireballprojectilekeybind = pygame.K_c
    selectlightningprojectilekeybind = pygame.K_v
    selectpoisoncloudprojectilekeybind = pygame.K_b
    selectholystrikeprojectilekeybind = pygame.K_n
    openshopkeybind = pygame.K_m

    # Sound volumes
    lightbulletsoundvolume = 1
    fireballbulletsoundvolume = 1
    lightningbulletsoundvolume = 1
    poisoncloudbulletsoundvolume = 1
    holystrikebulletsoundvolume = 1
    enemyhitsoundvolume = 1
    towerhitsoundvolume = 1
    musicvolume = 1

    # Game Data
    highScore = 0
    gameDifficulty = 1
    gameDifficultyText = {
      1:"Easy",
      2:"Medium",
      3:"Hard"
    }

    binding = ""
    isBinding = False

    @staticmethod
    def bind(event, window):
        '''
        Function to bind keys to key bindings.

        Parameters:
        event (pygame.Event): The event triggered by the key press.
        window (pygame.Surface): The game window surface.
        '''
        if event.type == pygame.KEYDOWN and SettingsMenu.isBinding:
            exec(f"SettingsMenu.{SettingsMenu.binding} = event.key")
            SettingsMenu.isBinding = False

    @staticmethod
    def reloadConfig():
      config = ConfigParser()
      config.read("config.ini")
      for iterator in config["KeyBinds"]:
        exec(f"SettingsMenu.{iterator} = {config['KeyBinds'][iterator]}")
      for iterator in config["AudioSettings"]:
        exec(f"SettingsMenu.{iterator} = {int(config['AudioSettings'][iterator])}")
      for iterator in config["GameData"]:
        exec(f"SettingsMenu.{iterator} = {config['GameData'][iterator]}")

    @staticmethod
    def saveConfig():
      configKeyBindsCurrent = {
        "firebulletkeybind":SettingsMenu.firebulletkeybind,
        "switchprojectilekeybind":SettingsMenu.switchprojectilekeybind,
        "placetowerkeybind":SettingsMenu.placetowerkeybind,
        "selectlighttowerkeybind":SettingsMenu.selectlighttowerkeybind,
        "selectfireballtowerkeybind":SettingsMenu.selectfireballtowerkeybind,
        "selectlightningtowerkeybind":SettingsMenu.selectlightningtowerkeybind,
        "selectpoisontowerkeybind":SettingsMenu.selectpoisontowerkeybind,
        "pausegamekeybind":SettingsMenu.pausegamekeybind,
        "selectlightprojectilekeybind":SettingsMenu.selectlightprojectilekeybind,
        "selectfireballprojectilekeybind":SettingsMenu.selectfireballprojectilekeybind,
        "selectlightningprojectilekeybind":SettingsMenu.selectlightningprojectilekeybind,
        "selectpoisoncloudprojectilekeybind":SettingsMenu.selectpoisoncloudprojectilekeybind,
        "selectholystrikeprojectilekeybind":SettingsMenu.selectholystrikeprojectilekeybind,
        "openshopkeybind":SettingsMenu.openshopkeybind
      }
      configAudioCurrent = {
        "lightbulletsoundvolume":SettingsMenu.lightbulletsoundvolume,
        "fireballbulletsoundvolume":SettingsMenu.fireballbulletsoundvolume,
        "lightningbulletsoundvolume":SettingsMenu.lightningbulletsoundvolume,
        "poisoncloudbulletsoundvolume":SettingsMenu.poisoncloudbulletsoundvolume,
        "holystrikebulletsoundvolume":SettingsMenu.holystrikebulletsoundvolume,
        "enemyhitsoundvolume":SettingsMenu.enemyhitsoundvolume,
        "towerhitsoundvolume":SettingsMenu.towerhitsoundvolume,
        "musicvolume":SettingsMenu.musicvolume
      }
      configGameDataCurrent = {
        "highScore":SettingsMenu.highScore,
        "gameDifficulty":SettingsMenu.gameDifficulty
      }
      newConfig = open("config.ini", mode="w+", encoding="utf-8")
      newConfig.write("[KeyBinds]\n")
      for k, v in configKeyBindsCurrent.items():
        keyBind = pygame.key.name(v)
        if len(keyBind) > 1:
          keyBind = keyBind.upper()
        newConfig.write(f"{k} = pygame.K_{keyBind}\n")
      newConfig.write("\n[AudioSettings]\n")
      for k, v in configAudioCurrent.items():
        newConfig.write(f"{k} = {v}\n")
      newConfig.write("\n[GameData]\n")
      for k, v in configGameDataCurrent.items():
        newConfig.write(f"{k} = {v}\n")

    def __init__(self, _visible, _parentUI):
        '''
        Initializes the SettingsMenu object.

        Parameters:
        _visible (bool): Flag indicating whether the menu is visible.
        _parentUI (pygame.Surface): The parent surface containing the menu.

        '''
        super().__init__(_visible, _parentUI)
        self.font = pygame.font.SysFont('Times New Roman', 25)
        self.gameDifficultyFont = pygame.font.SysFont('Times New Roman', 40)
        self.settingsBackground = Widget(
            "Assets/UI/settingsmenu.png", self.parent)
        self.returnButton = Button(
            returnButton, "Assets/UI/zz_keybindButton.png", self.parent, 80, 395)
        self.placetowerkeybindButton = Button(lambda: bindingButton(
            "placetowerkeybind"), "Assets/UI/zz_keybindButton.png", self.parent, 80, 65)
        self.selectlighttowerkeybind = Button(lambda: bindingButton(
            "selectlighttowerkeybind"), "Assets/UI/zz_keybindButton.png", self.parent, 80, 120)
        self.selectfireballtowerkeybind = Button(lambda: bindingButton(
            "selectfireballtowerkeybind"), "Assets/UI/zz_keybindButton.png", self.parent, 80, 175)
        self.selectlightningtowerkeybind = Button(lambda: bindingButton(
            "selectlightningtowerkeybind"), "Assets/UI/zz_keybindButton.png", self.parent, 80, 230)
        self.selectpoisontowerkeybind = Button(lambda: bindingButton(
            "selectpoisontowerkeybind"), "Assets/UI/zz_keybindButton.png", self.parent, 80, 285)
        self.pausegamekeybind = Button(lambda: bindingButton(
            "pausegamekeybind"), "Assets/UI/zz_keybindButton.png", self.parent, 80, 340)
        self.selectlightprojectilekeybind = Button(lambda: bindingButton(
            "selectlightprojectilekeybind"), "Assets/UI/zz_keybindButton.png", self.parent, 455, 65)
        self.selectfireballprojectilekeybind = Button(lambda: bindingButton(
            "selectfireballprojectilekeybind"), "Assets/UI/zz_keybindButton.png", self.parent, 455, 120)
        self.selectlightningprojectilekeybind = Button(lambda: bindingButton(
            "selectlightningprojectilekeybind"), "Assets/UI/zz_keybindButton.png", self.parent, 455, 175)
        self.selectpoisoncloudprojectilekeybind = Button(lambda: bindingButton(
            "selectpoisoncloudprojectilekeybind"), "Assets/UI/zz_keybindButton.png", self.parent, 455, 230)
        self.selectholystrikeprojectilekeybind = Button(lambda: bindingButton(
            "selectholystrikeprojectilekeybind"), "Assets/UI/zz_keybindButton.png", self.parent, 455, 285)
        self.openshopkeybind = Button(lambda: bindingButton(
            "openshopkeybind"), "Assets/UI/zz_keybindButton.png", self.parent, 455, 340)
        self.increaseDifficultyButton = Button(increaseDifficulty, "Assets/UI/plusicon.png", self.parent, 730, 395, 0.15, 0.15)
        self.decreaseDifficultyButton = Button(decreaseDifficulty, "Assets/UI/minusbutton.png", self.parent, 475, 395, 0.15, 0.15)
        self.uiElements.append(self.settingsBackground)
        self.uiElements.append(self.returnButton)
        self.uiElements.append(self.placetowerkeybindButton)
        self.uiElements.append(self.selectlighttowerkeybind)
        self.uiElements.append(self.selectfireballtowerkeybind)
        self.uiElements.append(self.selectlightningtowerkeybind)
        self.uiElements.append(self.selectpoisontowerkeybind)
        self.uiElements.append(self.pausegamekeybind)
        self.uiElements.append(self.selectlightprojectilekeybind)
        self.uiElements.append(self.selectfireballprojectilekeybind)
        self.uiElements.append(self.selectlightningprojectilekeybind)
        self.uiElements.append(self.selectpoisoncloudprojectilekeybind)
        self.uiElements.append(self.selectholystrikeprojectilekeybind)
        self.uiElements.append(self.openshopkeybind)
        self.uiElements.append(self.increaseDifficultyButton)
        self.uiElements.append(self.decreaseDifficultyButton)
        Menu.objects.append(self)

    def update(self):
        '''
        Updates the display in the settings menu.

        Returns:
        None
        '''
        for uiElement in self.uiElements:
            uiElement.update()
        window.blit(self.font.render(
            f"Done", 1, (255, 255, 255)), (225, 395 + 10))
        window.blit(self.font.render(
            f"Place Tower: {pygame.key.name(SettingsMenu.placetowerkeybind).upper()}", 1, (255, 255, 255)), (130, 65 + 10))
        window.blit(self.font.render(
            f"Select Light T: {pygame.key.name(SettingsMenu.selectlighttowerkeybind).upper()}", 1, (255, 255, 255)), (130, 120 + 10))
        window.blit(self.font.render(
            f"Select Fireball T: {pygame.key.name(SettingsMenu.selectfireballtowerkeybind).upper()}", 1, (255, 255, 255)), (130, 175 + 10))
        window.blit(self.font.render(
            f"Select Lightning T: {pygame.key.name(SettingsMenu.selectlightningtowerkeybind).upper()}", 1, (255, 255, 255)), (130, 230 + 10))
        window.blit(self.font.render(
            f"Select Poison T: {pygame.key.name(SettingsMenu.selectpoisontowerkeybind).upper()}", 1, (255, 255, 255)), (130, 285 + 10))
        window.blit(self.font.render(
            f"Pause Game: {pygame.key.name(SettingsMenu.pausegamekeybind).upper()}", 1, (255, 255, 255)), (130, 340 + 10))
        window.blit(self.font.render(
            f"Select Light P: {pygame.key.name(SettingsMenu.selectlightprojectilekeybind).upper()}", 1, (255, 255, 255)), (505, 65 + 10))
        window.blit(self.font.render(
            f"Select Fireball P: {pygame.key.name(SettingsMenu.selectfireballprojectilekeybind).upper()}", 1, (255, 255, 255)), (505, 120 + 10))
        window.blit(self.font.render(
            f"Select Lightning P: {pygame.key.name(SettingsMenu.selectlightningprojectilekeybind).upper()}", 1, (255, 255, 255)), (505, 175 + 10))
        window.blit(self.font.render(
            f"Select Poison P: {pygame.key.name(SettingsMenu.selectpoisoncloudprojectilekeybind).upper()}", 1, (255, 255, 255)), (505, 230 + 10))
        window.blit(self.font.render(
            f"Select Holy Strike: {pygame.key.name(SettingsMenu.selectholystrikeprojectilekeybind).upper()}", 1, (255, 255, 255)), (505, 285 + 10))
        window.blit(self.font.render(
            f"Open Shop: {pygame.key.name(SettingsMenu.openshopkeybind).upper()}", 1, (255, 255, 255)), (505, 340 + 10))
        if SettingsMenu.gameDifficulty == 1:
          window.blit(self.gameDifficultyFont.render(f"{SettingsMenu.gameDifficultyText[SettingsMenu.gameDifficulty]}", 1, (255, 255, 255)), (580, 395))
        elif SettingsMenu.gameDifficulty == 2:
          window.blit(self.gameDifficultyFont.render(f"{SettingsMenu.gameDifficultyText[SettingsMenu.gameDifficulty]}", 1, (255, 255, 255)), (550, 395))
        elif SettingsMenu.gameDifficulty == 3:
          window.blit(self.gameDifficultyFont.render(f"{SettingsMenu.gameDifficultyText[SettingsMenu.gameDifficulty]}", 1, (255, 255, 255)), (580, 395))