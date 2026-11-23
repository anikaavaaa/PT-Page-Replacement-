"""Shared simulation result structures."""
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Step:
    page: int
    frames: List[Optional[int]]
    hit: bool

@dataclass
class Result:
    name: str
    steps: List[Step]
    hits: int
    faults: int
    final_frames: List[Optional[int]]
