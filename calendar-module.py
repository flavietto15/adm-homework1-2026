# https://www.hackerrank.com/challenges/calendar-module/problem
import calendar
month, day, year = map(int, input().split())
print(calendar.day_name[calendar.weekday(year, month, day)].upper())
