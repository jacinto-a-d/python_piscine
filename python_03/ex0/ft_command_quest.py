#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/10 19:33:39 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/10 20:26:20 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def check_argument() -> None:
    """x"""
    count: int = len(sys.argv)
    print("=== Command Quest ===")
    if count == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {count}")

    else:
        print(f"Program name: {sys.argv[0]}")
        print("Arguments received:", count - 1)
        i: int = 1
        while i < count:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {count}")


if __name__ == "__main__":
    check_argument()
