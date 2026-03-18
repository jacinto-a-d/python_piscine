#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_vault_security.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/18 17:28:54 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/18 18:27:04 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def main() -> None:
    """
    Implements the vault security protocol.
    Uses 'with' to ensure automatic sealing (RAII).
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    with open("classified_data.txt", "r") as vault:
        for line in vault:
            print(line.strip())

    print("\nSECURE PRESERVATION:")
    with open("security_protocols.txt", "r") as vault:
        for line in vault:
            print(line.strip())

    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
