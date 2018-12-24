

from sense_hat import SenseHat
from math import sin
from math import cos
from math import radians
from math import degrees


sense = SenseHat()

# returns a dictionary with the corrected values
def normalize_accel(hat):
    result = {}
    g = 1

    # TODO: check whether raw is better than not raw
    acceleration = hat.get_accelerometer_raw()
    orientation = hat.get_orientation_radians()

    x_accel_raw = acceleration["x"]
    y_accel_raw = acceleration["y"]
    z_accel_raw = acceleration["z"]

    # X - roll, Y - pitch, Z - yaw
    roll = orientation["roll"]
    pitch = orientation["pitch"]
    yaw = orientation["yaw"]

    x_real = x_accel_raw - (x_accel_raw * cos(roll))
    y_real = y_accel_raw - (y_accel_raw * sin(pitch))



def main():
    normalize_accel(sense)

if __name__== "__main__":
  main()
  #check if push successful
