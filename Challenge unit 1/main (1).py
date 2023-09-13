#finding the leap year 
"""
year % 4 == 0 &
year % 100 ! = 0/
year % 400 == 0
"""
def isLeapYear(year):
  if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:

    return True

  else :
   return False 

year = 2024
if isLeapYear(year):
  print('{} is a year .'.format(year))
else:
  print('{} is not a leap year. '.format (year))"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

for c in ['red', 'green', 'blue', 'yellow']:
    t.color(c)
    t.forward(75)
    t.left(90)