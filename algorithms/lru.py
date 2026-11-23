"""LRU page replacement algorithm."""
from typing import List, Optional
from models import Step, Result


def lru_page_replacement(pages: List[int], frame_count: int) -> Result:
    frames: List[Optional[int]] = [None] * frame_count
    last_used = {}
    steps = []
    hits = faults = 0

    for index, page in enumerate(pages):
        if page in frames:
            hits += 1
            hit = True
        else:
            faults += 1
            hit = False
            if None in frames:
                slot = frames.index(None)
            else:
                least_recent_page = min(
                    (p for p in frames if p is not None),
                    key=lambda p: last_used[p]
                )
                slot = frames.index(least_recent_page)
            frames[slot] = page

        last_used[page] = index
        steps.append(Step(page, frames.copy(), hit))

    return Result("LRU", steps, hits, faults, frames.copy())
