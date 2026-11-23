"""FIFO page replacement algorithm."""
from typing import List, Optional
from models import Step, Result


def fifo_page_replacement(pages: List[int], frame_count: int) -> Result:
    frames: List[Optional[int]] = [None] * frame_count
    insertion_order = []
    steps = []
    hits = faults = 0

    for page in pages:
        if page in frames:
            hits += 1
            hit = True
        else:
            faults += 1
            hit = False
            if None in frames:
                slot = frames.index(None)
            else:
                oldest_page = insertion_order.pop(0)
                slot = frames.index(oldest_page)
            frames[slot] = page
            insertion_order.append(page)

        steps.append(Step(page, frames.copy(), hit))

    return Result("FIFO", steps, hits, faults, frames.copy())
