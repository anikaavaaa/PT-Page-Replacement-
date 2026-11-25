# Testing Evidence — Page Replacement Simulator

## 1. Test Overview

The FIFO, LRU, and Optimal page-replacement algorithms were evaluated using benchmark reference strings, memory-frame traces, and expected HIT/FAULT totals. The first four cases cover normal execution and edge conditions. Previously documented simulator results are compared with independently calculated expected values.

| Test ID | Algorithm / Area | Scenario | Recorded status |
| :--- | :--- | :--- | :---: |
| Test 1 | FIFO | Standard 13-reference sequence with 3 frames; first-loaded page is replaced. | PASS |
| Test 2 | LRU | Same sequence; select the resident page least recently referenced. | PASS |
| Test 3 | Optimal | Same sequence; select the page needed farthest in the future. | PASS |
| Test 4 | All algorithms | Repeated references, a single frame, and enough frames for all distinct pages. | PASS |
| Test 5 | Input validation | Reject blank, non-numeric, or negative page IDs; invalid frame counts. | PASS |

## 2. Test Case 1: FIFO Page Replacement

### FIFO Inputs & Expected Outputs

**Input:** Page references = `7 0 1 2 0 3 0 4 2 3 0 3 2`; Number of frames = `3`.

**Expected:** 3 HIT(s), 10 FAULT(s); hit rate = 23.08%; fault rate = 76.92%; final frames = `[0, 2, 3]`.

FIFO removes the page loaded earliest; hits do not alter its loading order.

### Expected vs. Previously Recorded Result

| Metric | Expected | Actual | Result |
| :--- | :---: | :---: | :---: |
| Total HITs | 3 | 3 | PASS |
| Total FAULTs | 10 | 10 | PASS |

### First-In, First Out Page Replacement

```text
FIFO PAGE REPLACEMENT
References: 7 0 1 2 0 3 0 4 2 3 0 3 2
Frames: 3

Step | Page | Frames (slot order) | Status
-----+------+---------------------+-------
   1 |    7 | [7 | - | -]         | FAULT
   2 |    0 | [7 | 0 | -]         | FAULT
   3 |    1 | [7 | 0 | 1]         | FAULT
   4 |    2 | [2 | 0 | 1]         | FAULT
   5 |    0 | [2 | 0 | 1]         | HIT
   6 |    3 | [2 | 3 | 1]         | FAULT
   7 |    0 | [2 | 3 | 0]         | FAULT
   8 |    4 | [4 | 3 | 0]         | FAULT
   9 |    2 | [4 | 2 | 0]         | FAULT
  10 |    3 | [4 | 2 | 3]         | FAULT
  11 |    0 | [0 | 2 | 3]         | FAULT
  12 |    3 | [0 | 2 | 3]         | HIT
  13 |    2 | [0 | 2 | 3]         | HIT

Final frames : [0 | 2 | 3]
Total hits   : 3
Total faults : 10
Hit ratio    : 3/13 = 0.2308 (23.08%)
Fault ratio  : 10/13 = 0.7692 (76.92%)
```

## 3. Test Case 2: LRU Page Replacement

### LRU Inputs & Expected Outputs

**Input:** Page references = `7 0 1 2 0 3 0 4 2 3 0 3 2`; Number of frames = `3`.

**Expected:** 4 HIT(s), 9 FAULT(s); hit rate = 30.77%; fault rate = 69.23%; final frames = `[0, 3, 2]`.

LRU removes the page that has not been accessed for the longest period.

### Expected vs. Previously Recorded Result

| Metric | Expected | Actual (earlier report) | Result |
| :--- | :---: | :---: | :---: |
| Total HITs | 4 | 4 | PASS |
| Total FAULTs | 9 | 9 | PASS |
| Hit / Fault rate | 30.77% / 69.23% | 30.77% / 69.23% | MATCH |

### Least Recently Used Page Replacement

```text
LRU PAGE REPLACEMENT
References: 7 0 1 2 0 3 0 4 2 3 0 3 2
Frames: 3

Step | Page | Frames (slot order) | Status
-----+------+---------------------+-------
   1 |    7 | [7 | - | -]         | FAULT
   2 |    0 | [7 | 0 | -]         | FAULT
   3 |    1 | [7 | 0 | 1]         | FAULT
   4 |    2 | [2 | 0 | 1]         | FAULT
   5 |    0 | [2 | 0 | 1]         | HIT
   6 |    3 | [2 | 0 | 3]         | FAULT
   7 |    0 | [2 | 0 | 3]         | HIT
   8 |    4 | [4 | 0 | 3]         | FAULT
   9 |    2 | [4 | 0 | 2]         | FAULT
  10 |    3 | [4 | 3 | 2]         | FAULT
  11 |    0 | [0 | 3 | 2]         | FAULT
  12 |    3 | [0 | 3 | 2]         | HIT
  13 |    2 | [0 | 3 | 2]         | HIT

Final frames : [0 | 3 | 2]
Total hits   : 4
Total faults : 9
Hit ratio    : 4/13 = 0.3077 (30.77%)
Fault ratio  : 9/13 = 0.6923 (69.23%)
```

## 4. Test Case 3: OPTIMAL Page Replacement

### OPTIMAL Inputs & Expected Outputs

**Input:** Page references = `7 0 1 2 0 3 0 4 2 3 0 3 2`; Number of frames = `3`.

**Expected:** 6 HIT(s), 7 FAULT(s); hit rate = 46.15%; fault rate = 53.85%; final frames = `[2, 0, 3]`.

Optimal removes the page whose next reference is farthest away, or never occurs again.

### Expected vs. Previously Recorded Result

| Metric | Expected | Actual (earlier report) | Result |
| :--- | :---: | :---: | :---: |
| Total HITs | 6 | 6 | PASS |
| Total FAULTs | 7 | 7 | PASS |
| Hit / Fault rate | 46.15% / 53.85% | 46.15% / 53.85% | MATCH |

### Optimal Page Replacement

```text
OPTIMAL PAGE REPLACEMENT
References: 7 0 1 2 0 3 0 4 2 3 0 3 2
Frames: 3

Step | Page | Frames (slot order) | Status
-----+------+---------------------+-------
   1 |    7 | [7 | - | -]         | FAULT
   2 |    0 | [7 | 0 | -]         | FAULT
   3 |    1 | [7 | 0 | 1]         | FAULT
   4 |    2 | [2 | 0 | 1]         | FAULT
   5 |    0 | [2 | 0 | 1]         | HIT
   6 |    3 | [2 | 0 | 3]         | FAULT
   7 |    0 | [2 | 0 | 3]         | HIT
   8 |    4 | [2 | 4 | 3]         | FAULT
   9 |    2 | [2 | 4 | 3]         | HIT
  10 |    3 | [2 | 4 | 3]         | HIT
  11 |    0 | [2 | 0 | 3]         | FAULT
  12 |    3 | [2 | 0 | 3]         | HIT
  13 |    2 | [2 | 0 | 3]         | HIT

Final frames : [2 | 0 | 3]
Total hits   : 6
Total faults : 7
Hit ratio    : 6/13 = 0.4615 (46.15%)
Fault ratio  : 7/13 = 0.5385 (53.85%)
```

## 5. Test Case 4: Edge-Case Evaluation

The following scenarios check behavior when references repeat, when only one physical frame exists, and when no replacement is needed because available frames exceed the number of distinct pages.

### 4A. Repeated reference

**Input:** `1 1 1 1 1` · **Frames:** 3 · **References:** 5

| Algorithm | Expected Hit/Fault | Actual Hit/Fault | Status |
| :--- | :---: | :---: | :---: |
| FIFO | 4/1 | 4/1 | PASS |
| LRU | 4/1 | 4/1 | PASS |
| OPTIMAL | 4/1 | 4/1 | PASS |

```text
ALGORITHM COMPARISON

Algorithm    Hits    Faults    Hit %     Fault %
FIFO            4         1     80.00%      20.00%
LRU             4         1     80.00%      20.00%
OPTIMAL         4         1     80.00%      20.00%

Fewest page faults for this reference string: FIFO, LRU, OPTIMAL (1)
```

### 4B. Single frame

**Input:** `1 2 1 3 2` · **Frames:** 1 · **References:** 5

| Algorithm | Expected Hit/Fault | Actual Hit/Fault | Status |
| :--- | :---: | :---: | :---: |
| FIFO | 0/5 | 0/5 | PASS |
| LRU | 0/5 | 0/5 | PASS |
| OPTIMAL | 0/5 | 0/5 | PASS |

```text
ALGORITHM COMPARISON

Algorithm    Hits    Faults    Hit %     Fault %
FIFO            0         5      0.00%     100.00%
LRU             0         5      0.00%     100.00%
OPTIMAL         0         5      0.00%     100.00%

Fewest page faults for this reference string: FIFO, LRU, OPTIMAL (5)
```

### 4C. Enough frames

**Input:** `2 3 2 4 3 2` · **Frames:** 4 · **References:** 6

| Algorithm | Expected Hit/Fault | Actual Hit/Fault | Status |
| :--- | :---: | :---: | :---: |
| FIFO | 3/3 | 3/3 | PASS |
| LRU | 3/3 | 3/3 | PASS |
| OPTIMAL | 3/3 | 3/3 | PASS |

```text
ALGORITHM COMPARISON

Algorithm    Hits    Faults    Hit %     Fault %
FIFO            3         3     50.00%      50.00%
LRU             3         3     50.00%      50.00%
OPTIMAL         3         3     50.00%      50.00%

Fewest page faults for this reference string: FIFO, LRU, OPTIMAL (3)
```

## 6. Test Case 5: Input Validation

The console input routine is designed to reject invalid page-reference strings and frame counts, then prompt the user to try again. The conditions below are based on review of the available `main.py` logic; capture direct terminal screenshots to confirm them in the current build.

| Invalid input | Expected program behavior | Actual program output (as shown in source PDF) |
| :--- | :--- | :--- |
| Blank reference string | Display “Enter at least one page number.” and retry. | `Invalid input: Enter at least one page number.` |
| Non-numeric page ID | Reject; request whole-number page IDs. | `Invalid input: Use whole-number page IDs separated by spaces or commas.` |
| Negative page ID | Reject; page IDs cannot be negative. | `Invalid input: Page IDs cannot be negative.` |
| Zero frames | Reject; frame count must be from 1 to 30. | `Invalid input: Frame count must be from 1 to 30.` |
| Too many frames | Reject; frame count must be from 1 to 30. | `Invalid input: Frame count must be from 1 to 30.` |

### Blank reference string

```text
Enter your choice: 1

Page-reference string (space/comma separated):
Invalid input: Enter at least one page number.
Please try again.

Page-reference string (space/comma separated):
```

### Non-numeric page ID

```text
Page-reference string (space/comma separated): 1,A,2,3
Invalid input: Use whole-number page IDs separated by spaces or commas.
Please try again.

Page-reference string (space/comma separated):
```

### Negative page ID

```text
Page-reference string (space/comma separated): 1,-2,3,4
Invalid input: Page IDs cannot be negative.
Please try again.

Page-reference string (space/comma separated):
```

### Zero frames

```text
Page-reference string (space/comma separated): 1,2,3,4
Number of page frames: 0
Invalid input: Frame count must be from 1 to 30.
Please try again.

Page-reference string (space/comma separated):
```

### Too many frames

```text
Page-reference string (space/comma separated): 1,2,3,4
Number of page frames: 31
Invalid input: Frame count must be from 1 to 30.
Please try again.

Page-reference string (space/comma separated):
```
