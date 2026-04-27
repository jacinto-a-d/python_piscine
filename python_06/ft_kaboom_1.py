#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_1.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 14:00:51 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/27 14:42:41 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    from alchemy.grimoire.dark_spellbook import dark_spell_record

    result: str = dark_spell_record("abra kadabra", "bats, arsenic")
    print(result)
