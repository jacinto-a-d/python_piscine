#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/08 18:18:14 by dipekko             #+#    #+#            #
#   Updated: 2026/03/10 16:26:41 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def check_temperature(temp_str: str) -> int | None:
    """Checks if the input string is a valid plant temperature."""
    try:
        num = int(temp_str)

        if num > 40:
            print(f"Error: {num}°C is too hot for plants (max 40°C)")
            return None
        elif num < 0:
            print(f"Error: {num}°C is too cold for plants (min 0°C)")
            return None

        print(f"Temperature {num}°C is perfect for plants!")
        return num
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input() -> None:
    """Demonstrates testing with various input scenarios."""

    tests: list[str] = ["25", "abc", "100", "-50"]

    for t in tests:
        print(f"Testing temperature: {t}")
        check_temperature(t)
        print("")


def main() -> None:
    print("=== Garden Temperature Checker ===")
    print("")
    test_temperature_input()
    print("All tests complete - program didn't crash!")


if __name__ == "__main__":
    main()
