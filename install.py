import os
import shutil
from pathlib import Path

def install_app():
    home = str(Path.home())

    # Create icon path and copy icon
    icon_src = os.path.join("assets", "icon.png")
    icon_dest = os.path.join(home, ".local", "share", "icons", "tictactoe.png")
    os.makedirs(os.path.dirname(icon_dest), exist_ok=True)
    shutil.copy(icon_src, icon_dest)

    # Prepare .desktop file
    desktop_src = "tictactoe.desktop"
    desktop_dest = os.path.join(home, ".local", "share", "applications", "tictactoe.desktop")
    os.makedirs(os.path.dirname(desktop_dest), exist_ok=True)

    # Read .desktop and write it with correct Exec path
    with open(desktop_src, "r") as f:
        content = f.read()
    content = content.replace("{EXEC_PATH}", os.path.abspath("main.py"))

    with open(desktop_dest, "w") as f:
        f.write(content)

    os.chmod(desktop_dest, 0o755)
    print("✅ App installed! You can now find 'Tic Tac Toe' in your App Menu.")

if __name__ == "__main__":
    install_app()
