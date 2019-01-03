
from sense_hat import SenseHat
from math import cos, sin, floor
import sys

sense = SenseHat()

def drawSquare(balance, color, background_color):

    board = [background_color for i in range(64)]

    row = balance[0]
    col = balance[1]

    if row > 6:
        row = 6
    if row < 0:
        row = 0

    if col > 6:
        col = 6
    if col < 0:
        col = 0


    #TODO: make dynamic color

    board[(row * 8) + col] = color
    board[(row * 8) + col + 1] = color
    board[((row + 1) * 8) + col] = color
    board[((row + 1) * 8) + col + 1] = color

    sense.set_pixels(board)



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



