#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/24 21:00:10 by jabad-di            #+#    #+#            #
#   Updated: 2026/02/24 21:30:57 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize()

    if unit == "packets":
        print(f"{name} seeds: {quantity} packets avaible")
    elif unit == "grams":
        print(f"{name} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{name} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
