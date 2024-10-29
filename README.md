# Project Introduction

Comparative Weather Analysis of Hong Kong and Doha
In this project, we aim to analyze and compare the weather data of Hong Kong and Doha, focusing on key metrics such as temperature, humidity, and "feels like" temperature. The "feels like" temperature is a crucial indicator that reflects how weather conditions affect human comfort, taking into account factors such as humidity and wind speed.

# Objectives
The primary goal of this analysis is to investigate why the "feels like" temperature in Hong Kong often appears higher than that in Doha, despite generally lower temperatures. By examining historical weather data, we hope to uncover the underlying reasons for this phenomenon, which may include:

Humidity Levels: 

Hong Kong typically experiences high humidity, which can significantly influence the "feels like" temperature. We will analyze how humidity in both cities correlates with temperature readings.


# Methodology

To achieve our objectives, we will utilize a combination of APIs to fetch real-time weather data for both cities. The data will include temperature, humidity, and "feels like" temperature readings. We will then store this data in an SQLite database for further analysis.

Key steps in our methodology include:

- Data Collection: Using weather APIs to gather relevant data over an extended period.

- Data Storage: Saving the collected data in an SQLite database to facilitate easy querying and analysis.
![SQLite Graph](graphs/SQLite.png)

- Graph: Temperature vs Humdidity, Temperature vs Feels Temperature, Heatmap
Hong Kong:
![HK](graphs/HK1.png)
![HK](graphs/HK2.png)
![HK](graphs/HK3.png)

Doha:
![DOHA](graphs/DOHA1.png)
![DOHA](graphs/DOHA2.png)
![DOHA](graphs/DOHA3.png)



- Interface design: Button with choose on Hong Kong or Doha to show further results.
![GUI Graph](graphs/GUI.png)


- Data Analysis: Performing statistical analyses to identify the avgerage humidity and weather type. Analysis trends and correlations between the weather variables in Hong Kong and Doha, to result the regression eqution of feels_temperature.

Through this project, we aim to provide insights that can help understand the comfort levels experienced by residents in these two distinct climates, ultimately contributing to better urban planning and public health strategies.

