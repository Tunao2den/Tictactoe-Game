class Players:
    def __init__(self, name):
        self.name = name


    def print_names():
        name1=input("Enter the name for player 1: ")
        name2=input("Enter the name for player 2: ")
        player1 = Players(name1)
        player2 = Players(name2)
        return[player1, player2]
