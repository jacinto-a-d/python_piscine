#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_transmutation_2.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 14:02:03 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/27 15:09:05 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy

if __name__ == "__main__":
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")

    result: str = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {result}")
