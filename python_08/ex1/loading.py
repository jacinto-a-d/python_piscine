#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <jabad-di@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/23 15:37:24 by jabad-di             #+#    #+#            #
#   Updated: 2026/04/24 13:54:08 by jabad-di            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import importlib
from typing import Any


def check_dependencies() -> None:
    packages: dict[str, str] = {"pandas": "Data manipulation ready",
                                "numpy": "Numerical computation ready",
                                "requests": "Network access ready",
                                "matplotlib": "Visualization ready"
                                }
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    for pkg, desc in packages.items():
        try:
            lib: Any = importlib.import_module(pkg)
            version: str = getattr(lib, "__version__", "unknown")
            print(f" [OK] {pkg} ({version}) - {desc}")
        except ImportError:
            print(f" [ERROR] {pkg} is missing.")
            print(
                "Install with: pip install -r requirements.txt"
                "OR poetry install"
            )
            sys.exit(1)


def analyze_data() -> None:

    np: Any = importlib.import_module("numpy")
    pd: Any = importlib.import_module("pandas")
    plt: Any = importlib.import_module("matplotlib.pyplot")

    n_points: int = 1000
    print("\nAnalyzing Matrix data...")
    data: Any = np.random.randn(n_points)
    df: Any = pd.DataFrame(data, columns=['Matrix Signal'])

    df.plot()
    print(f"Processing {n_points} data points...")
    print("Generating visualization...\n")
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    check_dependencies()
    analyze_data()
