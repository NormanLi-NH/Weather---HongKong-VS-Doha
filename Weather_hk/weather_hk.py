import requests
import pandas as pd
import schedule
import time
import csv
from datetime import datetime
import sqlite3
import json
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")  # Task 0 .Replace with your API key
your_city = 'Hong Kong'
API_URL = f'http://api.openweathermap.org/data/2.5/weather?q={your_city}&appid={API_KEY}&units=metric'
 
# Task 1. define a database and table
def initialize_database():
            conn = sqlite3.connect('Weather_hk/weather_hk2.db')
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather_hk2_data (
                timestamp DATETIME,
                temperature FLOAT,
                humidity INTEGER,
                weather VARCHAR(40),
                feels_temp FLOAT
            )
            ''')
            conn.commit()
 
def fetch_weather_hk_data():
    initialize_database()
    response = requests.get(API_URL.format(API_KEY))
    if response.status_code == 200:
        data = response.json()
        weather_hk2_data = {
            'timestamp': datetime.now(),
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'weather': data['weather'][0]['description'],
            'feels_temp': data['main']['feels_like']
        }
 
        print(weather_hk2_data)
 
        conn = sqlite3.connect('Weather_hk/weather_hk2.db')  
        cursor = conn.cursor()
        cursor.execute('''
         INSERT INTO weather_hk2_data (
            timestamp,
            temperature,
            humidity,
            weather,
            feels_temp
        ) VALUES (?, ?, ?, ?, ?)
        ''', (weather_hk2_data['timestamp'], weather_hk2_data['temperature'], weather_hk2_data['humidity'], weather_hk2_data['weather'], weather_hk2_data['feels_temp']))
    
 
        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

fetch_weather_hk_data()
 
 
 
 
 
# # Task 3. write functions to perform analysis - generate analysis based on weather data
# connection = sqlite3.connect('weather.db')
# df = pd.read_sql_query("SELECT * FROM weather.db;", connection)
 
# print(df.head())
# connection.close()
 
 
 
 
# Task 4. Create interface to interact with data or get reports, use tkinter or terminal but remember to make it data centric and user frinedly
 
# Bonus Task 5. compare cities
 
def main():
    interval = input("Enter the interval in minutes (default is 1): ")
    interval = int(interval) if interval.isdigit() else 1
 
    schedule.every(interval).minutes.do(fetch_weather_hk_data)
    
    print(f"Scheduler started. Fetching weather data every {interval} minute(s).")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()