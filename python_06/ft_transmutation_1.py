#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_transmutation_1.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 14:01:33 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/27 15:09:01 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.transmutation

if __name__ == "__main__":
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")

    result: str = alchemy.transmutation.lead_to_gold()
    print(f"Testing lead to gold: {result}")
