
from .display import run
import sys

def main():
    green = [0, 255, 0]
    black = [0, 0, 0]
    sensitivity = sys.argv[1]

    run(sensitivity, green, black)



main()
