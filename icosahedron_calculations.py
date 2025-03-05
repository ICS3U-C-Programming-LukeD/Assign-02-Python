#!/usr/bin/env python3

# Created By: Luke
# Date: March 5, 2025
# Calculates the volume and surface area of an icosahedron using the edge length

import math

# Adds math module


def main():
    print(
        "Welcome to Luke's icosahedron calculator! \nThis program will calculate the surface area and volume of your icosahedron!"
    )
    # Intro message
    edge_length = float(input(("Enter the length of your icosahedrons edge in cm: ")))
    # Asks user for edge length
    round_to = int(input("Enter the amount of decimals you want to round to: "))
    print()
    surface_area = 5 * (math.sqrt(3) * edge_length**2)
    # Calculates surface area using the proper formula
    volume = (5 * (3 + math.sqrt(5)) / 12) * edge_length**3
    # Calculates volume using the proper formula
    print("The surface area is: " + str(round(surface_area, round_to)) + "cm^2")
    # Displays surface area
    print("The volume is: " + str(round(volume, round_to)) + "cm^3")
    # Displays volume
    print("\nThank you for using this calculator!")
    # Outro message


if __name__ == "__main__":
    main()
