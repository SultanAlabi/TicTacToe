import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)
        
        # Game variables
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]
        self.game_active = True
        
        # Status label
        self.status_label = tk.Label(
            root, 
            text=f"Player {self.current_player}'s turn",
            font=('Arial', 12),
            pady=10
        )
        self.status_label.pack()
        
        # Game board frame
        self.board_frame = tk.Frame(root)
        self.board_frame.pack()
        
        # Create buttons for the board
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=('Arial', 20, 'bold'),
                    width=5,
                    height=2,
                    command=lambda idx=i*3+j: self.make_move(idx)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
        
        # Reset button
        self.reset_button = tk.Button(
            root,
            text="New Game",
            font=('Arial', 12),
            command=self.reset_game,
            pady=10
        )
        self.reset_button.pack(pady=10)
    
    def make_move(self, index):
        """Handle player moves"""
        if not self.game_active or self.board[index] != ' ':
            return
        
        # Update board and button
        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)
        
        # Set button color based on player
        if self.current_player == 'X':
            self.buttons[index].config(fg='blue')
        else:
            self.buttons[index].config(fg='red')
        
        # Check for winner
        winner = self.check_winner()
        if winner:
            self.status_label.config(text=f"Player {winner} wins! 🎉")
            self.game_active = False
            messagebox.showinfo("Game Over", f"Player {winner} wins! 🎉")
            return
        
        # Check for draw
        if self.is_board_full():
            self.status_label.config(text="It's a draw! 🤝")
            self.game_active = False
            messagebox.showinfo("Game Over", "It's a draw! 🤝")
            return
        
        # Switch players
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.status_label.config(text=f"Player {self.current_player}'s turn")
    
    def check_winner(self):
        """Check if there's a winner"""
        # Winning combinations
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        
        for win in wins:
            if (self.board[win[0]] == self.board[win[1]] == 
                self.board[win[2]] != ' '):
                # Highlight winning combination
                for idx in win:
                    self.buttons[idx].config(bg='light green')
                return self.board[win[0]]
        return None
    
    def is_board_full(self):
        """Check if the board is full"""
        return ' ' not in self.board
    
    def reset_game(self):
        """Reset the game to initial state"""
        # Reset game variables
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]
        self.game_active = True
        
        # Reset buttons
        for button in self.buttons:
            button.config(text="", bg='SystemButtonFace', fg='black')
        
        # Reset status
        self.status_label.config(text=f"Player {self.current_player}'s turn")

def main():
    # Create the main window
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()