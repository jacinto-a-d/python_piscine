#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   strategies.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/22 13:25:47 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/22 19:19:10 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        if isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal())


class InvalidStrategyError(Exception):
    pass
