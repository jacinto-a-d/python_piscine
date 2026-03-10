#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/10 17:26:20 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/10 17:53:25 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def create_archive() -> None:
    """Establishes a new preservation protocol by creating a storage unit."""
    file_name: str = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("")
    print(f"Initializing new storage unit: {file_name}")
    print("Storage unit created successfully...")
    print("")
    data: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]

    print("Inscribing preservation data...")
    with open("new_discovery.txt", "w") as fd:
        for line in data:
            fd.write(line + "\n")
            print(f"{line}")
    print("")
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")


if __name__ == "__main__":
    create_archive()
