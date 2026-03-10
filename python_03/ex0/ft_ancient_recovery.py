#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_ancient_recovery.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/09 23:51:13 by dipekko             #+#    #+#            #
#   Updated: 2026/03/10 00:34:06 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def recovery_ancient_frafment() -> None:
    """x"""
    try:
        with open("ascent_fragment.txt", "r") as fd:
            print("Connection established...\n")
            print("RECOVERED DATA:")

            data: str = fd.read()
            print(data)
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    else:
        print("Data recovery complete. Storage unit disconnected.")


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fracment.txt")
    recovery_ancient_frafment()


if __name__ == "__main__":
    main()
