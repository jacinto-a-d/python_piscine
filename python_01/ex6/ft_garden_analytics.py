#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 13:45:30 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/06 14:57:40 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    """x"""
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
        return f"- {self.name} ({self.height}cm)"


class FloweringPlant(Plant):
    """x"""
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
    """x"""
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        extra_point: int
    ) -> None:
        super().__init__(name, height, color)
        self.point: int = 10 + extra_point
        self.category: str = "prize flowers"

    def get_info(self) -> str:
        return super().get_info() + f", Prize points: {self.point}"


class GardenManager:
    """x"""
    total_manager: int = 0

    class GardenStats:
        """x"""
        def total_points(self, plants_list: list) -> int:
            total: int = 0
            for pl in plants_list:
                total += pl.point
            return total

        def garden_score(sel, plants: list) -> int:
            """x"""
            total_score: int = 0
            for ts in plants:
                total_score += ts.height + ts.point
            return total_score

        def get_count_growth(self, plant: list) -> dict:
            counts: dict = {
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

        def total_height(self, plants_list: list) -> int:
            suma: int = 0
            for su in plants_list:
                suma += su.height
            return suma

    def __init__(self, name: str, jardines: list = None) -> None:
        self.name: str = name
        self.jardines: list = jardines if jardines is not None else []
        self.stats = self.GardenStats()

    def add_plants(self, plant: Plant) -> None:
        self.jardines = self.jardines + [plant]
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self) -> None:
        for a in self.jardines:
            a.grow()

    @classmethod
    def create_garden_network(cls, garden_list: list = None) -> list:
        """x"""
        red: list = []
        names: list = garden_list if garden_list else []
        for r in names:
            now_garden = cls(r)
            red = red + [now_garden]
            cls.total_manager += 1
        return red

    def display_report(self) -> None:
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")

        for i in self.jardines:
            print(i.get_info())

        data: dict = self.stats.get_count_growth(self.jardines)

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
        for v in self.jardines:
            if v.height < 0:
                is_valid = False
        print(f"height validartion test: {is_valid}")

    @classmethod
    def display_summary(cls, network: list) -> None:
        """x"""
        print("Garden score - ", end="")
        first = True
        
        for sc in network:
            if not first:
                print(", ", end="")
            
            score = sc.stats.garden_score(sc.jardines)
            print(f"{sc.name}: {score}", end="")
            first = False

        print("")
        print(f"Total garden managed: {cls.total_manager}")

    @staticmethod
    def title() -> None:
        """x"""
        print("=== Garden Management System Demo ===\n")


def main() -> None:
    GardenManager.title()

    names: list = ["Alice", "Bob"]
    network: list = GardenManager.create_garden_network(names)
    alice_garden: GardenManager = network[0]

    tree = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 26, "Red")
    sunflower = PrizerFlower("Sunflower", 51, "Yellow", 10)

    alice_garden.add_plants(tree)
    alice_garden.add_plants(rose)
    alice_garden.add_plants(sunflower)
    print("")
    print("Alice helping all plants grow...")
    alice_garden.grow_all()
    print("")
    alice_garden.display_report()
    GardenManager.display_summary(network)


if __name__ == "__main__":
    main()
