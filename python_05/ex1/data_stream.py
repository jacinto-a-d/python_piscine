#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_stream.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/24 15:35:35 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/21 15:06:53 by jabad-di           ###   ########.fr      #
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
            lvl_ok = isinstance(data.get("log_level"), str)
            msg_ok = isinstance(data.get("log_message"), str)
            return lvl_ok and msg_ok

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

        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:

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


def main() -> None:

    ds: DataStream = DataStream()

    streams: list[Union[
        str,
        list[float],
        list[dict[str, str]],
        int,
        list[str]
    ]]

    streams = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    np: NumericProcessor = NumericProcessor()
    tp: TextProcessor = TextProcessor()
    lp: LogProcessor = LogProcessor()

    print("=== Code Nexus - Data Stream ===\n")
    print("Initializa Data Stream...")

    ds.print_processors_stats()
    print("")
    print("Registering Numeric Processor\n")
    print(f"Send first batch of data on stream: {streams}")
    ds.register_processor(np)
    ds.process_stream(streams)
    ds.print_processors_stats()
    print("")

    print("Registering other data processors")
    print("Send the same batch again")
    ds.register_processor(tp)
    ds.register_processor(lp)
    ds.process_stream(streams)
    ds.print_processors_stats()
    print("")

    print("Consume some elements from the data"
          "processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        np.output()
    for _ in range(2):
        tp.output()
    for _ in range(1):
        lp.output()

    ds.print_processors_stats()


if __name__ == "__main__":
    main()
