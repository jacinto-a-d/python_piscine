#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_distillation_1.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 14:00:06 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/27 16:56:41 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy

if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.potions.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")
