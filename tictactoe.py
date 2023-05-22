class Tictacoe:
    def __init__(self):
        self.deck = {1:"   ",2:"   ",3:"   ",4:"   ",5:"   ",6:"   ",7:"   ",8:"   ",9:"   "}
        players=Players.print_names()
        self.current_player = players[0]
        self.player1 = players[0]
        self.player2 = players[1]


    def show_deck(self):
        print("    1   2   3")
        print(f"a  {self.deck[1]}|{self.deck[2]}|{self.deck[3]}")
        print("   ———|———|———")
        print(f"b  {self.deck[4]}|{self.deck[5]}|{self.deck[6]}")
        print("   ———|———|———")
        print(f"c  {self.deck[7]}|{self.deck[8]}|{self.deck[9]}")


    def check_empty(self):
        for key,value in self.deck.items():
            if value =="   ":
                return True


    def take_position(self):
        print(f"{self.current_player.name}'s turn")
        position_map = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        while True:
            a=False
            position = input(f"Enter the which position you want to play {self.current_player.name}: ")
            if position not in position_map:
                print("Invalid input")
            else:
                for i in range(len(position_map)):
                    if position == position_map[i]:
                        position_key=i+1
                if self.deck[position_key]!="   ":
                    print("This position is already blanked!")   
                else:
                    a = True
                    return position_key
            if a:
                break


    def determine_letter(self):
        if self.current_player == self.player1:
                self.letter = " x "
        if self.current_player == self.player2:
            self.letter = " o "
        return self.letter
    
    def tie(self):
        counter = 0
        if self.check_for_winner()==True:
            return False
        else:
            for value in self.deck.items():
                if value !="   ":
                    counter +=1
            if counter>=9:
                return True
    

    def check_for_winner(self):
        for i in range(1,8,3):
            if self.deck[i] == self.deck[i+1] == self.deck[i+2]:
                if self.deck[i]!="   ":
                    return True
        for i in range(1,4):
            if self.deck[i] == self.deck[i+3] == self.deck[i+6]:
                if self.deck[i]!="   ":
                    return True
        if self.deck[1] == self.deck[5] == self.deck[9]:
            if self.deck[1]!="   ":
                return True
        if self.deck[3] == self.deck[5] == self.deck[7]:
            if self.deck[3]!="   ":
                return True


    def change_current(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


    def play(self):
            self.show_deck()
            while self.check_empty():
                position=self.take_position()
                self.deck[position] = self.determine_letter()
                self.show_deck()
                if self.check_for_winner():
                    print(self.current_player.name+" wins!")
                    break
                self.change_current()
            if self.tie():
                print("Tie!")
    

class Players:
    def __init__(self, name):
        self.name = name


    def print_names():
        name1=input("Enter the name for player 1: ")
        name2=input("Enter the name for player 2: ")
        player1 = Players(name1)
        player2 = Players(name2)
        print(player1.name)
        print(player2.name)
        return[player1, player2]
     
        
def main():
    while True:
        game = Tictacoe()
        game.play()
        c=int(input("For play again enter 1 - For quit press enter: "))
        if c==1:
            continue
        else:
            break


if __name__ == '__main__':
    main()