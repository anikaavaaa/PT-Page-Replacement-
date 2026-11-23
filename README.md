
# Group 1 — Page Replacement Simulator (PT 101)

A console-based **Page Replacement Simulator** developed using Python that implements three operating system page replacement algorithms: **First-In, First-Out (FIFO), Least Recently Used (LRU), and Optimal Page Replacement**.

The program simulates how pages are loaded and replaced in memory frames, tracks page hits and faults, and provides a step-by-step visualization of frame contents. It also allows users to compare the performance of all three algorithms.

The simulator uses a single-file architecture, with all algorithms, input validation, computations, and console interface implemented in `main.py`.

## Group 1 Members

- Aurelio, Anika Ava K.
- Garcia, Jessie Boy C. 
- Garing, Kristene Joy
- Barbacena, Christian Bryan M.
- Dollete, Klarklevin John G. 

## Documentation & Deliverables

- [User Guide (PDF)](documentation/User_Guide.pdf) — Instructions for executing the program, entering inputs, navigating the console menu, and interpreting simulation outputs.
- [Algorithm Explanation (PDF)](documentation/Algorithm_Explanation.pdf) — Explanation of FIFO, LRU, and Optimal, including their page replacement mechanisms and computations.
- [Test Cases (PDF)](testing/Test_Cases.pdf) — Test cases comparing expected and actual simulation results.


## Repository Structure

```text
PT-Page-Replacement/
│
├── algorithms/
│   ├── fifo.py                  # First-In, First-Out algorithm
│   ├── lru.py                   # Least Recently Used algorithm
│   └── optimal.py               # Optimal Page Replacement algorithm
│
├── documentation/
│   ├── User_Guide.pdf           # Program execution, inputs, and output interpretation
│   └── Test_Cases.pdf           # Test cases with expected and actual results
│
├── main.py                      # Main console interface and program execution
├── models.py                    # Shared simulation data structures
├── .gitignore                   # Excludes Python cache and unnecessary files
└── README.md                    # Project overview and instructions
```

## Quick Start

### Prerequisites

- Python 3.9 or later installed on Windows, macOS, or Linux.
- A terminal or command prompt for executing the program.
- No external libraries or third-party packages are required.

### How to Run

1. Clone or download this repository.
2. Open the `Page-Replacement-Simulator` folder in Visual Studio Code or a terminal.
3. Run the following command:

```bash
python main.py
```

On Windows, you may also use:

```bash
py main.py
```

4. Select an option from the interactive console menu.
5. Enter the page-reference string and number of page frames.
6. View the simulation results and performance metrics.

## Console Menu

The simulator provides the following options:

```text
==================================================
        PAGE REPLACEMENT SIMULATOR
            FIFO | LRU | OPTIMAL
==================================================

[1] First-In, First-Out (FIFO)
[2] Least Recently Used (LRU)
[3] Optimal Page Replacement
[4] Compare All Algorithms
[5] About the Program
[0] Exit
```

### Menu Functions

- **[1] FIFO** — Simulates First-In, First-Out page replacement.
- **[2] LRU** — Simulates Least Recently Used page replacement.
- **[3] Optimal** — Simulates Optimal page replacement.
- **[4] Compare All Algorithms** — Runs FIFO, LRU, and Optimal using the same input and displays their performance comparison.
- **[5] About the Program** — Displays information about the simulator and its algorithms.
- **[0] Exit** — Terminates the program.

## User Input

The program requires two inputs:

### 1. Page-Reference String

A sequence of page numbers representing the order in which pages are requested.

Example:

```text
7 0 1 2 0 3 0 4 2 3 0 3 2
```

Input Rules:
- Page numbers must be nonnegative integers.
- Values must be separated by spaces or commas.
- At least one page reference is required.
- A maximum of 1,000 page references is supported.

### 2. Number of Page Frames

Specifies the number of available memory frames.

Example:

```text
3
```

Input Rules:
- Must be a positive integer.
- Accepted values range from 1 to 30.

The program validates inputs and prompts the user to try again when invalid data is entered.

## Supported Algorithms

### 1. First-In, First-Out (FIFO)

FIFO replaces the page that has been in memory the longest.

- Pages are managed according to their loading order.
- The oldest loaded page is replaced when all frames are occupied.
- Page hits do not change the replacement order.

### 2. Least Recently Used (LRU)

LRU replaces the page that has not been accessed for the longest period.

- Tracks the most recent use of each page.
- Updates page usage information after each reference.
- Replaces the least recently accessed page when memory is full.

### 3. Optimal Page Replacement

Optimal replaces the page whose next use is farthest in the future.

- Examines upcoming page references.
- Replaces a page that will not be used again, when possible.
- Otherwise, replaces the page needed farthest in the future.
- Serves as a theoretical benchmark for comparing page replacement performance.

## Simulation Output

Each algorithm generates a frame-by-frame simulation showing the memory contents after every page reference.

The output contains the following columns:

| Column | Description |
|---|---|
| Step | Current reference number |
| Page | Requested page number |
| Frames (slot order) | Current contents of memory frames |
| Status | Indicates HIT or FAULT |

### Output Interpretation

- **HIT** — The requested page is already present in memory.
- **FAULT** — The requested page is not present and must be loaded.
- **Frames** — Show the updated memory contents after processing each reference.
- **Final Frames** — Show the memory contents after the entire reference string has been processed.

## Calculated Performance Metrics

The simulator calculates the following metrics:

### Total Page Hits

The number of page references successfully found in memory.

### Total Page Faults

The number of page references that require loading a page into memory.

### Hit Ratio

```text
Hit Ratio = Total Hits / Total Page References
```

### Fault Ratio

```text
Fault Ratio = Total Faults / Total Page References
```

### Hit Percentage

```text
Hit Percentage = Hit Ratio × 100
```

### Fault Percentage

```text
Fault Percentage = Fault Ratio × 100
```

These metrics help evaluate the performance of each page replacement algorithm.

## Algorithm Comparison

The **Compare All Algorithms** option executes FIFO, LRU, and Optimal using the same page-reference string and number of frames.

The program displays:
- Frame-by-frame simulation for each algorithm.
- Total page hits and page faults.
- Hit and fault percentages.
- A summary comparison table.
- The algorithm or algorithms with the fewest page faults.

### Sample Comparison

**Page-Reference String:**

```text
7 0 1 2 0 3 0 4 2 3 0 3 2
```

**Number of Frames:** `3`

| Algorithm | Hits | Faults | Hit % | Fault % |
|---|---:|---:|---:|---:|
| FIFO | 3 | 10 | 23.08% | 76.92% |
| LRU | 4 | 9 | 30.77% | 69.23% |
| Optimal | 6 | 7 | 46.15% | 53.85% |

For this example, Optimal produces the fewest page faults, followed by LRU and FIFO.

## Testing and Validation

The simulator was tested using different page-reference strings and frame configurations to verify the correctness of all three algorithms.

The following test cases were evaluated:

| Test Case | Description | Result |
|---|---|---|
| Test Case 1 | Standard page-reference string | PASS |
| Test Case 2 | Repeated page references | PASS |
| Test Case 3 | Single memory frame | PASS |
| Test Case 4 | More frames than distinct pages | PASS |

The expected and actual hit/fault counts matched for all tested algorithms.

Detailed testing results are available in [Test_Cases.pdf](testing/Test_Cases.pdf).

