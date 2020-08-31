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
day_num = date_time.strftime("%d")
week = date_time.strftime("%U")

'''
print("Date:", date)
print("Time:", time)
print("Day:", day)
print("Day number:", day_num)
print("Week:", week)
'''
print("--- Workhours tracker ---")
workhours = input("Insert hours: ")
print("Today you work "+ workhours + " hours. Great!")

# Add fieldnames to csv file
with open('workhours.csv', '+a', newline='') as file:
    fieldnames = ["DATE", "DAY", "WEEK", "HOURS"]
    field_writer = csv.DictWriter(file, dialect=('excel'), fieldnames = fieldnames)
    if not file_exists:
        field_writer.writeheader()

# Write data to csv file
with open('workhours.csv', 'a+', newline='') as file:
    writer = csv.writer(file, dialect=('excel'))
    writer.writerow([date, day, week, workhours])
    #writer.writerow([])                                     # add blank row

# Sum your monthly hours and add in new line in csv
if day_num == 1:
    with open('workhours.csv', 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        monthly_sum = 0
        for row in reader:
            #print(row['HOURS'])
            monthly_sum += float(row['HOURS'])
        print("Monthly sum: "+str(monthly_sum))
    with open('workhours.csv', 'a+', newline='') as file:
        writer.writerow([])                                     # add blank row
        writer.writerow(["Monthly sum: ", monthly_sum])
        writer.writerow([])                                     # add blank row
        field_writer = csv.DictWriter(file, dialect=('excel'), fieldnames = fieldnames)
