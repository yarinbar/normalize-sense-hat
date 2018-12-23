

from sense_hat import SenseHat
from math import sin
from math import cos


sense = SenseHat()

# returns a dictionary with the corrected values
def normalize_accel(x_accel, y_accel, z_accel, pitch, roll, yaw):
    result = {}
    g = 1
    result["x"] = x_accel + (g * cos(pitch))
    result["y"] = y_accel + (g * sin(pitch))
    print(result["x"])


def main():
    normalize_accel(1, 2, 3, 4, 5, 6)

if __name__== "__main__":
  main()
