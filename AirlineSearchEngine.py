'''
Project: Airline Search Engine
Collaborators: Kelsey Donavin, Connor Donegan, Trenton Fales, Hermes Obiang
Course: Big Data
'''

#table names: airlines, airports, routes

import psycopg2
import sys, os
import numpy as py
import pandas as pd
import example_psql as creds
import pandas.io.sql as psql

## ** LOAD PSQL DATABASE ** ##

# Set up a connection to the postgres server
conn_string = "host=" + creds.PGHOST + " port=" + "5432" + " dbname=" + creds.PGDATABASE + " user=" + creds.PGUSER \
    +" password=" + creds.PGPASSWORD
conn = psycopg2.connect(conn_string)
print("Connected!")

# Create a cursor object
cursor = conn.cursor()

def load_data(schema, table):

    sql_command = "SELECT * FROM {}.{};".format(str(schema), str(table))
    print (sql_command)

    # Load the data
    data = pd.read_sql(sql_command, conn)

    print(data.shape)
    return (data)

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
            sql_command = "SELECT name FROM airports WHERE country LIKE " + "'" + country + '%' + "'"
            data = pd.read_sql(sql_command, conn)
            print(data)
            # data.to_csv()
        elif (option == '2'):
            stops = input("Please enter number of stops: ")
            sql_command = "SELECT airline FROM routes WHERE stops LIKE " + "'" + stops + '%' + "'"
            data = pd.read_sql(sql_command, conn)
            print(data)
        elif (option == '3'):
            sql_command = "SELECT airline FROM routes WHERE codeshare LIKE 'Y%'"
            data = pd.read_sql(sql_command, conn)
            print(data)
        elif (option == '4'):
            sql_command = "SELECT name FROM airlines WHERE active LIKE 'Y%'"
            data = pd.read_sql(sql_command, conn)
            print(data)
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
            sql_command = "SELECT COUNT(country), country FROM airports Group by country ORDER BY COUNT(country) desc"
            country_list = pd.read_sql(sql_command, conn)
            print(country_list)
        elif (option == '2'):
            numCities = input("Number of cities to report: ")
            sql_command = "SELECT COUNT(source_airport), source_airport FROM routes GROUP BY source_airport ORDER BY Count(source_airport) desc"
            source_list = pd.read_sql(sql_command, conn)
            # print(source_list)
            sql_command = "SELECT COUNT(destination_airport), destination_airport FROM routes GROUP BY destination_airport ORDER BY Count(destination_airport) desc"
            destination_list = pd.read_sql(sql_command, conn)
            i = 0
            print("\nTotal\tCity")

            while i < int(numCities):
                total = source_list.loc[i][0]+ destination_list.loc[i][0]
                print(total, "\t", source_list.loc[i][1])
                i += 1

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
            sql_command = "DROP VIEW IF EXISTS plan;" \
                          "CREATE VIEW plan AS " \
                          "SELECT source_airport_id,source_airport,destination_airport,destination_airport_id,airline_id FROM routes WHERE source_airport_id IN (SELECT airport_id FROM airports WHERE city LIKE" + "'" + city1 + "%'" +");" \
                          "SELECT source_airport,destination_airport,airline_id from plan where destination_airport_id in(SELECT airport_id FROM airports WHERE city LIKE " + "'" + city2 + "%'" +");"
            data_list = pd.read_sql(sql_command, conn)
            # data_list = pd.read_sql("DROP VIEW route_plan", conn)
            print(data_list)
            # pd.read_sql("DROP VIEW plan;", conn)
            # sql_command = "DROP VIEW route_plan"
            # pd.read_sql(sql_command, conn)
        elif (option == '2'):
            city1 = input("Please enter a departure airport: ")
            city2 = input("Please enter an arrival airport: ")
            stops = input("Please enter number of stops: ")
            sql_command = "SELECT stops,airline_id,source_airport,destination_airport FROM routes WHERE destination_airport LIKE " + "'" + city1 + "%'" + " AND source_airport LIKE " + "'" + city2 + "%'"
            data_list = pd.read_sql(sql_command, conn)
            print(data_list)
        elif (option == '3'):
            city = input("Please enter a departure airport: ")
            stops = input("Please enter maximum number of hops: ")
            sql_command = "SELECT stops,airline_id,source_airport,destination_airport FROM routes WHERE source_airport LIKE " + "'" + city + "%'"
            data_list = pd.read_sql(sql_command, conn)
            print(data_list)
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