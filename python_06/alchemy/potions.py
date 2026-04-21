#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   potions.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/17 17:05:20 by dipekko             #+#    #+#            #
#   Updated: 2026/04/20 20:35:44 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from elements import create_fire, create_water
from .elements import create_earth, create_air


def healing_potion() -> str:

    earth = create_earth()
    air = create_air()
    return f"Healing potion brewed with '{earth} and '{air}'"


def strength_potion() -> str:

    fire = create_fire()
    water = create_water()
    return f"Strength potion brewed with '{fire} and '{water}'"
