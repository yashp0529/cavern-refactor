from src.screens.menu import MenuScreen
from src.screens.play import PlayScreen
from src.screens.game_over import GameOverScreen
from src.input import build_input_state

class App:
    def __init__(self):
        self.timer = 0

        self.menu_screen = MenuScreen(self)
        self.play_screen = PlayScreen(self)
        self.game_over_screen = GameOverScreen(self)

        self.screens = {
            "menu": self.menu_screen,
            "play": self.play_screen,
            "game_over": self.game_over_screen,
        }
        self.current = self.menu_screen

    def change_screen(self, name):
        self.current = self.screens[name]

    def update(self, keyboard):
        self.timer += 1
        input_state = build_input_state(keyboard)
        self.current.update(input_state)

    def draw(self, screen):
        self.current.draw(screen)

    # call your old draw_status but make it accept screen
    def draw_status(self, screen, game):
        from cavern import draw_status
        draw_status(screen, game)

