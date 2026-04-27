#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_0.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 14:00:27 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/27 15:08:44 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.grimoire.light_spellbook as light_spellbook

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    result: str = light_spellbook.light_spell_record(
        "Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {result}")
