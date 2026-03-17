#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_analytics_dashboard.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/16 20:02:24 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/17 19:38:23 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def list_score() -> None:
    """Processes player scores using list comprehensions to filter and
    identify duplicates."""
    scores: list[list[str, int]] = [
        ["alice", 4600, "active"], ["bob", 3600, "active"],
        ["charlie", 4300, "active"], ["diana", 4100, "deactivate"],
        ["tommy", 4600, "deactivate"], ["paco", 3600, "deactivate"],
        ["micky", 4300, "deactivate"], ["paca", 4100, "deactivate"]
    ]

    high_score: list[str] = [
        name for name, data, state in scores if data > 2000
    ][:3]
    vals: list[int] = [p[1] for p in scores]
    score_double: list[int] = [
        p[1] for p in scores if
        (vals.count(p[1]) > 1 and p == [s for s in scores if s[1] == p[1]][1])
    ]
    activate: list[str] = [
        name for name, data, state in scores if state == "active"
    ]

    print(f"High scorers (>2000): {high_score}")
    print(f"Scores doubled:{score_double}")
    print(f"Active players: {activate}")


def dict_classification() -> None:
    """Uses dictionary comprehensions to map player names, game modes,
    and achievements."""
    categories: dict[str, dict[str, any]] = {
        "player_1": {"name": "alice", "score": 2300,
                     "mode": "high", "level": 3, "achievement": 5},
        "player_2": {"name": "bob", "score": 1800,
                     "mode": "medium", "level": 2, "achievement": 3},
        "player_3": {"name": "charlie", "score": 2150,
                     "mode": "low", "level": 1, "achievement": 7}
    }

    player_score: dict[str, int] = {
        categories[p]["name"]: categories[p]["score"] for p in categories
    }
    cat_score: dict[str, int] = {
        categories[s]["mode"]: categories[s]["level"] for s in categories
    }
    cat_achievement: dict[str, int] = {
        categories[a]["name"]: categories[a]["achievement"] for a in categories
    }

    print(f"Player scores: {player_score}")
    print(f"Score categories: {cat_score}")
    print(f"Achievement counts: {cat_achievement}")


def set_regions() -> None:
    """Demonstrates set comprehensions to extract unique players,
    achievements, and regions."""
    regions: set[tuple[str, str, str]] = {
        ("alice", "first_kill", "north"),
        ("bob", "level_10", "east"),
        ("charlie", "boss_slayer", "central"),
        ("diana", "first_kill", "north")
    }

    uni_player: set[str] = {name[0] for name in regions}
    uni_achievement: set[str] = {achie[1] for achie in regions}
    act_regions: set[str] = {act[2] for act in regions}
    print(f"Unique players: {uni_player}")
    print(f"Unique achievements: {uni_achievement}")
    print(f"Active regions: {act_regions}")


def analytics() -> None:
    """Performs a global analysis of player data combining list and
    set comprehensions."""
    players_data: list[dict[str, int, set[str]]] = [
        {"name": "alice", "score": 2300,
         "achievements": {"a1", "a2", "a3", "a4", "a5"}},
        {"name": "bob", "score": 1800, "achievements":
         {"a9", "a10", "a11", "a12", "a1", "a2", "a3"}},
        {"name": "charlie", "score": 2150, "achievements": {"a6", "a7", "a8"}},
        {"name": "diana", "score": 2000, "achievements": {"a4", "a5", "a6"}}
    ]

    all_achievements: set[int] = {
        ach for p in players_data for ach in p["achievements"]}

    scores = [p["score"] for p in players_data]

    total_players: int = len(players_data)
    total_unique_achievements: int = len(all_achievements)
    avg_score: float = sum(scores) / len(scores)

    max_val: int = max(scores)
    top_p: dict[str, int, int] = [
        p for p in players_data if p["score"] == max_val][0]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_p['name']} ({top_p['score']} points,"
          f"{len(top_p['achievements'])} achievements)")


def main() -> None:
    """Main entry point for the Game Analytics Dashboard."""
    print("=== Game Analytics Dashboard ===")
    print("")
    print("=== List Comprehension Examples ===")
    list_score()
    print("")
    print("=== Dict Comprehension Examples ===")
    dict_classification()
    print("")
    print("=== Set Comprehension Examples ===")
    set_regions()
    print("")
    print("=== Combined Analysis ===")
    analytics()


if __name__ == "__main__":
    main()
