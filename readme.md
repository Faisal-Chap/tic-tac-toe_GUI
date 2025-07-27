# 🎮 Tic Tac Toe (GUI Edition for Linux)
A modern, beautiful Tic Tac Toe game built with Python's Tkinter — play against a friend or the computer, track scores, and view game history — now installable and launchable like a native Linux app!

## 🖼️ Features
- ✅ GUI-based game with modern, colorful theme

- 🧠 Play with Friend or vs Computer (Bot AI)

- 🎯 Track player names, scores, and game history

- 💾 Persistent score saving using local file

- 🔁 Restart game with a click

- - 📜 View all-time winners in a history window

- 📦 Installable on Linux as a desktop app with icon and terminal command

## 📦 Installation (Linux - App Menu & Terminal Access)
### 📥 1. Clone the repository
```bash
git clone https://github.com/Faisal-Chap/tic-tac-toe_GUI.git
cd tic-tac-toe_GUI
```
### 🚀 2. Install the app
Recommended: use pipx to install in an isolated environment and expose the tictactoe command globally:

```bash
pipx install .
```
If you don’t have pipx installed, you can install it with:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```
After installation, you can run:

```bash
tictactoe
```
### 🔧 3. Add app launcher to your desktop environment (App Menu)
Run:

```bash
python3 install.py
```
This will add the Tic Tac Toe app to your system app menu with icon support.

### 🧪 4. (Optional) Run directly from source
If you want to run without installing:

```bash
python3 -m tic_tac_toe
```
### 🧠 How to Play
- Launch the game from your App Menu or run tictactoe in terminal.

- Enter player name(s).

- Choose to play vs Friend or Bot (Computer).

- Click on the board to place your X or O.

- Use the Restart button to reset the game.

- Click the Winners button to view full game history and winners.

### 💡 Advanced Notes
The app icon and desktop launcher are installed in your home directory under ~/.local/share/ for user-only access.

Game data (scores & history) are saved persistently in a local file named history.json inside the tic_tac_toe package folder.

The command-line shortcut tictactoe runs the GUI from anywhere after pipx installation.

### 🧑‍💻 Author
Built with 💙 by Faisal Chap

### 📄 License
MIT License — feel free to use, modify, and share!
