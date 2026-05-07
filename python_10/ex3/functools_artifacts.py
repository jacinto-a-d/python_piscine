#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   functools_artifacts.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/05 19:59:29 by jabad-di            #+#    #+#            #
#   Updated: 2026/05/07 19:58:41 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not isinstance(spells, list):
        raise TypeError("Error: The invalid argument is not a list")
    if not all(isinstance(x, int) for x in spells):
        raise TypeError("all elements of the list must be int")
    if not isinstance(operation, str):
        raise TypeError("Invalid argument, requires a string")
    if len(spells) > 1000:
        raise ValueError("too many spells")
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError(f"invalid operator: {operation}")
    result: int = reduce(operations[operation], spells)
    return result


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:

    if not callable(base_enchantment):
        raise TypeError("base_enchantment must be callable")
    return {
        "fire": partial(base_enchantment, 50, 'Fire'),
        "ice": partial(base_enchantment, 50, 'Ice'),
        "shadow": partial(base_enchantment, 50, 'shadow')
    }


@lru_cache(maxsize=1024)
def memoized_fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be >= 0")
    if n > 1000:
        raise ValueError("n too large")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def shoot(spell: Any) -> str:
        return "unknown spell type"

    @shoot.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @shoot.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @shoot.register(list)
    def _(spell: list[str]) -> str:
        return f"Multi-cast: {len(spell)} spells"
    return shoot


def main() -> None:

    add_num: list[int] = [25, 25, 25, 25]
    mul_num: list[int] = [2, 3, 4, 5, 100, 20]
    nums: list[int] = [20, 3, 40, 34, 9]
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(add_num, 'add')}")
    print(f"Product: {spell_reducer(mul_num, 'multiply')}")
    print(f"Max: {spell_reducer(nums, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    list_spell: list[str] = ["heal", "shield", "lightning"]
    print("\nTesting spell dispatcher...")
    spell: Callable[[Any], str] = spell_dispatcher()
    print(f"{spell(42)}")
    print(f"{spell('fireball')}")
    print(f"{spell(list_spell)}")
    print(f"{spell(None)}")

    print("\nTesting partial_enchanter...")

    def enchanter(power: int, element: str, target: str) -> str:
        return f"Casting {element} spell (Power: {power}) on {target}!"
    mul_enchanter: dict[str, Callable[[str], str]] = (
        partial_enchanter(enchanter))
    print(mul_enchanter['fire']("Dragon"))
    print(mul_enchanter['ice']("Golem"))
    print(mul_enchanter['shadow']("shadow Figure"))


if __name__ == "__main__":
    main()
