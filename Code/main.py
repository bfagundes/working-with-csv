# Reading CSV as a normal file
print(f"---------- PYTHON ----------")
with open("./Files/weather_data.csv", newline="") as file:
    data = file.readlines()
    print(data)

# Reading CSV using the inbuilt CSV module    
print(f"---------- CSV Module ----------")
import csv

with open("./Files/weather_data.csv", newline="") as file:
    data = csv.reader(file)
  
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# Reading CSV using pandas library
print(f"---------- PANDAS Library ----------")
import pandas

data = pandas.read_csv("./Files/weather_data.csv")
print(data)

#print(f"Here's only the temperatures")
#print(data["temp"])

print(f"Average temperature: {data["temp"].mean()}")
print(f"Max temperature: {data["temp"].max()}")

print(f"Data for Monday")
print(data[data.day == "Monday"])