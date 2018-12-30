
from sense_hat import SenseHat


sense = SenseHat()

def drawSquare(row, col, color, background_color):

    board = [background_color for i in range(8)]

    # TODO: check for end of board

    board[(row * 8) + col] = color
    board[(row * 8) + col + 1] = color
    board[((row + 1) * 8) + col] = color
    board[((row + 1) * 8) + col + 1] = color

    sense.set_pixels(board)


def getAccel():
    accel = sense.get_accelerometer_raw()
    x = accel["x"]
    y = accel["y"]
    res = {"x" : -y, "y" : -x}

    return res


def showBalance(sensetivity, color, background_color):

    accel = getAccel()
    row = accel["x"] * sensetivity
    col = accel["y"] * sensetivity

    drawSquare(row, col, color, background_color)

