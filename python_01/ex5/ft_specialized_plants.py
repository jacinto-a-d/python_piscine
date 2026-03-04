#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_specialized_plants.py                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 13:45:25 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/04 13:45:26 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            shader: int,
            climbable: int
    ) -> None:
        super().__init__(name, height, age)
        self.shader: int = shader
        self.climbable: int = climbable

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.shader} square meters of shade")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest: str,
        vitamine: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest: str = harvest
        self.vitamine: str = vitamine

    def nutrient(self) -> None:
        print(f"{self.name} is rich in vitamine {self.vitamine}")


def main() -> None:
    print("=== Garden Plant Types ===\n")

    f1 = Flower("Rose", 25, 30, "Red")
    f2 = Flower("Cactus", 5, 90, "Green")

    for f in [f1, f2]:
        print(
            f"{f.name} (Flower): {f.height}cm, "
            f"{f.age} days, {f.color} red"
            )
        f.bloom()
    print("")

    t1 = Tree("Oak", 500, 3650, 78, 50)
    t2 = Tree("Mango", 500, 3650, 8, 20)

    for t in [t1, t2]:
        print(
            f"{t.name} (Tree): {t.height}cm, "
            f"{t.age} days, {t.climbable} diameter"
            )
        t.produce_shade()

    print("")

    v1 = Vegetable("Tomato", 80, 90, "summer", "C")
    v2 = Vegetable("Eggplant", 40, 120, "autumn", "A")
    for v in [v1, v2]:
        print(
            f"{v.name} (Vegetable): {v.height}cm, "
            f"{v.age} days, {v.harvest} harvest"
            )
        v.nutrient()


if __name__ == "__main__":
    main()
