# Rock Paper Scissors Game

A simple and interactive Rock Paper Scissors game with a graphical user interface.

## Features
- Play against the computer
- First to 5 points wins
- Modern and clean interface
- Score tracking
- Game over screen

## Installation

### Option 1: Run from Source
1. Make sure you have Python 3.x installed
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the game:
   ```bash
   python rock_paper_scissors_gui.py
   ```

### Option 2: Run Executable (Windows)
1. Download the `rock_paper_scissors.exe` from the releases
2. Double-click to run the game

## Building the Executable
To build the executable yourself:
1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run PyInstaller:
   ```bash
   pyinstaller --onefile --windowed rock_paper_scissors_gui.py
   ```
3. The executable will be created in the `dist` folder

## How to Play
1. Click on rock (✊), paper (✋), or scissors (✌️) to make your move
2. The computer will make its move
3. First player to reach 5 points wins
4. Use the reset button to start a new game

## Requirements
- Windows 7 or later
- For source code: Python 3.x
- For executable: No additional requirements 