import ChessPieces
class chessboard(object):
    """docstring for chessboard"""

    def __init__(self):
        #Note, when calling it is gameBoard[y][x]
        self.gameBoard = [[None,None,None,None,None,None,None,None],
                          [None,None,None,None,None,None,None,None],
                          [None,None,None,None,None,None,None,None],
                          [None,None,None,None,None,None,None,None],
                          [None,None,None,None,None,None,None,None],
                          [None,None,None,None,None,None,None,None],
                          [None,None,None,None,None,None,None,None],
                          [None,None,None,None,None,None,None,None]]

    def ConvertChessNotationToGameBoardCoord(self, chessString):
        #check if string, we dont want no 0,0 aka x,y we want the classic chess a1 b1
        if isinstance(chessString, str):

            xPos = None
            yPos = None

            chessString.strip()
            for x in chessString:
            	#if letter should be the a in a1
                if x.isalpha():
                    xPos = ord(x) - 96 - 1
                #otherwise it is the number.. luckily no double digit numbers here
                else:
                    yPos = int(x) - 1

            #Check if parsing worked, and not none
            if xPos is None or yPos is None:
                print("Position Conversion Failed: Bad input")
                return False
            #Check if on Game Board
            if xPos > 7 or yPos > 7:
            	print("Position Conversion Failed, input too high: {},{}".format(xPos,yPos))
            	return False

            yConversion = {0:7, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1, 7:0}

            xGameBoard = xPos
            yGameBoard = yConversion[yPos]
            #print(self.gameBoard[yGameBoard][xGameBoard])
            return (xGameBoard, yGameBoard)
        else:
            print("Maybe give Convert a string? <3")

    def ConvertGameCoordToChess(self,x,y):
        output = ""
        yConversion = {7:1, 6:2, 5:3, 4:4, 3:5, 2:6, 1:7, 0:8}
        yChess = str(yConversion[y])
        xChess = chr(x + 96 + 1)
        return (xChess+yChess)

    def CheckSpace(self, space):
        x, y = self.ConvertChessNotationToGameBoardCoord(space)
        if self.gameBoard[y][x] is not None:
            print(self.gameBoard[y][x])
            return True
        else:
            print("Empty Space")
            return False

    def SetBoard(self):
        #Set Pawns
        for i in range(0,8):
            xPos = chr(i + 96 + 1) 
            space = str(xPos) + str(2)
            self.SetPiece(space, ChessPieces.GamePiece(space,"P"))
        #Set Rooks
        self.SetPiece("a1", ChessPieces.GamePiece("a1","R"))
        self.SetPiece("h1", ChessPieces.GamePiece("h1","R"))
        #Set Knights
        self.SetPiece("b1", ChessPieces.GamePiece("b1","N"))
        self.SetPiece("g1", ChessPieces.GamePiece("g1","N"))
        #Set Bishops
        self.SetPiece("c1", ChessPieces.GamePiece("c1","B"))
        self.SetPiece("f1", ChessPieces.GamePiece("f1","B"))
        #Set Queen and King
        self.SetPiece("d1", ChessPieces.GamePiece("d1","Q"))
        self.SetPiece("e1", ChessPieces.GamePiece("e1","K"))

    def SetPiece(self, space, piece):
    	x, y = self.ConvertChessNotationToGameBoardCoord(space)
    	self.gameBoard[y][x] = piece

    def MoveGamePiece(self, space, newSpace):
    	x, y = self.ConvertChessNotationToGameBoardCoord(space)
    	gamePieceObject = self.gameBoard[y][x]
    	if gamePieceObject.CheckMove(newSpace) == True:
    		self.SetPiece(newSpace, gamePieceObject)
    		gamePieceObject.position = newSpace
    		gamePieceObject.moveCount += 1
    		self.gameBoard[y][x] = None

    #TODO Add color output
    def PrintMap(self):
        yCounter = 8
        for y in self.gameBoard:
            output = ""
            output += str(yCounter)
            for x in y:
                if x is None:
                    output += str(0)
                elif isinstance(x,str):
                    output += str(x)
                else:
                	output += str(x.piece)
            print(output)
            yCounter -= 1
        print("XABCDEFGH")

    def PrintSpot(self, space):
    	x, y = self.ConvertChessNotationToGameBoardCoord(space)
    	print(self.gameBoard[y][x])


if __name__ == '__main__':
	chessboard = chessboard()
	print(chessboard.CheckSpace("a1"))
	
	chessboard.SetPiece("a2", "P")
	chessboard.PrintMap()


