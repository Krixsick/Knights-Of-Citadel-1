class Menu:
    objects = []
    paused = False

    def __init__(self, _visible, _parentUI):
        '''
        Initializes the Menu object.

        Parameters
        ----------
        _visible : bool
            Determines if the menu is initially visible.
        _parentUI : pygame.Surface
            The parent user interface surface.
        '''
        self.visible = _visible
        self.parent = _parentUI
        self.uiElements = []

    def activateMenu(self):
        '''
        Activates the menu by setting its visibility to True.

        Returns
        -------
        None.
        '''
        self.visible = True

    def deactivateMenu(self):
        '''
        Deactivates the menu by setting its visibility to False.

        Returns
        -------
        None.
        '''
        self.visible = False

    def update(self):
        '''
        Updates the menu by updating each UI element.

        Returns
        -------
        None.
        '''
        for uiElement in self.uiElements:
            uiElement.update()