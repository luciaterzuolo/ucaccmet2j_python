# Weather Assignment 
# Student 1537962

# PART 1

import json
with open('precipitation.json') as file:
    data = json.load(file)
#Here, you will be able to use the data variable, whoch contains the data from precipitation.json

print(type(data))
# I now know that datra is a list of dicitonaries

seattle_station = []

# Now I select all the measurements belonging to Seattle
for measurement in data:
    if measurement['station'] == "GHCND:US1WAKG0038":
        seattle_station.append(measurement)
# Now I have a list called seattle_station containing all measurements from this station

month_values = []
# We split the dates 
for dict in seattle_station:
    split_dates = dict['date'].split('-')

    # We create a new list called short_list containing month and value
    short_list = [split_dates[1],dict['value']]
    month_values.append(short_list)
# We have a list called month_values containing all the pairs month-value

# We create a list called sum_month containing the sums by month
sum_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for pair in month_values:
    sum_month[int(pair[0])-1] += pair[1]

print(f'List with the total monthly precipitation: {sum_month}')

with open('monthly_precipiation.json', 'w') as monthly_file:
    json.dump(sum_month, monthly_file)

# PART 2
# Calculate the sum of precipitation over whole year

sum_year = sum(sum_month) 
print(f'The sum of precipitation over the whole year is {sum_year}.')

# Make a list with the monthly percentages
monthly_percentage = [] 
for month in sum_month:
    percentage = month/sum_year * 100
    monthly_percentage.append(percentage)
print(f'The list with the monthly percentages is: {monthly_percentage}')

Seattle_precipitation = {}
Seattle_precipitation.update({'station' : "GHCND:US1WAKG0038"})
Seattle_precipitation.update({'state' : "WA"})
Seattle_precipitation.update({'totalMonthlyPrecipitation': sum_month})
Seattle_precipitation.update({'relativeMonthlyPrecipitation': monthly_percentage})
Seattle_precipitation.update({'totalYearlyPrecipitation': sum_year})
print(Seattle_precipitation)

with open('result2.json', 'w') as seattle_file:
    json.dump({'Seattle':Seattle_precipitation}, seattle_file)
