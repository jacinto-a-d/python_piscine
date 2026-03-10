#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/26 17:08:10 by dipekko             #+#    #+#            #
#   Updated: 2026/03/10 15:11:20 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.ft_garden_intro import plant, height, age
from ex4.ft_garden_security import Plant
from ex5.ft_specialized_plants import Vegetable, Flower, Tree
from ex6.ft_garden_analytics import GardenManager, FloweringPlant, \
    PrizerFlower, Plant as PlantEx6


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
    valid = Plant("Rose", 25, 30)
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


def test_6() -> None:
    print("")
    GardenManager.title()

    names: list = ["Alice", "Bob"]
    network: list = GardenManager.create_garden_network(names)
    alice_garden: GardenManager = network[0]
    bob_garden: GardenManager = network[1]

    tree: list = PlantEx6("Oak Tree", 100)
    rose: list = FloweringPlant("Rose", 25, "Red")
    daisy: list = FloweringPlant("Daisy", 9, "Yellow")
    sunflower: list = PrizerFlower("Sunflower", 50, "Yellow", 0)

    alice_garden.add_plants(tree)
    alice_garden.add_plants(rose)
    alice_garden.add_plants(daisy)
    alice_garden.add_plants(sunflower)

    bob_plant: list = PlantEx6("Old Bush", 92)
    bob_garden.add_plants(bob_plant)
    print("")
    print("Alice helping all plants grow...")
    alice_garden.grow_all()
    print("")
    alice_garden.display_report()
    GardenManager.display_summary(network)
    print("")


def main() -> None:
    print("")
    print(" === Choose a number to check ===")
    print("")
    print("0 -> ex0 -> ft_garden_intro")
    print("1 -> ex1 -> ft_garden_data")
    print("2 -> ex2 -> ft_plant_growth")
    print("3 -> ex3 -> ft_plant_factory")
    print("4 -> ex4 -> ft_garden_security")
    print("5 -> ex5 -> ft_specialized_plants")
    print("6 -> ex6 -> ft_garden_analitics")
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
    elif choice == "6":
        test_6()
    else:
        print("Error: Number no valid.")


if __name__ == "__main__":
    main()
