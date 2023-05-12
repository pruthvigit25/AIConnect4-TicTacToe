import pygame
import sys

pygame.init()

SIZE = WIDTH, HEIGHT = 640, 640

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

CELL_SIZE = 80

FONT_SIZE = 40
FONT = pygame.font.SysFont(None, FONT_SIZE)

pygame.display.set_caption("Connect 4")

screen = pygame.display.set_mode(SIZE)

board = [[0] * 7 for _ in range(6)]

current_player = 1

def draw_board(board):
    """
    Draws the Connect 4 board on the screen.
    """
    for row in range(6):
        for col in range(7):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE))
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 5)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 5)


def get_row_col(x, y):
    """
    Converts the (x, y) coordinates to the row and column on the board.
    """
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col


def is_valid_move(board, col):
    """
    Checks if a move is valid in the given column.
    """
    return board[0][col] == 0


def get_next_open_row(board, col):
    """
    Gets the next open row in the given column.
    """
    for row in range(5, -1, -1):
        if board[row][col] == 0:
            return row
    return -1


def has_won(board, player):
    """
    Checks if the given player has won the game.
    """
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True

    # Check vertical
    for row in range(3):
        for col in range(7):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True

    # Check diagonal (up right)
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True

    # Check diagonal (up left)
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == player and board[row+3][col-3] == player:
                return True

    return False

def draw_text(text, color, x, y):
    """
    Draws text on the screen.
    """
    surface = FONT.render(text, True, color)
    rect = surface.get_rect()
    rect.center = (x, y)
    screen.blit(surface, rect)


def switch_player():
    """
    Switches the current player.
    """
    global current_player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1


def game_over():
    """
    Checks if the game is over.
    """
    if has_won(board, 1):
        draw_text("Player 1 wins!", RED, WIDTH // 2, HEIGHT // 2)
        return True
    elif has_won(board, 2):
        draw_text("Player 2 wins!", YELLOW, WIDTH // 2, HEIGHT // 2)
        return True
    elif all(board[i][j] != 0 for i in range(6) for j in range(7)):
        draw_text("Tie game!", BLACK, WIDTH // 2, HEIGHT // 2)
        return True
    else:
        return False


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = get_row_col(x, y)
            if is_valid_move(board, col):
                next_open_row = get_next_open_row(board, col)
                board[next_open_row][col] = current_player
                switch_player()

    screen.fill(WHITE)

    draw_board(board)

    if game_over():
        pygame.display.flip()
        pygame.time.wait(3000)
        board = [[0] * 7 for _ in range(6)]
        current_player = 1
        continue

    if current_player == 1:
        draw_text("Player 1's turn", RED, WIDTH // 2, FONT_SIZE // 2)
    else:
        draw_text("Player 2's turn", YELLOW, WIDTH // 2, FONT_SIZE // 2)

    pygame.display.flip()
