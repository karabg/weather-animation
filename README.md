# Weather Animation with PyQt6

This Python project is a graphical user interface (GUI) application that demonstrates weather animations (snow and rain) using PyQt6. The program includes a menu bar with options to display project information and start weather animations.

---

## Features

1. **Menu Bar**:
   - **About**: Displays information about the project.
   - **Weather**: Contains two sub-options:
     - **Snow**: Starts a snow animation.
     - **Rain**: Starts a rain animation.

2. **Weather Animations**:
   - **Snow**: Small white circles falling from the top of the window.
   - **Rain**: Thin blue rectangles falling to mimic raindrops.

3. **Custom Drawing**:
   - Animations are rendered using PyQt6's `QPainter`.

---

## Requirements

- Python 3.8 or higher
- PyQt6

---

## Installation

1. Clone this repository or download the code files.
   ```bash
   git clone https://github.com/karabg/weather-animation
   cd weather-animation
   ```

2. Create and activate a virtual environment (optional but recommended).
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies.
   ```bash
   pip install PyQt6
   ```

---

## Usage

1. Run the program:
   ```bash
   python main.py
   ```

2. Interact with the menu bar:
   - Select **About** to view project information.
   - Choose **Weather > Snow** or **Weather > Rain** to start the respective animations.