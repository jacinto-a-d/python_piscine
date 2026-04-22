#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   construct.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/22 19:39:44 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/22 20:17:00 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import os
import site

def is_venv() -> bool:
    """detecta si el script se ejecuta en un entorno virtual.
    Usa sys.prefix y sys.base_prefix para comparar"""
    return sys.prefix != sys.base_prefix


def main() -> None:
    in_construct: bool =  is_venv()
    python_path: str = sys.executable

    if not in_construct:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("Python3 -m venv matrix_env")
        print("source matrix_env/bin/active   # On Unix")
        print(r"matrix_env\Scripts\activate   # On Windows")
        print("\nThen run this program again.")
    else:
        venv_name: str = os.path.basename(sys.prefix)
        pkg_path: str = site.getsitespackages()[0]

        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {python_path}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print(f"\nPackage installation path:\n {pkg_path}")


if __name__ == "__main__":
    main()
