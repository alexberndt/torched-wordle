from wordle_torch.game import WordleGame
from wordle_torch.response import Response as Response


def test_basic():
    game = WordleGame("spilt")
    assert game.guess("spoil") == [Response.GREEN, Response.GREEN, Response.GREY, Response.YELLOW, Response.YELLOW]


def test_answer_abbey_1():
    game = WordleGame("abbey")
    assert game.guess("algae") == [Response.GREEN, Response.GREY, Response.GREY, Response.GREY, Response.YELLOW]
    assert game.guess("keeps") == [Response.GREY, Response.YELLOW, Response.GREY, Response.GREY, Response.GREY]
    assert game.guess("orbit") == [Response.GREY, Response.GREY, Response.GREEN, Response.GREY, Response.GREY]
    assert game.guess("abate") == [Response.GREEN, Response.GREEN, Response.GREY, Response.GREY, Response.YELLOW]
    assert game.guess("abbey") == [Response.GREEN, Response.GREEN, Response.GREEN, Response.GREEN, Response.GREEN]
      

def test_answer_abbey_2():
    game = WordleGame("abbey")
    assert game.guess("opens") == [Response.GREY, Response.GREY, Response.YELLOW, Response.GREY, Response.GREY]
    assert game.guess("babes") == [Response.YELLOW, Response.YELLOW, Response.GREEN, Response.GREEN, Response.GREY]
    assert game.guess("kebab") == [Response.GREY, Response.YELLOW, Response.GREEN, Response.YELLOW, Response.YELLOW]
    assert game.guess("abyss") == [Response.GREEN, Response.GREEN, Response.YELLOW, Response.GREY, Response.GREY]
    assert game.guess("abbey") == [Response.GREEN, Response.GREEN, Response.GREEN, Response.GREEN, Response.GREEN]


def test_answer_shire():
    game = WordleGame("shire")
    assert game.guess("adieu") == [Response.GREY, Response.GREY, Response.GREEN, Response.YELLOW, Response.GREY]
    assert game.guess("ships") == [Response.GREEN, Response.GREEN, Response.GREEN, Response.GREY, Response.GREY]
    assert game.guess("shive") == [Response.GREEN, Response.GREEN, Response.GREEN, Response.GREY, Response.GREEN]
    assert game.guess("shite") == [Response.GREEN, Response.GREEN, Response.GREEN, Response.GREY, Response.GREEN]
    assert game.guess("shine") == [Response.GREEN, Response.GREEN, Response.GREEN, Response.GREY, Response.GREEN]
    assert game.guess("shire") == [Response.GREEN, Response.GREEN, Response.GREEN, Response.GREEN, Response.GREEN]


def test_answer_elder():
    game = WordleGame("elder")
    assert game.guess("naval") == [Response.GREY, Response.GREY, Response.GREY, Response.GREY, Response.YELLOW]
    assert game.guess("evade") == [Response.GREEN, Response.GREY, Response.GREY, Response.YELLOW, Response.YELLOW]
    assert game.guess("fluff") == [Response.GREY, Response.GREEN, Response.GREY, Response.GREY, Response.GREY]
    assert game.guess("sunny") == [Response.GREY, Response.GREY, Response.GREY, Response.GREY, Response.GREY]
    assert game.guess("three") == [Response.GREY, Response.GREY, Response.YELLOW, Response.GREEN, Response.YELLOW]
    assert game.guess("paddy") == [Response.GREY, Response.GREY, Response.GREEN, Response.GREY, Response.GREY]
    assert game.guess("elder") == [Response.GREEN, Response.GREEN, Response.GREEN, Response.GREEN, Response.GREEN]


def test_answer_fluff():
    game = WordleGame("fluff")
    assert game.guess("naval") == [Response.GREY, Response.GREY, Response.GREY, Response.GREY, Response.YELLOW]


def test_answer_crimp():
    game = WordleGame("crimp")
    assert game.guess("raise") == [Response.YELLOW, Response.GREY, Response.GREEN, Response.GREY, Response.GREY]
    assert game.guess("mount") == [Response.YELLOW, Response.GREY, Response.GREY, Response.GREY, Response.GREY]
    assert game.guess("grime") == [Response.GREY, Response.GREEN, Response.GREEN, Response.GREEN, Response.GREY]
    assert game.guess("crimp") == [Response.GREEN, Response.GREEN, Response.GREEN, Response.GREEN, Response.GREEN]