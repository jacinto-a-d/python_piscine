#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 13:45:30 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/09 16:55:57 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    """Base class representing a generic plant with growth tracking."""
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.initial_height: int = height
        self.point: int = 0
        self.category: str = "regular"

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew {self.height}cm")

    def get_info(self) -> str:
        return f"- {self.name} {self.height}cm"


class FloweringPlant(Plant):
    """A plant that produces flowers and has a higher base point value."""
    def __init__(
        self,
        name: str,
        height: int,
        color: str
    ) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.point: int = 10
        self.category: str = "flowering"

    def get_info(self) -> str:
        return super().get_info() + f" {self.color} flowers (blooming)"


class PrizerFlower(FloweringPlant):
    """
    A premium flower category
    that includes additional competitive points.
    """
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        extra_point: int
    ) -> None:
        super().__init__(name, height, color)
        self.point: int = self.point + extra_point
        self.category: str = "prize flowers"

    def get_info(self) -> str:
        return super().get_info() + f", Prize points: {self.point}"


class GardenManager:
    """Handles garden operations, plant lists, and status reporting."""
    total_manager: int = 0

    class GardenStats:
        """
        Internal helper
        for calculating various garden performance metrics.
        """
        def garden_score(sel, plants: list[str]) -> int:
            """Calculates a total score based on height and plant points."""
            total_score: int = 0
            for ts in plants:
                total_score += ts.height + ts.point
            return total_score

        def get_count_growth(self, plant: list[str]) -> dict:
            """
            Generates a summary of total growth
            and category distribution.
            """
            counts: dict[str, int] = {
                "total_growth": 0,
                "total_count": 0,
                "regular": 0,
                "flowering": 0,
                "prize flowers": 0}

            for g in plant:
                counts["total_count"] += 1
                counts["total_growth"] += (g.height - g.initial_height)

                cat: str = g.category

                if cat == "regular":
                    counts["regular"] += 1
                elif cat == "flowering":
                    counts["flowering"] += 1
                elif cat == "prize flowers":
                    counts["prize flowers"] += 1

            return counts

        def total_height(self, plants_list: list[str]) -> int:
            """Calculates the sum of heights for all plants in the list."""
            suma: int = 0
            for su in plants_list:
                suma += su.height
            return suma

    def __init__(self, name: str, gardens: list[str] = None) -> None:
        self.name: str = name
        self.gardens: list[str] = gardens if gardens is not None else []
        self.stats = self.GardenStats()

    def add_plants(self, plant: Plant) -> None:
        """Adds a new plant instance to the garden list."""
        self.gardens = self.gardens + [plant]
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self) -> None:
        """Triggers the growth method for every plant in the garden."""
        for a in self.gardens:
            a.grow()

    @classmethod
    def create_garden_network(cls, garden_list: list[str] = None) -> list:
        """
        Initializes multiple GardenManager instances
        from a list of names.
        """
        red: list[str] = []
        names: list[str] = garden_list if garden_list else []
        for r in names:
            now_garden: GardenManager = cls(r)
            red = red + [now_garden]
            cls.total_manager += 1
        return red

    def display_report(self) -> None:
        """Prints a detailed report of plants, growth, and validity checks."""
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")

        for i in self.gardens:
            print(i.get_info())

        data: dict[str, int] = self.stats.get_count_growth(self.gardens)

        print("")
        print(
            f"Plant added: {data['total_count']},"
            f"Total growth: {data['total_growth']}cm"
        )
        print(
            f"Plant type: {data['regular']} regular, "
            f"{data['flowering']} flowering, "
            f"{data['prize flowers']} prize flowers\n"
        )

        is_valid: bool = True
        for v in self.gardens:
            if v.height < 0:
                is_valid: bool = False
        print(f"height validartion test: {is_valid}")

    @classmethod
    def display_summary(cls, network: list[str]) -> None:
        """Displays total scores for all gardens in the network"""

        print("Garden score - ", end="")
        first: bool = True

        for sc in network:
            if not first:
                print(", ", end="")

            score: int = sc.stats.garden_score(sc.gardens)
            print(f"{sc.name}: {score}", end="")
            first: bool = False

        print("")
        print(f"Total garden managed: {cls.total_manager}")

    @staticmethod
    def title() -> None:
        """Prints the main system header."""
        print("=== Garden Management System Demo ===\n")


def main() -> None:
    """Executes the demonstration script for the garden system."""
    GardenManager.title()

    names: list[str] = ["Alice", "Bob"]
    network: list[str] = GardenManager.create_garden_network(names)
    alice_garden: GardenManager = network[0]
    bob_garden: GardenManager = network[1]

    tree: list[str, int] = Plant("Oak Tree", 100)
    rose: list[str, int] = FloweringPlant("Rose", 25, "Red")
    daisy: list[str, int] = FloweringPlant("Daisy", 9, "Yellow")
    sunflower: list[str, int] = PrizerFlower("Sunflower", 50, "Yellow", 0)

    alice_garden.add_plants(tree)
    alice_garden.add_plants(rose)
    alice_garden.add_plants(daisy)
    alice_garden.add_plants(sunflower)

    bob_plant: list[str, int] = Plant("Old Bush", 92)
    bob_garden.add_plants(bob_plant)
    print("")
    print("Alice helping all plants grow...")
    alice_garden.grow_all()
    print("")
    alice_garden.display_report()
    GardenManager.display_summary(network)


if __name__ == "__main__":
    main()
