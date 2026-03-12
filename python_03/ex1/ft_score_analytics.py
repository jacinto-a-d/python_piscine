#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/11 14:02:00 by dipekko             #+#    #+#            #
#   Updated: 2026/03/11 16:13:47 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def parseo_score(args: list[str]) -> list[int]:
    """
    Parses a list of string arguments into a list of integers.
    Uses try/except to gracefully handle non-numeric inputs.
    """
    if not args:
        print(
            "No scores provided. Usage:",
            f"python3 {sys.argv[0]} <score1> <score2> ..."
        )
        return []

    score: list[int] = []

    for arg in args:
        try:
            num: int = int(arg)
            score += [num]
        except ValueError:
            print(f"Error: '{arg}' is not valid score.")
    return score


def mid_score(total_score: list[int]) -> float:
    """Calculates the average score from the provided list."""
    average: float = sum(total_score) / len(total_score)
    return average


def high_score(score: list[int]) -> int:
    """Finds the maximum value in the score list."""
    high: int = max(score)
    return high


def low_score(score: list[int]) -> int:
    """Finds the minimum value in the score list."""
    low: int = min(score)
    return low


def range_score(score: list[int]) -> int:
    """Calculates the range between the highest and lowest scores."""
    score_diff: int = max(score) - min(score)
    return score_diff


def main() -> None:
    """
    Main execution flow for Player Score Analytics.
    Handles command line arguments and displays calculated statistics.
    """
    print("=== Player Score Analytics ===")

    scores: list[int] = parseo_score(sys.argv[1:])

    if not scores:
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {mid_score(scores)}")
    print(f"High score: {high_score(scores)}")
    print(f"Low score: {low_score(scores)}")
    print(f"Score range: {range_score(scores)}")


if __name__ == "__main__":
    main()
