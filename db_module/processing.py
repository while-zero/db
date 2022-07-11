from dataclasses import dataclass
from typing import Callable, List


@dataclass
class Source:
    name: str
    type: str
    src: str
@dataclass
class Activity:
    name: str
    source: Source
    action: Callable[[Source], None]


@dataclass
class Stage:
    name: str
    activities: List[Activity]
@dataclass
class Process:
    stages: List[Stage]

@dataclass
class ProcessList:
    processes: List[Process]

@dataclass
class Client:
    name: str
    processes: ProcessList
