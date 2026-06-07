# ✈️ Airport Flight Analyzer

> Crunch the numbers behind the runway. A Python tool that reads airport departure data, spits out the stats that matter, and draws you a histogram of any airline's hourly departures.

---

## 📋 What It Does

Point it at an airport and a year, and it loads the matching flight data file, then tells you everything you'd want to know about the day's departures:

- 🛫 Total flights and how many used Runway One
- 🌍 Long-haul departures (over 500 miles)
- 🏴 British Airways flight count
- 🌧️ Flights that took off in the rain (and how many hours it rained)
- ⏱️ Average flights per hour
- 🇫🇷 Air France's share of all departures
- ⏳ Percentage of delayed flights
- 📍 The most popular destination(s)

It saves every report to a text file, and lets you plot a **histogram** of departures by hour for any airline you choose.

---

## 🗂️ Supported Airports

| Code | Airport |
|------|---------|
| LHR  | London Heathrow |
| MAD  | Madrid Adolfo Suárez-Barajas |
| CDG  | Charles De Gaulle International |
| IST  | Istanbul Airport International |
| AMS  | Amsterdam Schiphol |
| LIS  | Lisbon Portela |
| FRA  | Frankfurt Main |
| FCO  | Rome Fiumicino |
| MUC  | Munich International |
| BCN  | Barcelona International |

## 🏢 Supported Airlines

`BA` British Airways · `AF` Air France · `FR` Ryanair · `U2` easyJet · `TK` Turkish Airlines · `LH` Lufthansa · `IB` Iberia · `EK` Emirates · `QR` Qatar Airways

---

## 🚀 Getting Started

### Requirements
- Python 3.x
- The included `graphics.py` library (already in this repo)

### Run it

```bash
python flight_anlizer.py
```

Then just follow the prompts:

1. Enter a valid **3-letter airport code** (e.g. `LHR`)
2. Enter a **year** between 2000 and 2025
3. Read your flight report
4. Enter a **2-letter airline code** (e.g. `BA`) to see its hourly histogram
5. Choose whether to analyze another file

---

## 📁 File Structure

```
.
├── flight_anlizer.py      # Main program
├── graphics.py      # Graphics library for the histogram
├── LHR2025.csv      # Sample data: London Heathrow, 2025
├── CDG2021.csv      # Sample data: Charles De Gaulle, 2021
└── results.txt      # Saved analysis reports
```

> 📌 Data files must be named `<AIRPORTCODE><YEAR>.csv` — for example, `LHR2025.csv`.

---

## 📊 Sample Output

```
File LHR2025.csv selected - Planes departing London Heathrow in 2025.
**********************************************************************
The total number of flights from this airport was 290
The total number of flights departing Runway one was 151
The total number of departures of flights over 500 miles was 182
There were 88 British Airways flights from this airport
There were 153 flights from this airport departing in rain
There was an average of 24.17 flights per hour from this airport
Air France planes made up 16.21% of all departures
29.31% of all departures were delayed
There were 6 hours in which rain fell
The most common destinations are ['IST']
```

---

## 🎓 About

Built as a university project to practice file handling, data analysis, and basic graphics in Python.
