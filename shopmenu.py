import pygame
from widget import Widget
from button import Button
from menu import Menu
from initialization import window

def upgradeLightBullet():
    """
    Upgrades the light bullet if the upgrade conditions are met.
    """
    if (ShopMenu.lightBulletLevel < len(ShopMenu.lightBulletLevelCosts)) and (ShopMenu.currency >= ShopMenu.lightBulletLevelCosts[ShopMenu.lightBulletLevel]):
        ShopMenu.currency -= ShopMenu.lightBulletLevelCosts[ShopMenu.lightBulletLevel]
        ShopMenu.lightBulletLevel += 1

def upgradeFireballBullet():
    """
    Upgrades the fireball bullet if the upgrade conditions are met.
    """
    if (ShopMenu.fireballBulletLevel < len(ShopMenu.fireballBulletLevelCosts)) and (ShopMenu.currency >= ShopMenu.fireballBulletLevelCosts[ShopMenu.fireballBulletLevel]):
        ShopMenu.currency -= ShopMenu.fireballBulletLevelCosts[ShopMenu.fireballBulletLevel]
        ShopMenu.fireballBulletLevel += 1
                
def upgradeLightningBullet():
    """
    Upgrades the lightning bullet if the upgrade conditions are met.
    """
    if (ShopMenu.lightningBulletLevel < len(ShopMenu.lightningBulletLevelCosts)) and (ShopMenu.currency >= ShopMenu.lightningBulletLevelCosts[ShopMenu.lightningBulletLevel]):
        ShopMenu.currency -= ShopMenu.lightningBulletLevelCosts[ShopMenu.lightningBulletLevel]
        ShopMenu.lightningBulletLevel += 1
                
def upgradePoisonCloudBullet():
    """
    Upgrades the poison cloud bullet if the upgrade conditions are met.
    """
    if (ShopMenu.poisonBulletLevel < len(ShopMenu.poisonBulletLevelCosts)) and (ShopMenu.currency >= ShopMenu.poisonBulletLevelCosts[ShopMenu.poisonBulletLevel]):
        ShopMenu.currency -= ShopMenu.poisonBulletLevelCosts[ShopMenu.poisonBulletLevel]
        ShopMenu.poisonBulletLevel += 1
                
def upgradeHolyStrikeBullet():
    """
    Upgrades the holy strike bullet if the upgrade conditions are met.
    """
    if (ShopMenu.holyStrikeBulletLevel < len(ShopMenu.holyStrikeBulletLevelCosts)) and (ShopMenu.currency >= ShopMenu.holyStrikeBulletLevelCosts[ShopMenu.holyStrikeBulletLevel]):
        ShopMenu.currency -= ShopMenu.holyStrikeBulletLevelCosts[ShopMenu.holyStrikeBulletLevel]
        ShopMenu.holyStrikeBulletLevel += 1


def upgradeLightTower():
    """
    Upgrades the light tower if the upgrade conditions are met.
    """
    if (ShopMenu.lightTowerLevel < len(ShopMenu.lightTowerLevelCosts)) and (ShopMenu.currency >= ShopMenu.lightTowerLevelCosts[ShopMenu.lightTowerLevel]):
        ShopMenu.currency -= ShopMenu.lightTowerLevelCosts[ShopMenu.lightTowerLevel]
        ShopMenu.lightTowerLevel += 1

def upgradeFireballTower():
    """
    Upgrades the fireball tower if the upgrade conditions are met.
    """
    if (ShopMenu.fireballTowerLevel < len(ShopMenu.fireballTowerLevelCosts)) and (ShopMenu.currency >= ShopMenu.fireballTowerLevelCosts[ShopMenu.fireballTowerLevel]):
        ShopMenu.currency -= ShopMenu.fireballTowerLevelCosts[ShopMenu.fireballTowerLevel]
        ShopMenu.fireballTowerLevel += 1
                
def upgradeLightningTower():
    """
    Upgrades the lightning tower if the upgrade conditions are met.
    """
    if (ShopMenu.lightningTowerLevel < len(ShopMenu.lightningTowerLevelCosts)) and (ShopMenu.currency >= ShopMenu.lightningTowerLevelCosts[ShopMenu.lightningTowerLevel]):
        ShopMenu.currency -= ShopMenu.lightningTowerLevelCosts[ShopMenu.lightningTowerLevel]
        ShopMenu.lightningTowerLevel += 1
                
def upgradePoisonCloudTower():
    """
    Upgrades the poison cloud tower if the upgrade conditions are met.
    """
    if (ShopMenu.poisonTowerLevel < len(ShopMenu.poisonTowerLevelCosts)) and (ShopMenu.currency >= ShopMenu.poisonTowerLevelCosts[ShopMenu.poisonTowerLevel]):
        ShopMenu.currency -= ShopMenu.poisonTowerLevelCosts[ShopMenu.poisonTowerLevel]
        ShopMenu.poisonTowerLevel += 1


def purchaseLightTower():
    """
    Purchases the light tower if the player has enough currency.
    """
    if ShopMenu.currency >= ShopMenu.lightTowerCost:
        ShopMenu.currency -= ShopMenu.lightTowerCost
        ShopMenu.lightTowerCount += 1


def purchaseFireballTower():
    """
    Purchases the fireball tower if the player has enough currency.
    """
    if ShopMenu.currency >= ShopMenu.fireballTowerCost:
        ShopMenu.currency -= ShopMenu.fireballTowerCost
        ShopMenu.fireballTowerCount += 1

                
def purchaseLightningTower():
    """
    Purchases the lightning tower if the player has enough currency.
    """
    if ShopMenu.currency >= ShopMenu.lightningTowerCost:
        ShopMenu.currency -= ShopMenu.lightningTowerCost
        ShopMenu.lightningTowerCount += 1

                
def purchasePoisonCloudTower():
    """
    Purchases the poison cloud tower if the player has enough currency.
    """
    if ShopMenu.currency >= ShopMenu.poisonTowerCost:
        ShopMenu.currency -= ShopMenu.poisonTowerCost
        ShopMenu.poisonTowerCount += 1

          

class ShopMenu(Menu):
  '''
    Class representing the shop menu in the game.
  '''
  currency = 0

  # Tower Count
  lightTowerCount = 0
  fireballTowerCount = 0
  lightningTowerCount = 0
  poisonTowerCount = 0
  
  # Level Variables
  lightBulletLevel = 1
  fireballBulletLevel = 0
  lightningBulletLevel = 0
  poisonBulletLevel = 0
  holyStrikeBulletLevel = 0
  lightTowerLevel = 1
  fireballTowerLevel = 1
  lightningTowerLevel = 1
  poisonTowerLevel = 1

  # Cost
  lightBulletLevelCosts = [0, 150, 400, 900, 2000, float('inf')]
  fireballBulletLevelCosts = [200, 550, 1200, 2500, float('inf')]
  lightningBulletLevelCosts = [650, 1500, 2800, 4000, float('inf')]
  poisonBulletLevelCosts = [1500, 4000, 10000, 20000, float('inf')]
  holyStrikeBulletLevelCosts = [15000, float('inf')]
  lightTowerCost = 300
  fireballTowerCost = 550
  lightningTowerCost = 2000
  poisonTowerCost = 3000
  lightTowerLevelCosts = [0, 120, 250, 500, 750, float('inf')]
  fireballTowerLevelCosts = [0, 300, 500, 1000, 2000, float('inf')]
  lightningTowerLevelCosts = [0, 400, 650, 1100, 2500, float('inf')]
  poisonTowerLevelCosts = [0, 1200, 4200, 11000, 23000, float('inf')]
  
  
  def __init__(self, _visible, _parentUI):
    '''
    Initializes the ShopMenu object.

    Parameters:
    _visible (bool): Flag indicating whether the menu is visible.
    _parentUI (pygame.Surface): The parent surface containing the menu.

    '''
    super().__init__(_visible, _parentUI)
    self.shopBackground = Widget("Assets/UI/shopmenu.png", self.parent, 100, 25)
    self.costFont = pygame.font.SysFont('Times New Roman', 20)
    self.levelFont = pygame.font.SysFont('Times New Roman', 40)
    
    self.lightTower = Widget("Assets/Tower/blue_defense_tower.png", self.parent, 130, 55, 0.15, 0.15)
    self.upgradeLightTower = Button(upgradeLightTower, "Assets/UI/upgradebutton.png", self.parent, 215, 85)
    self.purchaseLightTower = Button(purchaseLightTower, "Assets/UI/purchasebutton.png", self.parent, 215, 109 + 15)
    
    self.fireBallTower = Widget("Assets/Tower/red_defense_tower.png", self.parent, 130, 135, 0.15, 0.15)
    self.upgradeFireballTower = Button(upgradeFireballTower, "Assets/UI/upgradebutton.png", self.parent, 215, 165)
    self.purchaseFireballTower = Button(purchaseFireballTower, "Assets/UI/purchasebutton.png", self.parent, 215, 189 + 15)
    
    self.lightningTower = Widget("Assets/Tower/purple_defense_tower.png", self.parent, 130, 215, 0.15, 0.15)
    self.upgradeLightningTower = Button(upgradeLightningTower, "Assets/UI/upgradebutton.png", self.parent, 215, 245)
    self.purchaseLightningTower = Button(purchaseLightningTower, "Assets/UI/purchasebutton.png", self.parent, 215, 269 + 15)
    
    self.poisonTower = Widget("Assets/Tower/green_defense_tower.png", self.parent, 130, 295, 0.15, 0.15)
    self.upgradePoisonTower = Button(upgradePoisonCloudTower, "Assets/UI/upgradebutton.png", self.parent, 215, 325)
    self.purchasePoisonTower = Button(purchasePoisonCloudTower, "Assets/UI/purchasebutton.png", self.parent, 215, 349 + 15)
    
    self.spell0 = Widget("Assets/UI/zz_lightBulletUIDisplay.png", self.parent, 430 + 80, 80, 0.25, 0.25)
    self.purchaseSpell0 = Button(upgradeLightBullet, "Assets/UI/upgradebutton.png", self.parent, 490 + 80, 80)
    
    self.spell1 = Widget("Assets/UI/zz_fireballBulletUIDisplay.png", self.parent, 430 + 80, 140, 0.25, 0.25)
    self.purchaseSpell1 = Button(upgradeFireballBullet, "Assets/UI/upgradebutton.png", self.parent, 490 + 80, 140)
    
    self.spell2 = Widget("Assets/UI/zz_lightningBulletUIDisplay.png", self.parent, 430 + 80, 200, 0.25, 0.25)
    self.purchaseSpell2 = Button(upgradeLightningBullet, "Assets/UI/upgradebutton.png", self.parent, 490 + 80, 200)
    
    self.spell3 = Widget("Assets/UI/zz_poisonCloudBulletUIDisplay.png", self.parent, 430 + 80, 260, 0.25, 0.25)
    self.purchaseSpell3 = Button(upgradePoisonCloudBullet, "Assets/UI/upgradebutton.png", self.parent, 490 + 80, 260)
    
    self.spell4 = Widget("Assets/UI/zz_holyStrikeBulletUIDisplay.png", self.parent, 430 + 80, 320, 0.25, 0.25)
    self.purchaseSpell4 = Button(upgradeHolyStrikeBullet, "Assets/UI/upgradebutton.png", self.parent, 490 + 80, 320)
    
    self.uiElements.append(self.shopBackground)
    self.uiElements.append(self.lightTower)
    self.uiElements.append(self.upgradeLightTower)
    self.uiElements.append(self.purchaseLightTower)
    self.uiElements.append(self.fireBallTower)
    self.uiElements.append(self.upgradeFireballTower)
    self.uiElements.append(self.purchaseFireballTower)
    self.uiElements.append(self.lightningTower)
    self.uiElements.append(self.upgradeLightningTower)
    self.uiElements.append(self.purchaseLightningTower)
    self.uiElements.append(self.poisonTower)
    self.uiElements.append(self.upgradePoisonTower)
    self.uiElements.append(self.purchasePoisonTower)
    self.uiElements.append(self.spell0)
    self.uiElements.append(self.purchaseSpell0)
    self.uiElements.append(self.spell1)
    self.uiElements.append(self.purchaseSpell1)
    self.uiElements.append(self.spell2)
    self.uiElements.append(self.purchaseSpell2)
    self.uiElements.append(self.spell3)
    self.uiElements.append(self.purchaseSpell3)
    self.uiElements.append(self.spell4)
    self.uiElements.append(self.purchaseSpell4)
    Menu.objects.append(self)
    
  def update(self):
    '''
    Updates the display in the shop menu.

    Returns:
    None
    '''
    for uiElement in self.uiElements:
      uiElement.update()

    window.blit(self.costFont.render(f"{ShopMenu.lightTowerLevel}", 1, (255, 255, 255)), (130 + 22, 55 + 22))
    window.blit(self.costFont.render(f"{ShopMenu.fireballTowerLevel}", 1, (255, 255, 255)), (130 + 22, 135 + 22))
    window.blit(self.costFont.render(f"{ShopMenu.lightningTowerLevel}", 1, (255, 255, 255)), (130 + 22, 215 + 22))
    window.blit(self.costFont.render(f"{ShopMenu.poisonTowerLevel}", 1, (255, 255, 255)), (130 + 22, 295 + 22))

    window.blit(self.costFont.render(f"{ShopMenu.lightTowerCount}", 1, (255, 255, 255)), (130 + 22, 55 + 22 + 55))
    window.blit(self.costFont.render(f"{ShopMenu.fireballTowerCount}", 1, (255, 255, 255)), (130 + 22, 135 + 22 + 55))
    window.blit(self.costFont.render(f"{ShopMenu.lightningTowerCount}", 1, (255, 255, 255)), (130 + 22, 215 + 22 + 55))
    window.blit(self.costFont.render(f"{ShopMenu.poisonTowerCount}", 1, (255, 255, 255)), (130 + 22, 295 + 22 + 55))

    window.blit(self.costFont.render(f"{ShopMenu.lightBulletLevel}", 1, (255, 255, 255)), (430 + 80 - 10, 80 - 10))
    window.blit(self.costFont.render(f"{ShopMenu.fireballBulletLevel}", 1, (255, 255, 255)), (430 + 80 - 10, 140 - 10))
    window.blit(self.costFont.render(f"{ShopMenu.lightningBulletLevel}", 1, (255, 255, 255)), (430 + 80 - 10, 200 - 10))
    window.blit(self.costFont.render(f"{ShopMenu.poisonBulletLevel}", 1, (255, 255, 255)), (430 + 80 - 10, 260 - 10))
    window.blit(self.costFont.render(f"{ShopMenu.holyStrikeBulletLevel}", 1, (255, 255, 255)), (430 + 80 - 10, 320 - 10))
    
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.lightTowerCost}", 1, (255, 200, 0)), (285 + 72, 109 + 15))
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.fireballTowerCost}", 1, (255, 200, 0)), (285 + 72, 189 + 15))
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.lightningTowerCost}", 1, (255, 200, 0)), (285 + 72, 269 + 15))
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.poisonTowerCost}", 1, (255, 200, 0)), (285 + 72, 349 + 15))
    
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.lightTowerLevelCosts[ShopMenu.lightTowerLevel]}", 1, (255, 200, 0)), (285 + 72, 85))
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.fireballTowerLevelCosts[ShopMenu.fireballTowerLevel]}", 1, (255, 200, 0)), (285 + 72, 165))
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.lightningTowerLevelCosts[ShopMenu.lightningTowerLevel]}", 1, (255, 200, 0)), (285 + 72, 245))
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.poisonTowerLevelCosts[ShopMenu.poisonTowerLevel]}", 1, (255, 200, 0)), (285 + 72, 325))
    
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.lightBulletLevelCosts[ShopMenu.lightBulletLevel]}", 1, (255, 200, 0)), (510 + 80, 110))
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.fireballBulletLevelCosts[ShopMenu.fireballBulletLevel]}", 1, (255, 200, 0)), (510 + 80, 170))
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.lightningBulletLevelCosts[ShopMenu.lightningBulletLevel]}", 1, (255, 200, 0)), (510 + 80, 230))
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.poisonBulletLevelCosts[ShopMenu.poisonBulletLevel]}", 1, (255, 200, 0)), (510 + 80, 290))
    window.blit(self.costFont.render(f"Cost: ${ShopMenu.holyStrikeBulletLevelCosts[ShopMenu.holyStrikeBulletLevel]}", 1, (255, 200, 0)), (510 + 80, 350))