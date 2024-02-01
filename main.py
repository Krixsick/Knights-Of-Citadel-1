# -*- coding: utf-8 -*-

"""
Knights of the Citadel
Version 1.0.0

This game combines elements of tower defense, real-time strategy, and projectile-based combat, challenging players to strategically use different projectiles and defense towers to protect their main tower from incoming waves of enemies.

Written in Python version 3.10.8
Written in Pygame version 2.1.2

Compatible with Python version 3.10.0 +
Compatible with Pygame version 2.1.0 +

Created on March 1, 2023
Last Updated June 5, 2023

@authors: Chris Pop, Hamza Elsayed, Linus Gao

Chris's Contributions:
    Defense Towers - Logic, Rendering (main.py, defenseTower.py)
    Enemies - Difficulty, Waves (main.py)
    Entity Handler - Logic (main.py, entityHandler.py)
    Projectiles - Logic, Rendering, UI Display (main.py, projectile.py)
    Settings - Audio, Keybinds (main.py, config.ini, settingsmenu.py)
    Shop - Balancing, Rendering (main.py, shopmenu.py)

Hamza's Contributions:
    Buttons - Logic, Rendering (button.py)
    Menus - Logic, Rendering (main.py, confirmationmenu.py, creditsmenu.py,mainmenu.py, menu.py, pausemenu.py, settingsmenu.py)
    Settings - Audio, File, Keybinds, Loading, Logic, Saving (main.py, config.ini, settingsmenu.py)
    Shop - Logic, Rendering (main.py, shopmenu.py)
    Widgets - Logic, Rendering (widget.py)

Linus's Contributions:
    Boss Enemy - Difficulty, Healthbars, Hitboxes, Logic, Pathing, Rendering, Spawning (main.py, boss.py, enemy.py)
    Enemies - Difficulty, Healthbars, Hitboxes, Logic, Pathing, Rendering, Waves (main.py, enemy.py)
    Projectiles - Hitbox, Logic (main.py, projectile.py)
    Tower - Healthbar, Hitbox (main.py, tower.py)

External Credits:
    Jem Parekh - Soundtrack

ALL VISUAL MEDIA, SOUND EFFECTS, AND SPRITES WERE TAKEN FROM FREE LICENSES AS SEEN BELOW:
    SFX - Mixkit | Mixkit Sound Effects Free License | https://mixkit.co/
    Sprites - Open Game Art | Free License | https://opengameart.org/
"""

# Import Libraries
import pygame
import sys
import random
import math
import os
import time
import initialization
import game
from pygame.locals import *
from projectile import Projectile
from entityHandler import entities, Entity
from enemy import Enemy
from tower import *
from defenseTower import AutomatedDefenseTower
from confirmationmenu import ConfirmationMenu
from creditsmenu import CreditsMenu
from mainmenu import MainMenu
from pausemenu import PauseMenu
from shopmenu import ShopMenu
from settingsmenu import SettingsMenu
from menu import Menu
from boss import Boss
from configparser import ConfigParser
from initialization import window


# Initialize Menu Variables
MainMenu(True, window)  # Pos 0
SettingsMenu(False, window)  # Pos 1
CreditsMenu(False, window)  # Pos 2
ShopMenu(False, window)  # Pos 3
PauseMenu(False, window)  # Pos 4
ConfirmationMenu(False, window) # Pos 5
 
# Begin Game
SettingsMenu.reloadConfig()
MainMenu.returnToMainMenu()
game.mainGame(window)