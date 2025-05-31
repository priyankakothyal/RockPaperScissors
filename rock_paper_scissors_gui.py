import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk
import os

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("900x700")
        self.root.configure(bg="#FFFFFF")  # White background
        
        # Initialize scores and win condition
        self.player_score = 0
        self.computer_score = 0
        self.win_condition = 5
        self.game_over = False
        
        # Emoji mappings
        self.emoji_map = {
            'rock': '✊',
            'paper': '✋',
            'scissors': '✌️'
        }
        
        # Create main frame with custom style
        style = ttk.Style()
        style.configure("Custom.TFrame", background="#FFFFFF")
        style.configure("Custom.TLabel", background="#FFFFFF", foreground="#000000")
        style.configure("Title.TLabel", font=("Helvetica", 32, "bold"), foreground="#000000")
        style.configure("Score.TLabel", font=("Helvetica", 20), foreground="#0000FF")
        style.configure("Result.TLabel", font=("Helvetica", 24), foreground="#FF0000")
        style.configure("Move.TLabel", font=("Helvetica", 18), foreground="#008000")
        
        self.main_frame = ttk.Frame(self.root, style="Custom.TFrame", padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title with shadow effect
        title_frame = ttk.Frame(self.main_frame, style="Custom.TFrame")
        title_frame.pack(pady=20)
        
        title_label = ttk.Label(
            title_frame,
            text="Rock Paper Scissors",
            style="Title.TLabel"
        )
        title_label.pack()
        
        # Score frame with modern design
        self.score_frame = ttk.Frame(self.main_frame, style="Custom.TFrame")
        self.score_frame.pack(pady=20)
        
        # Player score with icon
        self.player_score_label = ttk.Label(
            self.score_frame,
            text="👤 Player: 0",
            style="Score.TLabel"
        )
        self.player_score_label.pack(side=tk.LEFT, padx=30)
        
        # Computer score with icon
        self.computer_score_label = ttk.Label(
            self.score_frame,
            text="🤖 Computer: 0",
            style="Score.TLabel"
        )
        self.computer_score_label.pack(side=tk.LEFT, padx=30)
        
        # Win condition display
        self.win_condition_label = ttk.Label(
            self.main_frame,
            text=f"First to {self.win_condition} wins!",
            style="Score.TLabel"
        )
        self.win_condition_label.pack(pady=10)
        
        # Result label with animation
        self.result_label = ttk.Label(
            self.main_frame,
            text="Choose your move!",
            style="Result.TLabel"
        )
        self.result_label.pack(pady=20)
        
        # Choices frame with modern buttons
        self.choices_frame = ttk.Frame(self.main_frame, style="Custom.TFrame")
        self.choices_frame.pack(pady=20)
        
        # Create buttons for choices
        self.create_choice_buttons()
        
        # Moves display frame
        self.moves_frame = ttk.Frame(self.main_frame, style="Custom.TFrame")
        self.moves_frame.pack(pady=20)
        
        # Player move display
        self.player_move_label = ttk.Label(
            self.moves_frame,
            text="Your move: -",
            style="Move.TLabel"
        )
        self.player_move_label.pack(side=tk.LEFT, padx=30)
        
        # Computer move display
        self.computer_move_label = ttk.Label(
            self.moves_frame,
            text="Computer's move: -",
            style="Move.TLabel"
        )
        self.computer_move_label.pack(side=tk.LEFT, padx=30)
        
        # Reset button with modern style
        style.configure(
            "Reset.TButton",
            font=("Helvetica", 14, "bold"),
            padding=10
        )
        self.reset_button = ttk.Button(
            self.main_frame,
            text="Reset Game",
            style="Reset.TButton",
            command=self.reset_game
        )
        self.reset_button.pack(pady=20)

    def create_choice_buttons(self):
        # Create style for buttons
        style = ttk.Style()
        style.configure(
            "Choice.TButton",
            font=("Helvetica", 32),
            padding=20
        )
        
        # Create buttons for each choice with hover effect
        for choice in ['rock', 'paper', 'scissors']:
            btn = ttk.Button(
                self.choices_frame,
                text=self.emoji_map[choice],
                style="Choice.TButton",
                command=lambda c=choice: self.play_round(c)
            )
            btn.pack(side=tk.LEFT, padx=20)

    def play_round(self, player_choice):
        if self.game_over:
            return
            
        # Get computer's choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        # Update move displays
        self.player_move_label.config(
            text=f"Your move: {self.emoji_map[player_choice]}"
        )
        self.computer_move_label.config(
            text=f"Computer's move: {self.emoji_map[computer_choice]}"
        )
        
        # Determine winner
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update scores and result
        if result == "player":
            self.player_score += 1
            self.result_label.config(text="You win! 🎉")
        elif result == "computer":
            self.computer_score += 1
            self.result_label.config(text="Computer wins! 🤖")
        else:
            self.result_label.config(text="It's a tie! 🤝")
        
        # Update score display
        self.update_score_display()
        
        # Check for game over
        if self.player_score >= self.win_condition or self.computer_score >= self.win_condition:
            self.game_over = True
            winner = "Player" if self.player_score >= self.win_condition else "Computer"
            self.result_label.config(
                text=f"Game Over! {winner} wins the game! 🏆",
                foreground="#FFA500"  # Orange color for game over
            )
            self.disable_choice_buttons()

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        
        winning_combinations = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        
        if winning_combinations[player_choice] == computer_choice:
            return "player"
        return "computer"

    def update_score_display(self):
        self.player_score_label.config(text=f"👤 Player: {self.player_score}")
        self.computer_score_label.config(text=f"🤖 Computer: {self.computer_score}")

    def disable_choice_buttons(self):
        for child in self.choices_frame.winfo_children():
            child.configure(state='disabled')

    def enable_choice_buttons(self):
        for child in self.choices_frame.winfo_children():
            child.configure(state='normal')

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.game_over = False
        self.update_score_display()
        self.result_label.config(
            text="Choose your move!",
            foreground="#FF0000"  # Reset to red color
        )
        self.player_move_label.config(text="Your move: -")
        self.computer_move_label.config(text="Computer's move: -")
        self.enable_choice_buttons()

def main():
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main() 