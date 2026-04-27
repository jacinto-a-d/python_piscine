#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_transmutation_0.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 14:01:12 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/27 15:08:56 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.transmutation.recipes import lead_to_gold

if __name__ == "__main__":
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(f"Testing lead to gold: {lead_to_gold()}")
