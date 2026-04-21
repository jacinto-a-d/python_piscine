#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_validator.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/17 17:39:45 by dipekko             #+#    #+#            #
#   Updated: 2026/04/17 17:45:49 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:

    allowed = light_spell_allowed_ingredients()

    for item in allowed:
        if item.lower() in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
