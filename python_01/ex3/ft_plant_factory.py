#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/26 19:30:44 by dipekko             #+#    #+#            #
#   Updated: 2026/03/03 21:00:56 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    """creation of a data structure called class"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """__init__ is the class constructor"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def status(self) -> None:
        """generic phrase printout"""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    "run a demonstration five plant"
    plant_factory: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in plant_factory:
        plant.status()


if __name__ == "__main__":
    main()
