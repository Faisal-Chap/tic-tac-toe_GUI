import tkinter as tk
from tkinter import messagebox
from game import start_game
from game import start_game, show_history


def launch_app():
    name = name_entry.get().strip()
    mode = mode_var.get()
    if not name or mode not in ("friend", "bot"):
        messagebox.showwarning("⚠️ Missing Info", "Please enter your name and select a mode.")
        return
    root.destroy()
    start_game(player_name=name, mode=mode)

root = tk.Tk()
root.title("🎮 Welcome to Tic Tac Toe")
root.geometry("480x400")
root.configure(bg="#e7f0fd")

tk.Label(root, text="🧠 Tic Tac Toe", font=("Helvetica", 28, "bold"), bg="#e7f0fd", fg="#1f2937").pack(pady=20)

tk.Label(root, text="Enter your name:", font=("Helvetica", 14), bg="#e7f0fd").pack(pady=5)
name_entry = tk.Entry(root, font=("Helvetica", 13), justify="center")
name_entry.pack(pady=10)

tk.Label(root, text="Choose Mode:", font=("Helvetica", 14), bg="#e7f0fd").pack(pady=10)

mode_var = tk.StringVar()
tk.Radiobutton(root, text="👫 Play with Friend", variable=mode_var, value="friend",
               font=("Helvetica", 12), bg="#e7f0fd").pack()
tk.Radiobutton(root, text="🤖 Play with Bot (Computer)", variable=mode_var, value="bot",
               font=("Helvetica", 12), bg="#e7f0fd").pack()

tk.Button(root, text="🚀 Start Game", font=("Helvetica", 14, "bold"), bg="#3b82f6", fg="white",
          padx=20, pady=5, command=launch_app).pack(pady=30)

tk.Button(root, text="📜 View Winners", font=("Helvetica", 13), bg="#f59e0b", fg="white",
          padx=15, pady=4, command=show_history).pack(pady=5)

button_frame = tk.Frame(root, bg="#e7f0fd")
button_frame.pack(pady=20)



root.mainloop()
