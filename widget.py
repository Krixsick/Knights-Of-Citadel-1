import pygame


class Widget:
    def __init__(self, _sprite, _parentUI, _posX=0, _posY=0, _customWidthMultiplier=1, _customHeightMultiplier=1):
        """
        Initializes a Widget object.

        Args:
            _sprite (str): The file path of the sprite image.
            _parentUI (pygame.Surface): The parent UI surface where the widget will be rendered.
            _posX (int, optional): The X position of the widget's top-left corner. Defaults to 0.
            _posY (int, optional): The Y position of the widget's top-left corner. Defaults to 0.
            _customWidthMultiplier (int, optional): Custom width multiplier for scaling the widget's sprite. Defaults to 1.
            _customHeightMultiplier (int, optional): Custom height multiplier for scaling the widget's sprite. Defaults to 1.
        """
        self.parent = _parentUI
        self.sprite = pygame.image.load(_sprite)
        self.sprite = pygame.transform.scale(
            self.sprite, (self.sprite.get_width() * _customWidthMultiplier, self.sprite.get_height() * _customHeightMultiplier))
        self.widgetRect = self.sprite.get_rect()
        self.widgetRect.topleft = (_posX, _posY)

    def update(self):
        """
        Updates the widget by blitting its sprite onto the parent UI surface.
        """
        self.parent.blit(self.sprite, self.widgetRect)
