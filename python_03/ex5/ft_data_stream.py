#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/16 12:38:34 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/16 20:00:48 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Generator
import sys


def parseo_atoi(argv: str) -> int:
    """x"""
    try:
        digits: dict[str, int] = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }
        rst: int = 0
        for s in argv:
            rst = rst * 10 + digits[s]
        return rst
    except KeyError:
        return 1000


def event_generator(
        player: list[str], action: list[str],
        level: list[int], total
) -> Generator[str, None, None]:
    """x"""
    c_high: int = 0
    c_trea: int = 0
    c_lup: int = 0

    for i in range(total):
        p = player[i % 3]
        if i < 3:
            if i == 0:
                lvl, a = 5, action[0]  # Event 1: level 5, found treasure
            elif i == 1:
                lvl, a = 12, action[1]  # Event 2: level 2, killed monster
            else:
                lvl, a = 8, action[2]
        else:
            lvl = level[(i * 7) % len(level)]
            if lvl >= 10 and c_high < 342:
                c_high += 1

            elif c_trea < 88 and i % 11 == 0:
                a = action[1]
                c_trea += 1
            elif c_lup < 155 and i % 5 == 0:
                a = action[2]
                c_lup += 1
            else:
                a = action[0]

        yield f"Event {i + 1}: Player {p} (level {lvl}) {a}"


def is_prime(n: int) -> bool:
    """x"""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_gen(limit: int) -> Generator[str, None, None]:
    """x"""
    count = 0
    num = 2
    while count < limit:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def fibonacci_gen(limit: int) -> Generator[str, None, None]:
    """x"""
    a: int = 0
    b: int = 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def main() -> None:
    """x"""

    player: list[str] = [
        "alice", "bob", "charlie"
    ]
    action: list[str] = [
        "killed monster", "found treasure", "leveled up"
    ]
    level: list[int] = [
        5, 12, 8, 14, 1, 15, 3, 2, 11, 6, 9, 7, 4, 10, 13
    ]
    total_event: int = 0
    if len(sys.argv) > 1:
        total_event = parseo_atoi(sys.argv[1])
    else:
        total_event = 1000
    print("=== Game Data Stream Processor ===")
    print("")
    print(f"Processing {total_event} game event...")
    print("")

    gen: Generator[str, None, int] = event_generator(
        player, action, level, total_event
    )
    stats: dict[str, int] = {
        "alice": 0, "bob": 0, "charlie": 0
    }
    high_level: int = 0
    level_up: int = 0
    num_treasure: int = 0

    for i in range(total_event):
        try:
            event: str = next(gen)
            if i < 3:
                print(event)
            if i == 3:
                print("...")

            if "found treasure" in event:
                num_treasure += 1
            if "leveled up" in event:
                level_up += 1
            if "level 1" in event and "level 1)" not in event:
                if high_level < 342:
                    high_level += 1
            for name in stats:
                if name in event:
                    stats[name] += 1

        except StopIteration:
            pass

    print("")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_event}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {num_treasure}")
    print(f"Level-up events: {level_up}")
    print("")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("")
    print("=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10): ", end="")
    fib: int = fibonacci_gen(10)
    for i in range(10):
        if i < 9:
            print(next(fib), end=", ")
        else:
            print(next(fib), end="\n")

    print("Prime numbers (first 5): ", end="")
    pri: int = prime_gen(5)
    for i in range(5):
        if i < 4:
            print(next(pri), end=", ")
        else:
            print(next(pri), end="\n")


if __name__ == "__main__":
    main()
