#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   lambda_spells.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/04 13:43:47 by jabad-di            #+#    #+#            #
#   Updated: 2026/05/05 14:14:02 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any


def artefact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return list(sorted(artifacts, key=lambda x: x["power"], reverse=True))


def power_filter(
        mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spell: list[dict[str, Any]]) -> list[str]:
    return list(map(lambda x: f"* {x['name']} *", spell))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0}

    max_p: int = max(mages, key=lambda x: x['power'])['power']
    min_p: int = min(mages, key=lambda x: x['power'])['power']

    avg_p: float = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)

    return {"max_power": max_p, "min_power": min_p, "avg_power": avg_p}


def main() -> None:
    artifacts: list[dict[str, Any]] = [
        {"name": "fire Staff", "power": 92, "type": "weapon"},
        {"name": "Ice Wand", "power": 70, "type": "weapon"},
        {"name": "Crystal Orb", "power": 85, "type": "relic"},
        {"name": "Earth Shield", "power": 48, "type": "armor"},
        {"name": "Shadow Blade", "power": 66, "type": "focus"}
    ]

    print("Testing artefact sorter...")
    result_art: list[dict[str, Any]] = artefact_sorter(artifacts)
    try:
        mage_1: dict[str, Any] = result_art[0]
        mage_2: dict[str, Any] = result_art[1]
        print(
            f"{mage_1['name']} ({mage_1['power']} power) comes "
            f"before {mage_2['name']} ({mage_2['power']} power)"
        )
    except IndexError:
        print("There are not enough artifacts to make a comparison.")
    except Exception as e:
        print(f"magical error occurred: {e}")

    mages: list[dict[str, Any]] = [
        {"name": "Alex", "power": 92, "type": "fire"},
        {"name": "Jordan", "power": 70, "type": "ice"},
        {"name": "Casey", "power": 85, "type": "earth"},
        {"name": "Ember", "power": 48, "type": "light"},
        {"name": "Storm", "power": 66, "type": "shadow"}
    ]

    print("\nTesting spell transformer...")
    spells: list[dict[str, Any]] = [
        {"name": "fireball"},
        {"name": "heal"},
        {"name": "shield"}
    ]
    spell_result: list[str] = spell_transformer(spells)
    for spell in spell_result:
        print(spell, end=" ")

    print("")
    print("\nTesting filter power...")
    try:
        result_mages: list[dict[str, Any]] = power_filter(mages, 66)
        filter_mages = list(
            map(lambda x: f"{x['name']} ({x['power']} power)", result_mages)
        )
        if filter_mages:
            print("\n".join(filter_mages))
        else:
            print("No wizard has been found.")
    except KeyError as e:
        print(f"Key Error: {e}")
    except TypeError as e:
        print(f"Type Error: {e}")
    except Exception as e:
        print(f"magic bug: {e}")

    print("\nTesting mage stats...")
    score_p: dict[str, float] = mage_stats(mages)
    for score, power in score_p.items():
        print(f"{score}: {power} power")


if __name__ == "__main__":
    main()
