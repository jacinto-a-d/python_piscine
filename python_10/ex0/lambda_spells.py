#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   lambda_spells.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/04 13:43:47 by jabad-di            #+#    #+#            #
#   Updated: 2026/05/04 21:30:57 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def artefact_sorter(artifacts: list[dict]) -> list[dict]:
    """ -> Ordenar actefactos
        -> Usar sorted() con un lambda para ordenart por el nivel
        de power de forma descendente
        -> cada artefacto es un deccionario {'name': str, 'power': int, 'type': str}
        """
    return list(sorted(artifacts, key=lambda x: x["power"], reverse=True))
  

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """ -> Filtrar magos con power
        -> Usar Filter() con un lambda para encontrar magos cuyo poder
        sea >= min_power
        -> Cada mago es un diccionario {'name': str, 'power': int, 'type': str}
        """
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spell: list[str]) -> list[dict]:
    """ -> Transformar nombres de hechizos
        -> Usar map() con un lambda para añadir el prefijo "* " y
        el sufijo " *" a cada nombre
        -> "fireball" se convierte en "* fireball *"."""
    return list(map(lambda x: f"* {x['name']} *", spell))


def mage_stats(mages: list[dict]) -> dict:
    """ -> Calcular estadisticas de power
        -> Usar lambdas con max() y min() para encontrar
                -> El nivel de poder de mago mas poderoso
                -> El nivel de poder de mago menos poderoso
                -> El nivel de poder promedio (redondeado a 2 decimales)
        -> Devuelve un diccionario {'max_power': int, 'min_power': int, 'avg_power': float}.
        """
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0}

    max_p: int = max(lambda x: x['power']['power'])
    min_p: int = min(lambda x: x['power']['power'])

    total_p: int = sum(lambda x: x['power'], mages)
    avg_p: float = round(total_p / len(mages), 2)

    return {"max_power": max_p, "min_power": min_p, "avg_power": avg_p}


def main() -> None:

    artifacts: list[dict[str, int]] = [
        {"name": "fire Staff", "power": 92, "type": "weapon"},
        {"name": "Ice Wand", "power": 70, "type": "weapon"},
        {"name": "Crystal Orb", "power": 85, "type": "relic"},
        {"name": "Earth Shield", "power": 48, "type": "armor"},
        {"name": "Shadow Blade", "power": 66, "type": "focus"}
    ]

    print("Testing artefact sorter...")
    result_art: list[dict[str, int]] = artefact_sorter(artifacts)
    try:        
        mage_1: dict[str, int] = result_art[0]
        mage_2: dict[str, int] = result_art[1]
        print(f"{mage_1['name']} ({mage_1['power']} power) comes "
                f"before {mage_2['name']} ({mage_2['power']} power)"
        )
    except IndexError:
        print("There are not enough artifacts to make a comparison.")
    except Exception as e:
        print(f"magical error occurred: {e}")

    mages: list[dict[str, int]] = [
        {"name": "Alex", "power": 92, "type": "fire"},
        {"name": "Jordan", "power": 70, "type": "ice"},
        {"name": "Casey", "power": 85, "type": "earth"},
        {"name": "Ember", "power": 48, "type": "light"},
        {"name": "Storm", "power": 66, "type": "shadow"}
    ]

    print("\nTesting spell transformer...")
    spells: list[str] = ["fireball", "heal", "shield"]
    spell_result: list[str] = spell_transformer(spells)
    for spell in spell_result:
        print(spell)
    
    print("\nTesting filter power...")
    try:
        result_mages: list[dict[str, int]] = power_filter(mages, 66)
        filter_mages = list(map(lambda x: f"{x['name']} ({x['power']} power)", result_mages))
        if filter_mages:
            print("\n".join(filter_mages))
        else:
            print("No wizard has been found.")
    except KeyError as e:
        print(f"Key Error: {e}")
    except TypeError as e:
        print(f"Type Error: {e}")
    except Exception as e:
        print(f"magic bug: {e}")

    
        
        


if __name__ == "__main__":
    main()
