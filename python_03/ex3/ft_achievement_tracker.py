#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/16 12:38:17 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/17 19:32:46 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def all_achievements(players: dict[str, set[str]]) -> set[str]:
    """
    Retrieves a union of all unique achievements earned
    by all players.
    """
    result: set[str] = set()
    for achievement in players.values():
        result = result.union(achievement)
    return result


def common_achievements(players: dict[str, set[str]]) -> set[str]:
    """
    Identifies achievements that have been earned
    by every single player.
    """
    if not players:
        return set()
    return set.intersection(*players.values())


def rare_achievements(players: dict[str, set[str]]) -> set[str]:
    """
    Finds 'rare' achievements, defined as those owned
    by exactly one player.
    """
    all_arch: set[str] = all_achievements(players)
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
    """
    Main entry point of the script.
    Simulates the achievement tracking system and
    prints analytics to the console.
    """
    players: dict[str, set[str]] = {
        "Alice": {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
        "Bob": {"first_kill", "level_10", "boss_slayer", "collector"},
        "Charlie": {
            "level_10", "treasure_hunter", "boss_slayer",
            "speed_demon", "perfectionist"}
    }

    print("=== Achievement Tracker System ===")
    print("")
    for name, arch in players.items():
        print(f"Player {name} achievements: {arch}")
    print("")

    print("=== Achievements Analytics ===")
    all_unique: set[str] = all_achievements(players)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")
    print("")
    print(f"Common to all players: {common_achievements(players)}")
    print(f"Rare achievements (1 players): {rare_achievements(players)}")
    print("")

    p1: str = ""
    p2: str = ""
    if len(players) >= 2:
        p1, p2, *_ = players.keys()

    if p1 and p2:
        common_pair: set[str] = players[p1].intersection(players[p2])
        p1_unique: set[str] = players[p1].difference(players[p2])
        p2_unique: set[str] = players[p2].difference(players[p1])

        print(f"{p1} vs {p2} common: {common_pair}")
        print(f"{p1} unique: {p1_unique}")
        print(f"{p2} unique: {p2_unique}")


if __name__ == "__main__":
    main()
