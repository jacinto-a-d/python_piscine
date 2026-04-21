#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_raise_errors.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/10 17:25:54 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/13 14:17:32 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
) -> str:
    """Validates plant parameters and raises ValueError for invalid inputs."""
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")

    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Tests the health checker with various valid and invalid scenarios."""
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 5))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")


def main() -> None:
    """Main entry point for the plant health check script."""
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    main()
