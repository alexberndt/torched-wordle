

from enum import Enum
# import re
import pandas as pd 
from functools import partial 

class Predicate(Enum):
    green = 0
    yellow = 1
    grey = 2

def main():

    df = pd.read_parquet("data/wordle-valid-answers.parquet")
    print(len(df))
    print(df.columns)

    # df_txt = pd.read_csv("data/wordle-valid-answers.txt", header=None)
    # df_txt = df_txt.rename(columns={0: "word"})

    # df.to_parquet("data/wordle_list.parquet")

    # df_2 = pd.read_csv("data/wordle_accepted_words.txt")
    # print(len(df_2))

    # input:
    # - a = 1
    # - p != 4

    conditions = [
        # (0, Predicate.eqals, "a"),
        (0, Predicate.green, "l"),
        (1, Predicate.green, "a"),
        # (1, Predicate.not_equals, "l"),
    ]

    conditions += [(0, Predicate.grey, letter) for letter in ["w", "e", "r", "t", "u", "i", "o", "p", "s", "f", "h", "c"]]

    print(df.columns)

    conditional_matches = partial(word_matches_all_conditions, conditions=conditions)
    df_filtered = df[df["word"].apply(conditional_matches)]

    print(len(df_filtered))
    print(len(df))
    print(df_filtered["word"].tolist())


def word_matches_all_conditions(word, conditions):
    for condition in conditions:
        if not word_matches_condition(word, condition):
            return False
    return True

        
def word_matches_condition(word, condition) -> bool:
    position = condition[0]
    predicate = condition[1]
    character = condition[2]

    if predicate == Predicate.green:
        return word[position] == character
    elif predicate == Predicate.yellow:
        return character in word and word[position] != character
    elif predicate == Predicate.grey:
        return character not in word


if __name__ == "__main__":
    main()