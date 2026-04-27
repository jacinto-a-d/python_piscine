#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_3.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/13 14:42:07 by dipekko             #+#    #+#            #
#   Updated: 2026/04/27 15:08:17 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.elements import create_air

if __name__ == "__main__":
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using "
          "'from ... import ...' structure")
    print(f"Testing create_air: {create_air()}")
