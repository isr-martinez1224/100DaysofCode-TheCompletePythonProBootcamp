# Using regular file open
# with open("weather_data.csv") as data:
#     weather = data.readlines()
#     print(weather)
#     data.close()

# Using Import CSV
# import csv
#
# with open("weather_data.csv") as data:
#     weather = csv.reader(data)
#     temperatures = []
#     for row in weather:
#         print(row)
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)
#     data.close()

# Using Pandas
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

#print(f"Average Temperature: {sum(temp_list) / len(temp_list)}")

# Alternate Way
print(data["temp"].mean())
print(data["temp"].max())

#Get Data in Columns
print(data["condition"])
print(data.condition)

#Get Data in Rows
print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

print((monday["temp"] * 9/5) + 32)
#
# #(celsius * 9/5) + 32
#
# #OR
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
#
# #Create a Dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


#Squirrel Data
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#before len, it shows all data of color specified squirrels
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(f"Num of Gray Squirrels: {gray_squirrels}")
print(f"Num of Cinnamon Squirrels: {cinnamon_squirrels}")
print(f"Num of Black Squirrels: {black_squirrels}")

#Create a Dataframe
data_squirrels = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

new_data = pandas.DataFrame(data_squirrels)
print(new_data)
new_data.to_csv("squirrel_count.csv")