#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/10 00:35:24 by dipekko             #+#    #+#            #
#   Updated: 2026/03/10 00:45:25 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def create_archive() -> None:
    archive: str = (input("Enter data record to archive: "))

    print("Attempting to create new archive...")
    with open("new_archive.txt", "w") as fd:
        print("SYSTEM: Writing data to new_archive.txt...")
        fd.write(archive)
    print("SUCESS: Data record has been safely preserved.")


if __name__ == "__main__":
    create_archive()
