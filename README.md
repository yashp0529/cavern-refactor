Name - Yash Patel
Student No - 100785833

🎮 How to Run the Game
1️⃣ Install dependencies (if not already installed)

Make sure Python 3.12+ is installed.

Install Pygame Zero:
pip install pgzero

2️⃣ Run the game

From the project root folder:
pgzrun cavern.py

🧪 How to Run Tests

There are no automated unit tests in this version.
Testing was done manually by verifying:

Screen transitions (Menu → Play → Game Over)

Edge detection for SPACE key

Orb firing works correctly

Pause mode freezes simulation

Resume works cleanly without crashes


🏗 Architectural Changes (Summary)

This project was refactored to improve code structure and remove global state usage.

1️⃣ State Pattern – Screen Objects

Instead of using global state branching inside update() and draw(), the game now uses screen objects:

MenuScreen

PlayScreen

GameOverScreen

An App object owns the current screen.

Global update() and draw() are now thin delegates:

def update():
    app.update(keyboard)

def draw():
    app.draw(screen)


2️⃣ Command Pattern – Input Snapshot

The game no longer reads keyboard directly inside Player.update().

Instead, an InputState object is created once per frame.

It contains:

left

right

jump_pressed (edge detection)

fire_pressed (edge detection)

fire_held

pause_pressed

This allows:

Proper edge detection (pressed this frame only)

No global space_down

No direct keyboard access inside entities

This makes input handling centralized and clean.

3️⃣ Pause Mode (Task C)

Pause is toggled using the P key.

When paused:

Game simulation stops (no movement, no timers, no spawning)

The current scene still renders

A "PAUSED" overlay is displayed

Pressing P again resumes the game.

Pause works only in PlayScreen.


