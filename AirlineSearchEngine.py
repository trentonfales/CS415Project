'''
Project: Airline Search Engine
Collaborators: Kelsey Donavin, Connor Donegan, Trenton Fales, Hermes Obiang
Course: Big Data
'''

server_name = "PostgreSQL 12"
db_name = "CS415"
#table names: airlines, airports, routes

import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=db_name;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor = conn.cursor()

# cursor.execute('SELECT * FROM db_name.Table')

for row in cursor:
    print(row)

    
def displayMainMenu():
    print("\n\nPlease select an option:")
    print("1. Airport and Airline Search")
    print("2. Airline Aggregation")
    print("3. Trip Recommendation")
    print("4. Exit")
    option = input("Option: ")
    return option

def airportAndAirlineSearch():
    while True:
        print("\n\nPlease select an option:")
        print("1. Find a list of aiports operating in a country.")
        print("2. Find a list of airlines having X stops.")
        print("3. Find a list of airlines operating with code share.")
        print("4. Find a list of active airlines in the US.")
        print("5. Exit.")
        option = input("Option: ")
        
        if (option == '1'):
            country = input("Please select a country: ")
            # Insert query for country here
        elif (option == '2'):
            stops = input("Please enter number of stops: ")
            # Insert query for X stops here
        elif (option == '3'):
            print()
            # Insert query for code share here
        elif (option == '4'):
            print()
            # Insert query for active airlines in US here
        elif (option == '5'):
            break
    
def airlineAggregation():
    while True:
        print("\n\nPlease select an option:")
        print("1. Find which country/territory has the highest number of airports.")
        print("2. Find the top X cities with the most incoming/outgoing airlines.")
        print("3. Exit.")
        option = input("Option: ")
        
        if (option == '1'):
            print()
            # Insert code here
        elif (option == '2'):
            numCities = input("Number of cities to report: ")
            # Insert code here
        elif (option == '3'):
            break
    
def tripRecommendation():
    while True:
        print("\n\nPlease select an option:")
        print("1. Find a trip connecting two cities.")
        print("2. Find a trip connecting two cities with less than X stops.")
        print("3. Find all cities reachable within X hops of a city.")
        print("4. Exit.")
        option = input("Option: ")
        
        if (option == '1'):
            city1 = input("Please enter a departure city: ")
            city2 = input("Please enter an arrival city: ")
            # Insert code here
        elif (option == '2'):
            city1 = input("Please enter a departure city: ")
            city2 = input("Please enter an arrival city: ")
            stops = input("Please enter number of stops: ")
            # Insert code here
        elif (option == '3'):
            city = input("Please enter a city: ")
            stops = input("Please enter maximum number of hops: ")
        elif (option == '4'):
            break;
    
def main():
    while True:
        option = displayMainMenu()
        if (option == '1'):
            airportAndAirlineSearch()
        elif (option == '2'):
            airlineAggregation()
        elif (option == '3'):
            tripRecommendation()
        elif (option == '4'):
            break
    
main()