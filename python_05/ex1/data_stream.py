#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_stream.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jabad-di <jabad-di@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/24 15:35:35 by jabad-di            #+#    #+#            #
#   Updated: 2026/03/24 20:46:07 by jabad-di           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any, Optional, Dict, List, Union
from abc import ABC, abstractmethod

#clase base
class DataStream(ABC):
    """es la clase padre"""
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        # Añadir un print en el constructor de tus clases especializadas.
    
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        #filtra datos segun el criterio.
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        #devuelve estadisticas del flujo.
        pass

class SensorStream(DataStream):
    """clase hija, para datos ambientales(lecturas de sensores)"""
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

        print("Initializing Sensor Stream...")
        print(f"Stream ID: {stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:

        data_sensor: dict[Any, Any] = data_batch[0]
        items: List[str] = [f"{i}:{t}" for i, t in data_sensor.items()]
        print(f"Processing sensor batch: [{', '.join(items)}]")

        num_process: int = 0
        for _ in data_sensor:
            num_process += 1

        avg_tmp: float = data_sensor.get("temp", 0)
        print(f"sensor analysis: {num_process} reading processed, avg temp: {avg_tmp:.1f}°C")
        return ""

class TransactionStream(DataStream):
    """clase hija, para datos financieros(lecturas de compra/venta)"""
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

        print("Initializing Transaction Stream...")
        print(f"Stream ID: {stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:

        num_op: int = 0
        net_flow: float = 0.0
        items_dply: list[str] = []

        for op_dict in data_batch:
            for key, value in op_dict.items():
                items_dply.append(f"{key}:{value}")
                if "buy" in key.lower():
                    net_flow += value
                elif "sell" in key.lower():
                    net_flow -= value
            num_op += 1

        print(f"Processing transaction batch: [{', '.join(items_dply)}]")
        print(f"Transaction analysis: {num_op} operations, net flow: +{net_flow:.1f} units")
        return ""


class EventStream(DataStream):
    """clase hija, para eventos del sistema(log de usuario, errores)"""
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

        print("Initializing Event Stream...")
        print(f"Stream ID: {stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:

        event_set: List[Any] = data_batch[0]
        event_list: List[str] = []
        for e in event_set:
            event_list.append(e)

        print(f"Processing event batch: {event_list}")

        num_event: int = 0
        num_error: int = 0

        for event in event_set:
            if event == "error":
                num_error += 1
            num_event += 1

        print(f"Event analysis: {num_event} events, {num_error} error detected")
        return ""
            

class StreamProcessor:
    """es una clase aparte que su trabajo es recibir una lista de flujos(stream)
    y darle ordenes"""
    def __init__(self) -> None:
        self.streams: List[tupleDataStream] = [
            SensorStream("SENSOR_001"),
            TransactionStream("TRANS_001"),
            EventStream("EVENT_001")
        ]

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batch_dict: Dict[str, List[Any]]) -> None:
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

        for stream in self.streams:
            id: str = stream.stream_id
            data: List[Any] = batch_dict.get(id, [])
            stream.process_batch(data)
            print("")


def main() -> None:

    batchs: Dict[str, List[Any]] = {
        "SENSOR_001": [{"temp": 22.5, "humidity": 65, "pressure": 1013}],
        "TRANS_001": [{"buy": 100}, {"sell": 150}, {"buy": 75}],
        "EVENT_001": [{"login", "error", "logout"}]
    }
    
    processor: StreamProcessor = StreamProcessor()
    processor.process_all(batchs)


if __name__ == "__main__":
    main()
