'''
    main.py program for app Workhours_tracker
    Author: sakalaka8 (https://github.com/sakalaka8)
'''

# Import libraries
import datetime
import csv
import os.path

# Defines
file_exists = os.path.isfile('workhours.csv')
date_time = datetime.datetime.now()
date = date_time.strftime("%d.%m.%Y")
time = t = date_time.strftime("%H:%M:%S")
day = date_time.strftime("%A")
week = date_time.strftime("%U")

'''
print("Date:", date)
print("Time:", time)
print("Day:", day)
print("Week:", week)
'''
print("--- Workhours tracker ---")
workhours = input("Insert hours: ")
print("Today you work "+ workhours + " hours. Great!")

# Add fieldnames to csv file
with open('workhours.csv', '+a', newline='') as file:
    fieldnames = ["DATE", "DAY", "WEEK", "HOURS"]
    field_writer = csv.DictWriter(file, fieldnames = fieldnames)
    if not file_exists:
        field_writer.writeheader()

# Write data to csv file
with open('workhours.csv', 'a+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([date, day, week, workhours])
    
with open('workhours.csv', 'r', newline='') as file:
    reader = csv.DictReader(file, delimiter=',')
    monthly_sum = 0
    for row in reader:
        #print(row['HOURS'])
        monthly_sum += float(row['HOURS'])
    print("Monthly sum: "+str(monthly_sum))
