#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   creature_capability.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/21 15:16:17 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/21 15:24:13 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(target: str) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
