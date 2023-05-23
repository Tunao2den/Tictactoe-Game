from tictactoe import Tictactoe

def main():
    while True:
        game = Tictactoe()
        game.play()
        c=int(input("For play again enter 1 - For quit press enter: "))
        if c==1:
            continue
        else:
            break


if __name__ == '__main__':
    main()
