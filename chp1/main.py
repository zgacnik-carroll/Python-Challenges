"""
File: main.py
Author: Zack Gacnik
Date: 2026-01-27
Description:
    This program allows the user to query Montana county information by license plate prefix.
    Users can choose to see the county name, county seat, or both. The program reads
    data from 'MontanaCounties.csv' file and supports multiple queries until the user exits.
"""

import csv

def load_county_data(filename):
    """
    Loads county data from a CSV file into a dictionary.
    The dictionary uses the license plate prefix as the key and stores
    a tuple containing the county name and county seat as the value.

    Args:
        filename: Name of the CSV file to load.

    Returns:
        counties: Dictionary mapping license plate prefixes to county data.
    """

    # Dictionary to store the county data.
    counties = {}

    # Open the CSV file using a context manager.
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        # Process each row in the CSV file.
        for row in reader:
            # Convert the license plate prefix to an integer.
            prefix = int(row["License Plate Prefix"])

            # Store the county name and county seat as a tuple.
            counties[prefix] = (row["County"], row["County Seat"])

    return counties


def main():
    """
    Main program loop.
    Allows the user to query county information by license plate prefix.
    """

    # Load the county data from the CSV file.
    counties = load_county_data("MontanaCounties.csv")

    # Ask the user what information should be returned.
    print("What would you like to display?")
    print("1 - County name")
    print("2 - County seat")
    print("3 - Both")

    # Validate the user's selection.
    choice = input("Enter choice: ")

    while choice not in {"1", "2", "3"}:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = input("Enter choice: ")

    # Allow the user to make repeated queries.
    while True:
        user_input = input("\nEnter license plate prefix (or 'quit' to exit): ")

        if user_input.lower() == "quit":
            print("\nQuitting...Goodbye!")
            break

        try:
            prefix = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if prefix not in counties:
            print("No county found for that prefix, please try again.")
            continue

        county, seat = counties[prefix]

        if choice == "1":
            print(f"County name: {county}")
        elif choice == "2":
            print(f"County seat: {seat}")
        else:
            print(f"County name: {county}")
            print(f"County seat: {seat}")

# Main block where the code is executed.
if __name__ == "__main__":
    main()
