#################################################
# hw6.py
#
# Your name: Vijaya Vegesna
# Your andrew id: vsvegesn
#
# Your partner's name: Adithi Jawahar
# Your partner's andrew id: ajawahar
#################################################

import cs112_f21_week6_linter
import math, copy, random

from cmu_112_graphics import *

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

#checks if the number is a perfect square
def isPerfectSquare(n):
    if(n > 0):
        squareRoot = math.sqrt(n)
        if((int(squareRoot)**2 == (n))):
            return True
    return False

#checks to see if a number is sort of squarish 
def isSortOfSquarish(n):
    if (n <= 0):
        return False
    if (isPerfectSquare(n) == True):
        return False 
    numList = []
    newNumber = ""
    n = str(n)
    for i in range(len(n)):
        numList += [n[i]]
    for x in numList:
        if(int(x) == 0):
            return False 
    numList.sort()
    for number in numList:
        newNumber += number
    newNumber = int(newNumber)
    if (isPerfectSquare(newNumber) == True):
        return True
    else:
        return False
    
#checks to find the nth sort of squarish number
def nthSortOfSquarish(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isSortOfSquarish(guess)):
            found += 1
    return guess

#################################################
# s21-midterm1-animation
#################################################

#this is the app that sets all the variables used later in the problem
def s21MidtermAnimation_appStarted(app):
    app.color = 'green'
    app.timePassed = 0
    app.cx = 0
    app.cy = 0
    app.r = 20
    app.circleCoords = []
    app.fourCoords = []

#if r is pressed board is cleared and function restarts
def s21MidtermAnimation_keyPressed(app, event):
    if (event.key == 'r'):
        s21MidtermAnimation_appStarted(app)

#stores all the circle coordinates to a list and all the coordinates for the 
#shortest line to a list
def s21MidtermAnimation_mousePressed(app, event):
    shortestDistance = None
    shortestDistanceX = 0
    shortestDistanceY = 0
    app.cx = event.x
    app.cy = event.y
    #adds all clicked circle coordinates to a list
    app.circleCoords += [(app.cx, app.cy)]
    #finds the circle closest from the new circle
    if(len(app.circleCoords) > 1):
        xCordCompare = app.circleCoords[-1][0]
        YCordCompare = app.circleCoords[-1][1]
        for i in range(len(app.circleCoords)):
                xCordTwo = app.circleCoords[i][0]
                yCordTwo = app.circleCoords[i][1]
                if not (xCordCompare == xCordTwo and YCordCompare == yCordTwo):
                    distance = s21MidtermAnimation_findDistance(xCordCompare, 
                                            YCordCompare, xCordTwo,yCordTwo)
                    if (shortestDistance == None):
                        shortestDistance = distance
                        shortestDistanceX = xCordTwo
                        shortestDistanceY = yCordTwo
                    if (distance <= shortestDistance):
                        shortestDistance = distance 
                        shortestDistanceX = xCordTwo
                        shortestDistanceY = yCordTwo
        #stores coordinates of the newest circle and closest circle in a list
        app.fourCoords += [(xCordCompare, YCordCompare,
                                    shortestDistanceX, shortestDistanceY)]

#draws the circle and draws the lines to the closest circles
def s21MidtermAnimation_redrawAll(app, canvas):
    #draws circles
    for x in range(len(app.circleCoords)):
        xCord = app.circleCoords[x][0]
        yCord = app.circleCoords[x][1]
        canvas.create_oval(xCord-app.r, yCord-app.r,
                    xCord+app.r, yCord+app.r,
                    fill=app.color)
    #draws lines
    if(len(app.fourCoords) >= 1):
        for x in range(len(app.fourCoords)):
            canvas.create_line(app.fourCoords[x][0], app.fourCoords[x][1], 
                                app.fourCoords[x][2], app.fourCoords[x][3])

#after 5 seconds have passed board is cleared function restarts
def s21MidtermAnimation_timerFired(app):
    app.timePassed += app.timerDelay
    if (app.timePassed >= 5000):
        s21MidtermAnimation_appStarted(app)
        app.timePassed = 0

#finds the distance between two coordinate points
def s21MidtermAnimation_findDistance(xCordOne, yCordOne, xCordTwo, yCordTwo):
    distance = math.sqrt(((xCordTwo - xCordOne)**2) + 
                            ((yCordTwo - yCordOne)**2))
    return distance

def s21Midterm1Animation():
    runApp(width=400, height=400, fnPrefix='s21MidtermAnimation_')

#################################################
# Tetris
#################################################

#initializes the variables that will be used throughout 
def appStarted(app):
    app.isGameOver = False
    app.rows = gameDimensions()[0]
    app.cols = gameDimensions()[1]
    app.cellSize = gameDimensions()[2]
    app.margin = gameDimensions()[3]
    app.emptyColor = 'blue'
    app.board = [[app.emptyColor]*app.cols for i in range(app.rows)]
    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]
    tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    tetrisPiecesColors = [ "red", "yellow", "magenta", "pink", 
                                "cyan", "green", "orange"]
    app.tetrisPieces = tetrisPieces
    app.tetrisPiecesColors = tetrisPiecesColors
    newFallingPiece(app)
    app.fallingPieceRow = 0
    app.fallingPieceCol = app.cols//2-(len(app.fallingPiece[0])//2)
    app.score = 0

#randomly chooses a new piece,sets the color and positions in middle of top row
def newFallingPiece(app):
    if (app.isGameOver == False):
        randomIndex = random.randint(0, len(app.tetrisPieces) - 1)
        app.fallingPiece = app.tetrisPieces[randomIndex]
        app.fallingPieceColor = app.tetrisPiecesColors[randomIndex]
        app.fallingPieceRow = 0
        app.fallingPieceCol = app.cols//2-(len(app.fallingPiece[0])//2)

# the falling piece is drawn over the board. draws over the board in the color 
# of the falling piece 
def drawFallingPiece(app,canvas): 
    for x in range(len(app.fallingPiece)):
        for y in range(len(app.fallingPiece[0])):
            piece = app.fallingPiece[x][y]
            if(piece ==True):
                drawCell(app,canvas,x+app.fallingPieceRow,y+app.fallingPieceCol
                ,app.fallingPieceColor)

# checks to see if the piece is in the board and if it is in the bounds
def fallingPieceIsLegal(app):
    for row in range(len(app.fallingPiece)):
        for col in range(len(app.fallingPiece[0])):
            if (app.fallingPiece[row][col] == True):
                if ((col+app.fallingPieceCol< 0) or
                    (col+app.fallingPieceCol)>=app.cols or 
                    (row+app.fallingPieceRow<0 or
                    (row+app.fallingPieceRow)>=app.rows)):
                        return False
                if(app.board[app.fallingPieceRow+row]
                        [app.fallingPieceCol+col]
                        != app.emptyColor):
                        return False
    return True

#load the falling pieces onto the board
def placeFallingPiece(app):
    if(app.isGameOver == False):
        if(stopFalling(app)==True):
            return
        row = app.fallingPieceRow
        col = app.fallingPieceCol
        for x in range(len(app.fallingPiece)):
            for y in range(len(app.fallingPiece[0])):
                if(app.fallingPiece[x][y]==True):
                    app.board[x+row][y+col]=app.fallingPieceColor
    removeFullRows(app)

#if the piece is over the limits, the game is over 
def stopFalling(app):
    if(fallingPieceIsLegal(app) == False):
        app.isGameOver = True
        return True

#move the falling piece by a given number of rows and columns
def moveFallingPiece(app,drow,dcol):
    if (app.isGameOver == False):   
        app.fallingPieceRow += drow
        app.fallingPieceCol +=dcol 
        if(fallingPieceIsLegal(app)==False):
            app.fallingPieceRow -=drow
            app.fallingPieceCol-=dcol
            return False
    return True

#if the up arrow is pressed the piece is rotated around its center
def rotateFallingPiece(app):
    oldFallingPiece = copy.deepcopy(app.fallingPiece)
    newList = [[0]*(len(app.fallingPiece)) 
    for i in range(len(app.fallingPiece[0]))]
    oldRows = len(app.fallingPiece)
    oldCols = len(app.fallingPiece[0])
    newRows = oldCols
    newCols = oldRows 
    for x in range(oldRows):
        for y in range(oldCols):
            indexRows = oldCols-1-y
            indexCols = x
            newList[indexRows][indexCols] = app.fallingPiece[x][y] 
    app.fallingPieceRow = app.fallingPieceRow + oldRows//2 - newRows//2
    app.fallingPieceCol = app.fallingPieceCol + oldCols//2 - newCols//2
    app.fallingPiece = newList 
    if(fallingPieceIsLegal(app)==False):
        app.fallingPiece = oldFallingPiece

#dimensions of the board
def gameDimensions():
    dimensions = (15, 10, 20, 25)
    return dimensions

#this gives you the bounds of each individual cell you need to create
def getCellBounds(app, row, col):
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
    return (x0, y0, x1, y1)

#this one draws all the cells together to make the board
def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, canvas, row, col, app.board[row][col])

#draws the cells 
def drawCell(app, canvas, row, col,color):
    x0, y0, x1, y1 = getCellBounds(app, row, col)
    canvas.create_rectangle(x0, y0, x1, y1, fill = color )

#whenever a row is full, it is removed from the board
def removeFullRows(app):
    colorCounter = 0
    blueRows = 0
    newBoard = []
    tempBoard = app.board
    #check to see if there are any non blue squares then insert row into new one
    for i in range(app.rows):
        colorCounter = (tempBoard[((len(tempBoard)-1)-i)].count(app.emptyColor))
        if (colorCounter != 0):
            newBoard.insert(0, tempBoard[(len(tempBoard)-1)-i])
        elif(colorCounter == 0):
            blueRows += 1
            app.score +=1
    #create new blue rows on top based on how many empty ones there are
    for r in range(blueRows):
        newBoard.insert(0, [(app.emptyColor)] * app.cols)
    #reset board to new temp one created in this function
    app.board = newBoard

#plays the game based on the user's input of the key
def keyPressed(app, event):
    app.color = random.choice(['red', 'orange', 'yellow', 'green', 'blue'])
    if(event.key == "r"):
        appStarted(app)
    if(app.isGameOver == False):
        if(event.key == 'Down'):
            moveFallingPiece(app,+1, 0)
        elif(event.key == 'Right'):
            moveFallingPiece(app,0, +1)
        elif(event.key == "Left"):
            moveFallingPiece(app,0, -1)
        elif(event.key == "Up"):
            rotateFallingPiece(app)
        elif(event.key == 'Space'):
            hardDrop(app)

#whenver the space bar is hit there is a hard drop: goes to the bottom
def hardDrop(app):
    while(moveFallingPiece(app,+1, 0) == True):
        pass

#when the game is over, text appears saying the game is over
def gameOver(app, canvas):
    if (app.isGameOver == True):
        canvas.create_text(app.width/2, app.height/2, text = "Game Over", 
                            font = ("Arial", 35, "bold"))

#the score that is stored in app is dispplayed when the game is over
def scoreDisplay(app, canvas):
    if (app.isGameOver == True):
        canvas.create_text(app.width/2, 15, 
        text = f'score: {app.score}', font = ("Arial", 20, "bold"))

#this creates the border, draws the board, draws the falling pieces and all the
#text
def redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="orange")
    drawBoard(app, canvas)
    drawFallingPiece(app,canvas)
    gameOver(app, canvas)
    scoreDisplay(app, canvas)

#everytime the timer is fired, we check if the game is over and then the new 
#pieces fall 
def timerFired(app):
    if (fallingPieceIsLegal(app) ==False):
        app.isGameOver == True
    if (app.isGameOver == False):
        if (moveFallingPiece(app, +1, 0) == False):
            placeFallingPiece(app)
            newFallingPiece(app)

#this calls and starts the game of tetris so you can play 
def playTetris():
    rows,cols,cellSize,margin = gameDimensions()
    runApp(width= cellSize*cols+(2*margin),height= cellSize*rows+(2*margin))
#################################################
# Test Functions
#################################################

def testIsPerfectSquare():
    print('Testing isPerfectSquare(n))...', end='')
    assert(isPerfectSquare(4) == True)
    assert(isPerfectSquare(9) == True)
    assert(isPerfectSquare(10) == False)
    assert(isPerfectSquare(225) == True)
    assert(isPerfectSquare(1225) == True)
    assert(isPerfectSquare(1226) == False)
    print('Passed')


def testIsSortOfSquarish():
    print('Testing isSortOfSquarish(n))...', end='')
    assert(isSortOfSquarish(52) == True)
    assert(isSortOfSquarish(16) == False)
    assert(isSortOfSquarish(502) == False)
    assert(isSortOfSquarish(414) == True)
    assert(isSortOfSquarish(5221) == True)
    assert(isSortOfSquarish(6221) == False)
    assert(isSortOfSquarish(-52) == False)
    print('Passed')


def testNthSortOfSquarish():
    print('Testing nthSortOfSquarish()...', end='')
    assert(nthSortOfSquarish(0) == 52)
    assert(nthSortOfSquarish(1) == 61)
    assert(nthSortOfSquarish(2) == 63)
    assert(nthSortOfSquarish(3) == 94)
    assert(nthSortOfSquarish(4) == 252)
    assert(nthSortOfSquarish(8) == 522)
    print('Passed')

def testAll():
    testIsPerfectSquare()
    testIsSortOfSquarish()
    testNthSortOfSquarish()

#################################################
# main
#################################################

def main():
    cs112_f21_week6_linter.lint()
    s21Midterm1Animation()
    playTetris()
    testAll()

if __name__ == '__main__':
    main()
