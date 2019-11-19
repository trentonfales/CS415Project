'''
Project: Airline Search Engine
Collaborators: Kelsey Donavin, Connor Donegan, Trenton Fales, Hermes Obiang
Course: Big Data
'''


import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=db_name;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor = conn.cursor()

cursor.execute('SELECT * FROM db_name.Table')

for row in cursor:
    print(row)
