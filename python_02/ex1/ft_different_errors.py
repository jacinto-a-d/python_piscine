#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/08 22:55:18 by dipekko             #+#    #+#            #
#   Updated: 2026/03/10 17:12:18 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def garden_operations() -> None:
    """demostrates common Python errors in a garden contest"""

    try:
        print("Testing ValueError...")
        int("a")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        print("Testing ZeroDivisionError...")
        x: int = 10 / 0
        print(f"{x}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        print("Testing FileNotFoundError...")
        fd: str = open("whtdadac.txt", "r")
        fd.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    try:
        print("Testing KeyError...")
        garden: dict[str, int] = {"tomate": 5}
        print(garden["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    try:
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
