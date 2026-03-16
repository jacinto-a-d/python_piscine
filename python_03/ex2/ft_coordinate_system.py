#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/16 12:38:08 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/16 12:38:09 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import sys
import math


def parseo_coordinate(data: str) -> tuple[int, int, int] | None:
    """
    Parses a comma-separated string into a 3D coordinate tuple.

    Args:
        data (str): A string containing three integers separated by commas.

    Returns:
        tuple[int, int, int] | None: The parsed coordinates or None if invalid.
    """
    try:
        parts: list[str] = data.split(',')
        x_s, y_s, z_s = parts
        coords: tuple[int] = (
            int(x_s),
            int(y_s),
            int(z_s)
        )
        return coords

    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{data}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return None


def distance_coords(
        p1: tuple[int, int, int],
        p2: tuple[int, int, int] = (0, 0, 0)
) -> None:
    """
    Calculates and prints the Euclidean distance between two 3D points.

    Args:
        p1 (tuple[int, int, int]): Target point.
        p2 (tuple[int, int, int]): Origin point, defaults to (0, 0, 0).
    """
    if p1:
        dist: float = math.sqrt(
            (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2
        )
        print(f"Distance between: {p2} and {p1}: {dist:.2f}")


def main() -> None:
    """Main execution function to demonstrate the 3D coordinate system."""
    print("=== Game Coordinate System ===\n")
    coords_firts: tuple[int, int, int] = parseo_coordinate("10, 20, 5")
    print(f"Position created: {coords_firts}")
    distance_coords(coords_firts)
    print("")

    try:
        input_data: str = sys.argv[1]
        coordinates: tuple[int, int, int] = parseo_coordinate(input_data)

        if coordinates:
            print(f"Parsing coordinates: \"{input_data}\"")
            print(f"Position created: {coordinates}")
            distance_coords(coordinates)
            print("")
            print("Unpacking demonstration:")
            x, y, z = coordinates
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")

    except IndexError:
        pass


if __name__ == "__main__":
    main()
