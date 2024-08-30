import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import tkinter as tk 
from tkinter import messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
import numpy as np
import seaborn as sns



# Task 3. write functions to perform analysis - generate analysis based on weather data

### connect to the database of Doha 
connection = sqlite3.connect("Weather_doha/weather_doha.db")
df_doha = pd.read_sql_query("SELECT * FROM weather_doha_data", connection)
connection.close() 

###print last 5 items
print(df_doha.tail(5))

### show Doha avgreage temperature
temperature_doha = df_doha['temperature'].mean()
print(f" Doha Average temperature  is {temperature_doha:.2f} C")
### show Doha avgreage humidity
humidity_doha = df_doha['humidity'].mean()
print(f" Doha Average Humidity  is {humidity_doha:.2f} %")
feels_doha = df_doha['feels_temp'].mean()
print(f" Doha Average Feels Temperature is {feels_doha:.2f} C")

### show Doha weather
print(df_doha['weather'].unique())


### function of plotting data of Doha
def doha_plot():
    humidity_avg = df_doha['humidity'].mean()
    print(humidity_avg)

    #scatter plot
    plt.scatter(df_doha['temperature'], df_doha['humidity'])
    #regression line
    m1, b1 = np.polyfit(df_doha['temperature'], df_doha['humidity'], 1)
    plt.plot(df_doha['temperature'], m1 * df_doha['temperature'] + b1)

    plt.title('Doha Weather')
    plt.xlabel('Temperature')
    plt.ylabel('Humidity')
    plt.show()

    #scatter plot
    plt.scatter(df_doha['temperature'], df_doha['feels_temp'])
    #regression line
    m2, b2 = np.polyfit(df_doha['temperature'], df_doha['feels_temp'], 1)
    plt.plot(df_doha['temperature'], m2 * df_doha['temperature'] + b2)

    equation_tf_doha = f'Feels Temp = {m2:.2f} * Temperature + {b2:.2f}'
    print(equation_tf_doha)
    plt.title('Doha Temperature vs Feels Temperature')
    plt.xlabel('Temperature')
    plt.ylabel('Feels Temperature')
    plt.show()


    ###heatmap
    corr = df_doha[['temperature', 'humidity', 'feels_temp']].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Doha Heatmap')
    plt.show()


###################################################

### connect to the database of Hong Kong
connection = sqlite3.connect("Weather_hk/weather_hk2.db")
df_hk = pd.read_sql_query("SELECT * FROM weather_hk2_data", connection)
connection.close() 

###print last 5 items
print(df_doha.tail(5))

### show Doha avgreage temperature
temperature_hk = df_hk['temperature'].mean()
print(f" Hong Kong Average temperature  is {temperature_hk:.2f} C")
### show Hong Kong avgreage humidity
humidity_hk = df_hk['humidity'].mean()
print(f" Hong Kong Average Humidity is {humidity_hk:.2f} %")
### show Doha avgreage feels temperature
feels_hk = df_hk['feels_temp'].mean()
print(f" Hong Kong Average Feels Temperature is {feels_hk:.2f} C")

### show Hong Kong weather
print(df_hk['weather'].unique())


### function of plotting data of Doha
def hongkong_plot():
    humidity_avg = df_hk['humidity'].mean()
    print(humidity_avg)

    plt.scatter(df_hk['temperature'], df_hk['humidity'])
    m3, b3 = np.polyfit(df_hk['temperature'], df_hk['humidity'], 1)
    plt.plot(df_hk['temperature'], m3 * df_hk['temperature'] + b3)
    plt.title('Hong Kong Temperature vs Humdidity')
    plt.xlabel('Temperature')
    plt.ylabel('Humidity')
    plt.show()

    plt.scatter(df_hk['temperature'], df_hk['feels_temp'])
    m4, b4 = np.polyfit(df_hk['temperature'], df_hk['feels_temp'], 1)
    plt.plot(df_hk['temperature'], m4 * df_hk['temperature'] + b4)
    plt.title('Hong Kong Temperature vs Feels Temperature')
    plt.xlabel('Temperature')
    plt.ylabel('Feels Temperature')
    plt.show()

    ###heatmap
    corr = df_hk[['temperature', 'humidity', 'feels_temp']].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Hong Kong Heatmap')
    plt.show()

# Task 4. Create interface to interact with data or get reports, use tkinter or terminal but remember to make it data centric and user frinedly
### interface to choose which city

root = tk.Tk()
root.title('Choose a location')
root.geometry("400x400")

option_var = tk.StringVar(value= 'Hong Kong')


def choose_city():
    city = option_var.get()
    if city == "Hong Kong":
        hongkong_plot()
    elif city == "Doha":
        doha_plot()

    messagebox.showinfo("Selection", f"You selected: {city}")




# Create radio buttons for two options
radio1 = tk.Radiobutton(root, text="Hong Kong", variable=option_var, value="Hong Kong")
radio2 = tk.Radiobutton(root, text="Doha",  variable=option_var, value="Doha")

# Create a button to confirm selection
select_button = tk.Button(root, text='Select', command= choose_city)

# Arrange widgets in the window
radio1.pack(anchor=tk.W)
radio2.pack(anchor=tk.W)
select_button.pack()

root.mainloop()


# Bonus Task 5. compare cities
temperature_diff = round(temperature_doha - temperature_hk, 2)
print(f"Temperature different between Doha and Hong Kong is {temperature_diff}C")

humidity_diff  = round(humidity_hk - humidity_doha, 2)
print(f"Humidity different between Doha and Hong Kong is {humidity_diff}%")


feels_diff = round(feels_doha - feels_hk, 2)
print(f"Feels temperature different between Doha and Hong Kong is {feels_diff}C")

# Print the regression equation
m2, b2 = np.polyfit(df_doha['temperature'], df_doha['feels_temp'], 1)
equ_doha = f" Doha Feels Temperature = {b2:.2f} + {m2:.2f} * Temperature"
print(f"The regression equation of Hong Kong is {equ_doha}")

m4, b4 = np.polyfit(df_hk['temperature'], df_hk['feels_temp'], 1)
equ_hk = f"Hong Kong Feels Temperature = {b4:.2f} + {m4:.2f} * Temperature"
print(f"The regression equation of Hong Kong is {equ_hk}")



