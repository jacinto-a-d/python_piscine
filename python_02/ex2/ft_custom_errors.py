#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/08 23:49:13 by dipekko             #+#    #+#            #
#   Updated: 2026/03/09 00:29:50 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    """class for all garden-related custom exceptions."""


class PlantError(GardenError):
    """error handler class for any incident with the plan."""


class WaterError(GardenError):
    """error handler class for water incidents."""


def check_plant() -> None:
    """Simulates a plant health check and raises a PlantError."""
    raise PlantError("The tomate plant is wilting!")


def check_water() -> None:
    """Simulates a water level check and raises a WaterError."""
    raise WaterError("Not enough water in the tank!")


def test_customs_errors() -> None:
    """Demonstrates how to catch specific and inherited custom exceptions."""
    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("")
    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("")
    print("Testing catching all garden errors...")
    for check in [check_plant, check_water]:
        try:
            check()
        except GardenError as e:
            print(f"Caught a garden error: {e}")


def main() -> None:
    """Entry point for the custom errors demonstration script."""
    print("=== Custon Garden Errors Demo ===\n")
    test_customs_errors()
    print("\nAll custon error types work correctly!")


if __name__ == "__main__":
    main()
