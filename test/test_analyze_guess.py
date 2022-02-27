from wordle_torch.game import WordleGame
from wordle_torch.response import Response as r


def test_basic():

    game = WordleGame("spilt")
    response = game.guess("spoil")
    expected = [r.GREEN, r.GREEN, r.GREY, r.YELLOW, r.YELLOW]
    assert expected == response

def test_answer_abbey_1():

    game = WordleGame("abbey")

    assert game.guess("algae") == [r.GREEN, r.GREY, r.GREY, r.GREY, r.YELLOW]
    assert game.guess("keeps") == [r.GREY, r.YELLOW, r.GREY, r.GREY, r.GREY]
    assert game.guess("orbit") == [r.GREY, r.GREY, r.GREEN, r.GREY, r.GREY]
    assert game.guess("abate") == [r.GREEN, r.GREEN, r.GREY, r.GREY, r.YELLOW]
    assert game.guess("abbey") == [r.GREEN, r.GREEN, r.GREEN, r.GREEN, r.GREEN]
      

def test_answer_abbey_2():

    game = WordleGame("abbey")

    assert game.guess("opens") == [r.GREY, r.GREY, r.YELLOW, r.GREY, r.GREY]
    assert game.guess("babes") == [r.YELLOW, r.YELLOW, r.GREEN, r.GREEN, r.GREY]
    assert game.guess("kebab") == [r.GREY, r.YELLOW, r.GREEN, r.YELLOW, r.YELLOW]
    assert game.guess("abyss") == [r.GREEN, r.GREEN, r.YELLOW, r.GREY, r.GREY]
    assert game.guess("abbey") == [r.GREEN, r.GREEN, r.GREEN, r.GREEN, r.GREEN]


def test_answer_shire():

    game = WordleGame("shire")

    assert game.guess("adieu") == [r.GREY, r.GREY, r.GREEN, r.YELLOW, r.GREY]
    assert game.guess("ships") == [r.GREEN, r.GREEN, r.GREEN, r.GREY, r.GREY]
    assert game.guess("shive") == [r.GREEN, r.GREEN, r.GREEN, r.GREY, r.GREEN]
    assert game.guess("shite") == [r.GREEN, r.GREEN, r.GREEN, r.GREY, r.GREEN]
    assert game.guess("shine") == [r.GREEN, r.GREEN, r.GREEN, r.GREY, r.GREEN]
    assert game.guess("shire") == [r.GREEN, r.GREEN, r.GREEN, r.GREEN, r.GREEN]


def test_answer_elder():

    game = WordleGame("elder")

    assert game.guess("naval") == [r.GREY, r.GREY, r.GREY, r.GREY, r.YELLOW]
    assert game.guess("evade") == [r.GREEN, r.GREY, r.GREY, r.YELLOW, r.YELLOW]
    assert game.guess("fluff") == [r.GREY, r.GREEN, r.GREY, r.GREY, r.GREY]
    assert game.guess("sunny") == [r.GREY, r.GREY, r.GREY, r.GREY, r.GREY]
    assert game.guess("three") == [r.GREY, r.GREY, r.YELLOW, r.GREEN, r.YELLOW]
    assert game.guess("paddy") == [r.GREY, r.GREY, r.GREEN, r.GREY, r.GREY]
    assert game.guess("elder") == [r.GREEN, r.GREEN, r.GREEN, r.GREEN, r.GREEN]

def test_answer_fluff():

    game = WordleGame("fluff")

    assert game.guess("naval") == [r.GREY, r.GREY, r.GREY, r.GREY, r.YELLOW]
