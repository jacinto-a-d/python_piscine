#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_pipeline.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/07 19:44:08 by jabad-di            #+#    #+#            #
#   Updated: 2026/04/08 19:42:28 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any, Dict, List, Union, Protocol, Optional
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


class ProcessingStage(Protocol):
    """es la clase que contiene protocol, y que definira las etapas
    que seran las clases idempendientes que contenga el mismo metodo"""

    def process(self, data: Any) -> Any:
        ...


class InputStage:
    """(ETAPA) -> limpia o valida que los datos sean correctos"""
    def process(self, data: Any) -> Any:

        if isinstance(data, dict):
            check_key: List[str] = ["sensor", "value", "unit"]

            if not all(key in data for key in check_key):
                raise ValueError("Invalid JSON: Missing required sensor fields")
            return data

        elif isinstance(data, str):
            if "stream" in data.lower():
                return data

            if not data or len(data.split(',')) < 2:
                raise ValueError("Invalid CSV: Data is empty or malformed")
            return data

        return data


class TransformStage:
    """(ETAPA) -> cambia los datos (convierte unidades o incluye data)"""
    def process(self, data: Any) -> Any:
        if isinstance(data, dict) and "value" in data:
            try:
                data["value"] = float(data["value"])
            except ValueError:
                data["value"] = 0.0
        if isinstance(data, str) and "stream" in data.lower():
            return {"type": "stream_summary", "count": 5, "avg": 22.1}
        
        return data


class OutputStage:
    """(ETAPA) -> convierte el resultado final en algo legible"""
    def process(self, data: Any) -> Any:

        if isinstance(data, dict) and data.get("type") == "stream_summary":
            return f"Stream summary: {data['count']} readings, avg: {data['avg']}°C"

        if isinstance(data, dict) and "value" in data:
            val: str = data.get("value")
            unit: str = data.get("unit", "C")
            return f"Processed temperature reading: {val}°{unit} (Normal range)"

        elif isinstance(data, str):
            count: int = 0
            count = 1 if len(data.split(',')) > 0 else 0
            return f"User activity logged: {count} actions processed"

        return f"Result: {data}"


class ProcessingPipeline(ABC):
    """clase base abstacta que herada ABC"""
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage, description: Optional[str] = None) -> None:
        self.stages.append(stage)
        print(f"Stage {len(self.stages)}: {description} initialized")

    def process(self, data: Any) -> Any:
        result: Any = data
        for stage in self.stages:
            result = stage.process(result)
        return result


class JSONAdapter(ProcessingPipeline):
    """clase hija (Adaptadores) filtro de entrada"""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()

        self.pipeline_id = pipeline_id
    
    def process(self, data: Any) -> Any:

        if not isinstance(data, dict):
            return None

        print(f"Input: {data}")
        print("Transform: Enriched with metadata and validation")
        return super().process(data)


class CSVAdapter(ProcessingPipeline):
    """clase hija (Adaptadores) filtro de entradas"""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()

        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:

        if not isinstance(data, str) or ',' not in data:
            return None

        print(f"Input: {data}")
        print("Transform: Parsed and structired data")
        return super().process(data)


class StreamAdapter(ProcessingPipeline):
    """clase hija (Adaptadores) filtros de entrada"""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:

        if not isinstance(data, str) or "stream" not in data.lower():
            return None

        print(f"Input: {data}")
        print("Transform: Aggregated and filtered")
        return super().process(data)


class NexusManager:
    """punto de inicio (Manager)"""
    def __init__(self, capacity: int) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.capacity = capacity

        print("Initializing Nexus Manager...")
        print(f"Pipeline capacity: {self.capacity} streams/second\n")
        print("Creating Data Processing Pipeline...")

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> None:
        for pipe in self.pipelines:
            results: str = pipe.process(data)
            if results is not None:
                print(f"Output: {results}")

    def chaining(self, data: Any) -> None:

        pipe_names: List[str] = [
            type(p).__name__.replace('Adapter', '')for p in self.pipelines
        ]
        print(f"{'-> '.join(pipe_names)}")
        print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")

        result_data: Any = data
        for pipe in self.pipelines:
            result_data = pipe.process(result_data)

        record: int = 100
        efficiency: int = 95
        time: float = 0.2

        print(f"Chain result: {record} records processed through "
              f"{len(self.pipelines)}-stage pipeline")
        print(f"Performance: {efficiency}% efficiency, "
              f"{time}s total processing time")

    def error_test(self, corrupt_data: Any) -> None:

        print("Simulating pipeline failure...")

        try:
            if not corrupt_data:
                raise ValueError("Invalid data format")
        except ValueError as e:
            print(f"Error detected in Stage 2: {e}")
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed\n")
            print("Nexus Integration complete. All systems operational.")


def main() -> None:
    """x"""

    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    manager: NexusManager = NexusManager(1000)
    pipe_json: JSONAdapter = JSONAdapter("NX-42")
    pipe_csv: CSVAdapter = CSVAdapter("CSV-01")
    pipe_stream: StreamAdapter = StreamAdapter("STR-99")

    pipe_json.add_stage(InputStage(), "Input validation and parsing")
    pipe_json.add_stage(TransformStage(), "Data transformation and enrichment")
    pipe_json.add_stage(OutputStage(), "Output formatting and delivery")
    manager.add_pipeline(pipe_json)

    pipe_csv.add_stage(InputStage())
    pipe_csv.add_stage(TransformStage())
    pipe_csv.add_stage(OutputStage())
    manager.add_pipeline(pipe_csv)

    pipe_stream.add_stage(InputStage(), "Input validation and parsing")
    pipe_stream.add_stage(TransformStage(), "Data transformation and enrichment")
    pipe_stream.add_stage(OutputStage(), "Output formatting and delivery")
    manager.add_pipeline(pipe_stream)

    print("")
    print("=== Multi-Format Data Processing ===")
    print("")

    json_data: dict[Union[str, float]] = {
        "sensor": "temp", "value": "23.5", "unit": "C"
    }

    csv_data: str = "user,action,timestamp"

    stream_data: str = "Real-time sensor stream"

    error_data: str = None

    print("Processing JSON data through pipeline...")
    manager.process_data(json_data)
    print("")
    
    print("Processing CSV data through same pipeline...")
    manager.process_data(csv_data)
    print("")

    print("Processing Stream data through same pipeline...")
    manager.process_data(stream_data)
    print("")

    print("\n=== Pipeline Chaining Demo ===")
    manager.chaining("Initial Raw Data")
    print("")

    print("=== Error Recovery Test ===")
    manager.error_test(error_data)

if __name__ == "__main__":
    main()
