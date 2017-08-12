#Ideas
#if input is only a piece, set gameboard spaces to x where it can move
#Make sure all convertions check for a lowercase letter
import ChessMap as Map
import ChessPieces

chessboard = Map.chessboard()
chessboard.SetBoard()

while True:
    chessboard.PrintMap()
    gamePiece, moveplace = input("Move Piece: location, newlocation \n").split(",")
    chessboard.MoveGamePiece(gamePiece, moveplace)

