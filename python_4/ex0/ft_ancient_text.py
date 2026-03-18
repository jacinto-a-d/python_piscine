#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_ancient_text.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/10 17:35:15 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/18 12:47:37 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def recovery_ancient_fragment() -> None:
    """
    Accesses the ancient storage vault and recovers preserved data fragments.
    """
    try:
        with open("ancient_fragment.txt", "r") as fd:
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
    print("Accessing Storage Vault: ancient_fragment.txt")
    recovery_ancient_fragment()


if __name__ == "__main__":
    main()
