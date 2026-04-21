#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   battle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/20 21:57:14 by dipekko             #+#    #+#            #
#   Updated: 2026/04/21 15:03:49 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print("")


def test_battle(creature1: CreatureFactory,
                creature2: CreatureFactory) -> None:
    print("Testing battle")

    player1 = creature1.create_base()
    player2 = creature2.create_base()

    print(f"{player1.describe()}\n vs.")
    print(player2.describe())
    print("fight!")

    print(player1.attack())
    print(player2.attack())


if __name__ == "__main__":
    flame_factory: CreatureFactory = FlameFactory()
    aqua_factory: CreatureFactory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)
