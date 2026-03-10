#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 13:45:01 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/10 14:35:24 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    """Creation of a data structure called class."""
    def __init__(self, name: str, height: int, age_day: int) -> None:
        """__init__ is the class constructor"""
        self.name: str = name
        self.height: int = height
        self.age_day: int = age_day

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.age_day += 1

    def get_info(self) -> None:
        """Generic phrase printout."""
        print(f"{self.name}: {self.height}cm, {self.age_day} days old")


def main() -> None:
    "Run a demonstration of the class."
    days: int = 7
    growth_diary: int = 1
    garden_inventary: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Daisy", 20, 15),
        Plant("Cactus", 40, 35)
    ]

    for i in range(days):
        print(f"=== Day {i + 1} ===")
        for plant in garden_inventary:
            plant.get_info()
            plant.grow()
            plant.age()
    total_growth = days * growth_diary
    print(f"Growth this week: +{total_growth - 1}cm")


if __name__ == "__main__":
    main()
