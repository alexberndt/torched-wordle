import random
from typing import List
from pathlib import Path
from wordle_torch.utils import read_file
from wordle_torch.response import Response as r
import numpy as np

class WordleGame:
    def __init__(self, answer : str = None):

        root_dir = Path(__file__).resolve().parents[2]
        guesses_file = root_dir / 'assets/guesses'
        self.guesses = read_file(guesses_file)

        answers_file = root_dir / 'assets/wordlist'
        self.answers = read_file(answers_file)

        if answer not in self.answers:
            raise Exception(f"Answer '{answer}' not a valid answer word ...")

        self.answer = random.choice(self.answers) if answer is None else answer
        self.guess_count = 0


    def guess(self, guess_word : str) -> List[str]:

        if guess_word not in self.guesses + self.answers:
            raise Exception(f"Guess '{guess_word}' not a valid guess word ...")

        response = self._analyze_guess(guess_word)
        self.guess_count += 1

        return response


    def _analyze_guess(self, guess_word : str, answer_word : str = None) -> List[r]:

        answer_word = self.answer if answer_word is None else answer_word

        answer_wordlist = np.array(list(answer_word))
        guess_wordlist = np.array(list(guess_word))

        green = np.zeros(5, dtype=bool)
        yellow = np.zeros(5, dtype=bool)

        response = 5*[r.GREY]

        # find all the greens (right letter, right spot)
        for idx, char in enumerate(guess_wordlist):
            if char == answer_wordlist[idx]:
                green[idx] = True
                response[idx] = r.GREEN

        # find all the yellows (right letter, wrong spot) in remaining letters
        chars_seen = []
        for idx, char in enumerate(guess_wordlist):
            if green[idx]:
                continue

            if char in answer_wordlist[~green] and char not in chars_seen:
                yellow[idx] = True
                response[idx] = r.YELLOW
                chars_seen.append(char)

        return response