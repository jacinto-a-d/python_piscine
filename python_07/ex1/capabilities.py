#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   capabilities.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/21 15:16:17 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/22 17:59:38 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
