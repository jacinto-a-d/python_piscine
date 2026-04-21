#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dark_validator.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/17 17:39:08 by dipekko             #+#    #+#            #
#   Updated: 2026/04/17 18:13:25 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:

    allowed = dark_spell_allowed_ingredients()
    for item in allowed:
        if item.lower() in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
