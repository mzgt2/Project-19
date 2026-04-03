# Project-19

## 🐍 Snake Game

A classic Snake game built with Python's Turtle graphics library.

## 📋 Description

Control a snake to eat food and grow longer. Avoid hitting the walls or your own tail!

## 🎮 How to Play

- **Arrow Keys**: Control snake direction
  - ⬆️ Up Arrow - Move up
  - ⬇️ Down Arrow - Move down
  - ⬅️ Left Arrow - Move left
  - ➡️ Right Arrow - Move right

## 🎯 Game Rules

- Eat the blue food to increase your score and grow longer
- Each food collected adds 1 point to your score
- Don't hit the walls (game boundary)
- Don't run into your own tail
- The game ends when you collide with a wall or yourself

## 🚀 Installation & Setup

### Prerequisites

- Python 3.x installed on your system
- Turtle graphics library (comes pre-installed with Python)

### Installation

1. Clone or download this repository
2. Ensure all files are in the same directory:
   - `main.py`
   - `snake.py`
   - `food.py`
   - `scoreboard.py`

### Running the Game
```bash
python main.py
```

Or on some systems:
```bash
python3 main.py
```

## 📁 File Structure
```
snake-game/
│
├── main.py          # Main game loop and collision detection
├── snake.py         # Snake class (movement, growth, controls)
├── food.py          # Food class (spawning, positioning)
└── scoreboard.py    # Scoreboard class (score tracking, game over)
```

## 🛠️ Technical Details

### Game Configuration

- **Screen Size**: 600x600 pixels
- **Background**: Black
- **Game Speed**: 0.1 seconds per frame
- **Snake Color**: White
- **Food Color**: Blue
- **Score Display**: White text at top of screen

### Collision Detection

- **Food Collision**: Distance < 15 pixels
- **Wall Collision**: When snake head reaches boundary (280 pixels from center)
- **Self Collision**: Distance < 10 pixels between head and body segments

## 🎨 Customization

You can customize the game by modifying constants in `main.py`:
```python
COLLISION_DISTANCE = 15        # Food collection range
WALL_BOUNDARY = 280            # Wall collision boundary
SELF_COLLISION_DISTANCE = 10   # Self-collision sensitivity
GAME_SPEED = 0.1               # Game speed (lower = faster)
```

## 🐛 Known Issues

None currently. If you find bugs, please report them!

## 🔮 Future Enhancements

Potential improvements for future versions:

- [ ] High score tracking
- [ ] Difficulty levels (speed increase)
- [ ] Sound effects
- [ ] Pause functionality
- [ ] Restart without closing window
- [ ] Different snake skins/colors
- [ ] Obstacles/power-ups

## 📝 Code Structure

### Classes

**Snake** (`snake.py`)
- Manages snake segments
- Handles movement and direction
- Extends snake when food is eaten
- Prevents 180-degree turns

**Food** (`food.py`)
- Randomly spawns food on screen
- Refreshes position when collected

**Scoreboard** (`scoreboard.py`)
- Tracks and displays current score
- Shows "GAME OVER" message

## 🎓 Learning Concepts

This project demonstrates:

- Object-Oriented Programming (OOP)
- Class inheritance (Turtle graphics)
- Game loop implementation
- Collision detection
- Event handling (keyboard input)
- Modular code organization

## 👨‍💻 Author

Created as a Python learning project using Turtle graphics.

## 📄 License

Free to use and modify for educational purposes.

## 🙏 Acknowledgments

- Built with Python's Turtle graphics library
- Inspired by the classic Nokia Snake game

---

**Enjoy the game! 🐍🎮**
