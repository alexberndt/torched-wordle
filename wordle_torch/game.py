import random
from typing import List
from pathlib import Path
from wordle_torch.response import Response
import numpy as np

class WordleGame:
    def __init__(self, guesses: list[str], answers: list[str], solution: str):
        self.valid_guesses = guesses
        self.possible_solutions = answers

        if solution not in self.possible_solutions:
            raise Exception(f"Answer '{solution}' not a valid answer word ...")
        self.answer = solution

        self.guess_count = 0

    def guess(self, guess_word : str) -> List[Response]:

        if guess_word not in self.valid_guesses + self.possible_solutions:
            raise Exception(f"Guess '{guess_word}' not a valid guess word ...")

        response = self._analyze_guess(guess_word)
        self.guess_count += 1

        return response


    def _analyze_guess(self, guess_word : str, answer_word : str = None) -> List[Response]:

        answer_word = self.answer if answer_word is None else answer_word

        answer_wordlist = np.array(list(answer_word))
        guess_wordlist = np.array(list(guess_word))

        green = np.zeros(5, dtype=bool)
        yellow = np.zeros(5, dtype=bool)

        response = 5*[Response.GREY]

        # find all the greens (right letter, right spot)
        for idx, char in enumerate(guess_wordlist):
            if char == answer_wordlist[idx]:
                green[idx] = True
                response[idx] = Response.GREEN

        # find all the yellows (right letter, wrong spot) in remaining letters
        chars_seen = []
        for idx, char in enumerate(guess_wordlist):
            if green[idx]:
                continue

            if char in answer_wordlist[~green] and char not in chars_seen:
                yellow[idx] = True
                response[idx] = Response.YELLOW
                chars_seen.append(char)

        return response