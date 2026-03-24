#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   stream_processor.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/24 12:07:54 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/24 16:37:41 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, data: Any) -> str:
        return f"Output: {data}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        try:
            for item in data:
                item + 0
            return True
        except TypeError:
            return False

    def process(self, data: Any) -> str:

        if not self.validate(data):
            return "Error: Invalid data"

        count: int = 0
        total: int = 0
        for n in data:
            total += n
            count += 1
        avg: float = total / count if count > 0 else 0.0
        return self.format_output(
            f"Processed {count} numeric values, sum={total}, avg={avg}")


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        try:

            line: str = data[0]
            line + ""
            return True

        except TypeError:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error, Invalid data"

        line: str = data[0]
        letters: int = 0
        words: int = 0

        for _ in line:
            letters += 1

        list_aux: list[str] = line.split()
        for _ in list_aux:
            words += 1

        return self.format_output(
            f"Processed text: {letters} characters, {words} words")


class LogProcessor(DataProcessor):

    def format_output(self, data: Any) -> str:
        return f"Output: [ALERT] {data}"

    def validate(self, data: Any) -> bool:
        try:
            data + ""

            if "INFO" in data or "ERROR" in data:
                return True
            return False
        except TypeError:
            return False

    def process(self, data: Any) -> str:

        if "ERROR" in data:
            lvl: str = "ERROR"
            init: int = 7
        else:
            lvl = "INFO"
            init = 6

        clean: str = data[init:]
        return self.format_output(f"{lvl} level detected: {clean}")


def main() -> None:

    data_num: List[int] = [1, 2, 3, 4, 5]
    data_str: List[str] = ["Hello Nexus Words"]
    data_log: str = "ERROR: Connection timeout"

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("")
    print("Initializing Numeric Processor...")
    print(f"Processing data: {data_num}")

    proc_num: NumericProcessor = NumericProcessor()
    if proc_num.validate(data_num):
        print("Validation: Numeric data verified")
        print(proc_num.process(data_num))
    print("")

    print("Initializing Text Processor...")
    print(f"Processing data: {data_str}")

    proc_str: TextProcessor = TextProcessor()
    if proc_str.validate(data_str):
        print("Validation: Text data verified")
        print(proc_str.process(data_str))
    print("")

    print("Initializing Log Processor...")
    print(f"Processing data: \"{data_log}\"")

    proc_log: LogProcessor = LogProcessor()
    if proc_log.validate(data_log):
        print("Validation: Log entry varified")
        print(proc_log.process(data_log))
    print("")
    print("=== Polymorphic Processing Demo ===")
    print("")
    print("Processing multiple data types through same interface...")

    processor: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    dataset: List[Any] = [
        [1, 2, 3],
        ["Hello Nexus."],
        "INFO: System ready"
    ]

    i: int = 0
    while True:
        try:
            result: str = processor[i].process(dataset[i])
            print(f"Result {i + 1}: {result}")
            i += 1
        except IndexError:
            break
    print("")
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
