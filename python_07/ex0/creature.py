#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   creature.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/20 22:03:20 by dipekko             #+#    #+#            #
#   Updated: 2026/04/20 22:21:30 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, name: str, type: str) -> None:
        self.name: str = name
        self.type: str = type

    def descibe(self) -> None:
        pass

    @abstractmethod
    def attack(self) -> None:
        pass


class Flameling(Creature):
    pass


class Pyrodon(Creature):
    pass


class Aquabub(Creature):
    pass


class Torragon(Creature):
    pass


class CreatureFactory(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def Create_base(self) -> None:
        pass

    def create_evolved(self) -> None:
        pass


class FlameFactory(CreatureFactory):
    pass


class AquaFactory(CreatureFactory):
    pass
