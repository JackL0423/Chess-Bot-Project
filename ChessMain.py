<<<<<<< HEAD
"""
This is the main driver file. Responsible for handling user input and displaying current Gamestate object.
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animation later...
IMAGES = {}

'''
Initialise global dictionary of images. Will be called exactly once in main
'''


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


'''
The main driver for our code. This will handle user input and updating the graphics
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False        # Flag variable for when a move is made

    loadImages()            # Only do this once, before the while loop
    running = True
    sqSelected = ()         # no square is selected, keep track of the last click of the user tuple: row, col.
    playerClicks = []       # Keep track of player clicks (two tuples [(6, 4), (4, 4)])
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # Mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # (x, y) location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):  # User clicked same square twice
                    sqSelected = ()           # deselect
                    playerClicks = []         # reset player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:  # after 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                        sqSelected = ()  # Reset user clicks
                        playerClicks = []
                    else:
                        playerClicks = [sqSelected]
            # Key handlers
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:      # Undo when 'z' pressed
                    gs.undoMove()
                    moveMade = True
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Responsible for drawing all the graphics within a current game state.
'''


def drawGameState(screen, gs):
    drawBoard(screen)  # Draw squares on board
    # Add in piece highlighting or move suggestion
    drawPieces(screen, gs.board)  # Draw pieces on top of those squares


'''
Draw the squares on the board
'''


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draw the pieces on the board using current GameState.board
'''


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # not empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == '__main__':
    main()
=======
"""
This is the main driver file. Responsible for handling user input and displaying current Gamestate object.
"""

import pygame as ppy
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animation later...
IMAGES = {}

'''
Initialise global dictionary of images. Will be called exactly once in main
'''


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


'''
The main driver for our code. This will handle user input and updating the graphics
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False        # Flag variable for when a move is made

    loadImages()            # Only do this once, before the while loop
    running = True
    sqSelected = ()         # no square is selected, keep track of the last click of the user tuple: row, col.
    playerClicks = []       # Keep track of player clicks (two tuples [(6, 4), (4, 4)])
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # Mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # (x, y) location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):  # User clicked same square twice
                    sqSelected = ()           # deselect
                    playerClicks = []         # reset player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:  # after 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                        sqSelected = ()  # Reset user clicks
                        playerClicks = []
                    else:
                        playerClicks = [sqSelected]
            # Key handlers
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:      # Undo when 'z' pressed
                    gs.undoMove()
                    moveMade = True
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Responsible for drawing all the graphics within a current game state.
'''


def drawGameState(screen, gs):
    drawBoard(screen)  # Draw squares on board
    # Add in piece highlighting or move suggestion
    drawPieces(screen, gs.board)  # Draw pieces on top of those squares


'''
Draw the squares on the board
'''


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draw the pieces on the board using current GameState.board
'''


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # not empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == '__main__':
    main()
>>>>>>> 8cdb875 (Init Commit to GitHub)
