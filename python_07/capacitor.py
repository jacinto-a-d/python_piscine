#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   capacitor.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/21 15:14:27 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/22 13:20:19 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import TransformCapability, HealCapability


def main() -> None:
    print("Testing Creature with healing capability")

    hf: HealingCreatureFactory = HealingCreatureFactory()
    for label, creature in [("base", hf.create_base()),
                            ("evolved", hf.create_evolved())]:
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())

    print("\nTesting Creature with transform capability")

    tf: TransformCreatureFactory = TransformCreatureFactory()
    for label, creature in [("base", tf.create_base()),
                            ("evolved", tf.create_evolved())]:
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


if __name__ == "__main__":
    main()
