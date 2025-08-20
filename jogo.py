import pygame
import sys

# Inicialização do pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Cores RGB
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CROWN = pygame.transform.scale(pygame.image.load("crown.png"), (44, 25))  # você precisa dessa imagem na pasta

# Janela
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Damas FODA")

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, RED))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLUE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def get_piece(self, row, col):
        return self.board[row][col]

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = 0, piece
        piece.move(row, col)
        if row == 0 or row == ROWS - 1:
            piece.make_king()

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0

    def get_valid_moves(self, piece):
        moves = {}
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in directions:
            row, col = piece.row + dr, piece.col + dc
            if 0 <= row < ROWS and 0 <= col < COLS:
                target = self.get_piece(row, col)
                if target == 0:
                    moves[(row, col)] = []
                elif target.color != piece.color:
                    jump_row, jump_col = row + dr, col + dc
                    if 0 <= jump_row < ROWS and 0 <= jump_col < COLS:
                        if self.get_piece(jump_row, jump_col) == 0:
                            moves[(jump_row, jump_col)] = [target]
        return moves

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    turn = BLUE
    selected_piece = None
    valid_moves = {}

    while run:
        clock.tick(60)

        board.draw(WIN)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if selected_piece:
                    if (row, col) in valid_moves:
                        board.move(selected_piece, row, col)
                        captured = valid_moves[(row, col)]
                        board.remove(captured)
                        selected_piece = None
                        valid_moves = {}
                        turn = RED if turn == BLUE else BLUE
                    else:
                        selected_piece = None
                        valid_moves = {}
                piece = board.get_piece(row, col)
                if piece != 0 and piece.color == turn:
                    selected_piece = piece
                    valid_moves = board.get_valid_moves(piece)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


