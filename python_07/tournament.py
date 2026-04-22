#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   tournament.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/22 13:23:24 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/22 16:54:28 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.creature import Creature, FlameFactory, AquaFactory, CreatureFactory
from ex1.factories import TransformCreatureFactory, HealingCreatureFactory
from ex2.strategies import NormalStrategy, AggressiveStrategy, DefensiveStrategy, BattleStrategy
from typing import TypeAlias


def start_tournament(opponent: list[tuple[CreatureFactory, BattleStrategy]], tittle: str) -> None:
    print(f"{tittle}")
    opponent_data: list[tuple[Creature, BattleStrategy]] = []
    summary: list[str] = []
    for f, s in opponent:
        creature: Creature = f.create_base()
        opponent_data.append((creature, s))
        clean_creature: str = creature.name.replace("Creature", "")
        summary.append(f"({clean_creature}+{s.name})")
        
    print(f"[{', '.join(summary)}]")
    print("*** Tournament ***")
    print(f"{len(opponent_data)} opponents involved")
    

def main() -> None:
    test_0: list[tuple[CreatureFactory, BattleStrategy]] = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    test_1: list[tuple[CreatureFactory, BattleStrategy]] = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    test_2: list[tuple[CreatureFactory, BattleStrategy]] = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]

    start_tournament(test_0, "Tournament 0 (basic)")
    start_tournament(test_1, "Tournament 1 (error)")
    start_tournament(test_2, "Tournament 2 (multiple)")

if __name__ == "__main__":
    main()
    