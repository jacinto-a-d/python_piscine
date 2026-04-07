#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_pipeline.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/07 19:44:08 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/07 19:49:57 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any, Dict, List, Union
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def __init__(self, name: str) -> None:
        self._dataprocessor: list[tuple[int, str]] = []
        self._total_processed: int = 0
        self.name: str = name
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @property
    def processor_name(self) -> str:
        return type(self).__name__

    def output(self) -> tuple[int, str]:
        if not self._dataprocessor:
            raise IndexError("Error")
        element: tuple[int, str] = self._dataprocessor.pop(0)
        return element


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__(name="Numeric Processor")

    def validate(self, data: Any) -> bool:

        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, List):
            return all(isinstance(n, (int, float)) and not isinstance(n, bool)
                       for n in data)
        return False

    def ingest(self, data: Any) -> None:

        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items: List[Union[int, float]]
        items = data if isinstance(data, list) else [data]

        for n in items:
            self._dataprocessor.append((self._rank, str(n)))
            self._rank += 1
            self._total_processed += 1


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__(name="Text Processor")

    def validate(self, data: Any) -> bool:

        if isinstance(data, str):
            return True
        if isinstance(data, List):
            return all(isinstance(s, str) for s in data)
        return False

    def ingest(self, data: Any) -> None:

        if not self.validate(data):
            raise ValueError("Improper text data")

        items: List[str] = data if isinstance(data, list) else [data]

        for s in items:
            self._dataprocessor.append((self._rank, s))
            self._rank += 1
            self._total_processed += 1


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__(name="Log Processor")

    def validate(self, data: Any) -> bool:

        if isinstance(data, Dict):
            return 'log_level' in data and 'log_message' in data
        if isinstance(data, List):
            return all(self.validate(item) for item in data)
        return False

    def ingest(self, data: Any) -> None:

        if not self.validate(data):
            raise ValueError("Improper log data")

        items: List[dict[str, str]]
        items = data if isinstance(data, List) else [data]

        for log_dict in items:
            lvl: str = log_dict.get('log_level', "")
            msg: str = log_dict.get('log_message', "")
            log_formatted: str = f"{lvl}: {msg}"
            self._dataprocessor.append((self._rank, log_formatted))
            self._rank += 1
            self._total_processed += 1


class DataStream():

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """x"""
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """x"""
        for element in stream:
            check: bool = False

            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    check = True
                    break

            if not check:
                print(f"DataStream error -"
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:

        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            t: int = proc._total_processed
            r: int = len(proc._dataprocessor)
            print(f"{proc.name}: total {t} items processed, "
                  f"remaining {r} on processor")