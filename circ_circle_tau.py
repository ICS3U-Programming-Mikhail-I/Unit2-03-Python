#!/usr/bin/env python3
# Author: Mikhail Ibrahim
# Date: Mar 2, 2025
# Description: A Python program that calculates the circumference of a circle using Tau (𝞽) based on user input.

# Import the constant TAU from constants.py
import constants


def main():
    """Main function to calculate the circumference of a circle based on user input."""

    # Prompt the user to enter the radius of the circle
    try:
        radius = float(input("Enter the radius of the circle (cm): "))

        # Calculate the circumference using the formula C = 𝞽 * r
        circumference = constants.TAU * radius

        # Display the result with two decimal places
        print("\nFor a circle with radius {} cm:".format(radius))
        print("The circumference is {:.2f} centimeters.".format(circumference))

    except ValueError:
        # Handle invalid input if the user does not enter a number
        print("Invalid input! Please enter a numeric value.")


# Check if this script is being run directly (not imported) and call the main function
if __name__ == "__main__":
    main()
