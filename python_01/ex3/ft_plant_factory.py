#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 13:45:10 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/10 14:43:24 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    """Creation of a data structure called class."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """__init__ is the class constructor"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        """Generic phrase printout."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    """Run a demonstration five plant."""
    plant_factory: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in plant_factory:
        plant.get_info()


if __name__ == "__main__":
    main()
