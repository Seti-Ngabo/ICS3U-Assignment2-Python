#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program calculates the perimeter of a kite
#   with user input

import math


def main():
    # this function calculates the perimeter
    print("We will be calculating the perimeter of a Kite. ")
    print("")

    # input
    side_a = int(input("Enter the dimension of side A (cm): "))
    side_b = int(input("Enter the dimension of side B (cm): "))

    # process
    perimeter = 2 * (side_a + side_b)

    # output
    print("The perimeter is {} cm".format(perimeter))
    print("")
    print("Done")


if __name__ == "__main__":
    main()
