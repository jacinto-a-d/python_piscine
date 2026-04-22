#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   factories.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/21 15:28:51 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/22 17:59:31 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.creature import CreatureFactory, Creature
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()
        self.c_name = "Healing"

    def create_base(self) -> Creature:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Creature:
        return Bloomelle("Bloomelle", "Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()
        self.c_name = "Transform"

    def create_base(self) -> Creature:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Creature:
        return Morphagon("Morphagon", "Normal/Dragon")
