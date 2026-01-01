from dataclasses import dataclass
from typing import Generator


@dataclass
class Segment:
    id: int
    start: float
    end: float
    text: str


@dataclass
class TranscriptionResult:
    segments: Generator[Segment]
    language: str
