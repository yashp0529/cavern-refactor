# DESIGN DOCUMENT
## Cavern Refactor Project

**Name:** Yash Patel  
**Student Number:** 100785833  

---

# 1. Overview

This project refactors the original Cavern game to improve code structure, remove global state usage, and introduce cleaner input handling.

The main goals were:

- Eliminate direct keyboard access inside game entities
- Remove global state branching inside update() and draw()
- Introduce a proper screen management structure
- Implement pause functionality (Task C)

---

# 2. Architecture

The game now follows a structured object-oriented design.

## 2.1 Screen-Based State Management (State Pattern)

Instead of using global state checks inside update() and draw(), the game now uses screen objects:

- `MenuScreen`
- `PlayScreen`
- `GameOverScreen`

An `App` object owns and manages the current screen.

The global functions are now simple delegates:

```python
def update():
    app.update(keyboard)

def draw():
    app.draw(screen)

