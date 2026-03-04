#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/03 21:10:53 by dipekko             #+#    #+#            #
#   Updated: 2026/03/03 22:27:51 by dipekko            ###   ########.fr      #
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
