#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 13:45:17 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/04 13:45:18 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Segurity_factory:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self._height: int = 0
        self._age: int = 0

    def set_height(self, value: int) -> None:
        """function validates the value"""
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        """function validates the value"""
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def get_height(self) -> int:
        """returns the original value"""
        return self._height

    def get_age(self) -> int:
        """returns the original value"""
        return self._age


def main() -> None:
    valid = Segurity_factory("Rose", 25, 30)
    print("=== Garden Security System ===")
    print(f"Plant created: {valid.name}")
    valid.set_height(25)
    valid.set_age(30)
    print("")
    valid.set_height(-5)
    print("")
    print(
        f"Current plant: {valid.name} ({valid.get_height()}cm, """
        f"{valid.get_age()} days)"
    )


if __name__ == "__main__":
    main()
