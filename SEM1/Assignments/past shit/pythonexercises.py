import math
from datetime import datetime
# 1 Kilometers to miles converter

def km_to_miles(dist):
    return dist * 0.62137

# 2 Divisible by 11 checker

def is_divisible_by_11(number):
    return number % 11 == 0

# 3 highest number

def get_highest(n1,n2):
    if n1 > n2:
        return n1
    elif n1 <n2:
        return n2
    else:
        return "neither"


# 4 hexagon_area

def hexagon_area(len):
    return (3 * math.sqrt(3) / 2) * (len ** 2)


# 5 sleeps till christmas

def sleeps_until_xmas():
    today = datetime.today()
    christmas = datetime(today.year, 12, 25)
    
    # If today is after Christmas, calculate the difference to next year's Christmas
    if today > christmas:
        christmas = datetime(today.year + 1, 12, 25)
    
    # Calculate the difference in days
    days_until_xmas = (christmas - today).days
    return days_until_xmas

# 6 is_palindrone

def is_palindrone(word):
    return word == word[::-1]


# 7 fuel cost

def fuel_cost(distance, mpg=50, cpg=1):
    return (distance / mpg) * cpg

# 8 



print(round(hexagon_area(3),2))