Name: Yash Patel
Student Number: 100785833

Cavern – Refactoring Design Overview

This document explains the architectural decisions made while refactoring the Cavern game. The refactoring focuses on three main areas:

Screens architecture (State pattern)

Input handling (Command pattern + edge detection)

Pause implementation

1️⃣ Screens Architecture (State Pattern)
Problem Before Refactoring

Originally, the game used global branching based on a state variable inside the global update() and draw() functions.

This caused:

Tight coupling between screens

Large conditional blocks

Hard-to-maintain transitions

Global game object creation

Solution Implemented

I implemented the State Pattern using screen objects.

An App class now owns the current screen:

MenuScreen

PlayScreen

GameOverScreen

Each screen implements:

update(input_state)
draw(screen)

The global functions are now thin delegates:
def update():
    app.update(keyboard)

def draw():
    app.draw(screen)


Screen transitions are handled using:

app.change_screen(new_screen)

Game object creation happens inside screen transitions (for example, when moving from Menu → Play), not inside global update.

Benefits

No global state

Clear separation of responsibilities

Each screen controls its own behavior

Easier to extend (for example, adding Settings screen later)

2️⃣ Input Design (Command Pattern + Edge Detection)
Problem Before Refactoring

The game previously:

Used global variables like space_down

Accessed keyboard.* directly inside Player.update()

Mixed input reading with gameplay logic

This made testing and extension difficult.

Solution Implemented

I created an InputState class (dataclass style) that is built once per frame.

It contains:

left: bool

right: bool

jump_pressed: bool (edge detection)

fire_pressed: bool (edge detection)

fire_held: bool

pause_pressed: bool

Input is now centralized in input.py.

Edge detection works by comparing current frame input with the previous frame.

Example:

fire_pressed = space_now and not prev["space"]


The Player.update() method now consumes input_state instead of reading keyboard directly.

Benefits

No global space_down

No direct keyboard access in Player

Clean separation between input and gameplay

Correct “pressed this frame only” detection

Easier to extend to controller input later

3️⃣ Pause Implementation

Pause is implemented inside PlayScreen.

How It Works

Pressing P toggles self.paused

When paused:

Game simulation does not update

Entities do not move

Timers and spawning stop

Rendering still occurs

A "PAUSED" overlay is displayed

Pause can only be triggered inside PlayScreen.

Benefits

Clean isolation of pause logic

No crashes when resuming

Simulation freezing works correctly

Pause does not affect Menu or GameOver screens

Overall Design Improvements

The refactored architecture now follows:

Separation of concerns

Centralized input handling

Screen-level responsibility

Removal of global state

Clean screen transitions

The project is now more modular, easier to maintain, and follows proper object-oriented design principles.


