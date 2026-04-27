#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_1.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/13 14:33:44 by dipekko             #+#    #+#            #
#   Updated: 2026/04/27 14:19:25 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from elements import create_water

if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}")
