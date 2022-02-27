from wordle_torch.game import WordleGame

def main():

    game = WordleGame("abbey")

    response = game.guess("keeps")
    print(response)
    
if __name__ == "__main__":
    main()