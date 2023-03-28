import csv
with open("weather_data.csv") as data:
    data = csv.reader(data)
    temperatures = []
    for row in data:
        str(row)
        if row[1].isdigit():
            temperatures.append(int(row[1]))
    print(temperatures)