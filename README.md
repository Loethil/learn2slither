# 🐍 Learn2Slither

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**A Python-based Snake game with AI learning capabilities**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Game Controls](#-game-controls) • [Project Structure](#-project-structure)

</div>

---

## 📖 About

Learn2Slither is an interactive Snake game implementation built with Python and Pygame. The project features both visual and terminal-based rendering modes, making it perfect for both playing and developing AI agents to learn the game autonomously.

The game includes classic Snake mechanics with a twist:
- 🟢 **Green apples** make your snake grow
- 🔴 **Red apples** make your snake shrink
- 🏆 Win by reaching the target length
- 💀 Avoid walls and your own body!

## ✨ Features

- **🎮 Dual Rendering Modes**
  - Visual mode with Pygame graphics
  - Terminal mode with colored ASCII output
  
- **🎯 Classic Snake Gameplay**
  - Smooth snake movement with arrow key controls
  - Dynamic apple spawning (green and red)
  - Collision detection with walls and self
  - Win/lose conditions based on snake length

- **🧠 AI-Ready Architecture**
  - Environment class with state management
  - Snake vision system for agent perception
  - Agent infrastructure for reinforcement learning
  - Configurable game sessions for training

- **⚙️ Flexible Configuration**
  - Customizable board dimensions
  - Adjustable initial snake length
  - Configurable win conditions
  - Step-by-step debugging mode

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Loethil/learn2slither.git
   cd learn2slither
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

### Running the Game

#### Visual Mode (Default)
```bash
python src/main.py
```

#### Terminal Mode
```bash
python src/main.py -visual
```

### Command-Line Arguments

The game supports several command-line arguments for customization:

```bash
python src/main.py [OPTIONS]
```

| Option | Type | Description |
|--------|------|-------------|
| `-sessions` | int | Number of game sessions to run |
| `-visual` | flag | Enable visual interface (Pygame window) |
| `-dontlearn` | flag | Prevent the model from training (for testing) |
| `-step-by-step` | flag | Enable step-by-step visual debugging |
| `-load` | str | Path to load a saved model (default: `models/defaut.txt`) |

### Examples

```bash
# Run multiple training sessions
python src/main.py -sessions 100

# Run in visual mode with step-by-step debugging
python src/main.py -visual -step-by-step

# Load a specific model
python src/main.py -load models/my_model.txt
```

## 🕹️ Game Controls

| Key | Action |
|-----|--------|
| ⬆️ **Up Arrow** | Move snake up |
| ⬇️ **Down Arrow** | Move snake down |
| ⬅️ **Left Arrow** | Move snake left |
| ➡️ **Right Arrow** | Move snake right |
| ❌ **Close Window** | Quit game |

## 🎨 Visual Elements

### In Pygame (Visual Mode)
- 🟡 **Yellow/Brown** - Snake head
- 🔵 **Blue** - Snake body
- 🟢 **Green** - Green apple (grows snake)
- 🔴 **Red** - Red apple (shrinks snake)
- ⬜ **White** - Walls
- ⬛ **Gray** - Empty space

### In Terminal Mode
- **H** (Blue) - Snake head
- **S** (Cyan) - Snake body
- **G** (Green) - Green apple
- **R** (Red) - Red apple
- **W** (Yellow) - Walls
- **0** - Empty space

## 📁 Project Structure

```
learn2slither/
├── src/
│   ├── main.py              # Entry point and argument parsing
│   ├── renderer.py          # Terminal and Pygame rendering functions
│   └── classes/
│       ├── game.py          # Main game loop and event handling
│       ├── environment.py   # Game environment and board management
│       ├── snake.py         # Snake entity and movement logic
│       └── agent.py         # AI agent base class (WIP)
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## 🛠️ Technologies Used

- **Python 3.10+** - Core programming language
- **Pygame** - Graphics and game window management
- **NumPy** - Efficient array operations for the game board
- **Pandas** - Data management for AI training (future feature)

## 🎯 Game Mechanics

### Snake Vision System

The snake has a directional vision system that perceives the environment in four directions:
- **UP**: All cells from the head upward to the wall
- **DOWN**: All cells from the head downward to the wall
- **LEFT**: All cells from the head leftward to the wall
- **RIGHT**: All cells from the head rightward to the wall

This vision data can be used by AI agents to make intelligent movement decisions.

### Win/Lose Conditions

- **Win**: Grow your snake to the specified win condition length (default: 10)
- **Lose**: 
  - Collide with a wall
  - Collide with your own body
  - Shrink to length 0 (too many red apples!)

## 🚧 Future Enhancements

This project is under active development. Planned features include:

- [ ] **Reinforcement Learning Agent** - Fully implemented AI that learns to play
- [ ] **Multiple AI Algorithms** - Q-Learning, Deep Q-Network (DQN), PPO
- [ ] **Model Persistence** - Save and load trained models
- [ ] **Performance Metrics** - Track scores, survival time, and learning progress
- [ ] **Difficulty Levels** - Multiple board sizes and game speeds
- [ ] **Multiplayer Mode** - Compete with friends or AI
- [ ] **Replay System** - Review best games and training sessions

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines for Python code
- Add docstrings to new functions and classes
- Test your changes thoroughly before submitting
- Update documentation for any new features

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by the classic Snake game
- Built as a learning project for AI/ML game agents
- Thanks to the Pygame and NumPy communities

## 📧 Contact

For questions, suggestions, or issues, please open an issue on GitHub.

---

<div align="center">

**Happy Slithering! 🐍**

Made with ❤️ and Python

</div>