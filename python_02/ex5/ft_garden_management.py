#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_management.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/09 16:00:45 by dipekko             #+#    #+#            #
#   Updated: 2026/03/09 23:36:34 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    """class for all garden-related custom exceptions."""


class PlantError(GardenError):
    """error handler class for any incident with the plan."""


class WaterError(GardenError):
    """error handler class for water incidents."""


class GardenManager:
    """x"""
    def __init__(self) -> None:
        self.plants: list[str] = []

    def check_add_plant(self, name: str) -> None:
        """Adds a plant using only authorized operatiors"""
        try:
            if name == "":
                raise PlantError("Plant name cannot be empty!")
            self.plants = self.plants + [name]
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def check_water_plant(self) -> None:
        """Demostrates finally block for cleanup"""
        print("Opening watering system")
        try:
            if self.plants == "":
                raise WaterError("Not enough water in tank")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health_plant(self, name: str, water: int, sun: int) -> None:
        """Valites health and handles errors"""
        try:
            if water > 10:
                raise WaterError(f"Water level {water} is too high (max 10)")
            if water < 1:
                raise ValueError(f"Water level {water} is too low (min 1)")
            if sun > 12:
                raise PlantError(f"Sunlight hours {sun} is too high (max 12)")
            if sun < 2:
                raise PlantError(f"Sunlight hours {sun} is too low (min 2)")
            print(f"{name}: healthy (water: {water}, sun: {sun})")
        except (WaterError, PlantError) as e:
            print(f"Error checking {name}: {e}")


def test_garden_management() -> None:
    """x"""
    print("=== Garden Management ===\n")
    manager: GardenManager = GardenManager()
    print("Adding plants to garden...")
    manager.check_add_plant("tomato")
    manager.check_add_plant("lettuce")
    manager.check_add_plant("")
    print("")

    print("Watering plants...")
    manager.check_water_plant()
    print("")

    print("Checking plant health...")
    manager.check_health_plant("tomato", 5, 8)
    manager.check_health_plant("lettuce", 15, 5)
    print("")

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
