class MenuScreen:
    def __init__(self, app):
        self.app = app

    def update(self, input_state=None):
        if input_state and input_state.fire_pressed:
            self.app.play_screen.start_new_game()
            self.app.change_screen("play")

    def draw(self, screen):
        screen.blit("title", (0, 0))
        anim_frame = min(((self.app.timer + 40) % 160) // 4, 9)
        screen.blit("space" + str(anim_frame), (130, 280))
