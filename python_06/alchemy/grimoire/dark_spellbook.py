#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dark_spellbook.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/17 17:38:41 by dipekko             #+#    #+#            #
#   Updated: 2026/04/17 18:11:49 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .dark_validator import validate_dark_ingredients


def dark_spell_allowed_ingredients() -> list[str]:

    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:

    result = validate_dark_ingredients(ingredients)
    return f"Dark spell recorded: {spell_name} ({result})"
