#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/11 16:44:12 by dipekko             #+#    #+#            #
#   Updated: 2026/03/12 18:25:45 by jabad-di           ###   ########.fr      #
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
        return coords

    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{sys.argv[1]}\"")
        print(f"Error parsing coordinates: {e}")
        #no me deja utilizar type
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return None


def distance_coords(p1: tuple[int, int, int], p2: tuple[int, int, int] = (0, 0, 0)) -> None:
    """x"""
    if p1:
        dist: float = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)
        print(f"Distance between: {p2} and {p1}: {dist:.2f}")


def main() -> None:
    """x"""
    print("=== Game Coordinate System ===\n")
    coords_firts: tuple[int, int, int] = parseo_coordinate("10, 20, 5")
    print(f"Position created: {coords_firts}")
    distance_coords(coords_firts)
    print("")

    try:
        coordinates: tuple[int, int, int] = parseo_coordinate(sys.argv[1])
        print(f"Parsing coordinates: \"{sys.argv[1]}\"")
        print(f"Position created: {coordinates}")
        distance_coords(coordinates)
        print("")
        
        if coordinates:
            print("Unpacking demonstration:")
            x, y, z = coordinates
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except IndexError:
        pass


if __name__ == "__main__":
    main()
