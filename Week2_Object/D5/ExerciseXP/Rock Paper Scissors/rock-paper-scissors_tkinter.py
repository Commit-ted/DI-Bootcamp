import tkinter as tk
from game import Game

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")

        # Initialize game results
        self.results = {'win': 0, 'loss': 0, 'draw': 0}

        # Create and place widgets
        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play_game('r'), width=15, height=2)
        self.rock_button.pack(pady=10)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play_game('p'), width=15, height=2)
        self.paper_button.pack(pady=10)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play_game('s'), width=15, height=2)
        self.scissors_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        self.score_button = tk.Button(root, text="Show Scores and Exit", command=self.show_scores, width=25, height=2)
        self.score_button.pack(pady=10)

    def play_game(self, user_choice):
        game = Game()
        computer_choice = game.get_computer_item()
        result = game.get_game_result(user_choice, computer_choice)

        # Update the results
        self.results[result] += 1

        # Display the result of the current game
        result_text = f"You chose: {self.get_full_choice(user_choice)}. Computer chose: {self.get_full_choice(computer_choice)}. Result: {result.capitalize()}."
        self.result_label.config(text=result_text)

    def get_full_choice(self, choice):
        choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
        return choices[choice]

    def show_scores(self):
        # Display the game summary in a popup window
        summary_text = (
            f"Game Results:\n"
            f"You won {self.results['win']} times\n"
            f"You lost {self.results['loss']} times\n"
            f"You drew {self.results['draw']} times\n"
            f"\nThank you for playing!"
        )

        summary_window = tk.Toplevel(self.root)
        summary_window.title("Game Summary")

        summary_label = tk.Label(summary_window, text=summary_text, font=("Helvetica", 12))
        summary_label.pack(pady=20)

        exit_button = tk.Button(summary_window, text="Exit", command=self.root.quit, width=15, height=2)
        exit_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
