
class GamePiece(object):
    """One Chess Piece"""
    def __init__(self, position, piece):
        self.position = position
        self.piece = piece
        self.moveCount = 0

    def ParsePosition(self, position):
        if isinstance(position, str):

            xPos = None
            yPos = None

            position.strip()
            for x in position:
                if x.isalpha():
                    xPos = ord(x) - 96 - 1
                else:
                    yPos = int(x) - 1

            if xPos is None or yPos is None:
                print("Position Parsing Failed")
                return False
            else:
                return (xPos, yPos)

    def CheckMove(self, PosToMove):
        #Check if pos is on board
        #Check if allowed to move there
        #Check if another piece is already there
        #Check if piece is in the way 
        xCurrent, yCurrent = self.ParsePosition(self.position)
        xNew, yNew = self.ParsePosition(PosToMove)
        piece = self.piece

        #Self Check
        if(xNew == xCurrent and yNew == yCurrent):
            print("You can't move a piece onto itself...Its not Steve Bannon")
            return False
        #On GameBoard Check
        if(xNew > 7 or xNew < 0 or yNew > 7 or yNew < 0):
            print(xNew)
            print(yNew)
            print("Requested Position is off board.")
            return False
        #Check if game piece
        if piece not in "PRNBKQ":
            print("Not valid game piece")
            return False
        #Checking the rules of each game peice
        #Pawn
        if piece == "P":
            if xNew == xCurrent and yNew == yCurrent + 1:
                return True
            #TODO add en passant.. though I doubt it
            if self.moveCount == 0 and xNew == xCurrent and yNew == yCurrent + 2:
                return True
        #Knight
        #0X0X0
        #X000X
        #00N00
        #X000X
        #0X0X0
        if piece == "N":
            if (xNew == xCurrent - 2 or xNew == xCurrent + 2):
                if (yNew == yCurrent - 1 or yNew == yCurrent + 1):
                    return True
            if (yNew == yCurrent - 2 or yNew == yCurrent + 2):
                if(xNew == xCurrent - 1 or xNew == xCurrent + 1):
                    return True
        #King
        #XXX
        #XKX
        #XXX
        if piece == "K":
            if (xNew == xCurrent + 1 or xNew == xCurrent - 1 and yNew == yCurrent):
                return True
            elif (yNew == yCurrent + 1 or yNew == yCurrent - 1 and xNew == xCurrent):
                return True
            elif (yNew == yCurrent + 1 and (xNew == xCurrent + 1 or xNew == xCurrent - 1)):
                return True
            elif (yNew == yCurrent - 1 and (xNew == xCurrent + 1 or xNew == xCurrent - 1)):
                return True
        #Rook
        if piece == "R":
            if(xNew == xCurrent and yNew != yCurrent):
                return True
            elif (yNew == yCurrent and xNew != xCurrent):
                return True
        #Bishop
        #I dont know how I thought of this, but it works like a charm
        #meaning it works everytime I test it, yet I question the underlying logic
        if piece == "B":
            if (abs(xNew - xCurrent) == abs(yNew - yCurrent)):
                return True
        #Queen
        #All comes down to this
        if piece =="Q":
            if (abs(xNew - xCurrent) == abs(yNew - yCurrent)):
                return True
            elif(xNew == xCurrent and yNew != yCurrent):
                return True
            elif (yNew == yCurrent and xNew != xCurrent):
                return True
        #If we are at this point we know the move is bad
        print("Bad move")
        return False

