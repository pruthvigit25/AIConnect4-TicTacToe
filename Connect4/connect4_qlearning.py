import numpy as np
import pygame
import time
import random
pygame.init()

WIDTH, HEIGHT = 350, 300

window = pygame.display.set_mode((WIDTH, HEIGHT))

boardX, boardY = 7, 6

board = np.zeros([boardY, boardX])
Qlearn = np.random.rand(boardY, boardX)


game_running = True
no_winner = True

AI_wins = 0
AI_lose = 0

iteration = 0
target = 500


def connect_four(piece, matrix):
    for c in range(boardX-3):
        for r in range(boardY):
            if matrix[r][c] == piece and matrix[r][c+1] == piece and matrix[r][c+2] == piece and matrix[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(boardX):
        for r in range(boardY-3):
            if matrix[r][c] == piece and matrix[r+1][c] == piece and matrix[r+2][c] == piece and matrix[r+3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(boardX-3):
        for r in range(boardY-3):
            if matrix[r][c] == piece and matrix[r+1][c+1] == piece and matrix[r+2][c+2] == piece and matrix[r+3][c+3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(boardX-3):
        for r in range(3, boardY):
            if matrix[r][c] == piece and matrix[r-1][c+1] == piece and matrix[r-2][c+2] == piece and matrix[r-3][c+3] == piece:
                return True
    else:
        return False


def options(matrix):
    filtered = []
    ally, allx = np.where(matrix == 0)
    filter = {i: [] for i in allx}
    for pos, val in enumerate(allx):
        filter[val].append(ally[pos])

    filtered = [(z, max(filter[z])) for z in filter]
    return filtered


def can_win(potentialMove):
    for next in potentialMove:
        hmove = np.copy(board)
        hmove[next[1]][next[0]] = 1
        if connect_four(1, hmove):
            return(next)
    return(False)


def can_lose(potentialMove, nextboard):
    for next in potentialMove:
        hmove = np.copy(nextboard)
        hmove[next[1]][next[0]] = -1
        if connect_four(-1, hmove):
            return(next)
    return(False)


def it_trap(next):
    hmove = np.copy(board)
    hmove[next[1]][next[0]] = 1
    ops = options(hmove)
    if can_lose(ops, hmove):
        return True
    return False


def pick_max(postions):
    moves = [[Qlearn[y, x], (x, y)] for x, y in postions]
    moves.sort()
    return moves


def move():
    positions = options(board)

    move = can_win(positions)

    if move is False:
        coloumn = pick_max(positions)
        if it_trap(coloumn[0][1]) and len(coloumn) > 1:
            move = coloumn[1][1]
        else:
            move = coloumn[0][1]

    print(positions)
    print(move)

    board[move[1]][move[0]] = 1
    return board


def randomPlay():
    option = options(board)
    move = random.choice(option)
    board[move[1]][move[0]] = -1
    return board


def draw_screen():
    window.fill((0, 0, 50))
    for (x, y), val in np.ndenumerate(board):
        if val == 1:
            color = (255, 0, 0)
        elif val == -1:
            color = (255, 255, 0)
        else:
            color = (0, 0, 0)
        pygame.draw.rect(
            window, color, [50*y, 50*x, WIDTH/boardX, HEIGHT/boardY])
    pygame.display.update()


while game_running and iteration < target:
    board = np.zeros([boardY, boardX])
    Qlearn = np.random.rand(boardY, boardX)
    no_winner = True
    iteration += 20
    while no_winner:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        board = (move())
        draw_screen()

        board = (randomPlay())
        draw_screen()
        print(board)
        if connect_four(1, board):
            print("AI WINS")
            AI_wins += 1
            no_winner = False

        elif connect_four(-1, board):
            print("Opponent WINS")
            no_winner = False
            AI_lose += 1

        elif np.count_nonzero(board == 0) <= 0:
            print("It's A TIE")
            no_winner = False

print(f"AI:{AI_wins} \n Opponent: {AI_lose}")