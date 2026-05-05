#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   higher_magic.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/05 14:15:10 by jabad-di            #+#    #+#            #
#   Updated: 2026/05/05 17:45:05 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable


def spell_combiner(
        spell1: Callable[[str, int], str],
        spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:

    def combined_spell(target: str, power: int) -> tuple[str, str]:
        comb_1: str = spell1(target, power)
        comb_2: str = spell2(target, power)
        return (comb_1, comb_2)
    return combined_spell


def power_amplifier(
        base_spell: Callable[[str, int], str],
        multiplier: int
) -> Callable[[str, int], str]:

    def amplified_power(target: str, power: int) -> str:
        new_power: int = power * multiplier
        return base_spell(target, new_power)
    return amplified_power


def conditional_caster(
        condition: Callable[[str, int], bool],
        spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:

    def check_caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return check_caster


def spell_sequence(
        spell: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    
    def sequenced_spell(target: str, power: int) -> list[str]:
        result: list[str] = [s(target, power) for s in spell]
        return result
    return sequenced_spell


def main() -> None:
    def make_spell(name: str) -> Callable[[str, int], str]:
        def spell(target: str, power: int) -> str:
            if power < 40:
                return str(power)
            else:
                return f"{name} hits {target}"
        return spell

    print("\nTestinf spell combiner...")
    fireball: Callable[[str, int], str] = make_spell("fireball")
    heals: Callable[[str, int], str] = make_spell("heals")
    freeze: Callable[[str, int], str] = make_spell("freeze")

    print(
        f"Combined spell result: {fireball('dragon', 60)}, "
        f"{heals('dragon', 40)}"
    )

    print("\nTesting power amplifier...")
    ampli: Callable[[str, int], str] = power_amplifier(fireball, 10)
    print(
        f"Original: {fireball('dragon', 10)}, "
        f"Amplifier: {ampli('dragon', 3)}"
    )

    print("\nTesting conditional caster...")

    def conditional(target: str, power: int) -> bool:
        return power > 50

    spell_true: Callable[[str, int], str] = (
        conditional_caster(conditional, freeze))
    print("valid:")
    print(spell_true("dragon", 60))
    print("invalid:")
    print(spell_true("dragon", 50))

    print("\nTesting spell sequence...")
    spells: list[Callable[[str, int], str]] = [fireball, heals, freeze]
    cast_spells: Callable[[str, int], list[str]] = spell_sequence(spells)
    cast_total: list[str] = cast_spells("dragon", 40)
    for cast in cast_total:
        print(cast)


if __name__ == "__main__":
    main()
