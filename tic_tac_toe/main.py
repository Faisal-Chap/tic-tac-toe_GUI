import tkinter as tk
from tkinter import messagebox
from tic_tac_toe.game import start_game, show_history



def main():
    # --- Main Window Setup ---
    root = tk.Tk()
    root.title("🎮 Welcome to Tic Tac Toe")

    # Set initial size
    root.geometry("700x600")

    # Set minimum allowed size (user can't shrink below this)
    root.minsize(700, 600)

    root.configure(bg="#e7f0fd")

    # --- Title ---
    tk.Label(root, text="🧠 Tic Tac Toe", font=("Helvetica", 28, "bold"),
            bg="#e7f0fd", fg="#1f2937").pack(pady=20)

    # --- Player 1 Name ---
    tk.Label(root, text="Enter Player 1 name:", font=("Helvetica", 14),
            bg="#e7f0fd").pack(pady=5)
    player1_entry = tk.Entry(root, font=("Helvetica", 13), justify="center")
    player1_entry.pack(pady=5)

    # --- Player 2 Name (conditionally shown) ---
    player2_label = tk.Label(root, text="Enter Player 2 name:", font=("Helvetica", 14), bg="#e7f0fd")
    player2_entry = tk.Entry(root, font=("Helvetica", 13), justify="center")

    def update_mode_ui(*args):
        if mode_var.get() == "friend":
            player2_label.pack(pady=5)
            player2_entry.pack(pady=5)
        else:
            player2_label.pack_forget()
            player2_entry.pack_forget()

    # --- Mode Selection ---
    mode_var = tk.StringVar()
    mode_var.trace_add("write", update_mode_ui)

    tk.Label(root, text="Choose Mode:", font=("Helvetica", 14),
            bg="#e7f0fd").pack(pady=10)

    tk.Radiobutton(root, text="👫 Play with Friend", variable=mode_var, value="friend",
                font=("Helvetica", 12), bg="#e7f0fd").pack()
    tk.Radiobutton(root, text="🤖 Play with Bot (Computer)", variable=mode_var, value="bot",
                font=("Helvetica", 12), bg="#e7f0fd").pack()

    # --- Start Game Action ---
    def launch_app():
        p1 = player1_entry.get().strip()
        p2 = player2_entry.get().strip() if mode_var.get() == "friend" else "Computer"
        mode = mode_var.get()

        if not p1 or not mode or (mode == "friend" and not p2):
            messagebox.showwarning("⚠️ Missing Info", "Please fill all required fields.")
            return

        root.destroy()
        start_game(player_name=p1, mode=mode, player2_name=p2)

    # --- Buttons ---
    button_frame = tk.Frame(root, bg="#e7f0fd")
    button_frame.pack(pady=30)

    tk.Button(button_frame, text="🚀 Start Game", font=("Helvetica", 14, "bold"),
            bg="#3b82f6", fg="white", padx=20, pady=5,
            command=launch_app).pack(pady=5)

    tk.Button(button_frame, text="📜 View Winners", font=("Helvetica", 13),
            bg="#f59e0b", fg="white", padx=15, pady=4,
            command=show_history).pack(pady=5)

    # --- Launch ---
    root.mainloop()



if __name__ == "__main__":
    main()