#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   __init__.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/13 14:34:16 by dipekko             #+#    #+#            #
#   Updated: 2026/04/17 17:18:18 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .elements import create_air
from .potions import healing_potion


__all__ = ['create_air']

heal = healing_potion
