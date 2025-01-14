Bus Ridership Analysis
Project Overview
The Bus Ridership Analysis project is a comprehensive Python-based tool for processing and analyzing bus ridership data. The system works with bus ridership data stored in a CSV file, converts it into a relational SQLite database, and provides various features such as:

Analyzing daily ridership statistics.
Identifying trends in ridership over time.
Generating JSON reports of the most popular bus routes for each year.
Plotting ridership data for visualization and insights.
Simulating modifications (e.g., a 15% increase in ridership on weekends).
The goal of this project is to enable efficient management and analysis of bus data, making it easy to derive valuable insights for public transportation management.

Features
1. Data Conversion from CSV to SQLite
Convert a CSV file containing bus ridership data into an SQLite database.
The system checks for existing data and prevents overwriting of existing databases.
2. Average Ridership Calculation
Calculate the average daily ridership for each bus route.
Identify routes with underused days (i.e., days when ridership is under 200).
3. Yearly Max Route JSON Generation
Generate a JSON file (year_max.json) containing the most popular bus route for each year (2001 to 2021) based on ridership data.
4. Visualization of Ridership Trends
Plot average daily ridership over time using Matplotlib to identify ridership trends and visualize data.
5. Data Manipulation Simulation
Simulate a 15% increase in ridership for weekends and back up the original data to a separate database.
Create a backup of the original database before making any changes, ensuring data integrity.
Installation
To get started with this project, follow the steps below to set up the environment and run the code.

Prerequisites
You will need Python 3.x and a few Python libraries installed. The following packages are required:

sqlite3: Built-in library for SQLite database interaction.
csv: Built-in library for reading and writing CSV files.
json: Built-in library for working with JSON files.
matplotlib: For plotting graphs and visualizing data.
You can install matplotlib using the following command if it's not already installed:

bash
Copy code
pip install matplotlib
Step 1: Clone the Repository
Start by cloning the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/bus-ridership-analysis.git
Step 2: Download the Data
You will need a CSV file named bus_data.csv containing the ridership data for various bus routes. The data should have at least the following columns:

route: The name/identifier of the bus route.
date: The date the ridership data was recorded.
rides: The number of rides on that date.
daytype: The type of day (e.g., weekday, weekend, holiday).
The CSV file should be placed in the root of the project directory.

Step 3: Run the Code
Once the project is set up and the necessary data is in place, you can start executing the functions in the script. Here are some common functions you might want to use:

Convert CSV to SQLite Database:

Uncomment the following line in main.py to convert your CSV data into an SQLite database
