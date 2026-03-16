#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/14 22:22:25 by dipekko             #+#    #+#            #
#   Updated: 2026/03/15 17:25:29 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def parseo_arguments(args: list[str]) -> dict[str, int]:
    """x"""
    data: dict[str, int] = {}
    for arg in args[1:]:
        try:
            name, qty = arg.split(":")
            data[name] = int(qty)
        except ValueError:
            continue
    return data


def analytics_inventory(inventory: dict[str, dict[str, int]]) -> None:
    """x"""
    total_items: int = 0
    qty: int = 0
    for data in inventory.values():
        qty = data.get("quantity", 0)
        total_items += qty

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")
    print("")

    print("=== Current Inventory ===")
    for name, data in inventory.items():
        qty = data.get("quantity", 0)
        percentage: float = (qty / total_items * 100) if total_items > 0 else 0
        if qty == 1:
            print(f"{name}: {qty} unit ({percentage:.1f}%)")
        else:
            print(f"{name}: {qty} units ({percentage:.1f}%)")


def max_and_min_items(inventory: dict[str, dict[str, int]]) -> None:
    """x"""

    most_abundant: str = ""
    least_abundant: str = ""
    max_qty: int = 0
    min_qty: int = 0
    is_first: bool = True

    for name, data in inventory.items():
        qty = data.get("quantity", 0)

        if is_first:
            max_qty = qty
            min_qty = qty
            most_abundant = name
            least_abundant = name
            is_first = False
        else:

            if qty > max_qty:
                max_qty = qty
                most_abundant = name

            if qty < min_qty:
                min_qty = qty
                least_abundant = name

    print("=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant} ({max_qty} units)")
    print(f"Least abundant: {least_abundant} ({min_qty} unit)")


def categorice_and_restock(inventory: dict[str, dict[str, int]]) -> None:
    """x"""

    categories: dict[str, dict[str, int]] = {
        "Moderate": {},
        "Scarce": {}
    }
    first_name: bool = False
    restock_name: str = ""
    qty: int = 0
    for name, data in inventory.items():
        qty = data.get("quantity", 0)

        if qty >= 5:
            categories["Moderate"].update({name: qty})
        else:
            categories["Scarce"].update({name: qty})

            if qty == 1:
                if first_name:
                    restock_name += ", "
                restock_name += name
                first_name = True

    print("=== Item Categories ===")
    for group, item in categories.items():
        print(f"{group}: {item}")
    print("")

    print("=== Management Suggestions ===")
    if first_name:
        print(f"Restock needed: {restock_name}")


def dictionary_properties(inventory: dict[str, dict[str, int]]) -> None:
    """x"""

    first_name: bool = True
    all_name: str = ""
    all_qty: str = ""
    qty: int = 0

    for name, data in inventory.items():
        qty = data.get("quantity", 0)

        if not first_name:
            all_name += ", "
            all_qty += ", "

        all_name += name
        all_qty += f"{qty}"
        first_name = False

    print(f"Dictionary keys: {all_name}")
    print(f"Dictionary values: {all_qty}")


def main() -> None:
    """x"""
    inventory: dict[str, dict[str, int]] = {
        "potion": {"Name": "health potion", "type": "Consumable",
                   "quantity": 0, "value": 10},
        "armor": {"Name": "Iron armor", "type": "Equipment",
                  "quantity": 0, "value": 50},
        "shield": {"Name": "Shield", "type": "Equipment",
                   "quantity": 0, "value": 30},
        "sword": {"Name": "Iron sword", "type": "Equipment",
                  "quantity": 0, "value": 50},
        "helmet": {"Name": "Helmet", "type": "Equipment",
                   "quantity": 0, "value": 15}
    }

    backpack: dict[str, int] = parseo_arguments(sys.argv)
    for name, qty in backpack.items():
        if name in inventory:
            inventory[name].update({"quantity": qty})

    print("=== Inventory System Analysis ===")
    analytics_inventory(inventory)
    print("")
    max_and_min_items(inventory)
    print("")
    categorice_and_restock(inventory)
    print("")

    print("=== Dictionary Properties Demo ===")
    dictionary_properties(inventory)

    item_search: str = "sword"
    found: bool = item_search in inventory

    print(f"Sample lookup - '{item_search}' in inventory: {found}")


if __name__ == "__main__":
    main()
