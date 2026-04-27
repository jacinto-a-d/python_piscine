#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_5.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/13 14:43:19 by dipekko             #+#    #+#            #
#   Updated: 2026/04/27 14:20:37 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy import create_air

if __name__ == "__main__":
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")
