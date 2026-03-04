#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 13:44:44 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/04 13:44:58 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    """creation of a data structure called class"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """__init__ is the class constructor"""
        self.name: str = name
        self.height: int = height
        self.age: int = age


def main() -> None:
    "run a demonstration of the class"
    line_1 = Plant("Rose", 25, 30)
    line_2 = Plant("Sunflower", 80, 45)
    line_3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(f"{line_1.name}: {line_1.height}cm, {line_1.age} days old")
    print(f"{line_2.name}: {line_2.height}cm, {line_2.age} days old")
    print(f"{line_3.name}: {line_3.height}cm, {line_3.age} days old")


if __name__ == "__main__":
    main()
