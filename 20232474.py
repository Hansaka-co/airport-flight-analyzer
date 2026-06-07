from graphics import *
import csv
from collections import Counter

#Task A

data_list=[]

valid_airport_codes = {
    "LHR": "London Heathrow",
    "MAD": "Madrid Adolfo Suárez-Barajas",
    "CDG": "Charles De Gaulle International",
    "IST": "Istanbul Airport International",
    "AMS": "Amsterdam Schiphol",
    "LIS": "Lisbon Portela",
    "FRA": "Frankfurt Main",
    "FCO": "Rome Fiumicino",
    "MUC": "Munich International",
    "BCN": "Barcelona International"
    }

valid_airlines = {
    "BA": "British Airways",
    "AF": "Air France",
    "FR": "Ryanair",    
    "U2": "easyJet",
    "TK": "Turkish Airlines",
    "LH": "Lufthansa",
    "IB": "Iberia",
    "EK": "Emirates",
    "QR": "Qatar Airways"
}

#Enter valid airport codes

while True:
    airport_code=input("Enter valid Airpot code ").upper()
    
    if not airport_code .isalpha():
        print("Error!, airport code must be contains letters")
        continue

    if len(airport_code)!=3:
        print ("Error!, enter valid 3 digite airpot code")
        continue

    if airport_code not in valid_airport_codes:
        print("Error!, This airport code is not in the list")
        continue

    break

#Enter valid year
def get_valid_inputs():
    global data_list
    while True :
        year = input ( "Enter the year (2000-2025)")
        
        if not year .isdigit():
            print("Error!,year must be contains 4 digit number ")
            continue

        if len(year)!=4:
            print ("Error! enter 4 digit number ")
            continue

        year_num=int(year)
        
        if year_num <2000 or year_num>2025:
            print("Error!, year must be between 2000 and 2025")
            continue

        break


    filename = airport_code + year + ".csv"

    try:
        with open (filename,'r')as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                data_list.append(row)
                
        print(f" File {filename} selected - Planes departing {valid_airport_codes[airport_code]} in {year_num}.")

    except:
        print(f"Error!,the file {filename} does not exist in your folder")

        exit()

    return airport_code, year, filename

    
# Task B


# Store reslut var
def analyze_data(airport_code, year_input, filename):
    total_flights = len(data_list)
    runway_1_flights = 0
    flights_over_500 = 0
    british_airways_count = 0
    air_france_count = 0
    flights_in_rain = 0
    delayed_flights = 0
    rainy_hours_set = set()  
    destination_counter = Counter()

    def get_hour(time_str):
        return int (time_str.split(":")[0])

    for flight in data_list:
        flight_num = flight[1]          
        airline_code = flight_num[:2]   
        scheduled_dep = flight[2]       
        actual_dep = flight[3]          
        destination = flight[4]         
        distance = int(flight[5])       
        runway = flight[8]
        weather = flight[9]
        hour = get_hour(scheduled_dep)

    #Count flight
        
        if runway == "1":
            runway_1_flights += 1

        # Count flights over 500 miles
        if distance > 500:
            flights_over_500 += 1

        # Count British Airways flights
        if airline_code == "BA":
            british_airways_count += 1

        # Count Air France flights
        if airline_code == "AF":
            air_france_count += 1

        # Check if it's raining
        if "rain" in weather.lower():
            flights_in_rain += 1
            rainy_hours_set.add(hour)

        # Check if delayed
        if scheduled_dep != actual_dep:
            delayed_flights += 1

        # Count destinations
        destination_counter[destination] += 1
    
    # Average flights per hour (12 hours total)
    avg_flights_per_hour = round(total_flights / 12, 2)

    # Percentage of Air France flights
    air_france_pct = round((air_france_count / total_flights) * 100, 2)

    # Percentage of delayed flights
    delayed_pct = round((delayed_flights / total_flights) * 100, 2)

    # Number of rainy hours (use set to avoid duplicates)
    rain_hours = len(rainy_hours_set)

    # Most common destination(s)
    max_count = max(destination_counter.values())
    most_common_destinations = [dest for dest, count in destination_counter.items() if count == max_count]


    print(f"The total number of flights from this airport was {total_flights}")
    print(f"The total number of flights departing Runway one was {runway_1_flights}")
    print(f"The total number of departures of flights over 500 miles was {flights_over_500}")
    print(f"There were {british_airways_count} British Airways flights from this airport")
    print(f"There were {flights_in_rain} flights from this airport departing in rain")
    print(f"There was an average of {avg_flights_per_hour} flights per hour from this airport")
    print(f"Air France planes made up {air_france_pct}% of all departures")
    print(f"{delayed_pct}% of all departures were delayed")
    print(f"There were {rain_hours} hours in which rain fell")
    print(f"The most common destinations are {most_common_destinations}")

    return {
        "filename": filename,
        "airport_name": valid_airport_codes[airport_code],
        "year": year_input,
        "total_flights": total_flights,
        "runway_1": runway_1_flights,
        "over_500": flights_over_500,
        "british_airways": british_airways_count,
        "in_rain": flights_in_rain,
        "avg_per_hour": avg_flights_per_hour,
        "air_france_pct": air_france_pct,
        "delayed_pct": delayed_pct,
        "rain_hours": rain_hours,
        "common_destinations": most_common_destinations
    }


#Task C

def save_to_file(results):
    # Open the file in 'a' mode = append (don’t erase existing text)
    with open("results.txt", "a") as f:
        f.write(f"File {results['filename']} selected - Planes departing {results['airport_name']} in {results['year']}.\n")
        f.write("*" * 70 + "\n")
        f.write(f"The total number of flights from this airport was {results['total_flights']}\n")
        f.write(f"The total number of flights departing Runway one was {results['runway_1']}\n")
        f.write(f"The total number of departures of flights over 500 miles was {results['over_500']}\n")
        f.write(f"There were {results['british_airways']} British Airways flights from this airport\n")
        f.write(f"There were {results['in_rain']} flights from this airport departing in rain\n")
        f.write(f"There was an average of {results['avg_per_hour']} flights per hour from this airport\n")
        f.write(f"Air France planes made up {results['air_france_pct']}% of all departures\n")
        f.write(f"{results['delayed_pct']}% of all departures were delayed\n")
        f.write(f"There were {results['rain_hours']} hours in which rain fell\n")
        f.write(f"The most common destinations are {results['common_destinations']}\n")
        f.write("\n")


# Task D
def draw_histogram(airline_code, hourly_data, airport_name, year):
    airline_name = valid_airlines[airline_code]
    win = GraphWin(f"{airline_name} Departures", 700, 400)
    win.setCoords(0, 0, 14, 30)
    bar_width = 0.8

    for hour in range(12):
        x = hour + 1
        height = hourly_data[hour]
        bar = Rectangle(Point(x - bar_width / 2, 0), Point(x + bar_width / 2, height))
        bar.setFill("blue")
        bar.draw(win)
        Text(Point(x, -1), str(hour)).draw(win)
        Text(Point(x, height + 1), str(height)).draw(win)

    Text(Point(7, 28), f"{airline_name} Departures from {airport_name} in {year}").draw(win)
    win.getMouse()
    win.close()

# Run Program

airport_code, year_input, filename = get_valid_inputs()
results = analyze_data(airport_code, year_input, filename)
save_to_file(results)

# Draw histogram
while True:
    airline_code = input("Enter a two-letter Airline code to plot histogram (e.g., BA, AF): ").upper()
    if airline_code not in valid_airlines:
        print(" Not a valid airline code.")
        continue
    break

# Count flights

hourly_data = [0] * 12
for flight in data_list:
    if flight[1][:2] == airline_code:
        hour = int(flight[2].split(":")[0])
        if 0 <= hour < 12:
            hourly_data[hour] += 1

draw_histogram(airline_code, hourly_data, valid_airport_codes[airport_code], year_input)


# Task E 

while True:
    airport_code, year_input, filename = get_valid_inputs()
    results = analyze_data(airport_code, year_input, filename)
    save_to_file(results)

    while True:
        airline_code = input("Enter  airline code : ").upper()
        if airline_code not in valid_airlines:
            print("Invalid airline code.")
            continue
        break

    hourly_data = [0] * 12
    for flight in data_list:
        if flight[1][:2] == airline_code:
            hour = int(flight[2].split(":")[0])
            if 0 <= hour < 12:
                hourly_data[hour] += 1

    draw_histogram(airline_code, hourly_data, valid_airport_codes[airport_code], year_input)

    again = input("Do you want to process another file? (Y/N): ").upper()
    if again != "Y":
        print("Thank you!")
        break

    
