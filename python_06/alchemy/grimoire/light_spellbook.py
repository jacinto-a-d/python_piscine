#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_spellbook.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/17 17:39:25 by dipekko             #+#    #+#            #
#   Updated: 2026/04/17 17:43:25 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def light_spell_allowed_ingredients() -> list[str]:

    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:

    from .light_validator import validate_ingredients

    result = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({result})"
