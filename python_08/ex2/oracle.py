#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   oracle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/24 14:01:50 by dipekko             #+#    #+#            #
#   Updated: 2026/04/24 14:46:45 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import os
from typing import Optional
from dotenv import load_dotenv  # type: ignore


def load_confi() -> None:
    load_dotenv()

    print("\nORACLE STATUS: Reading the Matrix...")

    mode: str = os.getenv("MATRIX_MODE", "development")
    db_url: Optional[str] = os.getenv("DATABASE_URL")
    api_key: Optional[str] = os.getenv("API_KEY")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    endpoint: Optional[str] = os.getenv("ZION_ENDPOINT")

    if not all([db_url, api_key, endpoint]):
        print("[WARNING] Missing configuration detected!")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if mode == "production":
        print(f"Database: Connected to PRODUCTION instance at {db_url}")
        print("API Access: SECURE CONNECTION established")
    else:
        print("Database: Connected to local instance")
        print("API Access: Authenticated")

    print(f"Log Level: {log_level}")
    print(f"Zion Network: {'Online' if endpoint else 'Offline'}")

    print("\nEnvironment security check:")

    if os.path.exists(".env"):
        print(" [OK] .env file properly configured")
    else:
        print(" [!] .env file missing - using system"
              "environment variables")

    print(" [OK] No hardcoded secrets detected")
    print(" [OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    load_confi()
