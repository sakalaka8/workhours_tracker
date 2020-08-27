import datetime
import csv
import os.path

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
hours = input("Insert hours: ")
print("Today you work "+ hours + " hours.")

with open('workhours.csv', '+a', newline='') as file:
    fieldnames = ["DATE", "DAY", "WEEK", "HOURS"]
    field_writer = csv.DictWriter(file, fieldnames = fieldnames)
    if not file_exists:
        field_writer.writeheader()

with open('workhours.csv', 'a+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([date, day, week, hours])
    