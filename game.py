import tkinter as tk
from tkinter import messagebox
import random
import json
import os
from datetime import datetime

history_file = "history.json"

# Save game result with safe file handling
def save_history(winner, player_name):
    entry = {
        "winner": winner,
        "player": player_name,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data = []
    if os.path.exists(history_file):
        try:
            with open(history_file, "r") as f:
                content = f.read().strip()
                if content:
                    data = json.loads(content)
        except json.JSONDecodeError:
            data = []

    data.append(entry)
    with open(history_file, "w") as f:
        json.dump(data, f, indent=2)

# View game history safely
def show_history():
    if not os.path.exists(history_file):
        messagebox.showinfo("History", "No history found yet.")
        return

    try:
        with open(history_file, "r") as f:
            data = json.load(f)
    except Exception:
        messagebox.showerror("Error", "History file is corrupted.")
        return

    history_win = tk.Toplevel()
    history_win.title("Game History")
    history_win.geometry("500x400")
    history_win.configure(bg="#fef9f5")

    text = tk.Text(history_win, wrap="word", font=("Consolas", 11), bg="#fff7ed", fg="#333")
    text.pack(expand=True, fill="both", padx=10, pady=10)

    for entry in reversed(data[-20:]):
        line = f"{entry['timestamp']} - {entry['player']} ➤ {entry['winner']} wins\n"
        text.insert("end", line)

    text.config(state="disabled")


# Start the game
def start_game(player_name, mode, player2_name="Computer"):
    player_map = {
    "X": player_name,
    "O": player2_name
    }

    current_player = ["X"]
    board_state = [["" for _ in range(3)] for _ in range(3)]
    score = {"X": 0, "O": 0, "Tie": 0}

    def switch_player():
        current_player[0] = "O" if current_player[0] == "X" else "X"

    def check_winner():
        b = board_state
        lines = (
            b[0], b[1], b[2],
            [b[0][0], b[1][0], b[2][0]],
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]],
        )

        for line in lines:
            if line[0] and line.count(line[0]) == 3:
                return line[0]

        if all(cell for row in b for cell in row):
            return "Tie"

        return None

    def bot_move():
        empty = [(r, c) for r in range(3) for c in range(3) if board_state[r][c] == ""]
        if empty:
            row, col = random.choice(empty)
            make_move(row, col)

    def make_move(row, col):
        if board_state[row][col] != "":
            return

        board_state[row][col] = current_player[0]
        buttons[row][col]["text"] = current_player[0]
        buttons[row][col]["state"] = "disabled"
        root.update_idletasks()  # ✅ Force UI update

        winner = check_winner()
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Result", "It's a tie!")
            else:
                messagebox.showinfo("Result", f"{winner} wins!")

            score[winner] += 1
            update_score()
            save_history(player_map.get(winner, "Unknown"), player_name)

            return_to_main()
            return

        switch_player()

        # If bot’s turn, wait a bit then make move
        if mode == "bot" and current_player[0] == "O":
            root.after(400, bot_move)

    def reset_board():
        for r in range(3):
            for c in range(3):
                board_state[r][c] = ""
                buttons[r][c]["text"] = ""
                buttons[r][c]["state"] = "normal"
        current_player[0] = "X"

    def return_to_main():
        root.destroy()
        import main


    def update_score():
        score_label.config(
            text=f"X: {score['X']}    O: {score['O']}    Tie: {score['Tie']}",
        )

    # Main game window
    root = tk.Tk()
    root.title(f"Tic Tac Toe - {player_name}")
    root.geometry("500x600")
    root.configure(bg="#fef9f5")

    tk.Label(root, text=f"Player: {player_name}", font=("Helvetica", 14), bg="#f0f4f8").pack(pady=5)

    score_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg="#fef9f5", fg="#222")
    score_label.pack()

    names_label = tk.Label(root,
        text=f"{player_name} (X) vs {player2_name} (O)",
        font=("Helvetica", 12),
        bg="#fef9f5",
        fg="#4b5563"
    )
    names_label.pack()

    update_score()

    frame = tk.Frame(root, bg="#f0f4f8")
    frame.pack(pady=20)

    buttons = []
    for r in range(3):
        row = []
        for c in range(3):
            btn = tk.Button(frame, text="", font=("Helvetica", 28, "bold"), width=4, height=2,
                        bg="#fff", fg="#1f2937", activebackground="#e2e8f0",
                        command=lambda r=r, c=c: make_move(r, c))

            btn.grid(row=r, column=c, padx=5, pady=5)
            row.append(btn)
        buttons.append(row)

    control_frame = tk.Frame(root, bg="#f0f4f8")
    control_frame.pack(pady=10)

    tk.Button(control_frame, text="🔁 Restart", font=("Helvetica", 12), command=reset_board).pack(side="left", padx=10)
    tk.Button(control_frame, text="📜 History", font=("Helvetica", 12), command=show_history).pack(side="right", padx=10)

    root.mainloop()
