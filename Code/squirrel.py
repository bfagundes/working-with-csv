import pandas

data = pandas.read_csv("./Files/squirrel_census.csv")

print(f"How many Squirrels are from each color?")
print(data["Primary Fur Color"].value_counts())