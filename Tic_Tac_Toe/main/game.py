from copy import deepcopy


class TicTacToe:
    def __init__(self, other=None):
        self.board = [["   ", "   ", "   "] for i in range(3)]
        self.player = "X"
        self.oppon = "O"
        if other:
            self.__dict__ = deepcopy(other.__dict__)

    def checkmove(self, inp):
        b = TicTacToe(self)
        b.board[inp // 3][inp % 3] = " " + b.player + " "
        (b.player, b.oppon) = (b.oppon, b.player)
        return b

    def checktie(self):
        t = True
        for i in self.board:
            for k in i:
                if k == "   ":
                    t = False
        return t

    def check_game(self):
        if self.checktie():
            return "checktie!"
        for i in range(3):
            if self.board[i][0] != "   " and \
                    self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return f"{self.board[i][0][1:]}has won!"

            if self.board[0][i] != "   " and \
                    self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return f"{self.board[0][i][1:]}has won!"

        if self.board[0][0] != "   " and \
                self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return f"{self.board[0][0][1:]}has won!"

        if self.board[0][2] != "   " and \
                self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return f"{self.board[0][2][1:]}has won!"

        return False

    def checkwon(self):
        for i in range(3):
            if self.board[i][0] == f" {self.oppon} " and \
                    self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return True

            if self.board[0][i] == f" {self.oppon} " and \
                    self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return True

        if self.board[0][0] == f" {self.oppon} " and \
                self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return True

        if self.board[0][2] == f" {self.oppon} " and \
                self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return True

        return False

    def __str__(self):
        return "".join([x for i in self.board for x in ["".join([z for k in i for z in [k, "|"]][:-1]) +
                                                        "\n", "-----------" + "\n"]][:-1])

    def checkbestmove(self):
        return self._minimax(True)[1]

    def _minimax(self, player):
        if self.checkwon():
            if player:
                return (-1, None)
            else:
                return (1, None)

        elif self.checktie():
            return (0, None)

        elif player:
            checkbestmove = (-2, None)
            for i in range(9):
                if self.board[i // 3][i % 3] == "   ":
                    value = self.checkmove(i)._minimax(not (player))[0]
                    if value > checkbestmove[0]:
                        checkbestmove = (value, i)
            return checkbestmove

        else:
            checkbestmove = (2, None)
            for i in range(9):
                if self.board[i // 3][i % 3] == "   ":
                    value = self.checkmove(i)._minimax(not (player))[0]
                    if value < checkbestmove[0]:
                        checkbestmove = (value, i)
            return checkbestmove


if __name__ == "__main__":
    t = TicTacToe()
    print(t)

    while True:
        t = t.checkmove(int(input(":")) - 1)
        m = t.checkbestmove()
        t = t.checkmove(m)
        print(t)
