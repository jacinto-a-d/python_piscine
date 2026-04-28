#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   space_crew.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/28 15:45:32 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/28 17:24:00 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from enum import Enum
from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    year_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_misison(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")\

        ranks: list[Rank] = [mem.rank for mem in self.crew]
        if Rank.CAPTAIN not in ranks and Rank.COMMANDER not in ranks:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            member: list[CrewMember] = [
                m for m in self.crew if m.year_experience >= 5
            ]
            if len(member) < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need 50%"
                    "experienced crew (5+ years)"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")

    try:
        mem_1: CrewMember = CrewMember(
            member_id="M01",
            name="Sarah Conor",
            rank=Rank.COMMANDER,
            age=45,
            specialization="Mission Command",
            year_experience=20
        )

        mem_2: CrewMember = CrewMember(
            member_id="M02",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=30,
            specialization="Navigation",
            year_experience=8
        )

        mem_3: CrewMember = CrewMember(
            member_id="M03",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineering",
            year_experience=4
        )

        mission: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[mem_1, mem_2, mem_3],
            budget_millions=2500.0
        )
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew Size: {len(mission.crew)}")
        for mem in mission.crew:
            print(f"- {mem.name} ({mem.rank.value}) - {mem.specialization}")

    except ValidationError as e:
        print(e)

    print("\n=========================================")
    print("Expected validation error:")

    try:
        mem_4: CrewMember = CrewMember(
            member_id="M01",
            name="Sarah Conor",
            rank=Rank.CADET,
            age=45,
            specialization="Mission Command",
            year_experience=20
        )

        invalid_mission: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[mem_4, mem_2, mem_3],
            budget_millions=2500.0
        )
        print(invalid_mission.crew)
    except ValidationError as e:
        message: list[str] = [err['msg'] for err in e.errors()]
        print(message[0].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
