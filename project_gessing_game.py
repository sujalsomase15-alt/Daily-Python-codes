from py_compile import main
import random
import os

class GuessingGame:
    def __init__(self,mini_num=1, max_num=100):
        self.min_num = mini_num
        self.max_num = max_num
        self.secreat_number = None
        self.attempts = 0
        self.best_score = None
        self.game_over = False
        self.reset_game()

    def reset_game(self):
        """Reset the game state and generate a new secret number."""
        self.secreat_number = random.randint(self.min_num, self.max_num)
        self.attempts = 0
        self.game_over = False 
        print(f"\n🔁New game! Guess a number between {self.min_num} and {self.max_num}.")

    def get_guess(self):
        """Get and validate user input"""
        while True:
            try:
                guess = input(f"\n🔢 Enteryour guess ({self.min_num}-{self.max_num}): ")
                if guess.lower() in ['quit', 'exit', 'q']:
                    return None
                guess_num = int(guess)
                if guess_num < self.min_num or guess_num > self.max_num:
                    print(f"⚠️ Please enter a number between {self.min_num} and {self.max_num}.")
                    continue
                return guess_num
            except ValueError:
                print("❌ Please enter a valid number!")

    def play_round(self):
        """play one round of the game"""
        if self.game_over:
            print("⛔ Game over! Type 'new' to start a new game.")
            return

        guess = self.get_guess()
        if guess is None:
            print("👋 Exiting the game. Goodbye!")
            self.game_over = True
            return

        self.attempts += 1

        if guess == self.secreat_number:

            self.game_over = True
            print(f"\n🎉 Perfect! You guessed the number in {self.attempts} attempts{'s' if self.attempts > 1 else ''}!")
            print(f"🔢 The number was {self.secreat_number}")

            if self.best_score is None or self.attempts < self.best_score:
                self.best_score = self.attempts
                print(f"🏆 New best score!🎊")
            else:
                print(f"🥈 Your best score is {self.best_score} attempts")
                return True
        else:
            hint = "higher ⬆️" if guess < self.secreat_number else "lower ⬇️"
            print(f"❌ {guess} is too {'low' if guess < self.secreat_number else 'high'}. Try {hint}")
            print(f"📊 Attempts: {self.attempts}")
            return True

    def show_stats(self):
        """Display current statistics"""
        print("\n" + "=+"*40)
        print(f"📊 STATISTICS")
        print("="*40)
        print(f"🎯 Range: {self.min_num} - {self.max_num}")
        print(f"🔢 Attempts: {self.attempts}")
        if self.best_score:
            print(f"🏆 Best Score: {self.best_score} attempts")
        else:
            print("🏆 Best Score:--")
        if not self.game_over and self.secreat_number:
            print(f"🔍 Hint: Number is {'higher' if self.secreat_number > 50 else 'lower'} than 50")
        print("="*40)

    def run(self):
        """Main game loop"""
        print("\n" + "🎯GUESSING GAME🎯". center(50))
        print("="*50)
        print(f"🎮 Guessing a number between {self.min_num} and {self.max_num}")
        print("💡 Commands: 'quit' to 'exit','stats' for statistics, 'new' for new game")
        print("="*50)

        while True:
            if not self.game_over:
                print(f"\n📌 Attempt #{self.attempts + 1}")

            action = input("\n❓ what would you like do? [guess/stats/new/quit]: ").strip().lower()

            if action in ['quit', 'exit', 'q']:
                print("👋 Exiting the game. Goodbye!")
                break
            elif action in ['stats', 's']:
                self.show_stats()
            elif action in ['new', 'n']:
                self.reset_game()
            elif action in ['guess', 'g', '']:  
                if not self.play_round():
                    break
            else:
                print("❌ Unknown command. Try:guess, stats, new or quit.")

def main():
    """Main entry point"""
    print("\n🎯WELCOME TO THE GUESSING GAME!🎯")
    print("="*50)

    while True:
        try:
            use_custom = input("use custom range?(y/n):").lower()
            if use_custom in ['y', 'yes']:
                min_num = int(input("enter minimum number:"))
                max_num = int(input("enter maximum number:"))
                if min_num >= max_num:
                    print("⚠️ Minimum number must be less than maximum number. Try again.")
                    continue
                game = GuessingGame(min_num, max_num)
            else:
                game = GuessingGame()
            break
        except ValueError:
            print("❌ Please enter valid numbers!")

    game.run()
    game.show_stats()
    print("👋 Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()