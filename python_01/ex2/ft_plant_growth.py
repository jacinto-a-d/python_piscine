#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 13:45:01 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/04 13:45:03 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    """creation of a data structure called class"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """__init__ is the class constructor"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        self.height += 1
        self.age += 1

    def status(self) -> None:
        """generic phrase printout"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    "run a demonstration of the class"
    days: int = 7
    growth_diary: int = 1
    garden_inventary: list[Plant] = [
        Plant("Rose", 25, 30)
    ]

    for i in range(days):
        print(f"=== Day {i + 1} ===")
        for plant in garden_inventary:
            plant.status()
            plant.grow()
    total_growth = days * growth_diary
    print(f"Growth this week: +{total_growth - 1}cm")


if __name__ == "__main__":
    main()
