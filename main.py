"""
PT 101 - Page Replacement Simulator
Console-based FIFO, LRU and Optimal page replacement.
"""
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

def simulate(pages: List[int], frame_count: int, algorithm: str) -> Result:
    """Run a real page-replacement simulation, preserving frame slot positions."""
    if not pages or frame_count < 1 or any(p < 0 for p in pages):
        raise ValueError("Pages must be nonnegative and nonempty; frames must be positive.")
    algorithm = algorithm.upper()
    if algorithm not in ("FIFO", "LRU", "OPTIMAL"):
        raise ValueError("Unknown algorithm.")
    frames: List[Optional[int]] = [None] * frame_count
    insertion_order = []
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
            elif algorithm == "FIFO":
                page_to_replace = insertion_order.pop(0)
                slot = frames.index(page_to_replace)
            elif algorithm == "LRU":
                page_to_replace = min((p for p in frames if p is not None),
                             key=lambda p: last_used[p])
                slot = frames.index(page_to_replace)
            else:

                def next_use(p):
                    try:
                        return pages.index(p, index + 1)
                    except ValueError:
                        return float("inf")
                page_to_replace = max((p for p in frames if p is not None), key=next_use)
                slot = frames.index(page_to_replace)
            frames[slot] = page
            if algorithm == "FIFO":
                insertion_order.append(page)
        last_used[page] = index
        steps.append(Step(page, frames.copy(), hit))
    return Result(algorithm, steps, hits, faults, frames.copy())

def parse_pages(raw: str) -> List[int]:
    tokens = raw.replace(",", " ").split()
    if not tokens:
        raise ValueError("Enter at least one page number.")
    try:
        pages = [int(x) for x in tokens]
    except ValueError as exc:
        raise ValueError("Use whole-number page IDs separated by spaces or commas.") from exc
    if any(p < 0 for p in pages):
        raise ValueError("Page IDs cannot be negative.")
    if len(pages) > 1000:
        raise ValueError("Limit: 1000 page references.")
    return pages

def ask_input():
    while True:
        try:
            pages = parse_pages(input("\nPage-reference string (space/comma separated): "))
            frame_count = int(input("Number of page frames: ").strip())
            if not 1 <= frame_count <= 30:
                raise ValueError("Frame count must be from 1 to 30.")
            return pages, frame_count
        except ValueError as exc:
            print(f"Invalid input: {exc}\nPlease try again.")

def print_trace(result: Result, pages: List[int], count: int):
    print("\n" + "=" * 76)
    print(f" {result.name} PAGE REPLACEMENT")
    print("=" * 76)
    print("References:", " ".join(map(str, pages)))
    print("Frames:", count)
    print("-" * 76)
    print(f"{'Step':>4} | {'Page':>5} | {'Frames (slot order)':<35} | {'Status':<6}")
    print("-" * 76)
    for i, step in enumerate(result.steps, 1):
        contents = "[" + " | ".join("-" if x is None else str(x) for x in step.frames) + "]"
        print(f"{i:>4} | {step.page:>5} | {contents:<35} | {'HIT' if step.hit else 'FAULT':<6}")
    total = len(pages)
    final = "[" + " | ".join("-" if x is None else str(x) for x in result.final_frames) + "]"
    print("-" * 76)
    print(f"Final frames : {final}")
    print(f"Total hits   : {result.hits}")
    print(f"Total faults : {result.faults}")
    print(f"Hit ratio    : {result.hits}/{total} = {result.hits / total:.4f} ({100 * result.hits / total:.2f}%)")
    print(f"Fault ratio  : {result.faults}/{total} = {result.faults / total:.4f} ({100 * result.faults / total:.2f}%)")

def compare(pages: List[int], frame_count: int):
    results = [simulate(pages, frame_count, name) for name in ("FIFO", "LRU", "OPTIMAL")]
    for result in results:
        print_trace(result, pages, frame_count)
    print("\n" + "=" * 62)
    print(" ALGORITHM COMPARISON")
    print("=" * 62)
    print(f"{'Algorithm':<12}{'Hits':>8}{'Faults':>10}{'Hit %':>12}{'Fault %':>12}")
    print("-" * 62)
    for r in results:
        print(f"{r.name:<12}{r.hits:>8}{r.faults:>10}{r.hits / len(pages) * 100:>11.2f}%{r.faults / len(pages) * 100:>11.2f}%")
    fewest = min(r.faults for r in results)
    winners = ", ".join(r.name for r in results if r.faults == fewest)
    print(f"\nFewest page faults for this reference string: {winners} ({fewest})")
    print("Note: Optimal assumes future references are known (theoretical benchmark).")

def menu():
    while True:
        print("\n" + "=" * 50)
        print("        PAGE REPLACEMENT SIMULATOR")
        print("            FIFO | LRU | OPTIMAL")
        print("=" * 50)
        print("[1] First-In, First-Out (FIFO)")
        print("[2] Least Recently Used (LRU)")
        print("[3] Optimal Page Replacement")
        print("[4] Compare All Algorithms")
        print("[5] About the Program")
        print("[0] Exit")
        choice = input("\nEnter your choice: ").strip()
        if choice in ("1", "2", "3", "4"):
            pages, frames = ask_input()
            if choice == "4":
                compare(pages, frames)
            else:
                name = {"1": "FIFO", "2": "LRU", "3": "OPTIMAL"}[choice]
                print_trace(simulate(pages, frames, name), pages, frames)
        elif choice == "5":
            print("\nPT 101 | Topic 3: Page Replacement")
            print("FIFO evicts the oldest loaded page; LRU evicts the least recently used;")
            print("Optimal evicts the page used farthest in the future (or never again).")
            print("A HIT finds the requested page in memory; a FAULT requires loading it.")
        elif choice == "0":
            print("Thank you for using the Page Replacement Simulator.")
            return
        else:
            print("Invalid menu choice. Select 0, 1, 2, 3, 4 or 5.")

if __name__ == "__main__":
    try:
        menu()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed.")
