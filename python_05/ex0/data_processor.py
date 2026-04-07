#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_processor.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/07 16:32:09 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/07 19:34:43 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from typing import Any, Dict, List, Union
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._dataprocessor: list[tuple[int, str]] = []
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


class TextProcessor(DataProcessor):

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


class LogProcessor(DataProcessor):

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


def main() -> None:

    np: NumericProcessor = NumericProcessor()
    test1: int = 42
    test2: str = "Hello"
    test3: str = "foo"
    test4: List[int] = [1, 2, 3, 4, 5]

    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")

    print(f"Trying to validate input '{test1}': {np.validate(test1)}")
    print(f"Trying to validate input '{test2}': {np.validate(test2)}")

    print(f"Test invalid ingestion of string '{test3}'"
          f"without prior validation:")
    try:
        np.ingest(test3)
    except ValueError as e:
        print(f"Got exception: {e}")

    print(f"Processing data: {test4}")
    np.ingest(test4)
    extract_element_np: int = 3

    print(f"Extracting {extract_element_np} values...")
    for _ in range(0, extract_element_np):
        rank, value = np.output()
        print(f"Numeric value {rank}: {value}")

    print("")

    tp: TextProcessor = TextProcessor()
    test5: List[str] = ['Hello', 'Nexus', 'World']
    extract_element_tp: int = 1
    print("Testing Text Processor...")
    print(f"Trying to validate input '{test1}: {tp.validate(test1)}'")

    try:
        tp.ingest(test5)
    except ValueError as e:
        print(f"Got exception: {e}")

    print(f"Processing data: {test5}")
    print(f"Extracting {extract_element_tp} value...")

    for _ in range(0, extract_element_tp):
        rank, value = tp.output()
        print(f"Text value {rank}: {value}")

    print("")

    lp: LogProcessor = LogProcessor()
    test6: List[Dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]

    print("Testing Log Processor...")
    print(f"Trying to validate input '{test2}': {lp.validate(test2)}")
    print(f"Processing data: {test6}")

    try:
        lp.ingest(test6)
    except ValueError as e:
        print(f"Got exception: {e}")
    extract_element_lp: int = 2
    print(f"Extracting {extract_element_lp} values...")

    for _ in range(extract_element_lp):
        rank, value = lp.output()
        print(f"Log entry {rank}: {value}")

    print("")


if __name__ == "__main__":
    main()
