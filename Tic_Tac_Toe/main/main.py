import sys
from ui import *
from game import TicTacToe


class TicTac(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.btns = [
            self.ui.pb_1,
            self.ui.pb_2,
            self.ui.pb_3,
            self.ui.pb_4,
            self.ui.pb_5,
            self.ui.pb_6,
            self.ui.pb_7,
            self.ui.pb_8,
            self.ui.pb_9
        ]

        for i, btn in enumerate(self.btns):
            btn.clicked.connect(lambda _, b=i: self.pb(b))
        self.ui.pb_reset.clicked.connect(self.resetgame)
        self.tic = TicTacToe()

    def pb(self, n):
        if self.btns[n].text() == "":
            self.tic = self.tic.checkmove(n)
            if self.updategame():
                checkmove = self.tic.checkbestmove()
                self.tic = self.tic.checkmove(checkmove)
                self.updategame()

    def updategame(self):
        for i in range(9):
            self.btns[i].setText(self.tic.board[i // 3][i % 3].strip())
        s = self.tic.check_game()
        if s:
            QtWidgets.QMessageBox.about(self, "Game!", s)
            self.resetgame()
            return False
        return True

    def resetgame(self):
        self.tic = TicTacToe()
        self.updategame()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = TicTac()
    myapp.show()
    sys.exit(app.exec_())
