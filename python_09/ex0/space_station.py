#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   space_station.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/24 15:03:21 by dipekko             #+#    #+#            #
#   Updated: 2026/04/28 13:57:07 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="Operational"
        )
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxigen: {station.oxygen_level}%")
        print(f"status: {station.notes}")
    except ValidationError as e:
        print(f"Unexpected error creating valid station: {e}")

    print("")
    print("========================================")
    print("Expected validation error:")

    try:
        invalid_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=25,
            power_level=85,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="Operational"
        )
        print(invalid_station.crew_size)
    except ValidationError as e:
        message: list[str] = [err['msg'] for err in e.errors()]
        print(message[0])


if __name__ == "__main__":
    main()
