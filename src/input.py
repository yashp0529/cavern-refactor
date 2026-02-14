from dataclasses import dataclass

@dataclass
class InputState:
    left: bool = False
    right: bool = False
    jump_pressed: bool = False
    fire_pressed: bool = False
    fire_held: bool = False
    pause_pressed: bool = False

_prev = {
    "space": False,
    "p": False,
}

def build_input_state(keyboard):
    global _prev

    space_now = keyboard.space
    p_now = keyboard.p

    fire_pressed = space_now and not _prev["space"]
    pause_pressed = p_now and not _prev["p"]

    _prev["space"] = space_now
    _prev["p"] = p_now

    return InputState(
        left=keyboard.left,
        right=keyboard.right,
        jump_pressed=fire_pressed,   # we’ll separate later if needed
        fire_pressed=fire_pressed,
        fire_held=space_now,
        pause_pressed=pause_pressed
    )
