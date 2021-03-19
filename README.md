# weighted-interval-scheduling
Created by: Rami Isaac

## Description
Dynamic programming, weighted interval scheduling algorithm

## Requirements
1. Python 3.9.2 (may or may work with other versions of Python)

## Test File Requirements
FORMAT REQUIREMENTS
1. First row formatting:
A1 = "START", B1 = "FINISH", C1 = "VALUE"
IF .CSV IN PLAINTEXT FILE, THEN:
"START, FINISH, VALUE" 
2. Additional rows:
a. Each row represents a new interval
b. Formatted as start position, end position, interval value.

(example) requests-a.csv:
START,FINISH,VALUE
1, 3, 6
4, 5, 20
6, 9, 25
4, 10, 50

MISC. REQUIREMENTS:
1. Intervals do not need to be sorted

## User Manual
INSTALLING
1. Install Python 3.9.2.
4. Clone this repository to a convenient location.
RUNNING
1. Open a command terminal, and cd to the location of the script.
2. Run this script using 'schedule.py'.
3. The script will test 3 internal files, then prompt you to decide whether you would like to test your own file.
4. The maximum value for your file be shown in the terminal.