# Weather Assignment PART 1
# Student 1537962

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
    if pair[0] == '01':
        sum_month[0] += pair[1]  
    if pair[0] == '02':
        sum_month[1] += pair[1]
    if pair[0] == '03':
        sum_month[2] += pair[1]
    if pair[0] == '04':
        sum_month[3] += pair[1]  
    if pair[0] == '05':
        sum_month[4] += pair[1]
    if pair[0] == '06':
        sum_month[5] += pair[1]
    if pair[0] == '07':
        sum_month[6] += pair[1]
    if pair[0] == '08':
        sum_month[7] += pair[1]
    if pair[0] == '09':
        sum_month[8] += pair[1]
    if pair[0] == '10':
        sum_month[9] += pair[1]
    if pair[0] == '11':
        sum_month[10] += pair[1]
    if pair[0] == '12':
        sum_month[11] += pair[1]

print(f'List with the total monthly precipitation: {sum_month}')

with open('monthly_precipiation.json', 'w') as monthly_file:
    json.dump(sum_month, monthly_file)