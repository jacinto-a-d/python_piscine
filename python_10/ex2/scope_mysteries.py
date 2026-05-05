#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   scope_mysteries.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/05 17:29:20 by jabad-di            #+#    #+#            #
#   Updated: 2026/05/05 19:57:37 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(
        initial_power: int
) -> Callable[[], tuple[int, int, int]]:

    total_power: int = initial_power
    add: int = 10

    def add_power() -> tuple[int, int, int]:
        nonlocal add, total_power
        add += 10
        total_power += add
        return initial_power, add, total_power
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def enchantment(target: str) -> str:
        return f"{enchantment_type} {target}"
    return enchantment


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory_system: dict[str, str] = {}

    def store(key: str, value: str) -> str:
        memory_system[key] = value
        return f"Store '{key}' = {value}"

    def recall(key: str) -> str:
        value = memory_system.get(key)
        if value is None:
            return f"Recall '{key}': Memory not found"
        return f"Recall '{key}': {value}"
    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a: Callable[[], int] = mage_counter()
    counter_b: Callable[[], int] = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    power: Callable[[], tuple[int, int, int]] = spell_accumulator(100)
    for _ in range(2):
        t: tuple[int, int, int] = power()
        x, y, z = t
        print(f"Base {x} add {y} = {z}")

    print("\nTesting enchantment factory...")
    ench_1: Callable[[str], str] = enchantment_factory("Flaming")
    ench_2: Callable[[str], str] = enchantment_factory("Frozen")
    print(ench_1("Sword"))
    print(ench_2("Shiel"))

    print("\nTesting memory vault...")
    vault = memory_vault()

    print(vault['store']("secret", "42"))
    print(vault['recall']("secret"))
    print(vault['recall']("unknown"))


if __name__ == "__main__":
    main()
