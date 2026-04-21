#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_pipeline.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: dipekko <dipekko@student.42.fr>              +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/07 19:44:08 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/13 14:15:21 by dipekko            ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any, Dict, List, Union, Protocol
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

    def output(self) -> tuple[int, str]:
        if not self._dataprocessor:
            raise IndexError("No data to output")
        return self._dataprocessor.pop(0)


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__("Numeric Processor")

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

        for item in items:
            self._dataprocessor.append((self._rank, str(item)))
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

        for item in items:
            self._dataprocessor.append((self._rank, item))
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


class ExportPlugin(Protocol):
    """es la clase que contiene protocol, y que definira las etapas
    que seran las clases idempendientes que contenga el mismo metodo"""

    def process_output(self, data: List[tuple[int, str]]) -> None:
        ...


class CSVExport:
    """clase hija (Adaptadores) filtro de entrada"""
    def process_output(self, data: List[tuple[int, str]]) -> None:
        if not data:
            return

        print("CSV Output:")
        print(",".join([item[1] for item in data]))


class JSONExport:
    """clase hija (Adaptadores) filtro de entradas"""
    def process_output(self, data: List[tuple[int, str]]) -> None:
        if not data:
            return

        print("JSON Output:")
        items = [f'"item_{i}": "{val}"' for i, val in data]
        print("{" + ", ".join(items) + "}")


class DataStream:

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            collected = []
            for _ in range(nb):
                try:
                    collected.append(proc.output())
                except IndexError:
                    break
            plugin.process_output(collected)


def main() -> None:
    """x"""

    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    ds = DataStream()
    ds.print_processors_stats()
    print("")

    print("Registering Processors\n")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    batch1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch1}\n")
    ds.process_stream(batch1)
    ds.print_processors_stats()
    print("")
    print("Send 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVExport())
    print("")
    ds.print_processors_stats()
    print("")

    batch2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
              [{'log_level': 'ERROR',
                'log_message': '500 server crash'},
               {'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'}],
              [32, 42, 64, 84, 128, 168],
              'World hello']

    print(f"Send another batch of data: {batch2}\n")
    ds.process_stream(batch2)
    ds.print_processors_stats()
    print("")
    print("Send 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONExport())
    print("")
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
