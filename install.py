import os
import shutil
from pathlib import Path

home = str(Path.home())

# Paths
icon_src = os.path.join("assets", "icon.png")
icon_dest = os.path.join(home, ".local", "share", "icons", "tictactoe.png")

desktop_src = "tictactoe.desktop"
desktop_dest = os.path.join(home, ".local", "share", "applications", "tictactoe.desktop")

# Copy icon
os.makedirs(os.path.dirname(icon_dest), exist_ok=True)
shutil.copy(icon_src, icon_dest)

# Replace nothing — just copy desktop file (Exec=tictactoe)
os.makedirs(os.path.dirname(desktop_dest), exist_ok=True)
shutil.copy(desktop_src, desktop_dest)
os.chmod(desktop_dest, 0o755)

print("✅ Installed! Launch 'Tic Tac Toe' from the app menu.")
