#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   alien_contact.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/28 14:06:05 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/28 15:47:47 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validation_alien(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        is_physical: bool = self.contact_type == ContactType.PHYSICAL
        if is_physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        is_telepathic: bool = self.contact_type == ContactType.TELEPATHIC
        if is_telepathic and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")

    try:
        alien: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.RADIO,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Message: '{alien.message_received}'")
    except ValidationError as e:
        message_detail: list[str] = [err['msg'] for err in e.errors()]
        print(message_detail[0].replace("Value error, ", ""))

    print("\n======================================")
    print("Expected validation error:")

    try:
        invalid_alien: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
        print(invalid_alien.contact_type)
    except ValidationError as e:
        message: list[str] = [err['msg'] for err in e.errors()]
        print(message[0].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
