#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   creatures.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/21 15:28:32 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/22 13:12:44 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        Creature.__init__(self, name, creature_type)
        HealCapability.__init__(self)

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"

    def attack(self) -> str:
        attack1: str = "Vine Whip!"
        return f"{self.name} uses {attack1}"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        Creature.__init__(self, name, creature_type)
        HealCapability.__init__(self)

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"

    def attack(self) -> str:
        attack1: str = "Petal Dance!"
        return f"{self.name} uses {attack1}"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        Creature.__init__(self, name, creature_type)
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        Creature.__init__(self, name, creature_type)
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        else:
            return f"{self.name} attacks normally."
