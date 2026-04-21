#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_4.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/13 14:43:35 by dipekko             #+#    #+#            #
#   Updated: 2026/04/13 14:44:58 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy

print(alchemy.create_air())

try:
    print(alchemy.create_earth())
except ArithmeticError:
    print("Error: create_earth is not exposed")
