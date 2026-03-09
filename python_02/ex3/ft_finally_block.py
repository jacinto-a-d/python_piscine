#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_finally_block.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/09 00:31:29 by dipekko             #+#    #+#            #
#   Updated: 2026/03/09 14:35:29 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def water_plants(plant_list: list) -> None:
    """
    The function uses try, except, and finally,
    handling errors and ensuring with finally that the code continues running.
    """
    print("Opening watering system")
    try:
        for w in plant_list:
            if w is None:
                raise TypeError
            print(f"Watering {w}")
    except TypeError:
        print(f"Error: Cannot water {w} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    The goal is to test a normal test and an incorrect one,
    and have the program display until the end without crashing.
    """
    print("Testing normal watering...")

    list_1: list[str] = ["tomato", "lettuce", "carrots"]
    water_plants(list_1)
    print("Watering completed successfully!\n")

    print("Testing with error...")

    list_2: list[str] = ["tomato", None]
    water_plants(list_2)
    print("")
    print("Cleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===")
    print("")
    test_watering_system()


if __name__ == "__main__":
    main()
