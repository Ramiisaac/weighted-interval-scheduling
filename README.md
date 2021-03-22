# weighted-interval-scheduling
Created by: Rami Isaac

## Description
Dynamic programming, weighted interval scheduling algorithm. Sorts intervals in nondecreasing order and uses binary search to find non-conflicing interval. Runs in O(n log(n)) time. Implemented in Python. Reads intervals from .csv and returns largest interval value to console.

## Requirements
1. Python 3.9.2 (may or may work with other versions of Python)

## Test File Requirements

First row formatted as A1 = "START", B1 = "FINISH", C1 = "VALUE" OR "START, FINISH, VALUE" if plaintext file.

ADDITIONAL ROWS:
1. Each row represents a new interval
2. Formatted as start position, end position, interval value.

Intervals do not need to be sorted. See requests-a.csv for example.

## User Manual
INSTALLING
1. Install Python 3.9.2.
2. Clone this repository

RUNNING
1. Open a command terminal, and cd to the location of the script.
2. Run this script using 'schedule.py'.
3. The script will test 3 internal files, then prompt you to decide whether you would like to test your own file.
4. The maximum value for your file be shown in the terminal.
