# Page Replacement Simulator — User Guide

## 1. Program Execution

The program is a console-based Python application. It requires Python 3.9 or newer and uses no external libraries.

1. Download or extract the repository and open its folder.
2. Open a terminal (Command Prompt, PowerShell, or VS Code terminal).
3. Enter the command below and press Enter.

```bash
python main.py
```

On Windows, `py main.py` may also work. The main menu will appear. Enter a number to select an option.

## 2. Console Menu

| Choice | Function |
| :--- | :--- |
| 1 | Run First-In, First-Out (FIFO) |
| 2 | Run Least Recently Used (LRU) |
| 3 | Run Optimal Page Replacement |
| 4 | Run and compare all three algorithms |
| 5 | View About the Program |
| 0 | Exit |

## 3. User Inputs

After selecting options 1–4, enter the following information:

| Input | Description |
| :--- | :--- |
| Page-reference string | One or more nonnegative whole-number page IDs, separated by spaces or commas. Maximum: 1,000 references. |
| Number of page frames | Whole number from 1 to 30. This specifies how many pages can be stored at once. |

**Sample input:**

```text
Page-reference string: 7 0 1 2 0 3 0 4 2 3 0 3 2
Number of page frames: 3
```

The program rejects invalid values and prompts for input again. Negative page IDs, letters, an empty reference string, and frame counts outside 1–30 are not accepted.

## 4. Output Interpretation

For each requested page, the program displays a frame-by-frame trace with four columns:

| Column | Meaning |
| :--- | :--- |
| Step | Order of the current page request, starting at 1. |
| Page | Page ID requested at that step. |
| Frames (slot order) | Memory frame contents immediately after the request; a dash (`-`) means the slot is empty. |
| Status | **HIT:** the page is already in a frame. **FAULT:** the page was not in memory and must be loaded. |

## 5. Summary Results

After the trace, the program displays Final frames, Total hits, Total faults, Hit ratio, and Fault ratio. Ratios are displayed as decimals and percentages.

- Hit ratio = total hits / total page references.
- Fault ratio = total faults / total page references.
- Hits + faults = total page references.

## 6. Example Output

For FIFO with page references `1 2 1 3` and 2 frames:

```text
Step | Page | Frames (slot order) | Status
   1 |    1 | [1 | -]             | FAULT
   2 |    2 | [1 | 2]             | FAULT
   3 |    1 | [1 | 2]             | HIT
   4 |    3 | [3 | 2]             | FAULT
```

Page 1 is already in memory at Step 3, so it is a HIT. At Step 4, the frames are full; FIFO replaces the earliest loaded page (1) with page 3. The result is 1 hit, 3 faults, a 25% hit ratio, and a 75% fault ratio.

## 7. Comparing Algorithms

Choose **4 - Compare All Algorithms** to see the full FIFO, LRU, and Optimal traces and a comparison table showing hits, faults, hit percentages, and fault percentages. The program identifies the algorithm or algorithms with the fewest faults for that input.
