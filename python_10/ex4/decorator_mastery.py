#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   decorator_mastery.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/07 19:08:00 by jabad-di            #+#    #+#            #
#   Updated: 2026/05/11 13:12:04 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from functools import wraps
from collections.abc import Callable
from typing import Any
import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time: float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end_time: float = time.perf_counter()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(
        min_power: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if 'power' in kwargs:
                total_p: Any = kwargs['power']
            else:
                total_p = args[2] if len(args) > 2 else args[0]
            if isinstance(total_p, int) and total_p >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(
        max_attempts: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i < max_attempts:
                        print(f"Spell failed, retrying..."
                              f"(attempt {i}/{max_attempts})")
                    else:
                        return (f"Spell casting failed after"
                                f"{max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (isinstance(name, str) and len(name) >= 3 and all(
            s.isalpha() or s.isspace() for s in name))

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("\nTesting spell timer...")

    def fireball() -> None:
        time.sleep(0.101)
        print("Fireball cast!")

    spell: Callable[[], str] = spell_timer(fireball)
    print(f"Result: {spell()}\n")

    print("Testing retry spell...")

    @retry_spell(max_attempts=3)
    def failing_spell() -> None:
        raise Exception("Error")

    result: str = failing_spell()
    print(result)
    print("Waaaaaaagh spelled !\n")

    print("Testing MageGuild...")
    guild: MageGuild = MageGuild()

    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("G1"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
