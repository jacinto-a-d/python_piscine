#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/08 22:55:18 by dipekko             #+#    #+#            #
#   Updated: 2026/03/08 23:55:23 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def garden_operations() -> None:
    """demostrates common Python errors in a garden contest"""

    try:
        """when you receive something that is not a number"""
        print("Testing ValuError...")
        int("a")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        """when you cannot divide by 0"""
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        """When a file or directory is requested but doesn't exist"""
        print("Testing FileNotFoundError...")
        fd: str = open("whtdadac.txt", "a")
        fd.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    try:
        """When a dictionary key is not found in the set of existing keys"""
        print("Testing KeyError...")
        garden: dict[str, int] = {"tomate": 5}
        print(garden["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    try:
        """It picks up any errors that arise."""
        print("Testing multiples errors together...")
        int("not_number")
    except Exception:
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    """Wrapper function to execute garden operations and show continuity"""
    garden_operations()
    print("All error types tested successfully!")


def main() -> None:
    """Main entry point for the error types demo."""
    print("=== Garden Error Types Demo ===")
    print("")
    test_error_types()


if __name__ == "__main__":
    main()
