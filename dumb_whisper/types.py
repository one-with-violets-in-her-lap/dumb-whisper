from dataclasses import dataclass
from typing import Generator


@dataclass
class Segment:
    id: int
    start: float
    end: float
    text: str


@dataclass
class TranscriptionInfo:
    seconds_duration: float


@dataclass
class Transcription:
    segments: Generator[Segment]
    language: str
    info: TranscriptionInfo
