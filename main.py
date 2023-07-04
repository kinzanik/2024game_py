import os
from random import randint, choice
from termcolor import colored, cprint


class Board:
    def __init__(self):
        self.board = [[None, None, None, None], [None, None, None, None],
                      [None, None, None, None], [None, None, None, None]]
        a, b = randint(0, 3), randint(0, 3)
        self.board[a][b] = choice([2, 2, 2, 2, 4])
        while True:
            a, b = randint(0, 3), randint(0, 3)
            if self.board[a][b] == None:
                self.board[a][b] = choice([2, 4])
                break


    def print_board(self):
        print('-' * 29)
        for i in self.board:
            print('', end='I')
            for j in i:
                if j:
                    prob = 5 - len(str(j))
                    text = ' ' + str(j) + ' ' * prob
                    print(colored(text, 'red'), end='I')
                else:
                    print(' ' * 6, end='I')
            print()
            print('-' * 29)


    def sub(self):
        while True:
            a, b = randint(0, 3), randint(0, 3)
            if not self.board[a][b]:
                self.board[a][b] = choice([2, 2, 2, 2, 4])
                break

    def won(self):
        for i in self.board:
            if 2048 in i:
                return True

    def lose(self):
        for i in self.board:
            if None in i:
                return False
        return True

    def ret(self):
        return self.board.copy()


    def shag(self, pos):
        if pos == 'a':
            c = 0
            for i in self.board:
                if len(i) == 0:
                    continue
                new_row = []
                for j in i:
                    if j:
                        new_row.append(j)
                k = 0
                if len(new_row) > 1:
                    while k < len(new_row) - 1:
                        if new_row[k] == new_row[k + 1]:
                            new_row[k] = new_row[k] * 2
                            del new_row[k + 1]
                        k += 1
                while len(new_row) < 4:
                    new_row.append(None)
                self.board[c].clear()
                self.board[c] += new_row
                c += 1


        elif pos == 'd':
            c = 0
            for i in self.board:
                if len(i) == 0:
                    continue
                new_row = []
                for j in i:
                    if j:
                        new_row.append(j)
                k = 0
                if len(new_row) > 1:
                    while k < len(new_row) - 1:
                        if new_row[k] == new_row[k + 1]:
                            new_row[k] = new_row[k] * 2
                            del new_row[k + 1]
                        k += 1
                while len(new_row) < 4:
                    new_row.insert(0, None)
                self.board[c].clear()
                self.board[c] += new_row
                c += 1


        if pos == 'w':
            c = 0
            for i in range(4):
                new_row = []
                for j in range(4):
                    if self.board[j][i]:
                        new_row.append(self.board[j][i])
                k = 0
                if len(new_row) > 1:
                    while k < len(new_row) - 1:
                        if new_row[k] == new_row[k + 1]:
                            new_row[k] = new_row[k] * 2
                            del new_row[k + 1]
                        k += 1
                while len(new_row) < 4:
                    new_row.append(None)

                for j in range(4):
                    self.board[j][i] = new_row[j]

        if pos == 's':
            c = 0
            for i in range(4):
                new_row = []
                for j in range(4):
                    if self.board[j][i]:
                        new_row.append(self.board[j][i])
                k = 0
                if len(new_row) > 1:
                    while k < len(new_row) - 1:
                        if new_row[k] == new_row[k + 1]:
                            new_row[k] = new_row[k] * 2
                            del new_row[k + 1]
                        k += 1
                while len(new_row) < 4:
                    new_row.insert(0, None)
                reversed(new_row)
                for j in range(4):
                    self.board[j][i] = new_row[j]

        else:
            pass




def main():
    b = Board()
    print('Добро пожаловать в игру 2048!!!')
    while True:
        b.print_board()
        b1 = b.ret()
        print(b1)
        b.shag(input('Введите направление(w/a/s/d): '))
        os.system('cls')
        if b.won():
            print('Вы победили!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            break
        if b.lose():
            print('Проиграл((((((((((')
            break
        if b1 != b.ret().copy():
            b.sub()

if __name__ == '__main__':
    main()