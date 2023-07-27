from typing import Self
from GameFrame import Level

class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

            # set background image
Self.set_background_image("Background.png")
