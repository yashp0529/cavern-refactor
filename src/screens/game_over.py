class GameOverScreen:
    def __init__(self, app):
        self.app = app

    def update(self, input_state=None):
        if input_state and input_state.fire_pressed:
            self.app.change_screen("menu")

    def draw(self, screen):
        # keep original look
        self.app.draw_status(screen)
        screen.blit("over", (0, 0))
