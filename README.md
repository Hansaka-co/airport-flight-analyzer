# Traffic Data Analysis System

A Python application that processes, validates, and visualises junction traffic
data from CSV files. Built as individual coursework for the Software Development module.

## Features
- **Input validation** for user-entered survey dates (day, month, year).
- **CSV processing** that calculates statistics for two junctions: total vehicles,
  trucks, electric and two-wheeled vehicles, speeding vehicles, peak traffic hour,
  rain hours, and more.
- **Results logging** — appends each run's summary to `Results.txt`.
- **Histogram visualisation** — a dual-bar Tkinter chart of hourly vehicle
  frequency for both junctions, with labels and a legend.
- **Multi-file handling** to process several datasets in one session.

## Tech Stack
Python · Tkinter · CSV · OOP

## Project Structure
- `part_1.py` — input validation, CSV processing, statistics, and file output
- `part_2.py` — Tkinter histogram and multi-file controller

## How to Run
1. Place the CSV data files in the same directory as the scripts.
2. Run `python part_2.py`
3. Enter a survey date when prompted — the program shows statistics, saves them
   to `Results.txt`, and opens the histogram window.
