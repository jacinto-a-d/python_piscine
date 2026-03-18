#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_stream_management.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/18 12:47:19 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/18 17:36:06 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def main() -> None:
    """
    Manages the Cyber Archives communication interface.

    Prompts the user for an archivist ID and status report via stdin,
    then distributes the data across stdout (standard info) and
    stderr (system diagnostics) to verify multi-channel transmission.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    print("Input Stream active. ", end="", file=sys.stdout)
    arch_id: str = input("Enter archivist ID: ")

    print("Input Stream active. ", end="", file=sys.stdout)
    arch_report: str = input("Enter status report: ")
    print("")

    print(f"[STANDARD] Archive status from {arch_id}:"
          f" {arch_report}", file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print("")

    print("Three-channel communication test successful.", file=sys.stdout)


if __name__ == "__main__":
    main()
