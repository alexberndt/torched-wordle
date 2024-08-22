

from dataclasses import dataclass
from enum import Enum
from typing import Iterable
# import re
import pandas as pd 
from functools import partial 
import time 
class Predicate(Enum):
    green = 0
    yellow = 1
    grey = 2

@dataclass
class Condition:
    position: int
    predicate: Predicate
    letter: str

def main():

    df = pd.read_parquet("data/wordle-valid-answers.parquet")
    print(len(df))

    

    # # Add green, yellow, grey responses from Wordle gameplay
    conditions = [
        Condition(0, Predicate.yellow, "t"),
        Condition(1, Predicate.green, "r"),
        Condition(4, Predicate.green, "e"),
        # Condition(2, Predicate.yellow, "u"),
        # Condition(1, Predicate.green, "u"),
        # Condition(3, Predicate.green, "c"),
        # Condition(4, Predicate.green, "h"),
        # Condition(0, Predicate.yellow, "l"),
    ]
    conditions += [Condition(0, Predicate.grey, letter) for letter in ["a", "c"]]

    print(df.columns)

    conditional_matches = partial(word_matches_all_conditions, conditions=conditions)
    df_filtered = df[df["word"].apply(conditional_matches)]

    print(f"{len(df_filtered)} / {len(df)}")
    print(df_filtered["word"].tolist())


def word_matches_all_conditions(word: str, conditions: Iterable[Condition]):
    for condition in conditions:
        if not word_matches_condition(word, condition):
            return False
    return True

        
def word_matches_condition(word: str, condition: Condition) -> bool:
    position = condition.position
    predicate = condition.predicate
    character = condition.letter

    if predicate == Predicate.green:
        return word[position] == character
    elif predicate == Predicate.yellow:
        return character in word and word[position] != character
    elif predicate == Predicate.grey:
        return character not in word


if __name__ == "__main__":
    main()