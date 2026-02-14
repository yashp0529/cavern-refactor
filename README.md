# Cavern – Refactored Version

**Name:** Yash Patel  
**Student Number:** 100785833  

---

## Project Overview

This project is a refactored version of the Cavern game using Pygame Zero.

The goal of this refactoring was to:

- Improve code structure
- Remove global state usage
- Implement proper input handling
- Add pause functionality
- Separate logic using screen objects

The game includes a Menu screen, Play screen, and Game Over screen.

---

## How to Run the Game

### 1. Install Requirements

Make sure Python 3.12+ is installed.

Install Pygame Zero:

---

### 2. Run the Game

From the project root folder:



---

## Controls

- **Left Arrow** – Move left  
- **Right Arrow** – Move right  
- **Space** – Jump / Fire  
- **P** – Toggle Pause  

---

## Features Implemented

### 1. Screen-Based Architecture

The game uses separate screen classes:

- `MenuScreen`
- `PlayScreen`
- `GameOverScreen`

An `App` object manages the current screen.

Global `update()` and `draw()` functions delegate to the App.

---

### 2. Input Handling (Edge Detection)

Keyboard input is handled using an `InputState` object created once per frame.

It supports:

- Left / Right movement
- Jump pressed (edge detection)
- Fire pressed (edge detection)
- Fire hold
- Pause pressed

This removes direct keyboard access inside game entities.

---

### 3. Pause Mode (Task C)

- Press **P** to pause the game
- Game simulation stops (movement, timers, spawning)
- Current screen still renders
- A "PAUSED" overlay is displayed
- Press **P** again to resume

Pause functionality works only in `PlayScreen`.

---

## Testing

Testing was performed manually by verifying:

- Menu → Play → Game Over transitions
- Jump and fire edge detection
- Pause toggle behavior
- Resume functionality without crashes

No automated unit tests were implemented.

---

## Notes

- `__pycache__` and `.pyc` files are excluded using `.gitignore`
- Code is structured for clarity and maintainability
- No global state is used for input or screen management

---

## Author

Yash Patel  
Student Number: 100785833

