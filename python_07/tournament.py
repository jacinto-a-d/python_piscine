#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   tournament.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/22 13:23:24 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/22 19:25:25 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.creature import Creature, FlameFactory, AquaFactory, CreatureFactory
from ex1.factories import TransformCreatureFactory, HealingCreatureFactory
from ex2.strategies import NormalStrategy, AggressiveStrategy
from ex2.strategies import DefensiveStrategy, BattleStrategy
from ex2.strategies import InvalidStrategyError


def start_tournament(
        opponents: list[tuple[CreatureFactory, BattleStrategy]],
        tittle: str
) -> None:
    print(f"{tittle}")
    op_names: list[str] = []

    for f, s in opponents:
        f_name: str = f.c_name
        s_name: str = s.__class__.__name__.replace("Strategy", "")
        op_names.append(f"({f_name}+{s_name})")

    print(f" [ {', '.join(op_names)} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")


def battle(
        op_a: tuple[CreatureFactory, BattleStrategy],
        op_b: tuple[CreatureFactory, BattleStrategy]
) -> None:

    fact_a, str_a = op_a
    fact_b, str_b = op_b

    c1: Creature = fact_a.create_base()
    c2: Creature = fact_b.create_base()

    print("* Battle *")
    print(c1.describe())
    print(" vs.")
    print(c2.describe())
    print(" now fight!")

    if not str_a.is_valid(c1):
        raise InvalidStrategyError(
            f"Invalid Creature '{c1.name}' for this strategy"
        )
    str_a.act(c1)

    if not str_b.is_valid(c2):
        raise InvalidStrategyError(
            f"Invalid Creature '{c2.name}' for this strategy"
        )
    str_b.act(c2)
    print("")


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
    for i in range(len(test_0)):
        for j in range(i + 1, len(test_0)):
            if i == j:
                continue
            try:
                battle(test_0[i], test_0[j])
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")

    start_tournament(test_1, "Tournament 1 (error)")
    for i in range(len(test_1)):
        for j in range(i + 1, len(test_1)):
            try:
                battle(test_1[i], test_1[j])
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}\n")

    start_tournament(test_2, "Tournament 2 (multiple)")
    for i in range(len(test_2)):
        for j in range(i + 1, len(test_2)):
            try:
                battle(test_2[i], test_2[j])
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}\n")


if __name__ == "__main__":
    main()
