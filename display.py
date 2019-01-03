
from sense_hat import SenseHat
from math import cos, sin, floor
import sys

sense = SenseHat()

def drawSquare(balance, color, background_color):

    board = [background_color for i in range(64)]

    row = balance[0]
    col = balance[1]

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


def calcBalancePoint(sensitivity):

    accel = sense.get_accelerometer_raw()

    '''
    recommended setting is between 4 and 8
    4 - shows from -0.25(m/s^2) to 0.25(m/s^2)
    8 - shows from -0.5(m/s^2) to 0.5(m/s^2)
    '''
    x = round(accel["x"], 1)
    y = round(accel["y"], 1)

    col = -1 * int(floor(x * sensitivity))
    row = -1 * int(floor(y * sensitivity))

    # sets the center of the board as the 0 point
    col = col + 3
    row = row + 3

    balance = (row, col)

    return balance


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
            balance = calcBalancePoint(sensitivity)
            drawSquare(balance, color, background_color)
    except KeyboardInterrupt:
        sense.clear()
    except ArithmeticError:
        print("there was an arithmetic error")
        sense.clear()
    except MemoryError:
        print("memory error")
        sense.clear()



try:
    green = [0, 255, 0]
    black = [0, 0, 0]
    sensitivity = int(sys.argv[1])
    run(sensitivity, green, black)
except:
    print("Please enter sensitivity")



