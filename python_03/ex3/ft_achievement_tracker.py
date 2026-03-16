#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/14 20:18:31 by dipekko             #+#    #+#            #
#   Updated: 2026/03/14 22:20:58 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def all_archievements(players: dict[str, set[str]]) -> set[str]:
    """x"""
    result: set[str] = set()
    for name in players:
        result = result.union(players[name])
    return result


def common_archievements(players: dict[str, set[str]]) -> set[str]:
    """x"""
    result: set[str] = set()
    first: bool = True
    for name in players:
        if first:
            result = players[name]
            first = False
        else:
            result = result.intersection(players[name])
    return result


def rare_archievements(players: dict[str, set[str]]) -> set[str]:
    """x"""
    all_arch: set[str] = all_archievements(players)
    rare: set[str] = set()
    for arch in all_arch:
        count: int = 0
        for name in players:
            if arch in players[name]:
                count += 1
        if count == 1:
            rare = rare.union({arch})
    return rare


def main() -> None:
    """x"""
    players: dict[str, set[str]] = {
        "Alice": {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
        "Bob": {"first_kill", "level_10", "boss_slayer", "collector"},
        "Charlie": {
            "level_10", "treasure_hunter", "boss_slayer",
            "speed_demon", "perfectionist"}
    }

    all_possible: set[str] = {
        "first_kill", "level_10", "treasure_hunter",
        "speed_demon", "boss_slayer", "collector", "legendary_hero"
    }

    print("=== Archievement Tracker System ===")
    print("")
    for name in players:
        archievements = players[name]
        print(f"Player {name} archievements: {archievements}")
    print("")

    print("=== Archievements Analytics ===")
    print(f"All unique archievements: {all_possible}")
    print(f"Total unique archievements: {len(all_possible)}")
    print("")

    common: set[str] = common_archievements(players)
    print(f"Common to all players: {common}")

    rare: str[str] = rare_archievements(players)
    print(f"Rare archievements (1 players): {rare}")
    print("")

    p1: str = ""
    p2: str = ""
    count: int = 0
    for name in players:
        if count == 0:
            p1 = name
        elif count == 1:
            p2 = name
        count += 1

    if p1 and p2:
        common_pair: set[str] = players[p1].intersection(players[p2])
        p1_unique: set[str] = players[p1].difference(players[p2])
        p2_unique: set[str] = players[p2].difference(players[p1])

        print(f"{p1} vs {p2} common: {common_pair}")
        print(f"{p1} unique: {p1_unique}")
        print(f"{p2} unique: {p2_unique}")


if __name__ == "__main__":
    main()
