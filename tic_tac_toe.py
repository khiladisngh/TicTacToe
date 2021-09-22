class TicTacToe:
    """
    Game mechanics
    """
    def __init__(self):
        self.turn = None
        self.count = None
        self.board = {'7': '   ', '8': '   ', '9': '   ',
                      '4': '   ', '5': '   ', '6': '   ',
                      '1': '   ', '2': '   ', '3': '   '}

    def print_board(self):
        """
        Prints the board to the user.
        """
        print(f"{self.board['7']}|{self.board['8']}|{self.board['9']}")
        print("---+---+---")
        print(f"{self.board['4']}|{self.board['5']}|{self.board['6']}")
        print("---+---+---")
        print(f"{self.board['1']}|{self.board['2']}|{self.board['3']}\n")

    def play_game(self):
        """
        Starts the game
        """
        self.turn = " X "
        self.count = 0
        for i in range(10):
            self.print_board()
            move = input(f"It's {self.turn}'s turn\n> ")

            if self.board[move] == "   ":
                self.board[move] = self.turn
                self.count += 1
            else:
                print("That place is already filled!")
                continue

            if self.count >= 5:
                if self.check_winner():
                    break

            if self.check_draw():
                break

            self.change_turn()
        self.restart_game()

    def restart_game(self):
        """
        Ask user to restart the game.
        """
        restart = input("Do you want to play again?(Y/N)")
        if restart.upper() == "Y":
            for key in self.board.keys():
                self.board[key] = "   "
            self.play_game()
        else:
            print("Thanks for playing!")

    def check_winner(self):
        """
        Check whether the player has won the game.
        """
        if self.check_horizontal() or self.check_vertical() or self.check_diagonal():
            print(f"\nThe winner is {self.turn}!")
            self.print_board()
            return True

    def check_horizontal(self):
        """
        Check if the horizontal cells match.
        """
        horizontal_1 = self.board['7'] == self.board['8'] == self.board['9'] != "   "
        horizontal_2 = self.board['4'] == self.board['5'] == self.board['6'] != "   "
        horizontal_3 = self.board['1'] == self.board['2'] == self.board['3'] != "   "

        if horizontal_1 or horizontal_2 or horizontal_3:
            return True

    def check_vertical(self):
        """
        Check if the vertical cells match.
        """
        vertical_1 = self.board['7'] == self.board['4'] == self.board['1'] != "   "
        vertical_2 = self.board['8'] == self.board['5'] == self.board['2'] != "   "
        vertical_3 = self.board['9'] == self.board['6'] == self.board['3'] != "   "

        if vertical_1 or vertical_2 or vertical_3:
            return True

    def check_diagonal(self):
        """
        Check if the diagonal cells match.
        """
        diagonal_1 = self.board['7'] == self.board['5'] == self.board['3'] != "   "
        diagonal_2 = self.board['9'] == self.board['5'] == self.board['1'] != "   "

        if diagonal_1 or diagonal_2:
            return True

    def check_draw(self):
        """
        Check if the match has been draw.
        """
        if self.count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

    def change_turn(self):
        """
        Changes the turn to the different player.
        """
        if self.turn == " X ":
            self.turn = " O "
        else:
            self.turn = " X "
