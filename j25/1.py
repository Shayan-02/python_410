import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Tic-Tac-Toe")


player_turn = tk.StringVar()
player_turn.set("X")


buttons = [[None for _ in range(3)] for _ in range(3)]



def check_winner():
    for i in range(3):
        # Check rows and columns
        if (
            buttons[i][0]["text"]
            == buttons[i][1]["text"]
            == buttons[i][2]["text"]
            != ""
        ) or (
            buttons[0][i]["text"]
            == buttons[1][i]["text"]
            == buttons[2][i]["text"]
            != ""
        ):
            return True


    if (
        buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != ""
    ) or (
        buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != ""
    ):
        return True

    return False



def on_click(row, col):
    if buttons[row][col]["text"] == "" and not check_winner():
        buttons[row][col]["text"] = player_turn.get()
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {player_turn.get()} wins!")
            reset_board()
        else:
            # Switch turns
            player_turn.set("O" if player_turn.get() == "X" else "X")
    elif check_winner():
        messagebox.showinfo("Game Over", "Game has already been won!")



def reset_board():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
    player_turn.set("X")



for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(
            root,
            text="",
            font=("normal", 40),
            width=5,
            height=2,
            command=lambda row=i, col=j: on_click(row, col),
        )
        buttons[i][j].grid(row=i, column=j)


root.mainloop()
