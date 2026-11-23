"""OPTIMAL page replacement algorithm."""
from typing import List, Optional
from models import Step, Result


def optimal_page_replacement(pages: List[int], frame_count: int) -> Result:
    frames: List[Optional[int]] = [None] * frame_count
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
                # The page whose next use is farthest away is replaced.
                # A page never used again has infinite next-use distance.
                def next_use(resident_page: int) -> float:
                    try:
                        return pages.index(resident_page, index + 1)
                    except ValueError:
                        return float("inf")

                farthest_page = max(
                    (p for p in frames if p is not None),
                    key=next_use
                )
                slot = frames.index(farthest_page)
            frames[slot] = page

        steps.append(Step(page, frames.copy(), hit))

    return Result("OPTIMAL", steps, hits, faults, frames.copy())
