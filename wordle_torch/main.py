from wordle_torch.game import WordleGame
from wordle_torch.utils import read_file

def main():

    guesses_file = 'assets/guesses'
    guesses = read_file(guesses_file)

    answers_file = 'assets/wordlist'
    answers = read_file(answers_file)

    game = WordleGame(guesses, answers, solution="abbey")

    response = game.guess("keeps")
    print(response)
    
if __name__ == "__main__":
    main()