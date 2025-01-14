#I hereby attest that I have adhered to the rules for quizzes and projects as well as UIC’s
#Academic Integrity standards. Signed: [[Ibrahem Tamimi]]

import sqlite3
import csv
import os
import json
import matplotlib.pyplot as plt
#The json file will take a while to load as my project is first being introduced, however everything here is comprehnsive.
def convert_data(): #First to convert the data into the bus_data from csv to db
    if os.path.exists("bus_data.db"):
        print("Can’t convert: destination file already exists")
        return

    connection = sqlite3.connect("bus_data.db")
    cursor = connection.cursor()
    cursor.execute() #

    with open('bus_data.csv', 'r') as file: #assigning it to the opening index, with specific data retrievals with row's for a more friendly way.
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            cursor.execute((row[0], row[1], row[2], row[3])) #In relation to comment 16

    connection.commit()
    connection.close()


def retriever(route_name):
    connection = sqlite3.connect("bus_data.db")
    cursor = connection.cursor()

    cursor.execute( 'SELECT AVG(rides) FROM bus_data WHERE route = ?', (route_name,))
    average_ridership = cursor.fetchone()[0]
#Here is elif statments being printed to be able to sift throigh the data from input and respond through output 
#on daily average ridership, and if less than 200, with a formula of underused and total
    if average_ridership is not None:
        print(f"Average daily ridership for route {route_name}: {average_ridership:.2f} rides")
        cursor.execute('SELECT COUNT(*) FROM bus_data WHERE route = ? AND rides < 200', (route_name,))
        underused_days = cursor.fetchone()[0]
        total_days = cursor.execute('SELECT COUNT(*) FROM bus_data WHERE route = ?', (route_name,)).fetchone()[0]
        percentage_underused = (underused_days / total_days) * 100
        print(f"Percentage of underused days for route {route_name}: {percentage_underused:.2f}%")
    else:
        print(f"No data found for route {route_name}")

    connection.close()

def jsonin(): #As in referance to the beggining, this is the json file being created.
    connection = sqlite3.connect("bus_data.db")
    cursor = connection.cursor()

    yearly_max_routes = {}

    for year in range(2001, 2022): #Trickiest part of the code was trying to find between dates as some programs only could do
        #day and month vs month and day.
        cursor.execute(f'''
            SELECT route
            FROM bus_data
            WHERE date BETWEEN '{year}-01-01' AND '{year}-12-31'
            GROUP BY route
            ORDER BY SUM(rides) DESC
            LIMIT 1
        ''')
        result = cursor.fetchone()

        if result:
            max_route = result[0]
            yearly_max_routes[str(year)] = max_route
        else:
            yearly_max_routes[str(year)] = "No data"

    with open('year_max.json', 'w') as json_file:
        json.dump(yearly_max_routes, json_file, indent=4)

    connection.close()

def aplotg():
    connection = sqlite3.connect("bus_data.db")
    cursor = connection.cursor()

    cursor.execute('''
        SELECT date, AVG(rides)
        FROM bus_data
        GROUP BY date
    ''')
    data = cursor.fetchall()

    dates, avg_rides = zip(*data)

    plt.figure(figsize=(10, 6))
    plt.plot(dates, avg_rides, label='Average Daily Ridership')
    plt.xlabel('Date')
    plt.ylabel('Rides')
    plt.title('Average Daily Ridership Over Time')
    plt.legend()
    plt.show()

    connection.close()

def hack(): #Updating the data after the hack with the 15% difference
    connection_backup = sqlite3.connect("bus_data_backup.db")
    connection_original = sqlite3.connect("bus_data.db")

    cursor_backup = connection_backup.cursor()
    cursor_original = connection_original.cursor()

    cursor_original.execute('SELECT * FROM bus_data')
    data = cursor_original.fetchall()
    cursor_backup.executemany('INSERT INTO bus_data VALUES (?, ?, ?, ?)', data)

    cursor_original.execute('UPDATE bus_data SET rides = FLOOR(rides * 1.15) WHERE daytype = "U"') #formula being given with 1.15

    connection_backup.commit()
    connection_backup.close()

    connection_original.commit()
    connection_original.close()

# Uncomment the function calls you want to execute
#convert_data()
#retriever("X3") 
#jsonin()
#plotg()
#hack()
