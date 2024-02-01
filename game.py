#Importing all the modules and libraries 
import pygame
import sys
import random
import math
import os
import time
from pygame.locals import *
from projectile import Projectile
from entityHandler import entities, Entity
from enemy import Enemy
from tower import *
from defenseTower import AutomatedDefenseTower
from mainmenu import MainMenu
from pausemenu import PauseMenu
from shopmenu import ShopMenu
from settingsmenu import SettingsMenu
from menu import Menu
from boss import Boss

def mainGame(window):
  '''
    Main game portion.

    Parameters
    ----------
    window : SURFACE
        Surface to display game on.

    Returns
    -------
    None.

  '''
  asset_background_image = pygame.image.load('Assets/Tower/towerdefensebackground.jpg')
  background_image = pygame.transform.scale(asset_background_image, (900, 500))
  clock = pygame.time.Clock()
  offset_x, offset_y = 0, 0
  font = pygame.font.Font(None, 36)
  
  # Initialize Enemy Variables and Media
  wave = 0
  
  dragging = False
  enemies = []
  enemy_hit_sound = pygame.mixer.Sound('Assets/SFX/enemy_impact.wav')
  difficultyLevel = 2  # SET DIFFICULTY LEVEL IN SETTINGS MENU
  waveTimeEnded = 0
  spawningFrequencyDelay = 0
  enemyLoopIterator = 0
  detectingNewWave = 1
  renderTimeToNewWave = False
  
  # Initialize Projectile Variables and Media
  projectiles = []
  projectileList = ["lightBullet", "fireBall", "lightningBolt", "poisonCloud", "holyStrike"]

  
  #Projectile Type, each number represents a new projectile from 0-4
  projectileType = 0
  projectileDisplayDelay = 0
  bulletLevelsList = [ShopMenu.lightBulletLevel, ShopMenu.fireballBulletLevel, ShopMenu.lightningBulletLevel, ShopMenu.poisonBulletLevel, ShopMenu.holyStrikeBulletLevel]
  fireballBulletUsed = 0
  lightningBoltUsed = 0
  poisonCloudUsed = 0
  holyStrikeUsed = 0
  firedProjectileList = [0, fireballBulletUsed, lightningBoltUsed, poisonCloudUsed, holyStrikeUsed]
  projectileRegenTime= [1, 2500, 6000, 12000, 30000]
  
  #Loads image of the different types of projectiles and loads the sprite images of the projectiles
  light_bullet_image = pygame.transform.scale(
    pygame.image.load('Assets/Bullets/light_bullet.png'), (10, 10))
  fireball_bullet = [pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_1.png'), (40, 40)), pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_2.png'), (40, 40)), pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_3.png'), (
      40, 40)), pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_4.png'), (40, 40)), pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_5.png'), (40, 40)), pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_6.png'), (40, 40))]
  poison_cloud_bullet = pygame.transform.scale(pygame.image.load('Assets/Bullets/poison_cloud.png'), (150, 60))
  lightning_bolt_bullet = pygame.transform.scale(
      pygame.image.load('Assets/Bullets/lightning_bolt.png'), (600, 10))
  holy_strike_bullet = pygame.transform.scale(pygame.image.load(
      'Assets/Bullets/holy_strike_overlay.png'), (3000, 3000))
  
  #Loads UI images for selecting and using projectiles
  light_bullet_ui_display = pygame.transform.scale(pygame.image.load('Assets/UI/zz_lightBulletUIDisplay.png'), (50, 50))
  fireball_bullet_ui_display = pygame.transform.scale(pygame.image.load('Assets/UI/zz_fireballBulletUIDisplay.png'), (50, 50))
  lightning_bolt_bullet_ui_display = pygame.transform.scale(pygame.image.load('Assets/UI/zz_lightningBulletUIDisplay.png'), (50, 50))
  poison_cloud_bullet_ui_display = pygame.transform.scale(pygame.image.load('Assets/UI/zz_poisonCloudBulletUIDisplay.png'), (50, 50))
  holy_strike_bullet_ui_display = pygame.transform.scale(pygame.image.load('Assets/UI/zz_holyStrikeBulletUIDisplay.png'), (50, 50))
  projectileUIDisplayList = [light_bullet_ui_display, fireball_bullet_ui_display, lightning_bolt_bullet_ui_display, poison_cloud_bullet_ui_display, holy_strike_bullet_ui_display]
  
  #Loads the sounds for all the projectiles
  light_bullet_sound = pygame.mixer.Sound('Assets/SFX/light_bullet_cast.wav')
  fireball_bullet_sound = pygame.mixer.Sound('Assets/SFX/fireball_cast.wav')
  lightning_bullet_sound = pygame.mixer.Sound('Assets/SFX/lightning_cast.wav')
  poison_cloud_bullet_sound = pygame.mixer.Sound(
      'Assets/SFX/poison_cloud_cast.wav')
  holy_strike_sound = pygame.mixer.Sound('Assets/SFX/holy_strike_cast.wav')
  
  
  # Initialize Tower Defense Variables and Media
  displayDefenseTowerOverlay = False
  defenseTowers = []
  overlay_light_tower_image = pygame.transform.scale(
      pygame.image.load('Assets/Tower/o_blue_defense_tower.png').convert_alpha(), (85, 95))
  overlay_fireball_tower_image = pygame.transform.scale(
      pygame.image.load('Assets/Tower/o_red_defense_tower.png').convert_alpha(), (85, 95))
  overlay_poison_tower_image = pygame.transform.scale(
      pygame.image.load('Assets/Tower/o_green_defense_tower.png').convert_alpha(), (85, 95))
  overlay_lightning_tower_image = pygame.transform.scale(
      pygame.image.load('Assets/Tower/o_purple_defense_tower.png').convert_alpha(), (85, 95))
  o_towerList = [overlay_light_tower_image, overlay_fireball_tower_image,
                 overlay_lightning_tower_image, overlay_poison_tower_image]
  light_tower_image = pygame.transform.scale(
      pygame.image.load('Assets/Tower/blue_defense_tower.png').convert_alpha(), (85, 95))
  fireball_tower_image = pygame.transform.scale(
      pygame.image.load('Assets/Tower/red_defense_tower.png').convert_alpha(), (85, 95))
  poison_tower_image = pygame.transform.scale(
      pygame.image.load('Assets/Tower/green_defense_tower.png').convert_alpha(), (85, 95))
  lightning_tower_image = pygame.transform.scale(
      pygame.image.load('Assets/Tower/purple_defense_tower.png').convert_alpha(), (85, 95))
  towerList = [light_tower_image, fireball_tower_image,
               lightning_tower_image, poison_tower_image]
  defenseTowersDelays = [2500, 4000, 8000, 15000]
  towerType = 0
  
  canPlace = True
  locked_icon = pygame.transform.scale(pygame.image.load('Assets/UI/zz_lockedIcon.png'), (40,40))
  textBoxUIDisplay = pygame.transform.scale(pygame.image.load('Assets/UI/zz_emptyButton.png'), (120,30))
  pause_icon = pygame.transform.scale(pygame.image.load('Assets/UI/zz_pauseIcon.png'), (40,40))
  shop_icon = pygame.transform.scale(pygame.image.load('Assets/UI/zz_shopIcon.png'), (80,80))
  
  
  # Initialize Main Tower Variables and Media
  tower_health = 100
  tower_position = pygame.Rect(430, 168, 100, 82)
  castle_image = pygame.transform.scale(pygame.image.load('Assets/Tower/tower.png'), (85, 130))
  castle = Entity(castle_image, 100, True)

  pygame.mixer.init()
  pygame.mixer.music.load("Assets/last_stand.wav")
  pygame.mixer.music.play(-1)
  
  runGame = True
  while runGame:
      if MainMenu.mainMenuActive:
        break
      mouseX, mouseY = pygame.mouse.get_pos()
      try:
          mouseAngle = math.atan2((mouseY - 190), (mouseX - 430))
      except ZeroDivisionError:
          mouseAngle = math.atan2((mouseY - 190), (mouseX - 429))
      tickEvents = pygame.event.get()
      for event in tickEvents:
        if (event.type == pygame.KEYDOWN and event.key == SettingsMenu.pausegamekeybind) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseX >= 850 and mouseX <= 890 and mouseY >= 10 and mouseY <= 50):
          waveTimeEnded = pygame.time.get_ticks()
          if Menu.objects[4].visible:
            Menu.paused = False
            Menu.objects[4].visible = False
          else:
            Menu.paused = True
            Menu.objects[4].visible = True
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_m) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseX >= 5 and mouseX <= 85 and mouseY >= 415 and mouseY <= 495):
          if Menu.objects[3].visible:
            Menu.objects[3].visible = False
          else:
            Menu.objects[3].visible = True     
        SettingsMenu.bind(event, window)

      if Menu.paused:
        waveTimeEnded = pygame.time.get_ticks()

      else:
        # Draw window and tower and tower healthbar
        window.fill((0, 0, 0))
        window.blit(background_image, (0, 0))
        window.blit(castle_image, (385, 168))
        draw_tower(window, tower_health)

        for enemy in enemies:
            # After updating all enemies, redraw the tower with the updated health bar
            tower_health = collides_with_enemy(enemy, tower_position, tower_health)
        if tower_health <= 0:  # Tower destroyed, end the game
            MainMenu.gameOver = True
            draw_tower(window, tower_health)
            Menu.paused = True
            Menu.objects[4].visible = True  # CHANGE TO AN END SCREEN WITH HIGHSCORE AND RETURN TO MAIN MENU
            
        for event in tickEvents:  # Detect Events
            if event.type == pygame.QUIT:  # Exit the game loop or perform necessary actions to end the game
                runGame = False
                break
            if event.type == pygame.KEYDOWN:
              if event.key == SettingsMenu.pausegamekeybind:
                PauseMenu.activateMenu(PauseMenu)
  
            if event.type == pygame.MOUSEBUTTONDOWN:
              if event.button == 1:  # Left mouse button
                  if window.get_rect().collidepoint(event.pos):  # Check if mouse is over the window
                      dragging = True
                      mouse_x, mouse_y = event.pos
                      offset_x = mouse_x - window.get_rect().x
                      offset_y = mouse_y - window.get_rect().y
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    dragging = False
                  
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_x, mouse_y = event.pos
                    window_rect = window.get_rect()
                    window_rect.x = mouse_x - offset_x
                    window_rect.y = mouse_y - offset_y
  
          
            if event.type == pygame.KEYDOWN and event.key == SettingsMenu.pausegamekeybind:
                PauseMenu.activateMenu(PauseMenu)
    
            # Switch between projectiles with key (default: r)
            if event.type == pygame.KEYDOWN and event.key == SettingsMenu.switchprojectilekeybind:
                projectileType += 1
                projectileType = 0 if projectileType > 4 else projectileType
                while bulletLevelsList[projectileType] == 0:
                    projectileType += 1
                    projectileType = 0 if projectileType > 4 else projectileType
          
            if event.type == pygame.KEYDOWN:  # Detect when a key is pressed
                # Change the tower type while the overlay is being shown
                if event.key in [SettingsMenu.selectlightprojectilekeybind, SettingsMenu.selectfireballprojectilekeybind, SettingsMenu.selectlightningprojectilekeybind, SettingsMenu.selectpoisoncloudprojectilekeybind, SettingsMenu.selectholystrikeprojectilekeybind]:
                    match event.key:
                        case SettingsMenu.selectlightprojectilekeybind:
                            projectileType = 0
                          
                        case SettingsMenu.selectfireballprojectilekeybind:
                            projectileType = 1
                            while bulletLevelsList[projectileType] == 0:
                                projectileType += 1
                                projectileType = 0 if projectileType > 4 else projectileType
                          
                        case SettingsMenu.selectlightningprojectilekeybind:
                            projectileType = 2
                            while bulletLevelsList[projectileType] == 0:
                                projectileType += 1
                                projectileType = 0 if projectileType > 4 else projectileType
                          
                        case SettingsMenu.selectpoisoncloudprojectilekeybind:
                            projectileType = 3
                            while bulletLevelsList[projectileType] == 0:
                                projectileType += 1
                                projectileType = 0 if projectileType > 4 else projectileType
                          
                        case SettingsMenu.selectholystrikeprojectilekeybind:
                            projectileType = 4
                            while bulletLevelsList[projectileType] == 0:
                                projectileType += 1
                                projectileType = 0 if projectileType > 4 else projectileType
  
          
            # Switch between defense tower types with key (default: t)
            if event.type == pygame.KEYDOWN and event.key == SettingsMenu.placetowerkeybind:
                if displayDefenseTowerOverlay and canPlace and towerCounts[towerType] > 0.5:
                    # Add a new defense tower if the overlay is already being displayed so the players knows where it is being placed
                    newAutoDT = AutomatedDefenseTower(
                        mouseX - 40, mouseY - 50, projectileList[towerType], towerList[towerType], defenseTowersDelays[towerType])
                    defenseTowers.append(newAutoDT)
                    displayDefenseTowerOverlay = False
                    if towerType == 0:
                        ShopMenu.lightTowerCount -= 1
                    elif towerType == 1:
                        ShopMenu.fireballTowerCount -= 1
                    elif towerType == 2:
                        ShopMenu.lightningTowerCount -= 1
                    else:
                        ShopMenu.poisonTowerCount -= 1
                    
                elif ShopMenu.lightTowerCount or ShopMenu.fireballTowerCount or ShopMenu.lightningTowerCount or ShopMenu.poisonTowerCount:  # If not currently displaying overlay, display an overlay so the player knows where the tower will be placed
                    displayDefenseTowerOverlay = True
                    if ShopMenu.lightTowerCount != 0:
                        towerType = 0
                      
                    elif ShopMenu.fireballTowerCount != 0:
                        towerType = 1
                      
                    elif ShopMenu.lightningTowerCount != 0:
                        towerType = 2
                      
                    elif ShopMenu.poisonTowerCount != 0:
                        towerType = 3
                      
                    else:
                        displayDefenseTowerOverlay = False
                    
    
            if event.type == pygame.KEYDOWN:  # Detect when a key is pressed
                # Change the tower type while the overlay is being shown
                if event.key in [SettingsMenu.selectlighttowerkeybind, SettingsMenu.selectfireballtowerkeybind, SettingsMenu.selectlightningtowerkeybind, SettingsMenu.selectpoisontowerkeybind] and displayDefenseTowerOverlay:
                    if ShopMenu.lightTowerCount != 0:
                        towerType = 0
                      
                    elif ShopMenu.fireballTowerCount != 0:
                        towerType = 1
                      
                    elif ShopMenu.lightningTowerCount != 0:
                        towerType = 2
                      
                    elif ShopMenu.poisonTowerCount != 0:
                        towerType = 3
                      
                    else:
                        displayDefenseTowerOverlay = False

                  
                    match event.key:
                        case SettingsMenu.selectlighttowerkeybind:
                            if ShopMenu.lightTowerCount > 0:
                                towerType = 0
                              
                        case SettingsMenu.selectfireballtowerkeybind:
                            if ShopMenu.fireballTowerCount > 0:
                                towerType = 1
                              
                        case SettingsMenu.selectlightningtowerkeybind:
                            if ShopMenu.lightningTowerCount > 0:
                                towerType = 2
                              
                        case SettingsMenu.selectpoisontowerkeybind:
                            if ShopMenu.poisonTowerCount > 0:
                                towerType = 3
    
                # Fire selected projectile when key is pressed (default: SPACE)
                if event.key == SettingsMenu.firebulletkeybind:
                    pos = [430, 190]
                    posPlus = [math.cos(mouseAngle), math.sin(mouseAngle)]
                    vel = [math.cos(mouseAngle), math.sin(mouseAngle)]
    
                    match projectileList[projectileType]:
    
                        case "lightBullet":  # Fires low damage high speed small projectile
                            newProjectile = Projectile([p + 25*pPlus for p, pPlus in zip(pos, posPlus)], [
                                                       v * 10 for v in vel], 10, 10 * ShopMenu.lightBulletLevel, light_bullet_image)
                            pygame.mixer.Sound.play(light_bullet_sound)
                            projectiles.append(newProjectile)
    
                        case "fireBall":  # Fires medium damage medium speed small projectile
                            if (pygame.time.get_ticks() - fireballBulletUsed) > projectileRegenTime[1] and ShopMenu.fireballBulletLevel > 0:
                                newProjectile = Projectile([p + 25*pPlus for p, pPlus in zip(pos, posPlus)], [
                                                           v * 5 for v in vel], 11, 30 * ShopMenu.fireballBulletLevel, pygame.transform.scale(pygame.image.load('Assets/Bullets/fireball_frame_1.png'), (15, 15)), fireball_bullet)
                                pygame.mixer.Sound.play(fireball_bullet_sound)
                                fireballBulletUsed = pygame.time.get_ticks()
                                projectiles.append(newProjectile)
    
                        case "lightningBolt":  # Fires high damage instantaneous speed piercing projectile
                            print(ShopMenu.lightningBulletLevel)
                            if (pygame.time.get_ticks() - lightningBoltUsed) > projectileRegenTime[2] and ShopMenu.lightningBulletLevel > 0:
                                newProjectile = Projectile([p + 300*pPlus for p, pPlus in zip(pos, posPlus)], [
                                                           v * 1 for v in vel], 3, 12 * ShopMenu.lightningBulletLevel, lightning_bolt_bullet, None, mouseAngle)
                                pygame.mixer.Sound.play(lightning_bullet_sound)
                                lightningBoltUsed = pygame.time.get_ticks()
                                projectiles.append(newProjectile)
    
                        case "poisonCloud":  # Fires low damage low speed medium size piercing projectile
                             if (pygame.time.get_ticks() - poisonCloudUsed) > projectileRegenTime[3] and ShopMenu.poisonBulletLevel > 0:
                                newProjectile = Projectile([p + 25*pPlus for p, pPlus in zip(pos, posPlus)], [
                                                           v * 1 for v in vel], 15, 1 * ShopMenu.poisonBulletLevel, poison_cloud_bullet)
                                pygame.mixer.Sound.play(poison_cloud_bullet_sound)
                                poisonCloudUsed = pygame.time.get_ticks()
                                projectiles.append(newProjectile)
    
                        case "holyStrike":  # Fires large damage instantaneous speed mapwide mass effect projectile
                            if (pygame.time.get_ticks() - holyStrikeUsed) > projectileRegenTime[4] and ShopMenu.holyStrikeBulletLevel > 0:
                                newProjectile = Projectile([p + 0*pPlus for p, pPlus in zip(pos, posPlus)], [
                                                           v * 0.1 for v in vel], 99, 300 * ShopMenu.holyStrikeBulletLevel, holy_strike_bullet)
                                pygame.mixer.Sound.play(holy_strike_sound)
                                holyStrikeUsed = pygame.time.get_ticks()
                                projectiles.append(newProjectile)
    
                    
    
        # Logic for defense towers to periodically fire at enemies
        target_enemy = None
        for dTower in defenseTowers:
            # Check if the cooldown is up for the tower
            if (pygame.time.get_ticks() - dTower.last_spawn_time) % dTower.spawn_interval < 10:
                target_enemy = dTower.find_nearest_enemy(enemies)
                if target_enemy == None:
                    continue
                else:  # If target found, fire a projectile
                    # Initial variables which will be manipulated when summoning a projectile
                    projectileAngle = math.atan2(
                        (target_enemy[1] - dTower.y - 50), (target_enemy[0] - dTower.x - 40))
                    pos = [dTower.x + 40, dTower.y + 50]
                    posPlus = [math.cos(projectileAngle),
                               math.sin(projectileAngle)]
                    vel = [math.cos(projectileAngle), math.sin(projectileAngle)]
    
                    match dTower.projectileType:  # Match projectile type of the tower
                        case "lightBullet":
                            newProjectile = Projectile([p + 25*pPlus for p, pPlus in zip(pos, posPlus)], [
                                                       v * 5 for v in vel], 10, 25 * ShopMenu.lightTowerLevel, light_bullet_image)
                            pygame.mixer.Sound.play(light_bullet_sound)
    
                        case "fireBall":
                            newProjectile = Projectile([p + 25*pPlus for p, pPlus in zip(pos, posPlus)], [
                                                       v * 10 for v in vel], 11, 45 * ShopMenu.fireballTowerLevel, pygame.transform.scale(
                                pygame.image.load('Assets/Bullets/fireball_frame_1.png'), (15, 15)), fireball_bullet)
                            pygame.mixer.Sound.play(fireball_bullet_sound)
    
                        case "poisonCloud":
                            newProjectile = Projectile([p + 25*pPlus for p, pPlus in zip(pos, posPlus)], [
                                                       v * 2 for v in vel], 15, 1 * ShopMenu.poisonTowerLevel, poison_cloud_bullet)
                            pygame.mixer.Sound.play(poison_cloud_bullet_sound)
    
                        case "lightningBolt":
                            newProjectile = Projectile([p + 300*pPlus for p, pPlus in zip(pos, posPlus)], [
                                                       v * 1 for v in vel], 3, 8 * ShopMenu.lightningTowerLevel, lightning_bolt_bullet, None, projectileAngle)
                            pygame.mixer.Sound.play(lightning_bullet_sound)
    
                    projectiles.append(newProjectile)
    
    
        
        if len(enemies) == 0:
            renderTimeToNewWave = True
            if detectingNewWave > len(enemies): 
                waveTimeEnded = pygame.time.get_ticks()   
        else:
          renderTimeToNewWave = False
              
        if (pygame.time.get_ticks() - waveTimeEnded) > 10000 and len(enemies) == 0:
            tower_health += 10 if tower_health < 90 else 0
            wave += 1
            SettingsMenu.highScore = wave if wave > SettingsMenu.highScore else SettingsMenu.highScore
            ShopMenu.currency += 50
            enemyLoopIterator = 0
            waveTimeEnded = pygame.time.get_ticks()
        
        if (pygame.time.get_ticks() - spawningFrequencyDelay) > 1000:
            if enemyLoopIterator < (difficultyLevel * wave + 6):
                rand_nr = random.randint(0, 2)
                rand_pos = random.randint(0, 9)
                enemyDirections = ['right', 'left', 'left2']
                dictOfCoords = {'right': [[10,70], [5,75], [5, 80], [15, 85], [20, 90], [5, 95], [5,100], [10, 80], [10, 85], [10, 90]], 'left': [[880, 130],[880, 135],[880, 140],[880, 145],[880, 150],[875, 130],[875, 135],[875, 140],[875, 145],[875, 150]], 'left2':[[860, 380],[860, 385],[860, 390],[860, 395],[860, 400],[870, 400],[870, 405],[870, 410],[870, 415],[870, 420]]}
                newEnemy = Enemy(dictOfCoords[enemyDirections[rand_nr]][rand_pos][0], dictOfCoords[enemyDirections[rand_nr]][rand_pos][1], enemyDirections[rand_nr], 80 + 20 * wave)
                enemies.append(newEnemy)
                spawningFrequencyDelay = pygame.time.get_ticks()
                enemyLoopIterator += 1
                if (enemyLoopIterator == (difficultyLevel * wave + 6)) and ((wave - 1) % 5 == 0) and wave > 3:
                    bossEnemy = Boss(x=0, y=40, direction='left', health = 500 * wave / 5)  # Change the coordinates and direction as desired
                    bossEnemy.set_path()
                    enemies.append(bossEnemy)            
  
  
      # Update projectiles
        # Create a list to store projectiles that need to be removed
        projectiles_to_remove = []
    
        for projectile in projectiles:
            projectile.update()
    
            window.blit(projectile.image, projectile.displayRect)
            # Update enemies hit by a projectile
            hit_enemies = []
            for enemy in enemies:
                projectile.rect = [projectile.rect] if type(
                    projectile.rect) != list else projectile.rect
                for iterator in range(len(projectile.rect)):
                    # Check if the projectile is outside the screen
                    if not projectile.rect[iterator].colliderect(window.get_rect()):
                        projectiles_to_remove.append(projectile)
                        # Remove the projectile from the list
                        try:
                            projectiles[iterator].kill()
                        except IndexError:
                            continue
                          
                    if projectile.rect[iterator].colliderect(enemy.rect):
                        enemy.health -= projectile.damage
                        pygame.mixer.Sound.play(enemy_hit_sound)
                        hit_enemies.append(enemy)
                        # Add projectiles to the removal list except for lightning, poison, and holy strike
                        if projectile.size != 15 and projectile.size != 3 and projectile.size != 99:
                            projectiles_to_remove.append(projectile)
    
            projectile.draw(window)  # Draw projectiles
    
        # Remove the projectiles that need to be removed
        projectiles = [
            projectile for projectile in projectiles if projectile not in projectiles_to_remove]
    
        # Updage and draw enemies
        detectingNewWave = len(enemies)
        for enemy in enemies:
            if type(enemy) == Boss:
                enemy.move()
                enemy.stepIndex += 1
                if enemy.stepIndex >= 40:
                    enemy.stepIndex = 0
                if enemy.off_screen() or enemy.health <= 0:
                    enemies.remove(enemy)
                    ShopMenu.currency += 300 if (enemy.health > -1000 and enemy.health <= 0) else 0
            else:
                enemy.move()
                enemy.stepIndex += 1
                if enemy.stepIndex >= 40:
                    enemy.stepIndex = 0
                if enemy.off_screen() or enemy.health <= 0:
                    enemies.remove(enemy)
                    ShopMenu.currency += 10 if (enemy.health > -1000 and enemy.health <= 0) else 0
            enemy.draw(window)
  
  
        if displayDefenseTowerOverlay:
            # Create a rectangle representing the position and size of the overlay
            overlayRect = o_towerList[towerType].get_rect(center=[mouseX-40, mouseY-50])
        
            # Check if the overlay rectangle collides with any existing defense tower rectangles
            for dTower in defenseTowers:
                if overlayRect.colliderect(dTower.rect):
                    canPlace = False
                    break
            else:
                canPlace = True
        
            if canPlace:
                # If placement is allowed, blit the original tower image on the window
                window.blit(o_towerList[towerType], (mouseX-40, mouseY-50))
            else:
                # If placement is not allowed, create a tinted image to indicate invalid placement
        
                # Create a temporary surface with the non-transparent area of the tower image
                tempSurf = pygame.Surface(o_towerList[towerType].get_size(), pygame.SRCALPHA)
                tempSurf.blit(o_towerList[towerType], (0, 0), None, pygame.BLEND_RGBA_MAX)
        
                # Create a new surface for the tinted image and fill it with a red tint
                tinted_image = pygame.Surface(tempSurf.get_size(), flags=pygame.SRCALPHA)
                tinted_image.fill((190, 0, 0) + (128,), special_flags=pygame.BLEND_RGBA_MULT)
                tinted_image.blit(tempSurf, (0, 0))
        
                # Blit the tinted image on the window at the specified position
                window.blit(tinted_image, (mouseX-40, mouseY-50))
        
                # Create an overlay image with a translucent red color
                overlay_image = pygame.Surface(overlayRect.size, flags=pygame.SRCALPHA)
                overlay_image.fill((190, 0, 0, 100), None, pygame.BLEND_RGBA_ADD)
        
                # Blit the overlay image on the window at the specified position
                window.blit(overlay_image, (mouseX-40, mouseY-50))
      
      # Draw all the existing defense towers on the window
      for dTower in defenseTowers:
          dTower.draw(window)
  
      # Display Projectile Levels and Recharging
      firedProjectileList = [0, fireballBulletUsed, lightningBoltUsed, poisonCloudUsed, holyStrikeUsed]
      for iteratorIndex, iteratorValue in enumerate(projectileUIDisplayList):
          window.blit(iteratorValue, (90 + 60 * iteratorIndex, 445))
          tempsurf = pygame.Surface((50,(50 * max(0, (1 - ((pygame.time.get_ticks() - firedProjectileList[iteratorIndex]) / projectileRegenTime[iteratorIndex]))))))
          tempsurf.set_alpha(40)
          tempsurf.fill((255,255,255))
          window.blit(tempsurf, (90 + 60 * iteratorIndex, 445))
          tempsurf = pygame.Surface((50,50))
          tempsurf.set_alpha(10)
          tempsurf.fill((200,0,200))
          window.blit(tempsurf, (90 + 60 * projectileType, 445))
          if bulletLevelsList[iteratorIndex] == 0:
              window.blit(locked_icon, (95 + 60 * iteratorIndex, 450))
          else:
            window.blit(font.render(str(bulletLevelsList[iteratorIndex]), True, (255, 255, 255)), (90 + 60 * iteratorIndex, 445))
  
      # Update audio volume
      light_bullet_sound.set_volume(SettingsMenu.lightbulletsoundvolume)
      fireball_bullet_sound.set_volume(SettingsMenu.fireballbulletsoundvolume)
      lightning_bullet_sound.set_volume(SettingsMenu.lightningbulletsoundvolume)
      poison_cloud_bullet_sound.set_volume(SettingsMenu.poisoncloudbulletsoundvolume)
      holy_strike_sound.set_volume(SettingsMenu.holystrikebulletsoundvolume)
      enemy_hit_sound.set_volume(SettingsMenu.enemyhitsoundvolume)
  
      # Display currency, wave #, and high score
      window.blit(textBoxUIDisplay, (20,20))
      window.blit(font.render(str(f"${ShopMenu.currency}"), True, (255, 255, 0)), (25,23))
      window.blit(textBoxUIDisplay, (390,420))
      window.blit(font.render(str(f"Wave:{wave + 1}"), True, (255, 0, 0)), (395,423))
      window.blit(textBoxUIDisplay, (390,460))
      if not renderTimeToNewWave:
          window.blit(font.render(str(f"Best:{SettingsMenu.highScore + 1}"), True, (255, 0, 0)), (395,463))
      else:
          window.blit(font.render(str(f"Wave in:{max(0, round((10000 - (pygame.time.get_ticks() - waveTimeEnded)) / 1000) - 1)}"), True, (255, 0, 0)), (395,463))
      window.blit(pause_icon, (850, 10))
      window.blit(shop_icon, (5, 415))
    
      # Update screen and delay for next tick
      for menu in Menu.objects:
        if menu.visible:
          menu.update()

      towerCounts = [ShopMenu.lightTowerCount, ShopMenu.fireballTowerCount, ShopMenu.lightningTowerCount, ShopMenu.poisonTowerCount]
      bulletLevelsList = [ShopMenu.lightBulletLevel, ShopMenu.fireballBulletLevel, ShopMenu.lightningBulletLevel, ShopMenu.poisonBulletLevel, ShopMenu.holyStrikeBulletLevel]
    
      pygame.event.pump()
      pygame.time.delay(10)
      pygame.display.update()
      # Kill projectiles without a collision box such as lightning and holy strike
      for projectile in projectiles:
          if (projectile.size == 3 or projectile.size == 99):
              pygame.time.delay(20)
              projectiles.remove(projectile)
              projectile.kill()
  pygame.quit()