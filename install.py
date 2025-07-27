import os
import shutil
from pathlib import Path

def install_app():
    home = str(Path.home())

    # Copy icon to local icons folder
    icon_src = os.path.join("assets", "icon.png")
    icon_dest = os.path.join(home, ".local", "share", "icons", "tictactoe.png")
    os.makedirs(os.path.dirname(icon_dest), exist_ok=True)
    shutil.copy(icon_src, icon_dest)

    # Prepare .desktop file paths
    desktop_src = "tictactoe.desktop"
    desktop_dest = os.path.join(home, ".local", "share", "applications", "tictactoe.desktop")
    os.makedirs(os.path.dirname(desktop_dest), exist_ok=True)

    # Absolute path to main.py inside tic_tac_toe folder
    exec_path = os.path.abspath(os.path.join("tic_tac_toe", "main.py"))

    # Read .desktop file and replace {EXEC_PATH} with full python3 command
    with open(desktop_src, "r") as f:
        content = f.read()

    content = content.replace("{EXEC_PATH}", f"python3 {exec_path}")

    # Write modified desktop file
    with open(desktop_dest, "w") as f:
        f.write(content)

    # Make the .desktop file executable
    os.chmod(desktop_dest, 0o755)

    print("✅ App installed! You can now find 'Tic Tac Toe' in your App Menu.")

if __name__ == "__main__":
    install_app()
