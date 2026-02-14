class PlayScreen:
    def __init__(self, app):
        self.app = app
        self.game = None
        self.paused = False

    def start_new_game(self):
        from cavern import Game, Player
        self.game = Game(Player())
        self.paused = False

    def update(self, input_state=None):
        if not self.game:
            return

        # pause toggle (Task C)
        if input_state and getattr(input_state, "pause_pressed", False):
            self.paused = not self.paused

        if self.paused:
            return

        # IMPORTANT: for now call original update
        self.game.update(input_state)


        if self.game.player.lives < 0:
            self.game.play_sound("over")
            self.app.change_screen("game_over")

    def draw(self, screen):
        if self.game:
            self.game.draw()   # this uses global screen inside cavern.py (original game)
            self.app.draw_status(screen, self.game)

        if self.paused:
            screen.draw.text("PAUSED", center=(400, 60), fontsize=60)
