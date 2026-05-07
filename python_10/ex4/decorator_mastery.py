#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   decorator_mastery.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/07 19:08:00 by jabad-di            #+#    #+#            #
#   Updated: 2026/05/07 19:48:30 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from functools import wraps, staticmethod
from collections.abc import Callable
from typing import Any
import time

def spell_timer(func: Callable) -> Callable:
    """ * Decorador cronometro de ejecucion *
            -> Crea un decorador que mida el tiempo de ejecucion
        de la funcion
            -> Imprime "Casting [nombre_de_la_funcion]..." antes
        de la ejecucion
            -> Imprime "Spell completed in X.XXX seconds" despues
        de la ejecucion (con 3 decimales)
            -> Usa functools.wraps para preservar los metadatos
        originales de la funcion
            -> Devuelve el resultado original de la funcion 
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time: time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time: time = time.perf_counter()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper
        


def power_validator(min_power: int) -> Callable:
    """ * Decorador de validacion parametrizado *
            -> Crea una fabrica de decoradores que valide los
        niveles de poder
            -> Si aplica a una funcion indempendiente cuyo
        primer argumento es power
            -> Si el poder es valido (>= min_power), ejecuta
        la funcion normalmente
            -> Si es invalido, devuelve "Insufficient power for this spell".
            -> Usa functools.wraps correctamente
    """


def retry_spell(max_attemps: int) -> Callable:
    """ * Decorador de reintento *
            -> Crea un decorador que reintente hechizos fallidos
            -> Si la funcion lanza una excepcion, reintentala
        hasta max_attempts veces
            -> Imprime "Spell failed, retrying... (attempt n/max_attempts)".
            -> Si todos los intentos fallan, devuelve 
        "Spell casting failed after max_attempts attempts".
            -> Si un intento tiene exito, devuelve su resultado normalmente
    """


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
            -> Metodo estatico que verifica si un nombre es valido.
        Es valido si tiene al menos 3 caracteres y contiene solo letas
        y espacios
        """

    def cast_spell(self, spell_name: str, power: int) -> str:
        """
            -> Debe usar el decorador power_validator con min_power=10
            -> Si el poder es calido, 
        devuelve "Successfully cast [spell_name] with <power> power".         
            -> De lo contrario, devuelve Insufficient power for this spell"
        """


def main() -> None:
    """
    
    """


if __name__ == "__main__":
    main()
