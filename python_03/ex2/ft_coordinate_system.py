#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/11 16:44:12 by dipekko             #+#    #+#            #
#   Updated: 2026/03/12 11:42:44 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import math


def parseo_coordinate(data: str) -> tuple[int]:
    """x"""
    try:
        parts: list[str] = data.split(',')
        coords: tuple[int] = (
            int(parts[0]),
            int(parts[1]),
            int(parts[2])
        )
        print(f"Position created: {coords}")
        return coords
    except IndexError:
        pass

    except ValueError as e:
        print(f"Parsing invalid coordinates:{sys.argv[1]}")
        print(f"Error parsing coordinates: {e}")
        return None


def distance_coords(coordi: tuple[int]) -> None:
    """x"""
    if coordi:
        dist: float = math.sqrt(coordi[0]**2 + coordi[1]**2 + coordi[2]**2)
        print(f"Distance between: (0, 0, 0) and {coordi}: {dist:.2f}")


def main() -> None:
    """x"""
    print("=== Game Coordinate System ===\n")
    coords_firts: tuple[int] = parseo_coordinate("10, 20, 5")
    distance_coords(coords_firts)
    print("")

    print(f"Parsing coordinates: {sys.argv[1]}")
    coordinates: tuple[int] = parseo_coordinate(sys.argv[1])
    distance_coords(coordinates)
    print("")

    print("Unpacking demonstration:")
    x, y, z = coordinates
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
