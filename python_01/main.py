#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/26 17:08:10 by dipekko             #+#    #+#            #
#   Updated: 2026/03/04 00:39:13 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.ft_garden_intro import plant, height, age
from ex2.ft_plant_growth import Plant
from ex4.ft_garden_security import Segurity_factory
from ex5.ft_specialized_plants import Vegetable, Flower, Tree


def test_0() -> None:
    print("")
    print("=== Testing Exercise 0 ===\n")
    print(f"Plant Name: {plant}")
    print(f"Plant Height: {height}cm")
    print(f"Plant Age: {age} days")
    print("Test Ex0: OK\n")


def test_1() -> None:
    line_1 = Plant("Rose", 25, 30)
    line_2 = Plant("Sunflower", 80, 45)
    line_3 = Plant("Cactus", 15, 120)
    print("")
    print("=== Testing Exercise 1 ===\n")
    print("=== Garden Plant Registry ===")
    print(f"{line_1.name}: {line_1.height}cm, {line_1.age} days old")
    print(f"{line_2.name}: {line_2.height}cm, {line_2.age} days old")
    print(f"{line_3.name}: {line_3.height}cm, {line_3.age} days old")
    print("")


def test_2() -> None:
    days: int = 7
    growth_diary: int = 1
    garden_inventary: list[Plant] = [
        Plant("Rose", 25, 30)
    ]
    print("")
    for i in range(days):
        print(f"=== Day {i + 1} ===")
        for plants in garden_inventary:
            plants.status()
            plants.grow()
    total_growth = days * growth_diary
    print(f"Growth this week: +{total_growth - 1}cm")
    print("")


def test_3() -> None:
    plant_factory: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120)
    ]
    print("")
    print("=== Plant Factory Output ===")
    for plants in plant_factory:
        plants.status()
    print("")


def test_4() -> None:
    valid = Segurity_factory("Rose", 25, 30)
    print("")
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
    print("")


def test_5() -> None:
    print("")
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
    print("")


def main() -> None:
    print("")
    print(" === Choose a number to check ===")
    print("")
    print("0 -> ex0 ft_garden_intro")
    print("1 -> ft_garden_data")
    print("2 -> ft_plant_growth")
    print("3 -> ft_plant_factory")
    print("4 -> ft_garden_security")
    print("5 -> ft_specialized_plants")
    print("")
    choice = str(input("Enter a number: "))
    if choice == "0":
        test_0()
    elif choice == "1":
        test_1()
    elif choice == "2":
        test_2()
    elif choice == "3":
        test_3()
    elif choice == "4":
        test_4()
    elif choice == "5":
        test_5()
    else:
        print("Error: Number no valid.")


if __name__ == "__main__":
    main()
