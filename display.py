
from sense_hat import SenseHat
from math import cos, sin
import sys

sense = SenseHat()

def drawSquare(row, col, color, background_color):

    board = [background_color for i in range(8)]

    row_legal = row < 7 and row >= 0
    col_legal = col < 7 and col >= 0

    # if the row or the col is illegal find a legal position
    if not row_legal or not col_legal:
        row = findLegalPosition(row)
        col = findLegalPosition(col)


    #TODO: make dynamic color

    board[(row * 8) + col] = color
    board[(row * 8) + col + 1] = color
    board[((row + 1) * 8) + col] = color
    board[((row + 1) * 8) + col + 1] = color

    sense.set_pixels(board)



def findLegalPosition(position):

    while(position < 0):
        position += 1

    while(position >= 7):
        position -= 1

    return position


def getAccel():
    accel = sense.get_accelerometer_raw()
    x = round(accel["x"], 1)
    y = round(accel["y"], 1)

    '''
    minus sign is for depicting the acceleration the person
    inside the accelerating system is experiencing
    '''
    res = {"x": -x, "y": -y}

    return res


def showBalancePoint(sensitivity, color, background_color):

    accel = getAccel()

    '''
    recommended setting is between 4 and 8
    4 - shows from -0.25(m/s^2) to 0.25(m/s^2)
    8 - shows from -0.5(m/s^2) to 0.5(m/s^2)
    '''
    col = int(accel["x"] * sensitivity)
    row = int(accel["y"] * sensitivity)

    # sets the center of the board as the 0 point
    col = col + 3
    row = row + 3

    drawSquare(row, col, color, background_color)


def normalizePi():
    '''
    alpha - the roll angle (x axis)
    theta - the pitch angle (y axis)
    gamma - the yaw angle (z axis)
    '''

    orientation = sense.get_orientation_radians()
    alpha = orientation["roll"]
    theta = orientation["pitch"]
    gamma = orientation["yaw"]

    accel = sense.get_accelerometer_raw()
    x = accel["x"]
    y = accel["y"]

    # the '1' stands for the g in the z axis
    x = x - 1 * cos(alpha)
    y = y + 1 * cos(theta)

def run(sensitivity, color, background_color):
    try:
        while True:
            showBalancePoint(sensitivity, color, background_color)
    except KeyboardInterrupt:
        sense.clear()
    except ArithmeticError:
        print("there was an arithmetic error")
        sense.clear()
    except MemoryError:
        print("memory error")
        sense.clear()




green = [0, 255, 0]
black = [0, 0, 0]
sensitivity = sys.argv[1]
run(sensitivity, green, black)

